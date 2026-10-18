# -*- coding: utf-8 -*-
"""
SCENOVIS — treści strony (PL / EN).

Tu edytujesz teksty. Po zmianie uruchom:  python3 tools/build.py
Generator zapisze gotowe pliki HTML w /pl/ i /en/.

Zasady:
- Każdy klucz musi istnieć w obu językach (build sprawdza to automatycznie).
- {todo:...} w tekście = widoczny znacznik TODO w trybie roboczym (DRAFT=True w config.py).
- Wolno używać prostego HTML (<em>, <br>, <strong>, <a>).
- Pozycje menu: "#kotwica" = sekcja na stronie głównej, "@expo" / "@3d" = podstrona usługi.
- Dwie usługi (projekt stoiska i prezentacje 3D) są równorzędne — pilnuj tego przy edycji.
- Bez cenników, pakietów, fikcyjnych klientów, liczb i opinii.
"""

PL = {
    # ---------- wspólne ----------
    "lang_name": "Polski",
    "skip": "Przejdź do treści",
    "nav_label": "Nawigacja główna",
    "menu_open": "Otwórz menu",
    "menu_close": "Zamknij menu",
    "nav": [("@expo", "Stoiska EXPO"), ("@3d", "Prezentacje 3D"),
            ("#o-mnie", "O mnie"), ("#faq", "FAQ")],
    # menu na podstronach usług — kotwice do sekcji tej strony + druga usługa
    "nav_expo": [("#zakres", "Zakres"), ("#przyklad", "Zobacz stoisko"), ("#wspolpraca", "Współpraca"),
                 ("#faq", "FAQ"), ("@3d", "Prezentacje 3D")],
    "nav_3d": [("#viewer-host", "Model 3D"), ("#przyklad", "Co przygotujemy"), ("#faq", "FAQ"),
               ("@expo", "Stoiska EXPO")],
    "nav_cta": "Kontakt",
    "lang_switch_label": "Wersja językowa",
    "home_label": "Scenovis — strona główna",
    "alt": {
        "stand": "Render 3D stoiska targowego z mikroskopami, ekranem i kioskiem dotykowym",
        "visitor": "Stoisko targowe z perspektywy odwiedzającego: lada, ekran, dwa stanowiska z mikroskopami",
        "standmic": "Mikroskop na stanowisku pokazowym na stoisku targowym — render 3D",
        "kiosk": "Kiosk dotykowy z interaktywną prezentacją 3D mikroskopu na stoisku targowym",
        "product": "Model 3D mikroskopu w studyjnym oświetleniu — render produktowy",
        "exploded": "Widok rozłożony mikroskopu: głowica, okulary, kolumna, stolik i obiektywy rozsunięte w przestrzeni",
        "objectives": "Zbliżenie rewolweru z obiektywami mikroskopu — render 3D z głębią ostrości",
        "front": "Wizualizacja stoiska od strony alejki: lada z hokerami, ekran, dwa stanowiska z mikroskopami",
        "widok": "Wizualizacja całego stoiska z góry: ściany, oświetlenie, lada, kiosk i stanowiska pokazowe",
        "kioskscreen": "Kiosk dotykowy z interaktywną prezentacją 3D mikroskopu, w tle lada stoiska",
        "cover3d": "Zbliżenie obiektywów mikroskopu nad stolikiem z preparatem — okładka filmu z prezentacji 3D",
    },
    "footer_tagline": "Projekty stoisk targowych i interaktywne prezentacje produktów 3D.",
    "footer_services": "Usługi",
    "footer_privacy": "Polityka prywatności",
    "footer_location": "Gdańsk, Polska",
    "footer_lang": "Obsługa po polsku i angielsku",
    "breadcrumb_home": "Strona główna",

    # ---------- strona główna: meta ----------
    "home_title": "Scenovis — projekty stoisk targowych i prezentacje produktów 3D",
    "home_desc": "Projekt stoiska targowego z modelem 3D i zestawieniem kosztów oraz interaktywne prezentacje 3D "
                 "produktów technicznych — na targi, do showroomu i do sprzedaży.",

    # ---------- hero ----------
    "hero_eyebrow": "STOISKA EXPO • PREZENTACJE 3D",
    "hero_h1": "Pokaż produkt.<br>Zrozum stoisko.<br><em>Kontroluj budżet.</em>",
    "hero_lead": "Projektujemy stoiska targowe i interaktywne prezentacje 3D produktów. Łączymy koncepcję, "
                 "budżet i organizację udziału w targach — od projektu po obsługę na miejscu.",
    "hero_cta_primary": "Opowiedz o swoim projekcie",
    "hero_paths_label": "Usługi",
    "hero_paths": [("expo", "Projekt stoiska targowego"), ("3d", "Prezentacje produktów 3D")],
    "hero_note": "Gdańsk · projekty w całej Polsce i za granicą · rozmowa po polsku lub angielsku",
    # Warianty stoiska w hero — zakres zgodny z modelem Blender (EXPO_COST_DATA.json: presets ECONOMY/SMART/PREMIUM).
    # Punkty: (klucz pozycji, nazwa, typ kosztu). Pozycje punktów — assets/css/site.css (.tag--<klucz>).
    "variants": {
        "economy": {
            "name": "Economy",
            "scope": "Ściany systemowe, wykładzina, 4 reflektory, ekran 75″ i kiosk dotykowy — wszystko z wynajmu.",
            "alt": "Stoisko w wariancie Economy: ściany systemowe, wykładzina, cztery reflektory, ekran 75 cali i kiosk dotykowy",
            "tags": [("screen", "Ekran 75″", "wynajem"), ("spots", "4 reflektory", "wynajem"),
                     ("kiosk", "Kiosk dotykowy", "wynajem"), ("floor", "Wykładzina", "wynajem")],
        },
        "smart": {
            "name": "Smart",
            "scope": "Rama z grafiką tekstylną, podświetlany panel marki, 6 reflektorów i linia LED, ekran 98″, "
                     "podłoga modułowa — z wynajmu; kiosk własny lub z wynajmu.",
            "alt": "Stoisko w wariancie Smart: podświetlany panel marki, sześć reflektorów, linia LED, ekran 98 cali, podłoga modułowa i kiosk dotykowy",
            "tags": [("screen", "Ekran 98″", "wynajem"), ("spots", "6 reflektorów + linia LED", "wynajem"),
                     ("brand", "Podświetlany panel marki", "wynajem"), ("kiosk", "Kiosk dotykowy", "własne")],
        },
        "premium": {
            "name": "Premium",
            "scope": "Zakres Smart oraz trzy podświetlane pola, podświetlane postumenty, reflektory ze sterownikiem scen "
                     "i monitor profesjonalny 98″ — z wynajmu, z obsługą techniczną na miejscu.",
            "alt": "Stoisko w wariancie Premium: trzy podświetlane pola, podświetlone postumenty, reflektory ze sterownikiem scen, monitor profesjonalny 98 cali",
            "tags": [("screen", "Monitor profesjonalny 98″", "wynajem"), ("spots", "Reflektory ze sterownikiem scen", "wynajem"),
                     ("slats", "Podświetlane pola", "wynajem"), ("ped", "Podświetlane postumenty", "wynajem")],
        },
    },
    "hero_variant_label": "Wariant",
    "hero_figure_label": "Elementy stoiska opisane typem kosztu",

    # ---------- w skrócie ----------
    "tldr_title": "Scenovis w skrócie",
    "tldr_for": "<strong>Dla kogo:</strong> dla firm z produktem technicznym — przygotowujących stoisko na targi "
                "albo szukających czytelnego sposobu, by pokazać, jak działa ich produkt.",
    "tldr": [
        ("Projekt stoiska", "Koncepcja, układ i model 3D — oglądasz stoisko, zanim powstanie."),
        ("Koszty pod kontrolą", "Każdy element jako wynajem, własne wyposażenie lub usługa. Warianty do porównania."),
        ("Prezentacje produktów 3D", "Budowa, mechanizmy i działanie urządzenia — interaktywnie lub jako animacja."),
        ("Od pomysłu do realizacji", "Projekt, prezentacja produktu i organizacja udziału w targach — całość lub wybrany zakres."),
    ],

    # ---------- case study / film (strona główna i projekt stoiska) ----------
    "case_h2": "Zobacz stoisko. Porównaj możliwości.",
    "case_lead": "Obejrzyj układ, sprawdź wyposażenie i porównaj warianty przed realizacją.",
    "video_play": "Odtwórz film",
    "video_pause": "Zatrzymaj film",
    "video_replay": "↻ Obejrzyj ponownie",
    "video_duration": "Czas trwania",
    "video_captions_note": "Film ma napisy po polsku i angielsku. Dźwięk włącza się dopiero po kliknięciu.",
    "case_benefits": [
        ("Układ 3D", "zobacz przestrzeń i ekspozycję"),
        ("Przejrzysty budżet", "sprawdź wynajem, własne wyposażenie i usługi"),
        ("Porównanie wariantów", "wybierz Economy, Smart lub Premium"),
    ],
    "case_cta": "Omów projekt stoiska",

    # ---------- prezentacja produktu (podstrona prezentacji 3D) ----------
    "case3d_h2": "Interaktywna prezentacja produktu",
    "case3d_lead": "Budowa, części i działanie urządzenia technicznego pokazane w 3D — na ekranie, kiosku lub w przeglądarce.",
    "case3d_benefits": [
        ("Budowa urządzenia", "podzespoły widoczne także wewnątrz obudowy"),
        ("Element po elemencie", "wybierz część i obejrzyj ją z każdej strony"),
        ("Działanie produktu", "mechanizm w ruchu, bez transportu urządzenia"),
    ],
    "case3d_cta": "Porozmawiajmy o prezentacji produktu",

    # ---------- oferta ----------
    "services_label": "Oferta",
    "services_h2": "Dwie usługi — osobno lub razem",
    "services_lead": "Projekt stoiska i prezentację produktu 3D możesz zamówić niezależnie od siebie. "
                     "Każdy projekt wyceniamy indywidualnie, według uzgodnionego zakresu.",
    "services": [
        {
            "key": "expo", "code": "Usługa · EXPO", "title": "Projekt stoiska targowego",
            "desc": "Przemyślana przestrzeń targowa i decyzje podjęte przed produkcją — na podstawie modelu 3D "
                    "i zestawienia kosztów.",
            "items": ["Koncepcja stoiska", "Układ funkcjonalny i ergonomia", "Model i wizualizacje 3D",
                      "Dobór wyposażenia i technologii", "Analiza: wynajem czy własne elementy",
                      "Zestawienie elementów i szacunek kosztów", "Wsparcie w wyborze wykonawców"],
            "more": ("Więcej o projekcie stoiska", "expo"), "ask": "Omów projekt stoiska",
        },
        {
            "key": "3d", "code": "Usługa · 3D", "title": "Interaktywne prezentacje produktów 3D",
            "desc": "Pokazujesz wnętrze produktu i działanie mechanizmów — także urządzeń, których nie da się "
                    "łatwo zademonstrować na miejscu.",
            "items": ["Interaktywne modele produktów technicznych", "Prezentacje na ekranach dotykowych",
                      "Animacje działania maszyn i urządzeń", "Budowa produktu i jego komponenty",
                      "Wizualizacje techniczne i demonstracje funkcji",
                      "Materiały na targi, do showroomu i sprzedaży",
                      "Ponowne użycie — jeśli pozwala format i umowa"],
            "more": ("Więcej o prezentacjach 3D", "3d"), "ask": "Porozmawiajmy o prezentacji",
        },
    ],
    "full": {
        "label": "Kompleksowa obsługa targów",
        "title": "Od pomysłu do realizacji",
        "desc": "Projekt stoiska, prezentacja produktu i organizacja udziału w targach. "
                "Możemy zająć się całością lub wybranym zakresem.",
        "items": ["Projekt i wizualizacja 3D", "Interaktywne prezentacje produktów",
                  "Zabudowa, multimedia i wyposażenie", "Transport, montaż i demontaż",
                  "Hostessy, hości i obsługa gości", "Koordynacja przebiegu wydarzenia na miejscu"],
        "note": "Dobieramy zespół i wykonawców do zakresu projektu.",
        "cta": "Porozmawiajmy o Twoich targach",
    },
    "services_note": "Zakres każdego projektu ustalamy razem — bez sztywnych pakietów.",

    # ---------- koszty ----------
    "costs_label": "Koszty stoiska",
    "costs_h2": "Wiesz, za co płacisz.",
    "costs_lead": "Porównaj wyposażenie i sposób rozliczenia. Zakres oraz wycenę dopasujemy do Twojego projektu.",
    "costs_sheet_title": "Stoisko 5,4 × 3,8 m",
    "costs_variant_label": "Porównaj warianty",
    "costs_cols": ("Element", "Zakres", "Rozliczenie"),
    "cost_types": {"buy": "Zakup", "rent": "Wynajem", "service": "Usługa", "mix": "Wynajem i zakup"},
    # (element, [(typ, opis) dla economy, smart, premium]) — zgodnie z modelem Blender (EXPO_COST_DATA.json)
    "costs_rows": [
        ("Ściany i grafika", [("rent", "Ściany systemowe, grafika foliowa"), ("buy", "Własna rama, grafika tekstylna"),
                              ("buy", "Własna rama, grafika tekstylna")]),
        ("Podświetlenia marki", [("buy", "Bez podświetlenia"), ("buy", "Podświetlany panel marki"),
                                 ("buy", "Trzy podświetlane pola")]),
        ("Oświetlenie", [("rent", "4 reflektory LED"), ("mix", "6 reflektorów i linia LED"),
                         ("buy", "Własne reflektory, linia LED, postumenty")]),
        ("Ekran", [("buy", "Telewizor 75″"), ("buy", "Telewizor 98″"), ("buy", "Monitor profesjonalny 98″")]),
        ("Kiosk dotykowy", [("rent", "Kiosk z prezentacją 3D"), ("buy", "Własny kiosk z prezentacją 3D"),
                            ("buy", "Własny kiosk z prezentacją 3D")]),
        ("Podłoga", [("rent", "Wykładzina targowa"), ("buy", "Podłoga modułowa z listwą"),
                     ("buy", "Podłoga modułowa z listwą")]),
        ("Meble i ekspozycja", [("rent", "Lada, hokery, postumenty"), ("buy", "Lada z szafkami, hokery, postumenty"),
                                ("buy", "Lada z szafkami, hokery, postumenty")]),
        ("Transport i montaż", [("service", "Montaż i demontaż — 2 osoby"), ("service", "Montaż i demontaż — 3 osoby"),
                                ("service", "Montaż i demontaż — 4 osoby")]),
        ("Personel", [("service", "Hostessa"), ("service", "Hostessa i demonstrator produktu"),
                      ("service", "2 hostessy, demonstrator, technik")]),
        ("Koordynacja", [("service", "Na miejscu — do ustalenia"), ("service", "Na miejscu — do ustalenia"),
                         ("service", "Na miejscu — do ustalenia")]),
    ],
    "costs_more": "Pokaż zakres",
    "costs_more_items": [
        ["Przyłącze prądu 3 kW", "Treści na ekran — pakiet podstawowy", "Elektryk przy montażu",
         "Opłaty organizatora: powierzchnia, rejestracja, internet, sprzątanie"],
        ["Przyłącze prądu 3 kW", "Treści na ekran — pakiet standard", "Elektryk przy montażu",
         "Skrzynie transportowe i magazyn między targami",
         "Opłaty organizatora: powierzchnia, rejestracja, internet, sprzątanie"],
        ["Przyłącze prądu 9 kW", "Sterownik scen świetlnych", "Treści na ekran — pakiet rozszerzony",
         "Elektryk przy montażu", "Skrzynie transportowe i magazyn między targami",
         "Opłaty organizatora: powierzchnia, rejestracja, internet, sprzątanie"],
    ],
    "costs_price": "Indywidualna wycena",
    "costs_price_note": "Bez sztywnych pakietów — zakres i wycenę ustalamy dla konkretnych targów.",
    "costs_legend": [
        ("own", "Własne", "Twoje wyposażenie, wykorzystujemy je w projekcie"),
        ("rent", "Wynajem", "na czas targów"),
        ("service", "Usługa", "transport, montaż i obsługa"),
    ],

    # ---------- o mnie ----------
    "about_label": "O mnie",
    "about_h2": "Cześć, jestem Aleks.",
    "about_body": [
        "Scenovis prowadzę osobiście. Mam doświadczenie w BIM, koordynacji modeli 3D, wizualizacji "
        "i procesach technicznych — przy projektach budowlanych i przemysłowych.",
        "Samodzielnie prowadzę koncepcję, przygotowuję modele 3D i prezentacje techniczne, "
        "analizę funkcjonalną oraz zestawienia kosztów.",
        "Gdy zadanie wymaga innych kompetencji — produkcji, montażu, multimediów czy logistyki — współpracuję "
        "z podwykonawcami dobranymi do projektu. Rozmawiasz bezpośrednio ze mną, a skład współpracowników "
        "dopasowujemy do zakresu.",
    ],
    "about_photo_alt": "Aleks — Scenovis",
    "about_linkedin": "Profil na LinkedIn",

    # ---------- proces ----------
    "process_label": "Współpraca",
    "process_h2": "Jak wygląda współpraca",
    "process": [
        ("Rozmowa i brief", "Cel, termin, zakres i budżet. Na start wystarczy jedno zdanie."),
        ("Koncepcja", "Układ stoiska albo scenariusz prezentacji produktu."),
        ("Model 3D i zestawienie", "Wizualizacje, prezentacja lub zestawienie kosztów — zależnie od usługi."),
        ("Omówienie i decyzja", "Przechodzimy przez wynik razem i ustalamy kolejne kroki."),
        ("Realizacja i targi", "Zespół i wykonawcy dobrani do zakresu albo przekazanie materiałów Twojemu zespołowi."),
    ],

    # ---------- FAQ ----------
    "faq_label": "FAQ",
    "faq_h2": "Częste pytania",
    "faq": {
        "price": ("Jak wygląda wycena projektu?",
                  "<p>Każdy projekt wyceniamy indywidualnie — bez sztywnych pakietów. Wycena zależy od zakresu: "
                  "przy stoisku m.in. od powierzchni i liczby wariantów, przy prezentacji 3D od złożoności produktu "
                  "i formy prezentacji. Wycenę podajemy po krótkiej rozmowie, przed rozpoczęciem pracy.</p>"),
        "expo_process": ("Jak wygląda projektowanie stoiska?",
                         "<p>Zaczynamy od briefu: targi, termin, powierzchnia, cel i budżet. Potem przygotowujemy koncepcję "
                         "i układ funkcjonalny, model 3D oraz zestawienie elementów z typem kosztu. Omawiamy warianty "
                         "i dopiero wtedy decydujesz, co zamówić u wykonawców.</p>"),
        "factors": ("Od czego zależy koszt stoiska?",
                    "<p>Najczęściej od: powierzchni i typu zabudowy (systemowa lub indywidualna), materiałów "
                    "i wykończenia, grafiki, oświetlenia, multimediów, mebli, transportu, montażu i demontażu "
                    "oraz opłat organizatora (np. przyłącza mediów). Dla Twojego projektu rozpisujemy to element po elemencie.</p>"),
        "buyrent": ("Co wynająć, a co wykorzystać z własnego wyposażenia?",
                    "<p>Większość elementów — zabudowę, sprzęt AV, oświetlenie i meble — najlepiej wynająć na czas targów. "
                    "Własne elementy, np. kiosk, ekran czy grafikę z poprzednich targów, uwzględniamy w projekcie "
                    "i wyceniamy tylko wynajem tego, czego brakuje.</p>"),
        "reuse": ("Czy stoisko można wykorzystać na kolejnych targach?",
                  "<p>Tak, jeśli zaplanujemy to od początku: moduły, wymienne grafiki, transport i magazynowanie. "
                  "Pytamy o to już na etapie briefu, bo wpływa to na dobór elementów.</p>"),
        "materials": ("Jakie materiały są potrzebne na start?",
                      "<p>Wystarczy: nazwa targów i termin, powierzchnia i rodzaj stoiska (wyspowe, narożne, rzędowe), "
                      "co chcesz pokazać i orientacyjny budżet. Pomocne będą też: logo lub brandbook, zdjęcia albo modele "
                      "produktu (np. STEP) i regulamin techniczny organizatora.</p>"),
        "delivery": ("Czy możecie zająć się całą realizacją?",
                     "<p>Tak. Zabudowę, multimedia, transport, montaż, personel stoiska i koordynację na miejscu "
                     "organizujemy w zakresie, który ustalimy — dobieramy zespół i wykonawców do projektu. "
                     "Możesz też zamówić sam projekt z zestawieniem kosztów i zrealizować go z własnym wykonawcą.</p>"),
        "area": ("Gdzie działacie?",
                 "<p>Działamy z Gdańska dla klientów z całej Polski i przy targach za granicą. Projekt, model 3D i zestawienie "
                 "kosztów przygotowujemy zdalnie, a spotkania odbywają się online lub na miejscu. Obsługę i koordynację "
                 "na miejscu podczas targów ustalamy indywidualnie.</p>"),
        "time": ("Ile wcześniej trzeba zacząć?",
                 "<p>Najwygodniej zacząć 2–3 miesiące przed targami, a przy zabudowie indywidualnej lub dużym stoisku — "
                 "jeszcze wcześniej. Organizatorzy często wymagają zatwierdzenia projektu z wyprzedzeniem, a wykonawcy "
                 "potrzebują czasu na oferty i produkcję.</p>"
                 "<p>Przy mniejszym zakresie i gotowych materiałach (wymiary stoiska, logo, dane produktu) "
                 "da się pracować szybciej. Konkretny harmonogram ustalamy po briefie.</p>"),
        "3d_forms": ("W jakiej formie może powstać prezentacja 3D?",
                     "<p>Zależnie od potrzeb: jako interaktywna prezentacja, w której użytkownik sam wybiera elementy "
                     "produktu, jako animacja lub film albo jako zestaw wizualizacji i przekrojów. Formę dobieramy do "
                     "miejsca użycia — stoiska, showroomu, spotkania handlowego lub strony internetowej.</p>"),
        "3d_data": ("Jakie dane są potrzebne do prezentacji 3D produktu?",
                    "<p>Najlepiej pracuje się na modelach CAD (np. STEP) lub rysunkach technicznych. Jeśli ich nie ma, "
                    "zaczniemy od zdjęć, wymiarów i opisu działania — ustalimy razem, jaki poziom szczegółów ma sens.</p>"),
        "3d_hw": ("Na jakich urządzeniach działa interaktywna prezentacja?",
                  "<p>Standardowo prezentacja działa w przeglądarce — na laptopie lub na ekranie dotykowym. Jakość i sposób "
                  "uruchomienia dopasowujemy do sprzętu: wersja online (np. streaming w wysokiej jakości) wymaga internetu, "
                  "a na komputerze stacjonarnym lub w kiosku prezentacja może działać lokalnie, bez internetu. "
                  "Wariant ustalamy na początku projektu.</p>"),
        "3d_reuse": ("Czy prezentację można wykorzystać ponownie?",
                     "<p>Tak, jeśli pozwala na to format i ustalenia umowy. Model i materiały przygotowane na targi "
                     "mogą później służyć w sprzedaży, w showroomie lub jako film i grafiki na stronę internetową.</p>"),
        "3d_nofair": ("Czy prezentacja 3D musi być związana z targami?",
                      "<p>Nie. Prezentacja może wspierać handlowców na spotkaniach, działać w showroomie albo "
                      "na stronie internetowej. Stoisko nie jest do tego potrzebne.</p>"),
    },

    # ---------- kontakt ----------
    "contact_label": "Kontakt",
    "contact_h2": "Opowiedz o swoim projekcie.",
    "contact_h2_expo": "Omów projekt stoiska.",
    "contact_h2_3d": "Porozmawiajmy o prezentacji produktu.",
    "contact_lead": "Wystarczy telefon lub e-mail. Odezwiemy się, żeby ustalić szczegóły.",
    "contact_direct": "Albo napisz lub zadzwoń bezpośrednio",
    "contact_phone_sub": "Zadzwoń",
    "contact_email_sub": "Wyślij brief lub pliki",
    "contact_wa": "Napisz na WhatsApp",
    "contact_brief": "Masz już brief? Wyślij go na {email}.",
    "contact_lang": "Rozmawiamy po polsku i angielsku.",
    "form_title": "Szybkie zapytanie",
    "f_contact": "Telefon lub e-mail",
    "f_contact_hint": "Np. +48 500 000 000 lub imie@firma.pl",
    "f_required": "wymagane",
    "f_optional": "opcjonalnie",
    "f_topic": "Temat",
    "f_name": "Imię",
    "f_message": "Wiadomość",
    "f_message_ph": "Np. jaki produkt lub jakie targi, termin i czego potrzebujesz",
    "f_more": "Dodaj szczegóły projektu",
    "f_event": "Targi / wydarzenie",
    "f_city": "Miasto",
    "f_date": "Termin",
    "f_date_ph": "Np. marzec 2027",
    "f_area": "Powierzchnia stoiska (m²)",
    "f_budget": "Orientacyjny budżet",
    "f_budget_ph": "Np. kwota lub „do ustalenia”",
    "f_reuse": "Stoisko na kolejne targi?",
    "f_reuse_opts": [("", "Nie wiem jeszcze"), ("tak", "Tak, chcę użyć ponownie"), ("nie", "Nie, jednorazowo")],
    "f_submit": "Wyślij zapytanie",
    "f_sending": "Wysyłanie…",
    "f_disclaimer": "Dane wykorzystamy do obsługi zapytania i zabezpieczenia formularza. Szczegóły: <a href=\"{privacy}\">polityka prywatności</a>.",
    "f_err_empty": "Podaj numer telefonu lub adres e-mail.",
    "f_err_email": "Sprawdź adres e-mail — powinien wyglądać np. tak: imie@firma.pl.",
    "f_err_contact": "Wpisz numer telefonu albo adres e-mail.",
    "f_success": "Dziękujemy — zapytanie zostało wysłane. Odezwiemy się najszybciej, jak to możliwe.",
    "f_fail": "Formularz nie został wysłany — wiadomość nie dotarła. Twoja treść jest gotowa, wyślij ją e-mailem lub przez WhatsApp:",
    "f_fail_email": "Wyślij e-mailem",
    "f_fail_wa": "Wyślij przez WhatsApp",
    "f_turnstile_label": "Zabezpieczenie formularza",
    "f_turnstile_wait": "Trwa wczytywanie zabezpieczenia formularza — spróbuj ponownie za chwilę.",
    "f_turnstile_check": "Potwierdź weryfikację bezpieczeństwa formularza i spróbuj ponownie.",
    "f_turnstile_unavailable": "Formularz jest chwilowo niedostępny, więc wiadomość nie została wysłana. Wyślij ją e-mailem lub przez WhatsApp:",
    "f_preview": "To podgląd lokalny — wysyłka działa po publikacji. Możesz przetestować wysyłkę e-mailem:",
    "mail_subject": "Zapytanie ze strony Scenovis",
    "wa_hello": "Dzień dobry, piszę ze strony Scenovis.",
    "topics": {"general": "Zapytanie ogólne", "expo": "Projekt stoiska targowego", "3d": "Prezentacja produktu 3D",
               "delivery": "Kompleksowa obsługa targów"},
    "field_names": {"contact": "Kontakt", "name": "Imię", "message": "Wiadomość", "topic": "Temat",
                    "event": "Targi", "city": "Miasto", "date": "Termin", "area": "Powierzchnia",
                    "budget": "Budżet", "reuse": "Ponowne użycie"},

    # ---------- landing: projekt stoiska ----------
    "expo_slug": "projekt-stoiska-targowego",
    "expo_title": "Projekt stoiska targowego 3D z zestawieniem kosztów | Scenovis",
    "expo_desc": "Koncepcja, układ funkcjonalny i wizualizacja 3D stoiska targowego. Zestawienie elementów "
                 "i kosztów (wynajem, własne wyposażenie, usługa) oraz porównanie wariantów przed produkcją.",
    "expo_crumb": "Projekt stoiska targowego",
    "expo_eyebrow": "PROJEKT STOISKA TARGOWEGO",
    "expo_h1": "Projekt stoiska targowego, <em>w którym widać koszty.</em>",
    "expo_lead": "Przygotowujemy koncepcję i układ stoiska, model 3D oraz zestawienie elementów z kosztami. "
                 "Porównujesz rozwiązania i podejmujesz decyzje, zanim zamówisz produkcję.",
    "expo_points": ["Koncepcja i układ funkcjonalny", "Model i wizualizacje 3D",
                    "Wynajem / własne / usługa przy każdym elemencie", "Warianty do porównania przed realizacją"],
    "expo_cta": "Omów projekt stoiska",
    "expo_cta2": "Zobacz stoisko",
    "expo_get_h2": "Co obejmuje projekt stoiska",
    "expo_shots": [("front", "Koncepcja i układ — lada, ekran i stanowiska pokazowe widziane od strony alejki"),
                   ("widok", "Model 3D z wyposażeniem — podstawa zestawienia i porównania wariantów")],
    "expo_get": [
        ("Koncepcja", "Cel stoiska, przekaz i to, co odwiedzający ma zapamiętać."),
        ("Układ i ergonomia", "Strefy pokazu, rozmów i zaplecza, ruch odwiedzających, ekspozycja produktu."),
        ("Model i wizualizacje 3D", "Widoki z różnych stron i ujęcia do omówienia projektu w firmie."),
        ("Wyposażenie i technologia", "Dobór mebli, multimediów i oświetlenia do celu stoiska."),
        ("Zestawienie i warianty", "Elementy opisane jako wynajem, własne wyposażenie lub usługa — z wariantami do porównania."),
        ("Wybór wykonawców", "Materiały do zapytań ofertowych i wsparcie przy porównaniu ofert."),
    ],
    "cross_expo_h2": "Potrzebujesz też prezentacji produktu?",
    "cross_expo_text": "Na stoisku często trzeba wyjaśnić produkt, którego nie da się łatwo pokazać na żywo. "
                       "Interaktywna prezentacja 3D może być częścią projektu albo osobnym zleceniem.",
    "cross_expo_link": "Prezentacje produktów 3D",

    # ---------- landing: prezentacje 3D ----------
    "p3d_slug": "prezentacje-produktow-3d",
    "p3d_title": "Interaktywne prezentacje produktów 3D | Scenovis",
    "p3d_desc": "Interaktywne modele 3D, animacje działania i przekroje produktów technicznych. Na ekrany dotykowe, "
                "do showroomu, na spotkania handlowe i na targi.",
    "p3d_crumb": "Prezentacje produktów 3D",
    "p3d_eyebrow": "PREZENTACJE PRODUKTÓW 3D",
    "p3d_h1": "Pokaż, jak działa <em>Twój produkt.</em>",
    "p3d_lead": "Interaktywne modele, animacje i przekroje produktów technicznych. Pokazujesz budowę i mechanizmy, "
                "których nie widać z zewnątrz — w rozmowie handlowej, w showroomie i na targach.",
    "p3d_points": ["Budowa i komponenty produktu", "Animacje działania mechanizmów",
                   "Interakcja na ekranie dotykowym", "Wsparcie dla handlowców"],
    "p3d_cta": "Porozmawiajmy o prezentacji produktu",
    "p3d_cta2": "Zobacz film",
    "viewer": {
        "launch": "Uruchom model 3D", "loading": "Wczytywanie modelu…", "canvas_label": "Interaktywny model 3D mikroskopu",
        "explode": "Rozłóż", "assemble": "Złóż", "reset": "Widok startowy",
        "tour": "Zwiedzanie", "tour_stop": "Zatrzymaj", "prev": "Poprzednia", "next": "Następna", "close": "Zamknij opis",
        "hint": "Przeciągnij, aby obrócić · kółko lub dwa palce — przybliżenie · numery — zbliżenia części",
        "error": "Nie udało się uruchomić modelu 3D w tej przeglądarce. Poniżej zostaje render.",
        "note": "Model działa w przeglądarce (ok. 2–3 MB do pobrania).",
        "hotspots": [
            {"node": "Head_Body", "title": "Głowica z okularami", "text": "Tor obserwacyjny: obraz z obiektywu trafia przez głowicę do dwóch okularów."},
            {"node": "Nosepiece_Turret", "title": "Rewolwer z obiektywami", "text": "Trzy obiektywy: 4×, 10× i 40×. Obrót rewolweru zmienia powiększenie."},
            {"node": "Stage_Plate", "title": "Stolik przedmiotowy", "text": "Tu leży preparat. Uchwyt pozwala go precyzyjnie przesuwać."},
            {"node": "FocusKnob_Coarse_L", "title": "Pokrętła ostrości", "text": "Śruba makro- i mikrometryczna podnoszą stolik i ustawiają ostrość."},
            {"node": "Illuminator_Housing", "title": "Oświetlacz", "text": "Światło z podstawy przechodzi przez kondensor i preparat do obiektywu."},
        ],
    },
    "p3d_get_h2": "Co możemy przygotować",
    "p3d_shots": [("exploded", "Widok rozłożony — budowa urządzenia element po elemencie"),
                  ("kiosk", "Ta sama prezentacja na kiosku dotykowym na stoisku")],
    "p3d_get": [
        ("Interaktywny model", "Użytkownik sam obraca produkt, wybiera element i ogląda go z bliska."),
        ("Animacja działania", "Krótki film lub sekwencja pokazująca, jak pracuje mechanizm."),
        ("Budowa i komponenty", "Widok rozłożony: podzespoły rozsunięte w przestrzeni."),
        ("Przekrój", "Wnętrze urządzenia, przepływy i mechanizmy niewidoczne z zewnątrz."),
        ("Ekran dotykowy i kiosk", "Treści przygotowane pod konkretny ekran lub kiosk."),
        ("Materiał dla handlowca", "Prezentacja, która pomaga wyjaśnić produkt na spotkaniu z klientem."),
    ],
    "p3d_after_h2": "Targi się kończą. Prezentacja może pracować dalej.",
    "p3d_after": "Jeśli pozwala na to format i ustalenia umowy, model i materiały możesz wykorzystać ponownie — "
                 "w sprzedaży, w showroomie lub na stronie internetowej.",
    "p3d_after_tags": ["Sprzedaż", "Showroom", "Targi", "Strona WWW"],
    "cross_3d_h2": "Wystawiasz się na targach?",
    "cross_3d_text": "Prezentację możesz połączyć z projektem stoiska — z modelem 3D i zestawieniem kosztów. "
                     "Obie usługi zamawiasz osobno lub razem.",
    "cross_3d_link": "Projekt stoiska targowego",

    # ---------- polityka prywatności ----------
    "privacy_slug": "polityka-prywatnosci",
    "privacy_title": "Polityka prywatności | Scenovis",
    "privacy_desc": "Informacja o przetwarzaniu danych osobowych na stronie Scenovis.",
    "privacy_h1": "Polityka prywatności",
    "privacy_draft": "Wersja robocza — dane administratora, okres przechowywania danych i umowy z dostawcami wymagają "
                     "uzupełnienia i weryfikacji przed publikacją. Ten tekst nie został zweryfikowany prawnie.",

    # ---------- 404 ----------
    "nf_title": "Nie znaleziono strony | Scenovis",
    "nf_h1": "Nie ma tu takiej strony.",
    "nf_text": "Adres mógł się zmienić. Przejdź na stronę główną albo napisz do nas.",
    "nf_home": "Strona główna",
}

