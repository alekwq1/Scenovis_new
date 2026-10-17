# Scenovis 2026 — audyt, research, decyzje i zmiany

Data: 17.10.2026. Punkt wyjścia: repozytorium `Scenovis_new` (commit „Scenovis V5 – formularz i mobile”) i wersja live na `scenovis.malyshkogrodno.workers.dev`.
Kopia oryginału: historia git (commit `3ce9218`).

## 1. Audyt stanu wyjściowego

| Obszar | Ustalenia |
|---|---|
| **Pozycjonowanie** | Strona mówiła o „organizacji całych wydarzeń”, hostessach i zespole dwóch osób. Brak głównej przewagi: przejrzystych kosztów stoiska. Brak słów, które wpisuje klient z Google: „projekt stoiska targowego”, „wizualizacja stoiska”. |
| **Hosting vs formularz** | **Krytyczne:** strona działa na Cloudflare Workers, a formularz był skonfigurowany pod Netlify Forms (`data-netlify`). Na Cloudflare taki POST nigdzie nie trafia, więc zapytania najpewniej przepadały. Polityka prywatności też opisywała Netlify. |
| **PL/EN** | Jeden URL + `?lang=` + słownik JS (z resztkami RU). Google traktuje to jako jedną stronę. Treść EN była widoczna dla robota tylko po wykonaniu JS. Brak hreflang. |
| **CSS** | Dwa arkusze, ok. 10 warstw nadpisań (v12, v13, V3, V4, V5…), sprzeczne reguły, `!important`. Trudne w utrzymaniu. |
| **Typografia** | `Inter` był wpisany w CSS, ale nigdy nie ładowany — każdy widział font systemowy (Segoe/SF/Roboto). Etykiety 8–11 px, pogrubione wersaliki. |
| **Dostępność** | Dobre podstawy (skip link, fokus, reduced motion). Problemy: etykiety 8–10 px, `label-content-name-mismatch` (Lighthouse), placeholder jako jedyna podpowiedź formatu, cele dotykowe ok. 30 px w przełączniku języka. |
| **SEO** | Brak canonical, hreflang, robots.txt, sitemap, danych strukturalnych, OG image i Twitter card. `<title>` ustawiany przez JS. |
| **Wydajność** | Hero 190 KB WebP bez wariantów rozmiaru. Nieużywany PNG Lizy 2,5 MB w repo. 413 KB na stronę mobilną (Lighthouse). |
| **Zaufanie** | Uczciwe oznaczenie „Koncepcja AI” (zostaje). Brak dowodu działania (film tylko jako „tu pojawi się”). Gmail jako jedyny e-mail. Polityka z placeholderem administratora. |
| **Konwersja** | Krótki formularz był dobrym pomysłem i zostaje. Brakowało drogi awaryjnej, gdy wysyłka się nie uda, oraz kontekstu (targi, termin, m²). |

## 2. Research (2025–2026) — wnioski

Źródła: Google Search Central (wersje językowe, zarządzanie stronami wielojęzycznymi, VideoObject, Organization, LocalBusiness), web.dev (Core Web Vitals), W3C WAI (WCAG 2.2), pomoc Google Ads (landing page experience) oraz strony firm z branży stoisk (m.in. Quadrant2Design, Plus Exhibition Stands, Uit Holland).

- **Wersje językowe:** Google zaleca osobne URL dla wersji językowych, hreflang ze wzajemnymi odnośnikami i pełnymi adresami oraz x-default. Odradza parametry URL i **automatyczne przekierowania według języka**. → `/pl/`, `/en/`, ręczny przełącznik, x-default → `/en/`.
- **VideoObject:** wymagane `name`, `thumbnailUrl`, `uploadDate`, zalecane `contentUrl`, `duration`, `description`. → Generator tworzy VideoObject dopiero, gdy film istnieje (bez fikcyjnych dat).
- **Organization:** brak pól wymaganych. **LocalBusiness/ProfessionalService wymaga adresu.** → Dziś `Organization` + `Person`, a po podaniu adresu automatycznie `ProfessionalService`. Bez `aggregateRating`.
- **FAQ rich results** Google pokazuje dziś tylko dla stron rządowych i medycznych → FAQ jest dla ludzi, bez FAQPage JSON-LD.
- **Core Web Vitals:** LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1 (75. percentyl).
- **WCAG 2.2 AA:** m.in. 2.5.8 Target Size (min. 24×24 px), 2.4.11 Focus Not Obscured, 3.3.7 Redundant Entry.
- **Google Ads:** jakość strony docelowej = trafność i użyteczność dla osoby, która kliknęła reklamę. → Osobne landingi pod dwie intencje, ta sama obietnica w H1 co w reklamie.
- **Konkurencja:** duże firmy stawiają na liczby (lata, projekty, opinie), logotypy klientów i „darmowy projekt”. Ceny pokazują ogólnikowo (widełki lub kalkulator). Nikt z przeglądanych nie pokazuje **podziału kosztów na zakup / wynajem / usługę z wariantami** — to realna nisza dla Scenovis.

