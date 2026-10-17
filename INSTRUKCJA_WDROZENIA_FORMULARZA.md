# SCENOVIS — wdrożenie i formularz (Windows PowerShell)

Stan: 17.10.2026 | Cloudflare Workers + Resend + Turnstile | odbiorca: `contact@scenovis.com`

---

## 0. Dlaczego formularz zwracał `{"ok":false,"error":"not_configured"}`

Na zrzucie z panelu Cloudflare (`Workers & Pages → scenovis → Settings`) klucze
`RESEND_API_KEY`, `TURNSTILE_SECRET` i `TURNSTILE_SITE_KEY` są wpisane w sekcji
**Build → Variables and secrets**. To są zmienne **środowiska budowania** — istnieją tylko
w trakcie polecenia `npx wrangler deploy` w Cloudflare Builds. **Działający Worker ich nie widzi**,
więc `/api/contact-config` i `/api/lead` odpowiadają `not_configured`.

Sekcja **Runtime → Variables and secrets** u góry tej samej strony jest wyszarzona z komunikatem
„cannot be added to a Worker that only has static assets”. To znaczy, że w chwili zrzutu aktywna
wersja Workera nie zawierała skryptu `worker/index.js` (np. ostatnie wdrożenie było sprzed
dodania Workera albo się nie powiodło). Po wdrożeniu tej wersji kodu sekcja Runtime się odblokuje.

Naprawa = (1) wdrożyć ten kod, (2) ustawić te same trzy wartości jako zmienne **runtime** Workera
(krok 3 poniżej). Wpisy w „Build → Variables and secrets” możesz potem usunąć — kod ich nie używa.

Po wdrożeniu nowej wersji adres `/api/contact-config` dodatkowo pokazuje **nazwy** brakujących zmiennych
(nigdy wartości), np. `{"ok":false,"error":"not_configured","missing":["TURNSTILE_SITE_KEY"]}`.

---

## 1. Uruchomienie lokalnie

Wymagany Python 3.9+ i Node.js 20+.

```powershell
cd C:\ścieżka\do\Scenovis_new
python tools\build.py
python -m http.server 8080
# otwórz w przeglądarce: http://localhost:8080/pl/  oraz  http://localhost:8080/en/
```

Lokalnie formularz celowo nie wysyła — pokazuje gotową wiadomość e-mail / WhatsApp.

Podgląd z działającym Workerem (bez prawdziwej wysyłki, sekrety lokalne w `.dev.vars`, plik jest w `.gitignore`):

```powershell
npx wrangler dev
# http://localhost:8787/pl/
```

## 2. Przebudowa i testy

```powershell
python tools\build.py
node --check assets\js\site.js
node --check worker\index.js
node tools\test_form_worker.mjs
```

`test_form_worker.mjs` sprawdza m.in., że reguła walidacji w przeglądarce i w Workerze jest identyczna,
oraz 15 przypadków pola „Telefon lub e-mail”. Testy **symulują** Turnstile i Resend — nie zastępują
testu prawdziwej wiadomości (krok 5).

## 3. Sekrety runtime Workera (jednorazowo)

Wartości bierzesz z paneli, **nie** z repozytorium:

- `RESEND_API_KEY` — Resend → API Keys → klucz „Scenovis Contact Form” (Sending access, `forms.scenovis.com`).
  Pełna wartość `re_…` jest widoczna tylko przy tworzeniu klucza. Jeśli jej nie masz, utwórz nowy klucz z tym samym zakresem.
- `TURNSTILE_SECRET` — Cloudflare → Turnstile → „Scenovis Contact Form” → **Secret Key**.
- `TURNSTILE_SITE_KEY` — ten sam widget → **Site Key** (publiczny, zaczyna się od `0x4AAAA…`).

Najpierw wdroż kod (krok 4), potem w PowerShell, w katalogu repozytorium:

```powershell
npx wrangler login
npx wrangler secret put RESEND_API_KEY
npx wrangler secret put TURNSTILE_SECRET
npx wrangler secret put TURNSTILE_SITE_KEY
npx wrangler secret list
```

