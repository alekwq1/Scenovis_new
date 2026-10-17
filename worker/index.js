/**
 * SCENOVIS — Cloudflare Worker: przekierowania + formularz kontaktowy (Resend + Turnstile).
 *
 * Zmienne RUNTIME Workera (Cloudflare → Workers & Pages → scenovis → Settings → Variables and Secrets,
 * albo `npx wrangler secret put NAZWA`). NIE w repozytorium i NIE w "Build → Variables and secrets"
 * (tam są tylko zmienne środowiska budowania — Worker ich nie widzi i zwraca "not_configured"):
 *   RESEND_API_KEY       Secret — Resend, Sending access dla forms.scenovis.com
 *   TURNSTILE_SECRET     Secret — Cloudflare Turnstile, Secret Key
 *   TURNSTILE_SITE_KEY   Secret lub Text — Turnstile, publiczny Site Key
 * Opcjonalnie (bez nich używane są wartości domyślne poniżej):
 *   LEAD_TO_EMAIL        odbiorca zapytań      (domyślnie contact@scenovis.com)
 *   LEAD_FROM_EMAIL      nadawca wiadomości    (domyślnie Scenovis <form@forms.scenovis.com>)
 *
 * Domena forms.scenovis.com służy wyłącznie do wysyłki przez Resend.
 * Skrzynka contact@scenovis.com (Namecheap) odbiera wiadomości bez zmian w DNS.
 */
const FIELDS = ['contact', 'name', 'message', 'topic', 'event', 'city', 'date', 'area', 'budget', 'reuse', 'lang', 'page'];
// Limity rozmiaru pól chronią serwer przed nadużyciami. To NIE jest walidacja liczby cyfr telefonu.
const LIMITS = { contact: 140, name: 80, message: 2000, topic: 30, event: 120, city: 80, date: 60, area: 20, budget: 80, reuse: 30, lang: 2, page: 30 };
const MAX_BODY = 20000;
const DEFAULT_TO = 'contact@scenovis.com';
const DEFAULT_FROM = 'Scenovis <form@forms.scenovis.com>';
const TOPICS = { general: 'Zapytanie ogólne', expo: 'Projekt stoiska', '3d': 'Prezentacja 3D', delivery: 'Realizacja' };
const LABELS = { contact: 'Kontakt', name: 'Imię', message: 'Wiadomość', topic: 'Temat', event: 'Targi', city: 'Miasto',
  date: 'Termin', area: 'Powierzchnia (m²)', budget: 'Budżet', reuse: 'Ponowne użycie', lang: 'Język', page: 'Podstrona' };
const REQUIRED_ENV = ['RESEND_API_KEY', 'TURNSTILE_SECRET', 'TURNSTILE_SITE_KEY'];

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname;

    if (path === '/api/contact-config') {
      if (request.method !== 'GET') return json({ ok: false, error: 'method' }, 405);
      // Zwracamy wyłącznie NAZWY brakujących zmiennych (nigdy wartości) — ułatwia diagnozę wdrożenia.
      const missing = REQUIRED_ENV.filter(k => !env[k]);
      return env.TURNSTILE_SITE_KEY && missing.length === 0
        ? json({ ok: true, siteKey: env.TURNSTILE_SITE_KEY })
        : json({ ok: false, error: 'not_configured', missing }, 503);
    }
    if (path === '/api/lead') return handleLead(request, env, url);
    if (path === '/' || path === '/index.html') {
      const target = url.searchParams.get('lang') === 'en' ? '/en/' : '/pl/';
      return Response.redirect(new URL(target, url.origin).toString(), 301);
    }
    if (path === '/privacy.html') {
      const target = url.searchParams.get('lang') === 'en' ? '/en/privacy-policy/' : '/pl/polityka-prywatnosci/';
      return Response.redirect(new URL(target, url.origin).toString(), 301);
    }
    return env.ASSETS.fetch(request);
  }
};

function json(body, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Cache-Control': 'no-store',
      'X-Content-Type-Options': 'nosniff'
    }
  });
}

/* contact-rule:start — ta sama reguła w assets/js/site.js i worker/index.js (pilnuje tego tools/test_form_worker.mjs) */
  // Telefon: dowolny zapis z co najmniej jedną cyfrą — bez limitu liczby cyfr, bez wymaganego numeru
  // kierunkowego; spacje, nawiasy, myślniki, "+" i dopiski (np. "wew. 12") są dozwolone.
  // E-mail: wszystko, co zawiera "@", musi wyglądać jak adres: nazwa@domena.końcówka.
  function contactKind(value) {
    var v = typeof value === 'string' ? value.trim() : '';
    if (!v) return 'empty';
    if (v.indexOf('@') !== -1) {
      return /^[^\s@]+@[^\s@.]+(\.[^\s@.]+)*\.[^\s@.]{2,}$/.test(v) ? 'email' : 'bad_email';
    }
    return /\d/.test(v) ? 'phone' : 'bad';
  }
  /* contact-rule:end */