### Odpowiedzi na 5 pytań z briefu

1. **Co zachować:** grafit + pomarańcz, sticky header, duży hero, płynne przewijanie, statyczny HTML, krótki formularz, PL/EN, uczciwe oznaczenie ilustracji AI.
2. **Co jest przestarzałe lub nieczytelne:** `?lang=` + JS, etykiety 8–10 px w wersalikach, karuzela w hero, 4 filary z hostessami, „Dwie osoby…”, warstwy CSS, Netlify na Cloudflare.
3. **Co zwiększy zaufanie:** prawdziwy film z działającej prezentacji, prawdziwe screeny zamiast ilustracji AI, jasny podział „co robię sam / co robią wykonawcy”, e-mail we własnej domenie, uzupełniona polityka, brak przesadnych obietnic.
4. **Co zwiększy liczbę wartościowych zapytań:** przewaga „wiesz, za co płacisz” widoczna od razu w hero, landingi pod konkretne intencje (Ads), opcjonalne pola o targach (lepsza jakość leada bez dodatkowego tarcia), formularz, który nie gubi zapytań, CTA po obejrzeniu filmu.
5. **Moda, której nie dodaję:** karuzele, scroll-jacking i animacje każdej sekcji, model 3D w przeglądarce (ciężki, słaby na telefonach), chatboty, liczniki „lat doświadczenia”, kalkulator cen bez prawdziwych danych, light/dark toggle (marka jest ciemna).

## 3. Kierunek wizualny

Rozważone warianty:
- **A. Grafit + pomarańcz, „dokumentacja techniczna” — wybrany.** Zostaje charakter, który lubisz. Wyróżnik: adnotacje na stoisku (punkt, linia odniesienia, etykieta „zakup / wynajem / usługa”) i zestawienie elementów jak w dokumentacji (kody K-01, G-02…). To język BIM, czyli Twoja realna przewaga, a nie dekoracja.
- B. Jasny „blueprint” (papier, cienkie linie). Czytelny, ale zrywa z obecną marką i gorzej eksponuje rendery.
- C. Bardzo ciemny, wysoki kontrast + szeryfowy display. Efektowny, ale „luksusowo-eventowy” — pasowałby do agencji, nie do technicznego podejścia.

**Typografia:** jedna rodzina — **Inter Variable z osią optycznego rozmiaru** (nagłówki automatycznie dostają krój „Display”). Self-hosted WOFF2, podzbiór PL+EN, wagi 400–700: **46 KB, licencja SIL OFL**. Druga rodzina display nie była potrzebna, bo oś opsz daje charakter nagłówków bez kosztu kolejnego pliku.

**Kontrast (WCAG AA):** tekst #f1efe8 na #121617 ≈ 16:1; tekst drugorzędny #c4ccc9 ≈ 11:1; meta #a3adaa ≈ 7,9:1; ciemny tekst na przycisku #ff9364 ≈ 8,4:1. Minimalny tekst 12 px (wcześniej 8–10 px). Axe: 0 naruszeń na wszystkich stronach.

## 4. Architektura informacji

**Strona główna:** Hero (stoisko z adnotacjami kosztów) → W skrócie (dla kogo + 4 punkty) → **Przykład: film** → Oferta (3 filary) → **Koszty: „Nie tylko render. Wiesz, za co płacisz.”** → O mnie (+ „w czym pomagam” / „z kim współpracuję”) → Współpraca (5 kroków) → FAQ → Kontakt.
Kolejność jak w briefie, z jedną zmianą: „jak wykorzystywani są wykonawcy” jest częścią „O mnie” (jeden schemat zamiast dwóch sekcji), a proces jest osobno.

