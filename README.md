# Scenovis — strona (wersja 2026)

Statyczny HTML/CSS/JS bez frameworka + mały Worker Cloudflare (przekierowania i formularz).
Strony powstają z jednego źródła treści generatorem w Pythonie — dzięki temu PL i EN są zawsze spójne.

## Struktura

```
pl/  en/                      gotowe strony (generowane — nie edytuj ręcznie)
  index.html                  strona główna
  projekt-stoiska-targowego/  landing EXPO  (EN: exhibition-stand-design/)
  prezentacje-produktow-3d/   landing 3D    (EN: 3d-product-presentations/)
  polityka-prywatnosci/       polityka      (EN: privacy-policy/)
index.html, privacy.html      rezerwowe przekierowania ze starych adresów
site.js, site.css, refinements.css, netlify.toml   stara wersja V5 — nieużywana, wykluczona z publikacji (.assetsignore), można usunąć
404.html, robots.txt, sitemap.xml, favicon.ico, _headers
assets/css/site.css           jedyny arkusz stylów
assets/js/site.js             menu, warianty kosztów, film, formularz (walidacja = worker), dataLayer
assets/fonts/inter-var.woff2  Inter Variable (OFL), podzbiór PL+EN, 46 KB
assets/img/  assets/og/  assets/icons/  assets/video/
tools/content.py              ← TU EDYTUJESZ TEKSTY (PL i EN)
tools/config.py               ← domena, kontakt, film, tryb roboczy
tools/build.py                generator
worker/index.js, wrangler.jsonc, .assetsignore   Cloudflare
docs/RAPORT.md                audyt, research, decyzje, zmiany, pomiary
docs/CHECKLISTS.md            prywatność, Google Ads / Analytics, zdarzenia
TODO.md                       co musisz dostarczyć / uzupełnić
```

## Edycja treści

1. Zmień tekst w `tools/content.py` (każdy klucz ma wersję PL i EN).
2. Uruchom `python3 tools/build.py` (Python 3.9+, bez instalowania pakietów).
3. Podejrzyj: `python3 -m http.server 8080` i otwórz `http://localhost:8080/pl/`.
   Lokalnie formularz celowo nie wysyła — pokazuje gotową wiadomość e-mail.

`{todo:...}` w treści = pomarańczowy znacznik widoczny tylko w trybie roboczym (`DRAFT = True`).
Przed publikacją produkcyjną ustaw `DRAFT = False` w `tools/config.py` i przebuduj.

## Publikacja — Cloudflare Workers

Strona działa dziś na `scenovis.malyshkogrodno.workers.dev`. Repozytorium zawiera `wrangler.jsonc`:

- Cloudflare → Workers & Pages → projekt → Settings → Build:
  Build command: *(puste)*, Deploy command: `npx wrangler deploy`, Root: `/`.
- Albo ręcznie: `npx wrangler deploy` w folderze repozytorium.
- `.assetsignore` pilnuje, żeby `tools/`, `worker/`, `docs/` i README nie były publiczne.
- `_headers` ustawia nagłówki bezpieczeństwa (CSP) i cache. **Po dodaniu Google tag / GTM trzeba rozszerzyć CSP** — zob. `docs/CHECKLISTS.md`.

Worker obsługuje: `/` → 301 na `/pl/` (lub `/en/` dla starego `?lang=en`), `/privacy.html` → nowa polityka, `POST /api/lead`.

## Formularz — Resend + Cloudflare Turnstile

**Obecna integracja:** formularz PL/EN wysyła `POST /api/lead` do tego samego Cloudflare Workera. Worker obowiązkowo waliduje token Turnstile za pomocą Cloudflare Siteverify i dopiero wtedy używa API Resend. Odpowiedzi przychodzą na `contact@scenovis.com` (alias skrzynki Namecheap); nadawcą automatu jest `Scenovis <form@forms.scenovis.com>`. Dla adresów e-mail podanych przez klientów ustawiony jest nagłówek `Reply-To`.

**Zmienne runtime Workera** (instrukcja krok po kroku z poleceniami PowerShell: `INSTRUKCJA_WDROZENIA_FORMULARZA.md`):

| Type | Name | Value |
|---|---|---|
| Secret | `RESEND_API_KEY` | Klucz `re_...` Resend ograniczony do Sending access dla `forms.scenovis.com` |
| Secret | `TURNSTILE_SECRET` | Tajny klucz Turnstile |
| Secret lub Text | `TURNSTILE_SITE_KEY` | Publiczny Site Key z tego samego widgetu Turnstile |
| opcjonalnie | `LEAD_TO_EMAIL`, `LEAD_FROM_EMAIL` | Domyślnie `contact@scenovis.com` i `Scenovis <form@forms.scenovis.com>` |

**Ważne:** muszą być ustawione jako zmienne *runtime* (`npx wrangler secret put …` albo Settings → Variables and Secrets, sekcja Runtime), a **nie** w „Build → Variables and secrets” — tam Worker ich nie widzi i zwraca `not_configured`. `wrangler.jsonc` ma `keep_vars: true`, więc deploy nie kasuje zmiennych z panelu.