const EMAIL_RE = /^[^\s@<>]+@[^\s@<>.]+(\.[^\s@<>.]+)*\.[^\s@<>.]{2,}$/;
function mailFrom(env) {
  const v = (env.LEAD_FROM_EMAIL || '').trim();
  return v && /@/.test(v) && !/[\r\n]/.test(v) ? v : DEFAULT_FROM;
}
function mailTo(env) {
  const v = (env.LEAD_TO_EMAIL || '').trim();
  return EMAIL_RE.test(v) ? v : DEFAULT_TO;
}

async function verifyTurnstile(token, request, env, hostname) {
  if (!env.TURNSTILE_SECRET || !env.TURNSTILE_SITE_KEY) return 'unavailable';
  if (typeof token !== 'string' || !token || token.length > 2048) return 'invalid';
  const data = new URLSearchParams({ secret: env.TURNSTILE_SECRET, response: token });
  const ip = request.headers.get('CF-Connecting-IP');
  if (ip) data.set('remoteip', ip);
  try {
    const response = await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify', {
      method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: data
    });
    if (!response.ok) return 'unavailable';
    const result = await response.json();
    // Token z innej strony lub innego formularza nie może zostać tu wykorzystany ponownie.
    return result.success === true && result.hostname === hostname && result.action === 'scenovis_contact'
      ? 'ok' : 'invalid';
  } catch {
    return 'unavailable';
  }
}

async function handleLead(request, env, url) {
  if (request.method !== 'POST') return json({ ok: false, error: 'method' }, 405);
  const origin = request.headers.get('Origin');
  if (origin && origin !== url.origin) return json({ ok: false, error: 'origin' }, 403);
  const type = request.headers.get('Content-Type') || '';
  if (!type.toLowerCase().includes('application/json')) return json({ ok: false, error: 'type' }, 415);
  const advertisedLen = Number(request.headers.get('Content-Length') || 0);
  if (advertisedLen > MAX_BODY) return json({ ok: false, error: 'size' }, 413);

  let raw;
  try {
    const body = await request.text();
    if (body.length > MAX_BODY) return json({ ok: false, error: 'size' }, 413);
    raw = JSON.parse(body);
    if (!raw || typeof raw !== 'object' || Array.isArray(raw)) throw new Error('Bad payload');
  } catch {
    return json({ ok: false, error: 'parse' }, 400);
  }
  // Ukryte pole-pułapka (honeypot): po cichu odrzucamy oczywiste boty, bez wysyłki.
  if (raw.website) return json({ ok: true });

  const lead = {};
  for (const key of FIELDS) {
    if (raw[key] !== undefined && typeof raw[key] !== 'string') return json({ ok: false, error: 'fields' }, 422);
    const value = (raw[key] || '').trim();
    if (value.length > LIMITS[key]) return json({ ok: false, error: 'fields' }, 422);
    lead[key] = value;
  }
  const kind = contactKind(lead.contact);
  if (kind !== 'phone' && kind !== 'email') return json({ ok: false, error: 'contact', reason: kind }, 422);
  if (!TOPICS[lead.topic]) lead.topic = 'general';

  const verified = await verifyTurnstile(raw.turnstileToken, request, env, url.hostname);
  if (verified === 'unavailable') return json({ ok: false, error: 'security_unavailable' }, 503);
  if (verified !== 'ok') return json({ ok: false, error: 'turnstile' }, 403);
  if (!env.RESEND_API_KEY) return json({ ok: false, error: 'not_configured' }, 503);

  const text = [
    'Nowe zapytanie ze strony Scenovis',
    '',
    // Kontakt zapisany dokładnie tak, jak wpisał go klient (bez formatowania).
    `${LABELS.contact} (${kind === 'email' ? 'e-mail' : 'telefon'}): ${lead.contact}`,
    `${LABELS.topic}: ${TOPICS[lead.topic]}`,
    ...FIELDS.filter(k => lead[k] && !['contact', 'topic', 'message'].includes(k)).map(k => `${LABELS[k]}: ${lead[k]}`),
    ...(lead.message ? ['', `${LABELS.message}:`, lead.message] : []),
    '',
    `Otrzymano: ${new Date().toISOString()}`,
    `Kraj połączenia: ${request.cf?.country || '-'}`
  ].join('\n');

  try {
    const sent = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: { 'Authorization': `Bearer ${env.RESEND_API_KEY}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        from: mailFrom(env),
        to: [mailTo(env)],
        subject: `Scenovis — ${TOPICS[lead.topic]}`,
        text,
        // Reply-To tylko dla poprawnego adresu e-mail klienta; telefon zostaje w treści wiadomości.
        ...(kind === 'email' ? { reply_to: lead.contact } : {})
      })
    });
    const result = await sent.json().catch(() => ({}));
    // Sukces dopiero po potwierdzeniu przyjęcia wiadomości przez Resend (status 2xx + identyfikator).
    if (!sent.ok || !result || typeof result.id !== 'string') {
      // Logujemy tylko status i nazwę błędu Resend — nigdy danych klienta ani kluczy.
      console.error('Resend delivery failed:', sent.status, result && result.name ? result.name : '');
      return json({ ok: false, error: 'delivery' }, 502);
    }
    return json({ ok: true });
  } catch {
    console.error('Resend delivery failed: network');
    return json({ ok: false, error: 'delivery' }, 502);
  }
}
