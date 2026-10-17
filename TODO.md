# TODO — co musisz dostarczyć lub zdecydować

Strona działa bez tych materiałów (są eleganckie placeholdery i znaczniki `[TODO: …]` widoczne w trybie roboczym).
Wszystkie znaczniki znajdziesz poleceniem: `grep -rn "todo:" tools/`

## BLOCKERY przed produkcją / kampaniami

| # | Co | Dlaczego blokuje | Gdzie |
|---|----|------------------|-------|
| B1 | **Dane administratora danych** (pełna nazwa / imię i nazwisko, adres, NIP jeśli jest) | Polityka prywatności bez administratora jest niezgodna z RODO (art. 13) | `PRIVACY` w `tools/build.py` |
| B2 | **Sekrety runtime + test wysyłki** — `RESEND_API_KEY`, `TURNSTILE_SECRET`, `TURNSTILE_SITE_KEY` ustawić jako zmienne *runtime* Workera (dziś są w „Build → Variables”, stąd `not_configured`), potem prawdziwy test PL/EN | Bez tego żadne zapytanie nie dotrze; formularz pokazuje wtedy uczciwy błąd + e-mail/WhatsApp | `INSTRUKCJA_WDROZENIA_FORMULARZA.md` kroki 3–5 |
| B3 | **Retencja / dane administratora / umowy powierzenia** (Namecheap, Resend, Cloudflare, Turnstile) | Polityka musi opisywać faktycznych odbiorców danych | `PRIVACY` w `tools/build.py` |
| B4 | ~~Docelowa domena~~ — `SITE_URL = https://scenovis.com` (17.10.2026). Do zrobienia w panelu: Custom domain `scenovis.com` + `www.scenovis.com`, potem wyłączyć workers.dev | — | Cloudflare → Workers → scenovis → Domains |
| B5 | `DRAFT = False` po uzupełnieniu powyższych | Ukrywa znaczniki TODO | `tools/config.py` |

Polityka prywatności jest projektem — przed publikacją warto, by sprawdziła ją osoba z wiedzą prawną (nie jestem prawnikiem).

## MUST HAVE

| # | Materiał | Format / parametry | Gdzie użyty |
|---|----------|--------------------|-------------|
| 1 | ~~Dane kontaktowe~~ — **zrobione 17.10.2026**: +48 734 215 791 (tel., WhatsApp, JSON-LD), contact@scenovis.com | — | `tools/config.py` |
| 2 | ~~Docelowa domena~~ — scenovis.com | — | `SITE_URL` |
| 3 | **Film EXPO** (Ty sterujesz prezentacją Blender) | MP4 H.264 + AAC, 1920×1080, 25/30 fps, ~6–10 Mb/s, **2–4 min**, bez muzyki z prawami autorskimi; opcjonalnie WebM (VP9). Pierwsze 5 s: od razu widok stoiska | sekcja „Przykład” na stronie głównej i obu landingach |
| 4 | **Poster filmu** | JPG lub WebP 1920×1080, < 250 KB, kadr z widocznym panelem kosztów | odtwarzacz + VideoObject `thumbnailUrl` |
| 5 | **Napisy PL i EN** | WebVTT (`.vtt`), UTF-8 | odtwarzacz (WCAG 1.2.2) |
| 6 | **Transkrypcja / opis kroków** | tekst PL + EN | „Transkrypcja filmu” |
| 7 | **Dane do polityki prywatności** | B1 + B3 powyżej + data aktualizacji | polityka PL/EN |
| 8 | **Obszar działania** (np. cała Polska / wybrane targi za granicą) | 1–2 zdania | hero, FAQ „Gdzie działasz?” |
| 9 | **Daty publikacji i czas trwania filmu** | `uploadDate` (ISO), `duration` (np. PT3M20S) | `VIDEO` w config.py |

## SHOULD HAVE

| # | Materiał | Format | Gdzie |
|---|----------|--------|-------|
| 10 | **Screeny prezentacji Blender** (widok stoiska, panel kosztów elementu, porównanie Economy/Smart/Premium, kiosk, mikroskop) | PNG/JPG 2560×1440 lub 1920×1080, 4–6 szt. | zamiana ilustracji AI w hero i landingach na prawdziwe ujęcia — największy wzrost wiarygodności |
| 11 | ~~Zasady wyceny~~ — FAQ mówi „wycena indywidualna, bez pakietów” (bez kwot, zgodnie z założeniem) | — | FAQ „Jak wyceniasz projekt?” |
| 12 | **Terminy** — ile tygodni przed targami zacząć | 1–2 zdania | FAQ „Ile wcześniej trzeba zacząć?” |
| 13 | **Sprzęt prezentacji interaktywnej** (na czym działa, offline?) | 1–2 zdania | FAQ na landingu 3D |
| 14 | **Bio** — przepisane 17.10.2026 (BIM, koordynacja 3D, wizualizacja; zakres własny vs podwykonawcy). Przeczytaj i potwierdź | 3 akapity PL/EN | `about_body` w `tools/content.py` |
| 15 | **Dokładny zakres własny i zakres podwykonawców** — czy lista na stronie się zgadza? | lista | „Oferta”, „O mnie” |
| 16 | **Nazwisko do danych strukturalnych** (opcjonalnie) | tekst | `Person` w JSON-LD |

## NICE TO HAVE

| # | Materiał | Format | Gdzie |
|---|----------|--------|-------|
| 17 | Nowe zdjęcie Aleksa w podobnym świetle (obecne jest OK) | JPG ≥ 1200×1500, ciemne tło | „O mnie” |
| 18 | Adres działalności (jeśli publiczny) | tekst | JSON-LD zmieni się na ProfessionalService |
| 19 | Dodatkowe pytania FAQ, które słyszysz od klientów | lista | FAQ |
| 20 | Pierwszy prawdziwy projekt klienta (za zgodą) | zdjęcia + 3 zdania | przyszły drugi case study |

## Po zmianie domeny

1. `SITE_URL` → `python3 tools/build.py` → deploy.
2. Podłącz domenę w Cloudflare (Workers → Settings → Domains & Routes).
3. Stary adres `*.workers.dev`: przekierowanie 301 na nową domenę albo wyłączenie trasy workers.dev.
4. Google Search Console: dodaj domenę, wyślij `sitemap.xml`.

## Po aktualizacji 17.10.2026 — wymaga Twojego działania

1. Ustawić 3 sekrety runtime i wdrożyć (B2) → `INSTRUKCJA_WDROZENIA_FORMULARZA.md`.
2. Prawdziwy test wysyłki PL i EN (e-mail i telefon) + sprawdzenie Resend → Logs.
3. Polityka prywatności: administrator, retencja, DPA, podstawy prawne, data (B1, B3). Baner „wersja robocza” zniknie dopiero, gdy w `PRIVACY` (`tools/build.py`) nie będzie żadnego `{todo:`.
4. FAQ: obszar działania, terminy, sprzęt prezentacji 3D (offline?) — pola TODO.
5. Opcjonalnie: usunąć stare pliki V5 z katalogu głównego (`site.js`, `site.css`, `refinements.css`, `netlify.toml`, `README_V5.md`) — nie są używane ani publikowane.
6. Opcjonalnie: w Cloudflare usunąć wpisy z „Build → Variables and secrets” (kod ich nie używa).
