/* SCENOVIS — site.js (bez zależności). Brak narzędzi śledzących:
   zdarzenia trafiają tylko do window.dataLayer, który dziś nikt nie czyta.
   Po wdrożeniu zgody (Consent Mode) Google tag / GTM może je odebrać — zob. docs/CHECKLISTS.md */
(function () {
  'use strict';
  var doc = document.documentElement;
  doc.classList.remove('no-js');
  doc.classList.add('js');

  var body = document.body;
  var lang = body.getAttribute('data-lang') || 'pl';
  var pageType = body.getAttribute('data-page') || 'home';

  /* ---------- analityka: tylko dataLayer ---------- */
  window.dataLayer = window.dataLayer || [];
  function track(event, params) {
    var payload = { event: event, page_lang: lang, page_type: pageType };
    if (params) for (var k in params) payload[k] = params[k];
    window.dataLayer.push(payload);
  }
  window.scenovisTrack = track;

  document.addEventListener('click', function (e) {
    var a = e.target.closest('a, button');
    if (!a) return;
    var name = a.getAttribute('data-track');
    var href = a.getAttribute('href') || '';
    if (!name) {
      if (href.indexOf('tel:') === 0) name = 'phone_click';
      else if (href.indexOf('mailto:') === 0) name = 'email_click';
      else if (href.indexOf('wa.me') > -1) name = 'whatsapp_click';
    }
    if (name) track(name, { link_text: (a.textContent || '').trim().slice(0, 80) });
  });

  /* ---------- stare kotwice (#services, #about, #contact) ---------- */
  var aliases = lang === 'pl'
    ? { services: 'oferta', about: 'o-mnie', contact: 'kontakt' }
    : {};
  var h = location.hash.slice(1);
  if (aliases[h] && document.getElementById(aliases[h])) {
    history.replaceState(null, '', '#' + aliases[h]);
    requestAnimationFrame(function () { document.getElementById(aliases[h]).scrollIntoView(); });
  }

  /* ---------- przełącznik języka: zostań w tej samej sekcji ---------- */
  document.querySelectorAll('.lang-switch a[data-idmap]').forEach(function (a) {
    a.addEventListener('click', function () {
      var map; try { map = JSON.parse(a.getAttribute('data-idmap')); } catch (e) { return; }
      var mid = innerHeight * 0.4, cur = null;
      Object.keys(map).forEach(function (id) {
        var el = document.getElementById(id);
        if (el && el.getBoundingClientRect().top <= mid) {
          if (!cur || el.getBoundingClientRect().top > document.getElementById(cur).getBoundingClientRect().top) cur = id;
        }
      });
      if (cur && map[cur]) a.href = a.href.split('#')[0] + '#' + map[cur];
    });
  });

  /* ---------- menu mobilne ---------- */
  var toggle = document.querySelector('.menu-toggle');
  var nav = document.getElementById('site-nav');
  function setMenu(open) {
    if (!toggle || !nav) return;
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', toggle.getAttribute(open ? 'data-label-close' : 'data-label-open'));
    nav.classList.toggle('is-open', open);
  }
  if (toggle && nav) {
    toggle.addEventListener('click', function () { setMenu(toggle.getAttribute('aria-expanded') !== 'true'); });
    nav.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) { setMenu(false); toggle.focus(); }
    });
  }

  /* ---------- pasek postępu + aktywna pozycja menu ---------- */
  var bar = document.querySelector('.scroll-progress span');
  var ticking = false;
  function onScroll() {
    ticking = false;
    var max = Math.max(1, doc.scrollHeight - innerHeight);
    if (bar) bar.style.transform = 'scaleX(' + Math.min(1, scrollY / max) + ')';
  }
  addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  onScroll();

  if (nav && 'IntersectionObserver' in window) {
    var links = {};
    nav.querySelectorAll('a[href*="#"]').forEach(function (a) { links[a.hash.slice(1)] = a; });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        Object.keys(links).forEach(function (id) {
          if (id === en.target.id) links[id].setAttribute('aria-current', 'location');
          else links[id].removeAttribute('aria-current');
        });
      });
    }, { rootMargin: '-35% 0px -60% 0px' });
    Object.keys(links).forEach(function (id) { var s = document.getElementById(id); if (s) io.observe(s); });
  }

  /* ---------- temat zapytania z przycisków usług ---------- */
  var form = document.getElementById('lead-form');
  document.addEventListener('click', function (e) {
    var t = e.target.closest('[data-topic]');
    if (t && form) form.elements.topic.value = t.getAttribute('data-topic');
  });

  /* ---------- warianty Economy / Smart / Premium: jeden stan dla hero i zestawienia kosztów ---------- */
  var VARIANTS = ['economy', 'smart', 'premium'];
  function setVariant(v, src) {
    if (VARIANTS.indexOf(v) < 0) return;
    document.querySelectorAll('[data-variant-scope]').forEach(function (el) { el.setAttribute('data-variant', v); });
    document.querySelectorAll('.vbtn[data-set-variant]').forEach(function (b) {
      b.setAttribute('aria-pressed', String(b.getAttribute('data-set-variant') === v));
    });
    document.querySelectorAll('.vimg').forEach(function (p) {
      if (p.classList.contains('vimg--' + v)) p.removeAttribute('aria-hidden'); else p.setAttribute('aria-hidden', 'true');
    });
    document.querySelectorAll('.sheet').forEach(function (sheet) {
      var panel = sheet.querySelector('[role="tabpanel"]');
      sheet.querySelectorAll('[role="tab"]').forEach(function (t) {
        var on = t.getAttribute('data-set-variant') === v;
        t.setAttribute('aria-selected', String(on));
        t.tabIndex = on ? 0 : -1;
        if (on && panel) panel.setAttribute('aria-labelledby', t.id);
      });
    });
    if (src) track('variant_select', { variant: v, source: src });
  }
  document.querySelectorAll('.vbtn[data-set-variant]').forEach(function (b, i, all) {
    b.addEventListener('click', function () { setVariant(b.getAttribute('data-set-variant'), 'hero'); });
    b.addEventListener('keydown', function (e) {
      var n = null;
      if (e.key === 'ArrowRight') n = all[(i + 1) % all.length];
      if (e.key === 'ArrowLeft') n = all[(i - 1 + all.length) % all.length];
      if (n) { e.preventDefault(); n.focus(); setVariant(n.getAttribute('data-set-variant'), 'hero'); }
    });
  });
  document.querySelectorAll('.sheet').forEach(function (sheet) {
    var tabs = Array.prototype.slice.call(sheet.querySelectorAll('[role="tab"]'));
    tabs.forEach(function (tab, i) {
      tab.addEventListener('click', function () { setVariant(tab.getAttribute('data-set-variant'), 'costs'); });
      tab.addEventListener('keydown', function (e) {
        var n = null;
        if (e.key === 'ArrowRight') n = tabs[(i + 1) % tabs.length];
        if (e.key === 'ArrowLeft') n = tabs[(i - 1 + tabs.length) % tabs.length];
        if (e.key === 'Home') n = tabs[0];
        if (e.key === 'End') n = tabs[tabs.length - 1];
        if (n) { e.preventDefault(); setVariant(n.getAttribute('data-set-variant'), 'costs'); n.focus(); }
      });
    });
  });
  // obrazy pozostałych wariantów pobierane po załadowaniu strony — przełączenie bez czekania
  window.addEventListener('load', function () {
    document.querySelectorAll('.vimg img').forEach(function (im) { if (im.decode) im.decode().catch(function () {}); });
  });

  /* ---------- wideo w hero: pauza/odtwarzanie, bez autoodtwarzania przy ograniczonym ruchu ---------- */
  document.querySelectorAll('[data-hero-video-toggle]').forEach(function (btn) {
    var v = btn.parentNode.querySelector('video');
    if (!v) return;
    function sync() {
      var paused = v.paused;
      btn.setAttribute('aria-pressed', String(paused));
      btn.setAttribute('aria-label', btn.getAttribute(paused ? 'data-label-play' : 'data-label-pause'));
    }
    var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
    var userPaused = reduce; // ręczna pauza (lub ograniczony ruch) — nie wznawiamy automatycznie
    if (reduce) { v.removeAttribute('autoplay'); v.pause(); }
    btn.addEventListener('click', function () {
      if (v.paused) { userPaused = false; v.play(); } else { userPaused = true; v.pause(); }
    });
    // poza ekranem film się zatrzymuje (bateria, transfer), po powrocie rusza dalej
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (es) {
        es.forEach(function (e) {
          if (!e.isIntersecting) { if (!v.paused) v.pause(); }
          else if (!userPaused && v.paused) { var p = v.play(); if (p && p.catch) p.catch(function () {}); }
        });
      }, { threshold: 0.15 }).observe(v);
    }
    v.addEventListener('play', sync); v.addEventListener('pause', sync); sync();
  });

  /* ---------- film: start, 25%, 50%, koniec + CTA po filmie ---------- */
  document.querySelectorAll('.player video').forEach(function (video) {
    var wrap = video.closest('.player');
    var play = wrap.querySelector('.player-play');
    var name = video.getAttribute('data-video-name') || 'video';
    var sent = {};
    function once(ev, extra) { if (!sent[ev]) { sent[ev] = true; track(ev, Object.assign({ video_name: name }, extra || {})); } }
    if (play) play.addEventListener('click', function () { video.play(); video.focus(); });
    video.addEventListener('play', function () { wrap.classList.add('is-playing'); wrap.classList.remove('is-ended'); once('video_start'); });
    video.addEventListener('timeupdate', function () {
      if (!video.duration) return;
      var p = video.currentTime / video.duration;
      if (p >= 0.25) once('video_25', { video_percent: 25 });
      if (p >= 0.5) once('video_50', { video_percent: 50 });
    });
    video.addEventListener('ended', function () {
      once('video_complete', { video_percent: 100 });
      wrap.classList.add('is-ended');
      if (document.fullscreenElement) document.exitFullscreen().catch(function () {});
      var end = wrap.querySelector('.player-end');
      if (!end) {
        var cta = document.querySelector('.case-cta-btn');
        if (!cta) return;
        end = document.createElement('div');
        end.className = 'player-end';
        var box = document.createElement('div'); box.className = 'player-end-actions';
        var again = document.createElement('button');
        again.type = 'button'; again.className = 'button button-ghost player-replay';
        again.textContent = wrap.getAttribute('data-replay') || 'Replay';
        again.addEventListener('click', function () {
          wrap.classList.remove('is-ended'); video.currentTime = 0; video.play(); track('video_replay', { video_name: name });
        });
        box.appendChild(again);
        box.insertAdjacentHTML('beforeend', cta.outerHTML);
        end.appendChild(box);
        wrap.appendChild(end);
      }
      var btn = end.querySelector('a, button');
      if (btn) btn.focus();
    });
  });

  /* ---------- model 3D (Three.js) — ładowany dopiero po kliknięciu ---------- */
  var vHost = document.querySelector('[data-viewer]');
  var vBtn = vHost && vHost.querySelector('[data-viewer-launch]');
  if (vHost && vBtn) {
    var VT = JSON.parse(document.getElementById('viewer-i18n').textContent);
    var hasGL = (function () { try { var c = document.createElement('canvas'); return !!(window.WebGL2RenderingContext && c.getContext('webgl2')); } catch (e) { return false; } })();
    if (!hasGL) { vBtn.hidden = true; }
    vBtn.addEventListener('click', function () {
      var label = vBtn.querySelector('span');
      vBtn.disabled = true; vHost.classList.add('is-loading'); label.textContent = VT.loading;
      track('viewer_launch');
      var v = (document.querySelector('link[href*="site.css?v="]') || {}).href || '';
      var ver = (v.split('v=')[1] || '');
      import('/assets/js/viewer3d.js?v=' + ver).then(function (m) {
        return m.start(vHost, VT, function (p) { label.textContent = VT.loading + ' ' + Math.round(p * 100) + '%'; });
      }).then(function () {
        vHost.classList.remove('is-loading'); vHost.classList.add('is-3d'); vBtn.hidden = true;
        var c = vHost.querySelector('canvas'); if (c) c.focus({ preventScroll: true });
      }).catch(function () {
        vHost.classList.remove('is-loading'); vBtn.hidden = true;
        var p = document.createElement('p'); p.className = 'viewer-error'; p.setAttribute('role', 'status'); p.textContent = VT.error;
        vHost.appendChild(p); track('viewer_error');
      });
    });
  }

  /* ---------- formularz (Resend + Turnstile, no secrets in the browser) ---------- */
  if (!form) return;
  var T = JSON.parse(document.getElementById('form-i18n').textContent);
  var CFG = JSON.parse(document.getElementById('form-config').textContent);
  var input = form.elements.contact;
  var err = document.getElementById('f-error');
  var status = document.getElementById('f-status');
  var submit = form.querySelector('[type="submit"]');
  var captchaBox = document.getElementById('turnstile-container');
  var captchaId = null;
  var captchaReady = false;
  var captchaUnavailable = false;
  var local = location.protocol === 'file:' || /^(localhost|127\.0\.0\.1|\[::1\])$/.test(location.hostname);

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
  function data() {
    var out = {};
    ['contact', 'name', 'message', 'topic', 'event', 'city', 'date', 'area', 'budget', 'reuse', 'lang', 'page', 'website']
      .forEach(function (k) { if (form.elements[k]) out[k] = String(form.elements[k].value || '').trim(); });
    return out;
  }
  function plainText(d) {
    var lines = [];
    var f = T.fields;
    if (d.topic && T.topics[d.topic]) lines.push(f.topic + ': ' + T.topics[d.topic]);
    ['contact', 'name', 'event', 'city', 'date', 'area', 'budget', 'reuse'].forEach(function (k) {
      if (d[k]) lines.push(f[k] + ': ' + d[k]);
    });
    if (d.message) lines.push('', f.message + ':', d.message);
    return lines.join('\n');
  }
  function fallback(msg, d) {
    var text = plainText(d);
    var mail = 'mailto:' + CFG.email + '?subject=' + encodeURIComponent(T.mail_subject) + '&body=' + encodeURIComponent(text);
    var wa = 'https://wa.me/' + CFG.wa + '?text=' + encodeURIComponent(T.wa_hello + '\n\n' + text);
    status.className = 'form-status is-fail';
    status.innerHTML = '';
    var p = document.createElement('p'); p.textContent = msg; status.appendChild(p);
    var row = document.createElement('div'); row.className = 'cta-row';
    var a1 = document.createElement('a'); a1.className = 'button button-primary button-small'; a1.href = mail; a1.textContent = T.f_fail_email;
    var a2 = document.createElement('a'); a2.className = 'button button-ghost button-small'; a2.href = wa; a2.target = '_blank'; a2.rel = 'noopener'; a2.textContent = T.f_fail_wa;
    row.appendChild(a1); row.appendChild(a2); status.appendChild(row);
    status.focus();
    track('lead_form_fallback_shown');
  }
  function clearErr() { err.textContent = ''; input.removeAttribute('aria-invalid'); }
  function showContactError(kind) {
    err.textContent = kind === 'empty' ? T.f_err_empty : kind === 'bad_email' ? T.f_err_email : T.f_err_contact;
    input.setAttribute('aria-invalid', 'true');
    input.focus();
  }
  // Komunikat po opuszczeniu pola — tylko dla wyraźnie błędnego e-maila (nie przeszkadza przy pisaniu).
  input.addEventListener('blur', function () {
    if (input.value.trim() && contactKind(input.value) === 'bad_email') {
      err.textContent = T.f_err_email;
      input.setAttribute('aria-invalid', 'true');
    }
  });
  function resetCaptcha() {
    if (captchaReady && captchaId !== null && window.turnstile) {
      window.turnstile.reset(captchaId);
    }
  }
  input.addEventListener('input', clearErr);

  // The sitekey is public. Retrieve it from the same Worker to avoid hardcoding
  // it across 6 generated pages. The private Turnstile secret never leaves the Worker.
  function initCaptcha() {
    if (local) return;
    fetch('/api/contact-config', { headers: { Accept: 'application/json' }, cache: 'no-store' })
      .then(function (r) { if (!r.ok) throw new Error('No Turnstile config'); return r.json(); })
      .then(function (cfg) {
        if (!cfg || !cfg.ok || typeof cfg.siteKey !== 'string') throw new Error('Invalid Turnstile config');
        var tag = document.createElement('script');
        tag.src = 'https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit';
        tag.async = true;
        tag.onload = function () {
          try {
            captchaId = window.turnstile.render('#turnstile-container', {
              sitekey: cfg.siteKey,
              theme: 'dark',
              action: 'scenovis_contact',
              appearance: 'interaction-only',
              'response-field': false,
              callback: function () { clearErr(); },
              'expired-callback': function () { resetCaptcha(); },
              'error-callback': function () { /* retry is controlled by Turnstile */ }
            });
            captchaReady = true;
          } catch (e) { captchaUnavailable = true; }
        };
        tag.onerror = function () { captchaUnavailable = true; };
        document.head.appendChild(tag);
      }).catch(function () { captchaUnavailable = true; });
  }
  initCaptcha();

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    clearErr();
    status.className = 'form-status'; status.textContent = '';
    var kind = contactKind(input.value);
    if (kind !== 'phone' && kind !== 'email') { showContactError(kind); return; }
    var d = data();
    if (local) { fallback(T.f_preview, d); return; }
    if (captchaUnavailable) { fallback(T.f_turnstile_unavailable, d); return; }
    if (!captchaReady) { err.textContent = T.f_turnstile_wait; return; }
    var token = window.turnstile.getResponse(captchaId);
    if (!token) { err.textContent = T.f_turnstile_check; return; }
    d.turnstileToken = token;

    submit.disabled = true; submit.textContent = T.f_sending;
    form.setAttribute('aria-busy', 'true');
    fetch(form.getAttribute('action'), {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify(d)
    }).then(function (r) {
      return r.json().catch(function () { return {}; }).then(function (j) {
        if (!r.ok || j.ok !== true) throw new Error(j.error || 'delivery');
      });
    }).then(function () {
      status.className = 'form-status is-ok';
      status.textContent = T.f_success;
      status.focus();
      track('lead_form_submit', { form_topic: d.topic || 'general', has_details: !!(d.event || d.city || d.date || d.area || d.budget) });
      form.reset();
    }).catch(function (e) {
      if (e.message === 'turnstile') {
        err.textContent = T.f_turnstile_check;
        status.focus();
      } else if (e.message === 'contact') {
        showContactError(contactKind(input.value));
      } else {
        fallback(T.f_fail, d);
      }
    }).then(function () {
      resetCaptcha(); // Tokens are single use, including after an API error.
      submit.disabled = false; submit.textContent = T.f_submit;
      form.removeAttribute('aria-busy');
    });
  });
})();
