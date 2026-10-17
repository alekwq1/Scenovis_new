# Checklisty — prywatność, Google Ads / Analytics

> Nie jestem prawnikiem. Punkty oznaczone ⚖️ warto skonsultować z osobą zajmującą się RODO.

## A. Prywatność (stan na teraz)

- [ ] ⚖️ Administrator danych: pełna nazwa / imię i nazwisko, adres, NIP (jeśli jest) — **BLOCKER**
- [ ] Wybrana obsługa formularza (Resend lub KV) wpisana do polityki jako odbiorca
- [ ] Dostawca skrzynki e-mail wpisany do polityki (dziś Gmail → Google)
- [ ] ⚖️ Umowy powierzenia (DPA) / transfery poza EOG: Cloudflare, Google, Resend
- [ ] ⚖️ Okres przechowywania zapytań (polityka + `expirationTtl` w `worker/index.js`, jeśli KV)
- [ ] Data ostatniej aktualizacji polityki
- [x] Brak cookies analitycznych i reklamowych, brak skryptów firm trzecich
- [x] Font i film serwowane z własnego serwera (bez Google Fonts / YouTube)
- [x] Brak localStorage (język wynika z adresu `/pl/` lub `/en/`)
- [x] Formularz: minimum danych, link do polityki przy przycisku
- [x] Link WhatsApp — informacja w polityce, że obowiązują zasady Meta
- [ ] `DRAFT = False` po uzupełnieniu

**Dane, które musisz mi dostarczyć do dokończenia polityki:**
1. Forma działalności i pełne dane administratora (nazwa, adres, NIP/REGON jeśli dotyczy).
2. Adres e-mail do spraw danych osobowych (może być ten sam co kontaktowy).
3. Gdzie trafiają zapytania: skrzynka (dostawca), ewentualny CRM, arkusz.
4. Jak długo trzymasz zapytania bez współpracy (np. 12 miesięcy).
5. Czy planujesz newsletter / marketing (dziś polityka mówi: nie).
6. Czy w ciągu najbliższych miesięcy planujesz GA4 / Google Ads / Meta Pixel (wtedy CMP + aktualizacja polityki).

### Gdy dodasz Analytics / Ads / YouTube / inne cookies firm trzecich

- [ ] ⚖️ Baner zgody (CMP) z opcją „Odrzuć” równie łatwą jak „Akceptuj”
- [ ] **Google Consent Mode v2** (`ad_storage`, `analytics_storage`, `ad_user_data`, `ad_personalization` domyślnie `denied` w EOG), certyfikowany CMP Google wymagany dla reklamodawców w EOG
- [ ] Aktualizacja sekcji 6 polityki: lista narzędzi, cele, okresy, odbiorcy, transfery
- [ ] Rozszerzenie CSP w `_headers` (przykład niżej)
- [ ] YouTube tylko w trybie `youtube-nocookie.com` i po zgodzie — albo zostań przy własnym MP4 (zalecane)

## B. Architektura zdarzeń (gotowa w `assets/js/site.js`)

Wszystkie zdarzenia trafiają do `window.dataLayer` z parametrami `page_lang` (pl/en) i `page_type` (home/expo/3d/privacy). **Dziś nikt ich nie czyta** — nie ma żadnego tagu.

| Zdarzenie | Kiedy | Parametry | Konwersja Ads? |
|---|---|---|---|
| `lead_form_submit` | serwer potwierdził przyjęcie formularza | `form_topic`, `has_details` | **TAK — główna** |
| `phone_click` | klik w `tel:` | `link_text` | tak (dodatkowa) |
| `email_click` | klik w `mailto:` | `link_text` | tak (dodatkowa) |
| `whatsapp_click` | klik w link wa.me | `link_text` | tak (dodatkowa) |
| `video_start` | start filmu | `video_name` | nie (mikrokonwersja) |
| `video_25` / `video_50` | 25% / 50% filmu | `video_name`, `video_percent` | nie |
| `video_complete` | koniec filmu | `video_name`, `video_percent` | nie |
| `case_cta_click` | CTA pod filmem / po filmie | `link_text` | nie |
| `hero_cta_case`, `hero_cta_contact` | CTA w hero | `link_text` | nie |
| `cost_variant_select` | przełączenie Economy/Smart/Premium | `variant` | nie |
| `lead_form_fallback_shown` | wysyłka nie powiodła się → pokazano e-mail/WhatsApp | – | nie (monitoring błędów) |