**Walidacja pola „Telefon lub e-mail”** — jedna reguła (`contactKind`) skopiowana 1:1 do `assets/js/site.js` i `worker/index.js`; test pilnuje, żeby się nie rozjechały:
- wpis z `@` musi wyglądać jak adres (`nazwa@domena.pl`), inaczej komunikat o błędnym e-mailu,
- wpis bez `@` z co najmniej jedną cyfrą = telefon, bez limitu liczby cyfr i bez formatowania (zapisywany dokładnie tak, jak go wpisano),
- puste pole → prośba o telefon lub e-mail. Limit 140 znaków to zabezpieczenie rozmiaru, nie walidacja cyfr.

**Status wysyłki:** „wysłano” pokazuje się dopiero po odpowiedzi Resend z identyfikatorem wiadomości. Każdy błąd (Turnstile, brak konfiguracji, błąd Resend) pokazuje prawdziwy status i gotowe przyciski e-mail / WhatsApp.

**Test po wdrożeniu**: `INSTRUKCJA_WDROZENIA_FORMULARZA.md`, krok 5. Testy automatyczne: `node tools/test_form_worker.mjs`.

Na podglądzie lokalnym (file:// i localhost) formularz pokazuje awaryjny `mailto:` — nie wysyła do API.

**Awaria integracji:** na stronie pozostają bezpieczne linki do bezpośredniego kontaktu e-mail/WhatsApp, a formularz NIE pokazuje potwierdzenia wysłania. Wysyłka ma limity Resend; rozważ dodatkową regułę Cloudflare Rate Limiting na `/api/lead` przed kampaniami.

**Prywatność:** w tekście polityki wpisano Resend, Cloudflare Turnstile oraz Namecheap Private Email. Przed publikacją uzupełnij pola TODO dotyczące administratora danych, retencji i podstaw przekazywania danych dostawcom. 

## Rendery z Blendera (obrazy na stronie)

Obrazy w hero, sekcji „Przykład” i na podstronach usług to rendery projektu demonstracyjnego
`D:\Prywat\SCENOVIS\MODELE\SCENOVIS_EXPO_BOOTH\EXPO_INTERACTIVE_PRESENTATION.blend` (Cycles, OptiX).
Źródłowe PNG: `D:\Prywat\SCENOVIS\WWW_RENDERS\final`. Rozmiary i nazwy: słownik `IMG` w `tools/build.py`,
opisy alternatywne: klucz `alt` w `tools/content.py`. Znaczniki na obrazie w hero (`.tag--*` w `site.css`)
mają współrzędne w pełnym kadrze 16:9 — po podmianie renderu trzeba je zaktualizować.

## Dodanie filmu EXPO

1. Wgraj do `assets/video/`: MP4 (H.264 + AAC, 1920×1080), poster (JPG/WebP 1920×1080), napisy `*.pl.vtt` i `*.en.vtt`.
2. Uzupełnij słownik `VIDEO` w `tools/config.py` (przykład jest w pliku).
3. `python3 tools/build.py` — pojawi się odtwarzacz, napisy, zdarzenia video_* i dane VideoObject.
4. Wklej transkrypcję do `case_transcript_body` w `tools/content.py`.

## Zmiana domeny

`SITE_URL` w `tools/config.py` → przebuduj. Zmienią się canonical, hreflang, sitemap, OpenGraph i dane strukturalne.
Na starym adresie `workers.dev` ustaw przekierowanie 301 na nową domenę (szczegóły w TODO.md).

## Hosting poza Cloudflare

Strony działają na każdym hostingu statycznym (rezerwowe przekierowania w `index.html` i `privacy.html`), ale formularz wymaga odpowiednika `/api/lead`, a nagłówki z `_headers` trzeba przenieść do konfiguracji tego hostingu.

## Podmiana grafik wariantów i filmu (18.10.2026)

**Trzy obrazy wariantów (hero):**
1. Przygotuj `stoisko-economy.png`, `stoisko-smart.png`, `stoisko-premium.png` — ta sama kamera (CAM_EXPO_MAIN), 16:9.
2. `python tools/warianty.py FOLDER_Z_PNG` → pliki trafią do `assets/img/warianty/` (AVIF + WebP, 4 rozmiary).
3. Za pierwszym razem ustaw `VARIANT_RENDERS = True` w `tools/config.py` i uruchom `python tools/build.py`.
   Każdą kolejną poprawkę obrazów wystarczy wgrać tym samym skryptem — nazwy plików są stałe, bez przebudowy HTML.
4. Punkty z opisami: treść w `tools/content.py` → `variants`, położenie w `assets/css/site.css` (`.tag--screen` itd.).

**Film (sekcja „Zobacz stoisko”):** pliki do `assets/video/`, uzupełnij `VIDEO` w `tools/config.py`, potem `python tools/build.py`.

**Wideo w oknie hero podstrony „Projekt stoiska”:** MP4 + okładka do `assets/video/`, uzupełnij `EXPO_HERO_VIDEO` w `tools/config.py`, potem `python tools/build.py`.
Okno filmu ma ten sam rozmiar co obecna okładka.