Każde `secret put` poprosi o wklejenie wartości (nie pojawi się na ekranie ani w historii poleceń).
Alternatywa w panelu: `Workers & Pages → scenovis → Settings → Variables and Secrets` (sekcja **Runtime**, nie Build) → Add → Type: **Secret**.

Opcjonalnie (domyślne wartości są w kodzie, nie musisz ich ustawiać):

```powershell
npx wrangler secret put LEAD_TO_EMAIL     # domyślnie contact@scenovis.com
npx wrangler secret put LEAD_FROM_EMAIL   # domyślnie Scenovis <form@forms.scenovis.com>
```

`wrangler.jsonc` ma `"keep_vars": true`, więc kolejne wdrożenia nie skasują zmiennych ustawionych w panelu.
Sekrety są zachowywane zawsze.

## 4. Wdrożenie przez GitHub i Cloudflare

Repozytorium `alekwq1/Scenovis_new` jest połączone z Workerem (Build: puste, Deploy: `npx wrangler deploy`, Root: `/`).

```powershell
git status
git add -A
git commit -m "Scenovis 2026: dwie usługi, formularz, Worker/Resend, nowy telefon"
git push origin main
```

Albo ręcznie z komputera: `npx wrangler deploy`.

Potem: Cloudflare → `Workers & Pages → scenovis → Deployments` → ostatnia wersja ma status **Success**
i pochodzi z najnowszego commita. W `Settings` sekcja **Runtime → Variables and secrets** powinna być aktywna.

## 5. Sprawdzenie konfiguracji i dostarczenia zapytania

```powershell
Invoke-RestMethod https://scenovis.malyshkogrodno.workers.dev/api/contact-config
```

Oczekiwane: `ok : True` i `siteKey : 0x4AAAA…`. Jeśli `not_configured` — pole `missing` mówi, czego brakuje.

Test właściwy (tylko w przeglądarce — Turnstile wymaga prawdziwej przeglądarki):

1. `https://scenovis.malyshkogrodno.workers.dev/pl/#kontakt` — wpisz swój e-mail, temat „Projekt stoiska”, wiadomość `Test formularza PL`.
2. Po wysłaniu ma się pojawić „Dziękuję — zapytanie zostało wysłane”. Ten komunikat pojawia się **wyłącznie**, gdy Resend potwierdzi przyjęcie wiadomości.
3. Sprawdź skrzynkę `contact@scenovis.com` (Namecheap). „Odpowiedz” powinno wskazywać e-mail z formularza.
4. Powtórz na `/en/#contact` z numerem telefonu (np. `+49 (0) 123 456789`) — wiadomość dotrze, bez Reply-To, telefon w treści.
5. Resend → **Emails / Logs**: obie wiadomości ze statusem *Delivered*.
6. Przy błędzie: Cloudflare → Workers → scenovis → **Observability / Logs** (Worker loguje tylko kod błędu Resend, bez danych klienta).

Szybki test odrzucenia bez tokenu Turnstile (nie wysyła e-maila, ma zwrócić błąd 403 `turnstile`):

```powershell
$body = '{"contact":"test@example.com","message":"test"}'
try { Invoke-RestMethod -Method Post -Uri https://scenovis.malyshkogrodno.workers.dev/api/lead -ContentType 'application/json' -Body $body }
catch { $_.ErrorDetails.Message }
```

## 6. Czego NIE robić

- Nie wpisuj kluczy do `wrangler.jsonc`, `tools/config.py`, frontendu ani GitHuba.
- Nie zmieniaj rekordów MX Namecheap ani DNS `forms.scenovis.com` — wysyłka działa bez tego.
- Nie podłączaj domeny `scenovis.com` do Workera, zanim nie zdecydujesz o docelowej domenie (`SITE_URL`).
- Nie ustawiaj `DRAFT = False`, dopóki polityka prywatności ma niewypełnione pola (TODO.md, B1–B3).