**Landingi pod Ads** (bez menu, jedno CTA, ta sama obietnica co w reklamie):
- `/pl/projekt-stoiska-targowego/` · `/en/exhibition-stand-design/`
- `/pl/prezentacje-produktow-3d/` · `/en/3d-product-presentations/`
Opisowe slugi zamiast `/expo/`: zgodne z wyszukiwaną frazą i czytelne w wyniku wyszukiwania.

**Hero — rozważone warianty H1:**
1. „Pokaż produkt. Zrozum stoisko. Kontroluj budżet.” — **wybrany na stronę główną** (Twój kierunek, rytm, trzy obietnice).
2. „Projekt stoiska targowego, w którym widać koszty.” — **wybrany na landing EXPO** (zawiera frazę z wyszukiwarki).
3. „Stoisko, które rozumiesz, zanim zapłacisz.” — odrzucony: ładny, ale nie mówi, co robisz.

**Ton „O mnie”** (zgodnie z Twoją uwagą): bez „za wszystko odpowiadam”. Zamiast tego: „Cześć, jestem Aleks… mam doświadczenie w BIM… pomagam firmom dobrze przygotować się do targów… współpracuję z wykonawcami”.

## 5. Co zmieniłem

- Usunięte: Liza (profil, zdjęcia 2,7 MB, LinkedIn, tłumaczenia, aria), „Dwie osoby. Jedno podejście.”, hostessy i organizacja eventów jako filary, sekcja „Planujesz wydarzenie w Polsce?”, słowniki RU, `site.css` + `refinements.css` + `site.js`, `netlify.toml`, README_V5.
- Nowe: 8 stron (PL/EN × główna, 2 landingi, polityka) + 404, generator, jeden arkusz CSS, nowy JS, Worker, `_headers` (CSP, cache), `robots.txt`, `sitemap.xml` z hreflang, favicon (ICO/SVG/Apple), OG 1200×630 PL/EN, JSON-LD (Organization, WebSite, WebPage, Person, Service, BreadcrumbList; VideoObject gotowy), obrazy AVIF/WebP w 3–4 rozmiarach.
- Formularz: 1 pole wymagane, imię i wiadomość opcjonalne, szczegóły targów zwinięte (progressive disclosure), temat ustawiany z przycisków usług, honeypot, walidacja dostępna (aria-invalid, role=alert), **awaryjna wiadomość e-mail/WhatsApp z gotową treścią**, gdy wysyłka się nie uda.
- Film: natywny `<video>`, `preload="none"`, poster, `playsinline`, napisy PL/EN, transkrypcja, brak autoplay, CTA po zakończeniu, zdarzenia 25/50/100%. Przetestowany na klipie testowym.
- Stare linki działają: `/?lang=en` → `/en/`, `/privacy.html` → polityka, `#services/#about/#contact` → nowe kotwice PL.

## 6. Pomiary (rzeczywiste, nie szacunki)

Lighthouse 12 (lokalnie, Worker przez `wrangler dev`, throttling symulowany). Wyniki laboratoryjne z localhost — po wdrożeniu sprawdź PageSpeed Insights i dane terenowe w Search Console.

| Strona | Profil | Perf | A11y | BP | SEO | LCP | CLS | TBT | Waga |
|---|---|---|---|---|---|---|---|---|---|
| Stara (index.html) | mobile | 92 | 100 | 100 | 100 | 3,3 s | 0 | – | 413 KiB |
| Nowa `/pl/` | mobile | 100 | 100 | 100 | 100 | 1,6 s | 0 | 0 ms | 114 KiB |
| Nowa `/pl/` | desktop | 100 | 100 | 100 | 100 | 0,4 s | 0 | 0 ms | 114 KiB |
| Landing EXPO PL | mobile | 100 | 100 | 100 | 100 | 1,6 s | 0 | 20 ms | 113 KiB |
| Landing 3D EN | mobile | 100 | 100 | 100 | 100 | 1,5 s | 0 | 0 ms | 94 KiB |

INP nie da się zmierzyć w laboratorium. JS jest mały (11 KB, 3,8 KB po gzip, bez zależności), TBT 0–20 ms.