EN = {
    "lang_name": "English",
    "skip": "Skip to content",
    "nav_label": "Main navigation",
    "menu_open": "Open menu",
    "menu_close": "Close menu",
    "nav": [("@expo", "Exhibition stands"), ("@3d", "3D presentations"),
            ("#about", "About"), ("#faq", "FAQ")],
    "nav_expo": [("#scope", "Scope"), ("#example", "See the stand"), ("#process", "Process"),
                 ("#faq", "FAQ"), ("@3d", "3D presentations")],
    "nav_3d": [("#viewer-host", "3D model"), ("#example", "What we prepare"), ("#faq", "FAQ"),
               ("@expo", "Exhibition stands")],
    "nav_cta": "Contact",
    "lang_switch_label": "Language",
    "home_label": "Scenovis — home",
    "alt": {
        "stand": "3D render of an exhibition stand with microscopes, a screen and a touch kiosk",
        "visitor": "Exhibition stand from a visitor’s perspective: counter, screen and two microscope stations",
        "standmic": "Microscope on a demo station at an exhibition stand — 3D render",
        "kiosk": "Touch kiosk with an interactive 3D microscope presentation at an exhibition stand",
        "product": "3D model of a microscope in studio lighting — product render",
        "exploded": "Exploded view of a microscope: head, eyepieces, column, stage and objectives spread out in space",
        "objectives": "Close-up of the microscope objective turret — 3D render with depth of field",
        "front": "Stand visualisation from the aisle: counter with stools, screen and two microscope stations",
        "widok": "Visualisation of the whole stand from above: walls, lighting, counter, kiosk and demo stations",
        "kioskscreen": "Touch kiosk with an interactive 3D microscope presentation, the stand counter behind it",
        "cover3d": "Close-up of the microscope objectives above the specimen stage — cover of the 3D presentation video",
    },
    "footer_tagline": "Exhibition stand design and interactive 3D product presentations.",
    "footer_services": "Services",
    "footer_privacy": "Privacy policy",
    "footer_location": "Gdańsk, Poland",
    "footer_lang": "Polish and English",
    "breadcrumb_home": "Home",

    "home_title": "Scenovis — exhibition stand design and 3D product presentations",
    "home_desc": "Exhibition stand design with a 3D model and cost breakdown, plus interactive 3D presentations "
                 "of technical products — for trade fairs, showrooms and sales.",

    "hero_eyebrow": "EXHIBITION STANDS • 3D PRESENTATIONS",
    "hero_h1": "Show the product.<br>Understand the stand.<br><em>Control the budget.</em>",
    "hero_lead": "We design exhibition stands and interactive 3D product presentations. We bring together the concept, "
                 "the budget and the organisation of your trade fair — from design to on-site support.",
    "hero_cta_primary": "Tell me about your project",
    "hero_paths_label": "Services",
    "hero_paths": [("expo", "Exhibition stand design"), ("3d", "3D product presentations")],
    "hero_note": "Based in Gdańsk, Poland · projects across Poland and abroad · Polish or English",
    "variants": {
        "economy": {
            "name": "Economy",
            "scope": "System walls, carpet, 4 spotlights, a 75″ screen and a touch kiosk — all rented.",
            "alt": "Stand in the Economy option: system walls, carpet, four spotlights, a 75-inch screen and a touch kiosk",
            "tags": [("screen", "75″ screen", "rent"), ("spots", "4 spotlights", "rent"),
                     ("kiosk", "Touch kiosk", "rent"), ("floor", "Carpet", "rent")],
        },
        "smart": {
            "name": "Smart",
            "scope": "Frame with fabric graphics, a backlit brand panel, 6 spotlights and an LED line, a 98″ screen, "
                     "modular flooring — rented; your own kiosk or a rented one.",
            "alt": "Stand in the Smart option: backlit brand panel, six spotlights, LED line, 98-inch screen, modular flooring and a touch kiosk",
            "tags": [("screen", "98″ screen", "rent"), ("spots", "6 spotlights + LED line", "rent"),
                     ("brand", "Backlit brand panel", "rent"), ("kiosk", "Touch kiosk", "own")],
        },
        "premium": {
            "name": "Premium",
            "scope": "The Smart scope plus three backlit panels, lit pedestals, spotlights with a scene controller "
                     "and a professional 98″ display — rented, with on-site technical support.",
            "alt": "Stand in the Premium option: three backlit panels, lit pedestals, spotlights with a scene controller and a professional 98-inch display",
            "tags": [("screen", "Professional 98″ display", "rent"), ("spots", "Spotlights with scene controller", "rent"),
                     ("slats", "Backlit panels", "rent"), ("ped", "Lit pedestals", "rent")],
        },
    },
    "hero_variant_label": "Option",
    "hero_figure_label": "Stand elements labelled by cost type",

    "tldr_title": "Scenovis at a glance",
    "tldr_for": "<strong>Who it’s for:</strong> companies with a technical product — preparing a trade fair stand "
                "or looking for a clear way to show how their product works.",
    "tldr": [
        ("Stand design", "Concept, layout and 3D model — see the stand before it is built."),
        ("Costs in view", "Every element marked as rent, own equipment or service. Options to compare."),
        ("3D product presentations", "The build, mechanisms and operation of a device — interactive or animated."),
        ("From idea to delivery", "Stand design, product presentation and trade fair organisation — all of it or a chosen part."),
    ],

    "case_h2": "See the stand. Compare the options.",
    "case_lead": "Explore the layout, check the equipment and compare options before delivery.",
    "video_play": "Play video",
    "video_pause": "Pause video",
    "video_replay": "↻ Watch again",
    "video_duration": "Duration",
    "video_captions_note": "Captions are available in Polish and English. Sound plays only after you press play.",
    "case_benefits": [
        ("3D layout", "see the space and the display"),
        ("A clear budget", "check rentals, own equipment and services"),
        ("Option comparison", "choose Economy, Smart or Premium"),
    ],
    "case_cta": "Discuss your stand design",

    "case3d_h2": "An interactive product presentation",
    "case3d_lead": "The build, parts and operation of a technical device shown in 3D — on a screen, a kiosk or in a browser.",
    "case3d_benefits": [
        ("How the device is built", "components visible even inside the housing"),
        ("Part by part", "pick a part and look at it from every side"),
        ("How the product works", "the mechanism in motion, without shipping the device"),
    ],
    "case3d_cta": "Let’s talk about your product presentation",

    "services_label": "Services",
    "services_h2": "Two services — separately or together",
    "services_lead": "You can order stand design and a 3D product presentation independently of each other. "
                     "We quote every project individually, based on the agreed scope.",
    "services": [
        {
            "key": "expo", "code": "Service · EXPO", "title": "Exhibition stand design",
            "desc": "A well-planned stand and decisions made before production — based on a 3D model and a cost breakdown.",
            "items": ["Stand concept", "Functional layout and ergonomics", "3D model and visuals",
                      "Choice of furniture and technology", "Analysis: rent or use your own elements",
                      "List of elements and cost estimate", "Help choosing contractors"],
            "more": ("More about stand design", "expo"), "ask": "Discuss your stand design",
        },
        {
            "key": "3d", "code": "Service · 3D", "title": "Interactive 3D product presentations",
            "desc": "Show the inside of your product and how its mechanisms work — including devices that are hard "
                    "to demonstrate on site.",
            "items": ["Interactive models of technical products", "Touchscreen presentations",
                      "Animations of machines and devices in operation", "Product build and components",
                      "Technical visuals and feature demos",
                      "Material for trade fairs, showrooms and sales",
                      "Reuse — where the format and contract allow"],
            "more": ("More about 3D presentations", "3d"), "ask": "Talk about a presentation",
        },
    ],
    "full": {
        "label": "Full trade fair service",
        "title": "From idea to delivery",
        "desc": "Stand design, product presentation and the organisation of your trade fair. "
                "We can handle all of it or a chosen part.",
        "items": ["Design and 3D visualisation", "Interactive product presentations",
                  "Stand build, multimedia and furniture", "Transport, build-up and dismantling",
                  "Hosts and visitor service", "On-site event coordination"],
        "note": "We assemble the team and contractors to match the project scope.",
        "cta": "Let’s talk about your trade fair",
    },
    "services_note": "We agree the scope of each project together — no fixed packages.",

    "costs_label": "Stand costs",
    "costs_h2": "You know what you pay for.",
    "costs_lead": "Compare the equipment and how each part is paid for. We match the scope and the quote to your project.",
    "costs_sheet_title": "Stand 5.4 × 3.8 m",
    "costs_variant_label": "Compare options",
    "costs_cols": ("Element", "Scope", "Payment"),
    "cost_types": {"buy": "Buy", "rent": "Rent", "service": "Service", "mix": "Rent and buy"},
    "costs_rows": [
        ("Walls and graphics", [("rent", "System walls, vinyl graphics"), ("buy", "Own frame, fabric graphics"),
                                ("buy", "Own frame, fabric graphics")]),
        ("Brand lighting", [("buy", "No backlighting"), ("buy", "Backlit brand panel"), ("buy", "Three backlit panels")]),
        ("Lighting", [("rent", "4 LED spotlights"), ("mix", "6 spotlights and an LED line"),
                      ("buy", "Own spotlights, LED line, pedestals")]),
        ("Screen", [("buy", "75″ TV"), ("buy", "98″ TV"), ("buy", "Professional 98″ display")]),
        ("Touch kiosk", [("rent", "Kiosk with 3D presentation"), ("buy", "Own kiosk with 3D presentation"),
                         ("buy", "Own kiosk with 3D presentation")]),
        ("Flooring", [("rent", "Exhibition carpet"), ("buy", "Modular floor with edging"), ("buy", "Modular floor with edging")]),
        ("Furniture and display", [("rent", "Counter, stools, pedestals"), ("buy", "Counter with cabinets, stools, pedestals"),
                                   ("buy", "Counter with cabinets, stools, pedestals")]),
        ("Transport and build", [("service", "Build-up and dismantling — 2 people"), ("service", "Build-up and dismantling — 3 people"),
                                 ("service", "Build-up and dismantling — 4 people")]),
        ("Staff", [("service", "Host"), ("service", "Host and product demonstrator"),
                   ("service", "2 hosts, demonstrator, technician")]),
        ("Coordination", [("service", "On site — to be agreed"), ("service", "On site — to be agreed"),
                          ("service", "On site — to be agreed")]),
    ],
    "costs_more": "Show scope",
    "costs_more_items": [
        ["3 kW power connection", "Screen content — basic package", "Electrician during build-up",
         "Organiser fees: space, registration, internet, cleaning"],
        ["3 kW power connection", "Screen content — standard package", "Electrician during build-up",
         "Transport cases and storage between fairs", "Organiser fees: space, registration, internet, cleaning"],
        ["9 kW power connection", "Lighting scene controller", "Screen content — extended package",
         "Electrician during build-up", "Transport cases and storage between fairs",
         "Organiser fees: space, registration, internet, cleaning"],
    ],
    "costs_price": "Individual quote",
    "costs_price_note": "No fixed packages — we agree the scope and the quote for your specific fair.",
    "costs_legend": [
        ("own", "Own", "your equipment, used in the design"),
        ("rent", "Rent", "for the time of the fair"),
        ("service", "Service", "transport, installation and staffing"),
    ],

    "about_label": "About",
    "about_h2": "Hi, I’m Aleks.",
    "about_body": [
        "I run Scenovis myself. My background is in BIM, 3D model coordination, visualisation and technical "
        "processes — on construction and industrial projects.",
        "I personally lead the concept and prepare 3D models, technical presentations, functional analysis "
        "and cost breakdowns.",
        "When a task needs other skills — production, installation, multimedia or logistics — I work with "
        "subcontractors selected for the project. You talk directly to me, and we match the team of partners "
        "to the scope.",
    ],
    "about_photo_alt": "Aleks — Scenovis",
    "about_linkedin": "LinkedIn profile",

    "process_label": "Process",
    "process_h2": "How we work together",
    "process": [
        ("Call and brief", "Goal, dates, scope and budget. One sentence is enough to start."),
        ("Concept", "A stand layout or a storyline for the product presentation."),
        ("3D model and breakdown", "Visuals, a presentation or a cost breakdown — depending on the service."),
        ("Review and decision", "We go through the result together and agree the next steps."),
        ("Delivery and the fair", "A team and contractors matched to the scope, or a hand-over of materials to your own team."),
    ],

    "faq_label": "FAQ",
    "faq_h2": "Frequently asked questions",
    "faq": {
        "price": ("How do you price a project?",
                  "<p>Every project is quoted individually — there are no fixed packages. The quote depends on the scope: "
                  "for a stand, for example, on floor space and the number of options; for a 3D presentation, on the "
                  "complexity of the product and the format. We give you a quote after a short call, before any work starts.</p>"),
        "expo_process": ("What does the stand design process look like?",
                         "<p>We start with a brief: the fair, dates, floor space, goal and budget. We then prepare the concept "
                         "and functional layout, a 3D model and a list of elements with their cost type. We go through the "
                         "options, and only then do you decide what to order from contractors.</p>"),
        "factors": ("What drives the cost of a stand?",
                    "<p>Usually: floor space and build type (modular or custom), materials and finish, graphics, lighting, "
                    "multimedia, furniture, transport, build-up and dismantling, plus organiser fees (e.g. utility connections). "
                    "For your project we break this down element by element.</p>"),
        "buyrent": ("What should be rented and what can come from your own equipment?",
                    "<p>Most elements — the stand build, AV equipment, lighting and furniture — are best rented for the time "
                    "of the fair. Your own elements, such as a kiosk, a screen or graphics from previous fairs, are included "
                    "in the design, and we only quote the rental of what is missing.</p>"),
        "reuse": ("Can the stand be reused at future fairs?",
                  "<p>Yes, if we plan for it from the start: modules, replaceable graphics, transport and storage. "
                  "We ask about it in the brief, because it affects which elements we choose.</p>"),
        "materials": ("What is needed to start?",
                      "<p>Enough to start: the fair and its dates, floor space and stand type (island, corner, inline), "
                      "what you want to show and a rough budget. Also helpful: logo or brand guide, product photos or models "
                      "(e.g. STEP) and the organiser’s technical rules.</p>"),
        "delivery": ("Can you handle the whole delivery?",
                     "<p>Yes. Stand build, multimedia, transport, installation, stand staff and on-site coordination are "
                     "organised within the scope we agree — we assemble the team and contractors for the project. "
                     "You can also order just the design with a cost breakdown and build it with your own contractor.</p>"),
        "area": ("Where do you work?",
                 "<p>We work from Gdańsk for clients across Poland and at trade fairs abroad. The design, 3D model and cost "
                 "breakdown are prepared remotely, with meetings online or in person. On-site service and coordination "
                 "during the fair are agreed individually.</p>"),
        "time": ("How early should we start?",
                 "<p>Ideally start 2–3 months before the fair, and earlier for a custom-built or large stand. "
                 "Organisers often require design approval in advance, and contractors need time for quotes and production.</p>"
                 "<p>With a smaller scope and materials ready (stand dimensions, logo, product data) "
                 "we can work faster. We agree a specific schedule after the brief.</p>"),
        "3d_forms": ("What form can a 3D presentation take?",
                     "<p>Depending on your needs: an interactive presentation where the user picks parts of the product, "
                     "an animation or film, or a set of visuals and cutaways. We choose the format for where it will be "
                     "used — a stand, a showroom, a sales meeting or a website.</p>"),
        "3d_data": ("What data do you need for a 3D product presentation?",
                    "<p>CAD models (e.g. STEP) or technical drawings work best. If you don’t have them, we can start from "
                    "photos, dimensions and a description of how it works — and agree the right level of detail together.</p>"),
        "3d_hw": ("Which devices does the interactive presentation run on?",
                  "<p>As standard, the presentation runs in a web browser — on a laptop or a touchscreen. Quality and set-up "
                  "are matched to the hardware: an online version (e.g. high-quality streaming) needs internet access, "
                  "while on a desktop computer or kiosk it can run locally, offline. We agree the option at the start "
                  "of the project.</p>"),
        "3d_reuse": ("Can the presentation be reused?",
                     "<p>Yes, where the format and the contract allow it. A model and materials prepared for a fair can later "
                     "support sales, a showroom, or be used as video and images on your website.</p>"),
        "3d_nofair": ("Does a 3D presentation have to be for a trade fair?",
                      "<p>No. A presentation can support sales reps in meetings, run in a showroom or on a website. "
                      "You don’t need a stand for it.</p>"),
    },

    "contact_label": "Contact",
    "contact_h2": "Tell me about your project.",
    "contact_h2_expo": "Discuss your stand design.",
    "contact_h2_3d": "Let’s talk about your product presentation.",
    "contact_lead": "A phone number or email is enough. We’ll get back to you to discuss the details.",
    "contact_direct": "Or contact us directly",
    "contact_phone_sub": "Call",
    "contact_email_sub": "Send a brief or files",
    "contact_wa": "Message on WhatsApp",
    "contact_brief": "Already have a brief? Send it to {email}.",
    "contact_lang": "We work in Polish and English.",
    "form_title": "Quick enquiry",
    "f_contact": "Phone or email",
    "f_contact_hint": "E.g. +48 500 000 000 or name@company.com",
    "f_required": "required",
    "f_optional": "optional",
    "f_topic": "Topic",
    "f_name": "Name",
    "f_message": "Message",
    "f_message_ph": "E.g. which product or fair, when, and what you need",
    "f_more": "Add project details",
    "f_event": "Fair / event",
    "f_city": "City",
    "f_date": "Dates",
    "f_date_ph": "E.g. March 2027",
    "f_area": "Stand size (m²)",
    "f_budget": "Rough budget",
    "f_budget_ph": "E.g. an amount or “to be agreed”",
    "f_reuse": "Reuse at future fairs?",
    "f_reuse_opts": [("", "Not sure yet"), ("yes", "Yes, I want to reuse it"), ("no", "No, one-off")],
    "f_submit": "Send enquiry",
    "f_sending": "Sending…",
    "f_disclaimer": "We use your details to respond to your enquiry and protect the form. Details: <a href=\"{privacy}\">privacy policy</a>.",
    "f_err_empty": "Please enter a phone number or an email address.",
    "f_err_email": "Please check the email address — it should look like name@company.com.",
    "f_err_contact": "Enter a phone number or an email address.",
    "f_success": "Thank you — your enquiry has been sent. We’ll get back to you as soon as we can.",
    "f_fail": "The form wasn’t sent — your message did not go through. It’s ready to send by email or WhatsApp instead:",
    "f_fail_email": "Send by email",
    "f_fail_wa": "Send via WhatsApp",
    "f_turnstile_label": "Form security check",
    "f_turnstile_wait": "Security check is loading — please try again in a moment.",
    "f_turnstile_check": "Please complete the security check and try again.",
    "f_turnstile_unavailable": "The form is temporarily unavailable, so your message was not sent. Please send it by email or WhatsApp:",
    "f_preview": "This is a local preview — sending works once the site is published. You can test sending by email:",
    "mail_subject": "Enquiry from the Scenovis website",
    "wa_hello": "Hello, I’m writing from the Scenovis website.",
    "topics": {"general": "General enquiry", "expo": "Exhibition stand design", "3d": "3D product presentation",
               "delivery": "Full trade fair service"},
    "field_names": {"contact": "Contact", "name": "Name", "message": "Message", "topic": "Topic",
                    "event": "Fair", "city": "City", "date": "Dates", "area": "Stand size",
                    "budget": "Budget", "reuse": "Reuse"},

    "expo_slug": "exhibition-stand-design",
    "expo_title": "Exhibition stand design in 3D with cost breakdown | Scenovis",
    "expo_desc": "Exhibition stand concept, functional layout and 3D visualisation. A list of elements and costs "
                 "(rent, own equipment, service) and an option comparison before production.",
    "expo_crumb": "Exhibition stand design",
    "expo_eyebrow": "EXHIBITION STAND DESIGN",
    "expo_h1": "Exhibition stand design <em>with the costs in view.</em>",
    "expo_lead": "We prepare the stand concept and layout, a 3D model and a list of elements with their costs. "
                 "You compare solutions and make decisions before you order production.",
    "expo_points": ["Concept and functional layout", "3D model and visuals",
                    "Rent / own / service for every element", "Options to compare before delivery"],
    "expo_cta": "Discuss your stand design",
    "expo_cta2": "See the stand",
    "expo_get_h2": "What stand design includes",
    "expo_shots": [("front", "Concept and layout — counter, screen and demo stations seen from the aisle"),
                   ("widok", "3D model with equipment — the basis for the breakdown and option comparison")],
    "expo_get": [
        ("Concept", "The purpose of the stand, the message and what visitors should remember."),
        ("Layout and ergonomics", "Demo, meeting and storage zones, visitor flow, product display."),
        ("3D model and visuals", "Views from every side and shots for discussing the project internally."),
        ("Furniture and technology", "Choosing furniture, multimedia and lighting to fit the stand’s purpose."),
        ("Breakdown and options", "Elements described as rent, own equipment or service — with options to compare."),
        ("Choosing contractors", "Material for requests for quotation and help comparing quotes."),
    ],
    "cross_expo_h2": "Need a product presentation too?",
    "cross_expo_text": "On a stand you often need to explain a product that is hard to show live. "
                       "An interactive 3D presentation can be part of the project or a separate commission.",
    "cross_expo_link": "3D product presentations",

    "p3d_slug": "3d-product-presentations",
    "p3d_title": "Interactive 3D product presentations | Scenovis",
    "p3d_desc": "Interactive 3D models, working animations and cutaways of technical products. For touchscreens, "
                "showrooms, sales meetings and trade fairs.",
    "p3d_crumb": "3D product presentations",
    "p3d_eyebrow": "3D PRODUCT PRESENTATIONS",
    "p3d_h1": "Show how <em>your product works.</em>",
    "p3d_lead": "Interactive models, animations and cutaways of technical products. Show the build and the mechanisms "
                "you can’t see from outside — in sales meetings, in a showroom and at trade fairs.",
    "p3d_points": ["Product build and components", "Animations of mechanisms at work",
                   "Touchscreen interaction", "Support for sales teams"],
    "p3d_cta": "Let’s talk about your product presentation",
    "p3d_cta2": "Watch the video",
    "viewer": {
        "launch": "Launch 3D model", "loading": "Loading model…", "canvas_label": "Interactive 3D model of a microscope",
        "explode": "Explode", "assemble": "Assemble", "reset": "Reset view",
        "tour": "Guided tour", "tour_stop": "Stop", "prev": "Previous", "next": "Next", "close": "Close description",
        "hint": "Drag to rotate · scroll or pinch to zoom · numbers zoom in on parts",
        "error": "The 3D model could not start in this browser. The render stays below.",
        "note": "The model runs in your browser (about 2–3 MB to download).",
        "hotspots": [
            {"node": "Head_Body", "title": "Head with eyepieces", "text": "The viewing path: the image from the objective travels through the head to both eyepieces."},
            {"node": "Nosepiece_Turret", "title": "Objective turret", "text": "Three objectives: 4×, 10× and 40×. Turning the turret changes the magnification."},
            {"node": "Stage_Plate", "title": "Specimen stage", "text": "The slide sits here. The holder lets you move it precisely."},
            {"node": "FocusKnob_Coarse_L", "title": "Focus knobs", "text": "Coarse and fine focus raise the stage to bring the image into focus."},
            {"node": "Illuminator_Housing", "title": "Illuminator", "text": "Light from the base passes through the condenser and the specimen into the objective."},
        ],
    },
    "p3d_get_h2": "What we can prepare",
    "p3d_shots": [("exploded", "Exploded view — the device built up part by part"),
                  ("kiosk", "The same presentation on a touch kiosk at the stand")],
    "p3d_get": [
        ("Interactive model", "The user rotates the product, picks a part and looks at it up close."),
        ("Working animation", "A short film or sequence showing how the mechanism operates."),
        ("Build and components", "An exploded view: components spread out in space."),
        ("Cutaway", "The inside of the device — flows and mechanisms you can’t see from outside."),
        ("Touchscreen and kiosk", "Content prepared for a specific screen or kiosk."),
        ("Material for sales", "A presentation that helps explain the product in a customer meeting."),
    ],
    "p3d_after_h2": "The fair ends. The presentation can keep working.",
    "p3d_after": "Where the format and the contract allow, the model and materials can be reused — "
                 "in sales, in a showroom or on your website.",
    "p3d_after_tags": ["Sales", "Showroom", "Trade fairs", "Website"],
    "cross_3d_h2": "Exhibiting at a trade fair?",
    "cross_3d_text": "You can combine the presentation with a stand design — with a 3D model and a cost breakdown. "
                     "Order the services separately or together.",
    "cross_3d_link": "Exhibition stand design",

    "privacy_slug": "privacy-policy",
    "privacy_title": "Privacy policy | Scenovis",
    "privacy_desc": "How personal data is processed on the Scenovis website.",
    "privacy_h1": "Privacy policy",
    "privacy_draft": "Draft — the controller’s details, retention period and provider agreements must be completed and "
                     "checked before publication. This text has not been legally reviewed.",

    "nf_title": "Page not found | Scenovis",
    "nf_h1": "This page doesn’t exist.",
    "nf_text": "The address may have changed. Go to the home page or contact us.",
    "nf_home": "Home page",
}

CONTENT = {"pl": PL, "en": EN}
