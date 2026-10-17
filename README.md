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
404.html, robots.txt, sitemap.xml, favicon.ico, _headers
assets/css/site.css           jedyny arkusz stylów
assets/js/site.js             menu, warianty kosztów, film, formularz, dataLayer
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

**W ustawieniach istniejącego Workera** (Cloudflare → Workers & Pages → scenovis → Settings → Variables and Secrets) ustaw:

| Type | Name | Value |
|---|---|---|
| Secret | `RESEND_API_KEY` | Klucz `re_...` Resend ograniczony do Sending access dla `forms.scenovis.com` |
| Secret | `TURNSTILE_SECRET` | Tajny klucz Turnstile; nie kopiować do repozytorium |
| Text | `TURNSTILE_SITE_KEY` | Publiczny Site Key z tego samego widgetu Turnstile |

Pierwsze dwa sekrety zostały już utworzone przez właściciela w panelu Cloudflare. **Przed wdrożeniem należy jeszcze dodać `TURNSTILE_SITE_KEY` jako Text**. Pole `Value encrypted` przy sekretach jest prawidłowe — nie wpisuj tych wartości do `wrangler.jsonc`, frontendu ani GitHuba.

W Turnstile widget musi zezwalać na hosty `scenovis.malyshkogrodno.workers.dev` i `scenovis.com`. Domenę `www` konfigurujemy dopiero przed uruchomieniem produkcji. Domeny wysyłkowej `forms.scenovis.com` (zweryfikowanej w Resend) NIE łączymy z Workerm ani nie zmieniamy rekordów Namecheap MX.

**Test po wdrożeniu**:

1. `GET https://scenovis.malyshkogrodno.workers.dev/api/contact-config` ma zwrócić JSON `ok:true` i PUBLICZNY `siteKey`. Jeśli zwraca 503, brakuje zmiennej `TURNSTILE_SITE_KEY` albo nowej wersji Workera.
2. Otwórz `/pl/`, wyślij testowe zapytanie z prawdziwym adresem e-mail.
3. Upewnij się, że pojawiło się „zapytanie zostało wysłane”, wiadomość trafiła na `contact@scenovis.com`, a w Namecheap `aleks@scenovis.com` masz możliwość odpowiedzi na adres podany w formularzu.
4. Powtórz z `/en/` oraz z numerem telefonu zamiast e-maila. Sprawdź Logs w Resend w przypadku błędu wysyłania.
5. Wyślij zapytanie bez tokenu Turnstile poprzez odpowiednio przygotowany POST testowy — serwer musi odrzucić je z błędem `turnstile` (403), bez wysłania e-maila.

Na podglądzie lokalnym (file:// i localhost) formularz pokazuje awaryjny `mailto:` — nie wysyła do API.

**Awaria integracji:** na stronie pozostają bezpieczne linki do bezpośredniego kontaktu e-mail/WhatsApp, a formularz NIE pokazuje potwierdzenia wysłania. Wysyłka ma limity Resend; rozważ dodatkową regułę Cloudflare Rate Limiting na `/api/lead` przed kampaniami.

**Prywatność:** w tekście polityki wpisano Resend, Cloudflare Turnstile oraz Namecheap Private Email. Przed publikacją uzupełnij pola TODO dotyczące administratora danych, retencji i podstaw przekazywania danych dostawcom. 

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
