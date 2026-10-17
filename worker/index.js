/**
 * SCENOVIS — Cloudflare Worker / mail from the contact form.
 * Secrets configured in Cloudflare (NEVER in this repository):
 *   RESEND_API_KEY       Resend: Sending access, forms.scenovis.com
 *   TURNSTILE_SECRET     Cloudflare Turnstile Siteverify secret
 * Public variable configured in Cloudflare:
 *   TURNSTILE_SITE_KEY   Cloudflare Turnstile public site key (Text, not Secret)
 *
 * Domain forms.scenovis.com is only for outgoing messages via Resend.
 * Namecheap continues to receive contact@scenovis.com.
 */
const FIELDS = ['contact', 'name', 'message', 'topic', 'event', 'city', 'date', 'area', 'budget', 'reuse', 'lang', 'page'];
const LIMITS = { contact: 140, name: 80, message: 2000, topic: 30, event: 120, city: 80, date: 60, area: 20, budget: 80, reuse: 30, lang: 2, page: 30 };
const MAX_BODY = 20000;
const MAIL_TO = 'contact@scenovis.com';
const MAIL_FROM = 'Scenovis <form@forms.scenovis.com>';
const TOPICS = { general: 'Zapytanie ogólne', expo: 'Stoisko EXPO', '3d': 'Prezentacja 3D', delivery: 'Realizacja' };

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname;

    if (path === '/api/contact-config') {
      if (request.method !== 'GET') return json({ ok: false, error: 'method' }, 405);
      return env.TURNSTILE_SITE_KEY
        ? json({ ok: true, siteKey: env.TURNSTILE_SITE_KEY })
        : json({ ok: false, error: 'not_configured' }, 503);
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

function validContact(v) {
  if (typeof v !== 'string' || v.length > LIMITS.contact) return false;
  const email = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v);
  const digits = v.replace(/\D/g, '');
  const phone = /^[+\d\s().\-\/]+$/.test(v) && digits.length >= 7 && digits.length <= 15;
  return email || phone;
}

async function verifyTurnstile(token, request, env, hostname) {
  if (!env.TURNSTILE_SECRET || !env.TURNSTILE_SITE_KEY) return 'unavailable';
  if (typeof token !== 'string' || !token || token.length > 2048) return 'invalid';
  const data = new URLSearchParams({ secret: env.TURNSTILE_SECRET, response: token });
  const ip = request.headers.get('CF-Connecting-IP');
  if (ip) data.set('remoteip', ip);
  let response;
  try {
    response = await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify', {
      method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: data
    });
    if (!response.ok) return 'unavailable';
    const result = await response.json();
    // A token from a different allowed website or form must not be reusable here.
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
  // Hidden honeypot: quietly discard obvious bot submissions.
  if (raw.website) return json({ ok: true });

  const lead = {};
  for (const key of FIELDS) {
    if (raw[key] !== undefined && typeof raw[key] !== 'string') return json({ ok: false, error: 'fields' }, 422);
    const value = (raw[key] || '').trim();
    if (value.length > LIMITS[key]) return json({ ok: false, error: 'fields' }, 422);
    lead[key] = value;
  }
  if (!validContact(lead.contact)) return json({ ok: false, error: 'contact' }, 422);

  const verified = await verifyTurnstile(raw.turnstileToken, request, env, url.hostname);
  if (verified === 'unavailable') return json({ ok: false, error: 'security_unavailable' }, 503);
  if (verified !== 'ok') return json({ ok: false, error: 'turnstile' }, 403);
  if (!env.RESEND_API_KEY) return json({ ok: false, error: 'not_configured' }, 503);

  const received = new Date().toISOString();
  const country = request.cf?.country || '';
  const text = [
    'Nowe zapytanie ze strony Scenovis',
    ...FIELDS.filter(k => lead[k]).map(k => `${k}: ${lead[k]}`),
    `received: ${received}`,
    `country: ${country}`
  ].join('\n');
  const topic = TOPICS[lead.topic] || TOPICS.general;
  try {
    const sent = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: { 'Authorization': `Bearer ${env.RESEND_API_KEY}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        from: MAIL_FROM,
        to: [MAIL_TO],
        subject: `Scenovis — ${topic}`,
        text,
        ...(lead.contact.includes('@') ? { reply_to: lead.contact } : {})
      })
    });
    if (!sent.ok) {
      // Log status only. Never log the customer's personal data or secret keys.
      console.error('Resend delivery failed:', sent.status);
      return json({ ok: false, error: 'delivery' }, 502);
    }
    return json({ ok: true });
  } catch {
    return json({ ok: false, error: 'delivery' }, 502);
  }
}
