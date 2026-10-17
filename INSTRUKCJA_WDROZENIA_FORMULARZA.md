# SCENOVIS — formularz: instrukcja wdrożenia

Stan: 17.10.2026 | Cloudflare Workers Free + Namecheap Private Email + Resend + Turnstile

## Co już jest skonfigurowane w panelach

- Namecheap: odbiór na `contact@scenovis.com` (alias → `aleks@scenovis.com`).
- Resend: domena wysyłkowa `forms.scenovis.com` zweryfikowana; **receiving OFF**.
- Cloudflare Worker `scenovis`: sekrety `RESEND_API_KEY` oraz `TURNSTILE_SECRET` zapisane.
- Turnstile: dozwolone `scenovis.malyshkogrodno.workers.dev` oraz `scenovis.com`.
- Główna domena `scenovis.com` pozostaje **celowo odłączona** od Workera.

## Krok 1. Dodaj tylko publiczny Site Key Turnstile

1. Cloudflare → Turnstile → otwórz widget **Scenovis Contact Form** → skopiuj **Site Key**, a NIE Secret Key.
2. Cloudflare → Workers & Pages → **scenovis** → **Settings → Variables and Secrets → Add**.
3. Dodaj **Type: Text**; **Name: TURNSTILE_SITE_KEY**; **Value: skopiowany Site Key**.
4. Zapisz / Deploy. Sprawdź, że `RESEND_API_KEY` i `TURNSTILE_SECRET` nadal widnieją jako **Secret / Value encrypted**.

Site Key jest publiczny, ale **nie przekazuj** nikomu `RESEND_API_KEY` ani `TURNSTILE_SECRET`.

## Krok 2. Wdroż kod na istniejącego Workera

1. Rozpakuj paczkę. Jej pliki (`wrangler.jsonc`, `worker/`, `assets/`, `tools/`, `pl/`, `en/` itd.) są przygotowane **bezpośrednio do katalogu głównego repozytorium**.
2. W istniejącym repozytorium strony zastąp nimi odpowiednie pliki (nie twórz nowego Workera).
3. Jeżeli repo ma już połączenie z Cloudflare, commit/push wywoła dotychczasowy deploy `npx wrangler deploy`. Jeśli robisz wdrożenie z lokalnego katalogu, użyj `npx wrangler deploy` w katalogu zawierającym `wrangler.jsonc`.
4. W Cloudflare → Workers & Pages → scenovis → **Deployments** sprawdź status **Success**. Nie podłączaj jeszcze domeny `scenovis.com`.

**Uwaga:** `DRAFT=True` oraz adres strony `workers.dev` są celowo zachowane. Nie przełączaj na `scenovis.com`, póki strona jest w budowie.

## Krok 3. Test konfiguracji

W przeglądarce otwórz:

`https://scenovis.malyshkogrodno.workers.dev/api/contact-config`

Oczekiwany wynik to JSON `{"ok":true,"siteKey":"..."}` — Site Key jest publiczny. Jeżeli widzisz `503`, sprawdź `TURNSTILE_SITE_KEY` i czy nowa wersja Workera jest wdrożona.

## Krok 4. Test wiadomości

1. Wejdź na `https://scenovis.malyshkogrodno.workers.dev/pl/#kontakt`.
2. Wypełnij formularz swoim prawdziwym adresem e-mail i napisz `Test formularza Scenovis`.
3. Wyślij. Po pozytywnej odpowiedzi API powinien pojawić się komunikat o wysłaniu.
4. Sprawdź w Namecheap Private Email (`aleks@scenovis.com`), czy dotarła wiadomość na alias `contact@scenovis.com`.
5. Odpowiedz na tę wiadomość: `Reply-To` powinien wskazywać e-mail wpisany w formularzu, a nie `form@forms.scenovis.com`.
6. Powtórz test na `/en/#contact` i opcjonalnie z telefonem zamiast e-maila. Przy błędach sprawdź **Resend → Emails / Logs** i **Cloudflare → Workers → Observability**.

## Co zostało zmienione

- `worker/index.js` — walidacja tokena Turnstile na serwerze (hostname, action), wysyłka Resend, `Reply-To`, kontrola żądań i błędów.
- `assets/js/site.js` — widget Turnstile i komunikaty PL/EN; formularz nie pokazuje sukcesu, gdy API zwróci błąd.
- `tools/config.py` — publiczny adres kontaktowy `contact@scenovis.com`.
- `tools/build.py`, `tools/content.py` — integracja widgetu, lokalizacja komunikatów i informacja o dostawcach w projekcie polityki prywatności.
- `_headers` — CSP pozwalający wczytać zasoby Turnstile.
- `assets/css/site.css` — drobny styl pola zabezpieczeń. Reszta wyglądu bez zmian.
- Wygenerowane strony `/pl/` i `/en/` — przebudowane z oryginalnego generatora.

## Ważne przed publicznym startem

- Uzupełnij `TODO.md`: dane administratora, retencję, weryfikację DPA/RODO oraz docelową domenę.
- Potwierdź numer telefonu/WhatsApp w `tools/config.py`.
- Wykonaj realny test wysyłki oraz zabezpieczeń na `workers.dev`.
- Dopiero potem podłącz `scenovis.com` i zdecyduj o przekierowaniu `www`.
- W razie większej liczby zgłoszeń dołóż regułę Cloudflare Rate Limiting dla `POST /api/lead`.

## Testy wykonane przed przekazaniem paczki

`node --check assets/js/site.js`

`node --check worker/index.js`

`node tools/test_form_worker.mjs`

`python tools/build.py`

Testy symulują wysyłkę — **nie zastępują testu wiadomości z prawdziwej strony.**
