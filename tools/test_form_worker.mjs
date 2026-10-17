/* Testy formularza (Node 22+, bez zależności):  node tools/test_form_worker.mjs
   - ta sama reguła walidacji w przeglądarce (assets/js/site.js) i w Workerze (worker/index.js),
   - przypadki z briefu: telefony w różnych formatach, e-maile, puste pole,
   - Turnstile, Resend (sukces / błąd / brak konfiguracji), honeypot, origin.
   Testy SYMULUJĄ Turnstile i Resend — nie potwierdzają dostarczenia prawdziwej wiadomości. */
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import vm from 'node:vm';

const read = p => readFileSync(new URL(p, import.meta.url), 'utf8');
const workerSource = read('../worker/index.js');
const siteSource = read('../assets/js/site.js');

/* ---------- 1. Reguła walidacji identyczna w obu plikach ---------- */
const block = src => {
  const m = src.match(/\/\* contact-rule:start[\s\S]*?\/\* contact-rule:end \*\//);
  assert.ok(m, 'brak bloku contact-rule');
  return m[0].split('\n').map(l => l.trim()).join('\n');
};
assert.equal(block(siteSource), block(workerSource), 'Reguła walidacji w site.js i worker/index.js musi być identyczna');
const browserKind = vm.runInNewContext(block(siteSource) + '; contactKind');

/* ---------- 2. Przypadki z briefu ---------- */
const cases = [
  ['+48 734 215 791', 'phone'],
  ['734215791', 'phone'],
  ['+49 (0) 123 456789', 'phone'],
  ['+1 (555) 010-2030-4455-6677-8899', 'phone'],   // więcej cyfr niż 15
  ['112', 'phone'],                                // mniej cyfr niż 7
  ['58 123-45-67 wew. 12', 'phone'],               // dopisek wewnętrzny
  ['name@company.com', 'email'],
  ['imie.nazwisko@firma.com.pl', 'email'],
  ['name@company', 'bad_email'],
  ['abc@', 'bad_email'],
  ['@firma.pl', 'bad_email'],
  ['name@company.', 'bad_email'],
  ['', 'empty'],
  ['   ', 'empty'],
  ['Jan Kowalski', 'bad'],
];

const { default: worker } = await import(`data:text/javascript;base64,${Buffer.from(workerSource).toString('base64')}`);
const base = 'https://scenovis.malyshkogrodno.workers.dev';
const fullEnv = {
  TURNSTILE_SITE_KEY: '0x_public_example',
  TURNSTILE_SECRET: 'private_example',
  RESEND_API_KEY: 're_fake_test',
  ASSETS: { fetch: async () => new Response('asset') }
};
let env = { ...fullEnv };
let calledVerify = 0, calledMail = 0, lastMail = null, verified = true, siteverifyDown = false, resendMode = 'ok';
globalThis.fetch = async (url, opts) => {
  if (url.includes('/siteverify')) {
    calledVerify++;
    if (siteverifyDown) throw Error('offline');
    return Response.json({ success: verified, hostname: 'scenovis.malyshkogrodno.workers.dev', action: 'scenovis_contact' });
  }
  if (url.includes('/emails')) {
    calledMail++;
    lastMail = JSON.parse(opts.body);
    if (resendMode === 'error') return Response.json({ name: 'validation_error', message: 'domain not verified' }, { status: 403 });
    if (resendMode === 'noid') return Response.json({}, { status: 200 });
    return Response.json({ id: 'test-id' }, { status: 200 });
  }
  throw Error('unexpected external request');
};
const origErr = console.error; const logs = [];
console.error = (...a) => logs.push(a.join(' '));
const get = path => worker.fetch(new Request(base + path), env);
const post = (d, headers = {}) => worker.fetch(new Request(base + '/api/lead', {
  method: 'POST', headers: { 'Content-Type': 'application/json', Origin: base, ...headers }, body: JSON.stringify(d)
}), env);
const valid = { contact: 'client@example.org', name: 'Client', message: 'Hello', topic: 'expo', website: '', turnstileToken: 'token' };

const results = [];
for (const [input, expected] of cases) {
  assert.equal(browserKind(input), expected, `przeglądarka: "${input}"`);
  const res = await post({ ...valid, contact: input });
  const ok = expected === 'phone' || expected === 'email';
  assert.equal(res.status, ok ? 200 : 422, `worker: "${input}"`);
  if (ok) assert.ok(lastMail.text.includes(input.trim()), 'kontakt zapisany bez zmian w treści wiadomości');
  if (ok) assert.equal(lastMail.reply_to, expected === 'email' ? input : undefined, `reply_to dla "${input}"`);
  results.push(`${JSON.stringify(input).padEnd(36)} → ${expected.padEnd(9)} przeglądarka=OK worker=${res.status}`);
}

/* ---------- 3. Konfiguracja, Turnstile, Resend ---------- */
let config = await get('/api/contact-config');
assert.equal(config.status, 200);
assert.deepEqual(await config.json(), { ok: true, siteKey: fullEnv.TURNSTILE_SITE_KEY });

// 10. Poprawny kontakt + szczegóły opcjonalne
const before = calledMail;
let r = await post({ ...valid, contact: '+48 734 215 791', event: 'Targi X', city: 'Poznań', date: 'marzec 2027', area: '24', budget: 'do ustalenia', reuse: 'tak', topic: '3d' });
assert.equal(r.status, 200); assert.deepEqual(await r.json(), { ok: true });
assert.equal(calledMail, before + 1);
assert.deepEqual(lastMail.to, ['contact@scenovis.com']);
assert.equal(lastMail.from, 'Scenovis <form@forms.scenovis.com>');
assert.equal(lastMail.subject, 'Scenovis — Prezentacja 3D');
assert.ok(lastMail.text.includes('Targi: Targi X') && lastMail.text.includes('Miasto: Poznań'));
assert.equal(lastMail.reply_to, undefined);

// Nieznany temat → zapytanie ogólne
r = await post({ ...valid, topic: 'xyz' }); assert.equal(r.status, 200);
assert.equal(lastMail.subject, 'Scenovis — Zapytanie ogólne');

// Opcjonalne LEAD_TO_EMAIL / LEAD_FROM_EMAIL
env = { ...fullEnv, LEAD_TO_EMAIL: 'inbox@example.org', LEAD_FROM_EMAIL: 'Test <form@example.org>' };
r = await post(valid); assert.equal(r.status, 200);
assert.deepEqual(lastMail.to, ['inbox@example.org']); assert.equal(lastMail.from, 'Test <form@example.org>');
env = { ...fullEnv };

// Turnstile: brak tokenu / odrzucony / niedostępny
const verifyBefore = calledVerify;
assert.equal((await post({ ...valid, turnstileToken: '' })).status, 403);
assert.equal(calledVerify, verifyBefore, 'bez tokenu nie pytamy Siteverify');
verified = false; const mailBefore = calledMail;
assert.equal((await post(valid)).status, 403); assert.equal(calledMail, mailBefore);
verified = true;
siteverifyDown = true; assert.equal((await post(valid)).status, 503); siteverifyDown = false;

// 11. Symulowany błąd Resend → brak sukcesu, kod 502, w logu tylko status i nazwa błędu
resendMode = 'error'; logs.length = 0;
r = await post(valid); assert.equal(r.status, 502); assert.deepEqual(await r.json(), { ok: false, error: 'delivery' });
assert.ok(logs.join(' ').includes('403') && !logs.join(' ').includes('client@example.org') && !logs.join(' ').includes('re_fake'));
resendMode = 'noid';
assert.equal((await post(valid)).status, 502, 'bez identyfikatora wiadomości nie potwierdzamy wysyłki');
resendMode = 'ok';

// 12. Brak konfiguracji
env = { ...fullEnv, RESEND_API_KEY: undefined };
assert.equal((await post(valid)).status, 503);
config = await get('/api/contact-config');
assert.equal(config.status, 503);
assert.deepEqual(await config.json(), { ok: false, error: 'not_configured', missing: ['RESEND_API_KEY'] });
env = { ASSETS: fullEnv.ASSETS };
assert.equal((await post(valid)).status, 503);
assert.deepEqual((await (await get('/api/contact-config')).json()).missing, ['RESEND_API_KEY', 'TURNSTILE_SECRET', 'TURNSTILE_SITE_KEY']);
env = { ...fullEnv };

// Honeypot, origin, metoda, rozmiar, przekierowania
const hpBefore = calledMail;
r = await post({ ...valid, website: 'http://spam' }); assert.equal(r.status, 200); assert.equal(calledMail, hpBefore);
assert.equal((await post(valid, { Origin: 'https://evil.example' })).status, 403);
assert.equal((await worker.fetch(new Request(base + '/api/lead', { method: 'GET' }), env)).status, 405);
assert.equal((await post({ ...valid, message: 'x'.repeat(2001) })).status, 422);
assert.equal((await get('/')).headers.get('Location'), base + '/pl/');
assert.equal((await get('/?lang=en')).headers.get('Location'), base + '/en/');

console.error = origErr;
console.log(results.join('\n'));
console.log('PASS: identyczna reguła PL/EN/Worker, 15 przypadków kontaktu, szczegóły opcjonalne, temat, LEAD_*, Turnstile, błąd Resend, brak konfiguracji, honeypot, origin, limity, przekierowania.');