Testy: axe-core (WCAG 2.0/2.1/2.2 AA + best practices) — 0 naruszeń na 9 stronach przy 1440 i 390 px. Brak poziomego przewijania przy 360, 390, 430, 768, 1024, 844×390 (landscape), 1280, 1920. Klawiatura: skip link, menu (Esc), zakładki wariantów (strzałki/Home/End), FAQ, formularz. CSP: brak naruszeń w konsoli.

## 7. Czego świadomie nie zrobiłem

- Nie uruchomiłem analityki ani reklam (brak zgody / CMP) — tylko `dataLayer`.
- Nie wpisałem cen, liczby projektów, lat doświadczenia, klientów ani opinii.
- Nie podmieniłem ilustracji AI na „realizacje” — nadal są oznaczone jako koncepcja.
- Nie skonfigurowałem wysyłki e-mail (wymaga Twojego konta / domeny).


## Aktualizacja 17.10.2026 — „Scenovis 2026” (ulepszenie, nie nowa strona)

Wygląd, grafiki, zdjęcia, placeholder filmu, paleta i typografia — bez zmian. Zmiany w źródłach generatora, nie w HTML.

| Obszar | Zmiana | Pliki |
|---|---|---|
| Pozycjonowanie | Dwie równorzędne usługi (projekt stoiska / prezentacje 3D) w hero, menu, ofercie, stopce; „Realizacja” jako opcjonalna koordynacja przez wykonawców | `content.py`, `build.py` |
| Hero | Krótszy lead (obie usługi), jedno główne CTA „Opowiedz o swoim projekcie” + dwa linki do usług | `content.py`, `build.py`, `site.css` |
| Podstrona 3D | Sekcja „Przykład” opisuje prezentację produktu (nie koszty stoiska), uczciwie: nagranie w przygotowaniu, projekt koncepcyjny | `build.py` (`case(kind="3d")`) |
| Podstrony usług | Odnośnik do drugiej usługi („osobno lub razem”) | `build.py` (`cross`) |
| O mnie | Bio: BIM, koordynacja modeli 3D, wizualizacja; wyraźny podział: co robię sam / co robią wykonawcy | `content.py` |
| FAQ | Osobne zestawy: EXPO (proces, wycena, wykonawcy, terminy) i 3D (formy, dane, urządzenia, ponowne użycie, „czy musi być z targami”) | `content.py`, `build.py` |
| CTA | Kontekstowe: „Omów projekt stoiska”, „Porozmawiajmy o prezentacji produktu”, „Opowiedz o swoim projekcie”; nagłówek kontaktu zależny od podstrony | `content.py`, `build.py` |
| Formularz | Widoczne pole „Temat” (ustawiane przez CTA, domyślne na podstronach), brak limitu cyfr telefonu, walidacja e-maila, osobne komunikaty; honeypot bez napisu „Website”, odporny na brak CSS | `build.py`, `site.js`, `site.css` |
| Worker | Wspólna reguła `contactKind`, sukces dopiero po `id` z Resend, `reply_to` tylko dla e-maila, `LEAD_TO_EMAIL`/`LEAD_FROM_EMAIL`, diagnostyka `missing`, logi bez danych osobowych | `worker/index.js` |
| Wdrożenie | `keep_vars`, `observability`; stare pliki V5 i `*.md` wykluczone z publikacji | `wrangler.jsonc`, `.assetsignore` |
| Kontakt | +48 734 215 791 (tel:, wa.me, JSON-LD, stopka, 404) | `config.py` |
| Prywatność | Opis faktycznego przepływu (Worker bez bazy danych, Turnstile, Resend, Namecheap, metadane wiadomości); placeholdery dla danych administratora i retencji; baner „wersja robocza” do czasu ich uzupełnienia | `build.py` |
| UX | Wyrównanie kart oferty (subgrid), kompaktowe linki usług na mobile | `site.css` |

Diagnoza `not_configured`: sekrety wpisane w Cloudflare „Build → Variables and secrets” (zmienne budowania), a nie jako zmienne runtime Workera.

Testy: `node tools/test_form_worker.mjs` (15 przypadków kontaktu + Turnstile/Resend/konfiguracja), test przeglądarkowy formularza PL/EN z symulowanym API, zrzuty 360/390/430/768/1024/1440/1920 px bez poziomego przewijania, `wrangler deploy --dry-run`. Prawdziwa wysyłka przez Resend — niepotwierdzona (wymaga sekretów runtime).
