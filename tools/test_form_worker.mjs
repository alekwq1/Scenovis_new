/* Node 22+ smoke tests: API contract, Turnstile validation and Resend delivery mock. */
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
const workerSource = readFileSync(new URL('../worker/index.js', import.meta.url), 'utf8');
const { default: worker } = await import(`data:text/javascript;base64,${Buffer.from(workerSource).toString('base64')}`);
const base = 'https://scenovis.malyshkogrodno.workers.dev';
const env = {
  TURNSTILE_SITE_KEY: '0x_public_example',
  TURNSTILE_SECRET: 'private_example',
  RESEND_API_KEY: 're_fake_test',
  ASSETS: { fetch: async () => new Response('asset') }
};
const valid = { contact: 'client@example.org', name: 'Client', message: 'Hello', topic: 'expo', website: '', turnstileToken: 'token' };
let calledVerify = 0, calledMail = 0, lastMail = null, verified = true, siteverifyDown = false, resendDown = false;
globalThis.fetch = async (url, opts) => {
  if (url.includes('/siteverify')) {
    calledVerify++;
    if (siteverifyDown) throw Error('offline');
    return Response.json({success: verified, hostname: 'scenovis.malyshkogrodno.workers.dev', action: 'scenovis_contact'});
  }
  if (url.includes('/emails')) {
    calledMail++;
    lastMail = JSON.parse(opts.body);
    return new Response('{}', {status: resendDown ? 500 : 200});
  }
  throw Error('unexpected external request');
};
const get = path => worker.fetch(new Request(base+path), env);
const post = (d, headers={}) => worker.fetch(new Request(base+'/api/lead', {
  method: 'POST', headers: { 'Content-Type': 'application/json', Origin: base, ...headers }, body: JSON.stringify(d)
}), env);
const config = await get('/api/contact-config');
assert.equal(config.status, 200);
assert.deepEqual(await config.json(), {ok:true, siteKey:env.TURNSTILE_SITE_KEY});
assert.equal((await post({...valid,contact:'bad'})).status,422);
assert.equal((await post({...valid,turnstileToken:''})).status,403);
assert.equal(calledVerify,0);
verified=false;
assert.equal((await post(valid)).status,403);
assert.equal(calledMail,0);
verified=true;
assert.deepEqual(await (await post(valid)).json(), {ok:true});
assert.equal(calledMail,1);
assert.deepEqual(lastMail.to,['contact@scenovis.com']);
assert.equal(lastMail.from,'Scenovis <form@forms.scenovis.com>');
assert.equal(lastMail.reply_to,'client@example.org');
assert.equal(lastMail.subject,'Scenovis — Stoisko EXPO');
assert.equal((await post({...valid,contact:'+48 555 555 555'})).status,200);
assert.equal(lastMail.reply_to,undefined);
siteverifyDown=true;
assert.equal((await post(valid)).status,503);
siteverifyDown=false;
resendDown=true;
assert.equal((await post(valid)).status,502);
assert.equal((await post(valid,{Origin:'https://evil.example'})).status,403);
assert.equal((await worker.fetch(new Request(base+'/api/lead',{method:'GET'}),env)).status,405);
console.log('PASS: config, contact validation, missing/failed Turnstile, Resend success/error, phone and origin.');