Uwaga: `email_click` / `whatsapp_click` liczą zamiar, nie wysłanie wiadomości.

### Wdrożenie (po zgodzie)

1. GTM lub Google tag ładowany **po** domyślnym stanie Consent Mode (`denied`).
2. GA4: zdarzenia niestandardowe 1:1 z tabeli; `lead_form_submit` jako kluczowe zdarzenie.
3. Google Ads: import `lead_form_submit` z GA4 lub tag konwersji Ads na to samo zdarzenie; `phone_click` jako konwersja dodatkowa.
4. Rozszerzenie CSP (`_headers`), przykład dla GTM + GA4 + Ads:
   ```
   script-src 'self' https://www.googletagmanager.com;
   connect-src 'self' https://*.google-analytics.com https://*.analytics.google.com https://*.googletagmanager.com https://www.google.com https://googleads.g.doubleclick.net;
   img-src 'self' data: https://*.google-analytics.com https://*.googletagmanager.com https://www.google.com https://googleads.g.doubleclick.net;
   frame-src https://www.googletagmanager.com;
   ```
   GTM z niestandardowymi tagami HTML wymaga nonce lub `'unsafe-inline'` — lepiej używać szablonów tagów.

## C. Google Ads — przygotowanie (nic nie zostało uruchomione)

### Struktura kampanii → landingi

| Kampania / grupa | Przykładowe frazy (dopasowanie do fraz/ścisłe) | Landing |
|---|---|---|
| EXPO — projekt | projekt stoiska targowego, projektowanie stoisk targowych, koncepcja stoiska | `/pl/projekt-stoiska-targowego/` |
| EXPO — 3D | projekt stoiska 3D, wizualizacja stoiska targowego, wizualizacja 3D stoiska | `/pl/projekt-stoiska-targowego/` |
| EXPO — koszt | ile kosztuje stoisko targowe, koszt stoiska targowego, kosztorys stoiska | `/pl/projekt-stoiska-targowego/#koszty` |
| 3D — produkt | prezentacja produktu 3D, wizualizacja produktu 3D, animacja produktu | `/pl/prezentacje-produktow-3d/` |
| 3D — targi | multimedia na targi, ekran dotykowy na targi, interaktywna prezentacja produktu | `/pl/prezentacje-produktow-3d/` |
| EN | exhibition stand design Poland, trade show booth design 3D | `/en/exhibition-stand-design/` |

**Wykluczenia (start):** praca, oferty pracy, staż, darmowy, za darmo, szablon, tanie, używane, sprzedam, kurs, studia, AutoCAD/SketchUp tutorial, pdf.

**Teksty reklam — zgodne z landingiem:** „Projekt stoiska z kosztorysem” · „Zakup, wynajem, usługa — przy każdym elemencie” · „Porównaj warianty przed produkcją” · „Wizualizacja 3D stoiska”. Bez obietnic typu „najtańsze”, „gwarancja”.

### Checklist przed startem

- [ ] Blokery z TODO.md (domena, polityka, formularz) zamknięte
- [ ] Konwersja `lead_form_submit` testowo zarejestrowana (Tag Assistant)
- [ ] CMP + Consent Mode v2 działają (test z odrzuceniem zgody)
- [ ] Film i prawdziwe screeny na landingach (wyższa jakość strony docelowej)
- [ ] Rozszerzenia: telefon, linki do podstron (Projekt stoiska / Prezentacje 3D / Kontakt)
- [ ] Harmonogram zgodny z godzinami odbierania telefonu
- [ ] Lokalizacja: Polska (+ ew. DE/CZ dla EN), wykluczenie „zainteresowania” bez obecności
- [ ] Search Console: domena zweryfikowana, sitemap wysłana
