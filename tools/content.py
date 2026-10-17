# -*- coding: utf-8 -*-
"""
SCENOVIS — treści strony (PL / EN).

Tu edytujesz teksty. Po zmianie uruchom:  python3 tools/build.py
Generator zapisze gotowe pliki HTML w /pl/ i /en/.

Zasady:
- Każdy klucz musi istnieć w obu językach (build sprawdza to automatycznie).
- {todo:...} w tekście = widoczny znacznik TODO w trybie roboczym (DRAFT=True w config.py).
- Wolno używać prostego HTML (<em>, <br>, <strong>, <a>).
"""

PL = {
    # ---------- wspólne ----------
    "lang_name": "Polski",
    "skip": "Przejdź do treści",
    "nav_label": "Nawigacja główna",
    "menu_open": "Otwórz menu",
    "menu_close": "Zamknij menu",
    "nav": [("#oferta", "Oferta"), ("#przyklad", "Przykład"), ("#koszty", "Koszty"),
            ("#o-mnie", "O mnie"), ("#faq", "FAQ")],
    "nav_cta": "Kontakt",
    "lang_switch_label": "Wersja językowa",
    "home_label": "Scenovis — strona główna",
    "concept_caption": "Ilustracja koncepcyjna wygenerowana z pomocą AI — nie jest realizacją dla klienta.",
    "concept_badge": "Koncepcja (AI)",
    "footer_tagline": "Projekt stoisk targowych, prezentacje produktów 3D i multimedia.",
    "footer_privacy": "Polityka prywatności",
    "footer_location": "Gdańsk, Polska",
    "footer_lang": "Obsługa po polsku i angielsku",
    "breadcrumb_home": "Strona główna",

    # ---------- strona główna: meta ----------
    "home_title": "Scenovis — projekt stoiska targowego, 3D i kosztorys",
    "home_desc": "Projekt i wizualizacja 3D stoiska targowego z przejrzystym zestawieniem kosztów: "
                 "zakup, wynajem, usługa. Prezentacje produktów 3D i multimedia na targi.",

    # ---------- hero ----------
    "hero_eyebrow": "EXPO • 3D • MULTIMEDIA • KOSZTY",
    "hero_h1": "Pokaż produkt.<br>Zrozum stoisko.<br><em>Kontroluj budżet.</em>",
    "hero_lead": "Pomagam zaprojektować stoisko targowe: układ, model 3D i zestawienie kosztów, "
                 "w którym widać, co jest zakupem, co wynajmem, a co usługą. Do produkcji, "
                 "multimediów i montażu dobieram wykonawców odpowiednich do projektu.",
    "hero_cta_primary": "Zobacz, jak to działa",
    "hero_cta_secondary": "Omówmy Twoje targi",
    "hero_note": "Gdańsk, cała Polska {todo:potwierdź obszar działania} · rozmowa po polsku lub angielsku",
    "hero_tags": [
        ("led", "Ściana LED", "wynajem"),
        ("light", "Oświetlenie", "wynajem"),
        ("kiosk", "Kiosk dotykowy", "zakup"),
        ("build", "Montaż i demontaż", "usługa"),
    ],
    "hero_variant_label": "Wariant",
    "hero_figure_label": "Przykład: elementy stoiska opisane typem kosztu",

    # ---------- w skrócie ----------
    "tldr_title": "Scenovis w skrócie",
    "tldr_for": "<strong>Dla kogo:</strong> dla firm, które wystawiają się na targach — "
                "szczególnie z produktem technicznym, który trzeba dobrze wyjaśnić.",
    "tldr": [
        ("Koncepcja i układ", "Strefy, ruch odwiedzających, miejsce na rozmowy i pokaz produktu."),
        ("Model i wizualizacja 3D", "Oglądasz stoisko z każdej strony, zanim powstanie."),
        ("Koszty bez zgadywania", "Każdy element jako zakup, wynajem lub usługa. Warianty do porównania."),
        ("Realizacja z wykonawcami", "Zabudowę, multimedia i montaż dobieram do zakresu i budżetu."),
    ],

    # ---------- case study / film ----------
    "case_label": "Przykład",
    "case_tag": "Projekt demonstracyjny / Scenovis Concept",
    "case_h2": "Od koncepcji stoiska do decyzji budżetowej",
    "case_lead": "Zobacz, jak klient może obejrzeć stoisko, sprawdzić koszt każdego elementu "
                 "i porównać warianty przed produkcją.",
    "case_intro": "Na filmie sam steruję interaktywną prezentacją zbudowaną w Blenderze. "
                  "To zapis działającego narzędzia, a nie animacja.",
    "video_placeholder_title": "Film w przygotowaniu",
    "video_placeholder_text": "Tutaj pojawi się nagranie prezentacji stoiska.",
    "video_todo": "{todo:EXPO VIDEO — MP4 + poster + napisy PL/EN, zob. TODO.md}",
    "video_play": "Odtwórz film",
    "video_duration": "Czas trwania",
    "video_captions_note": "Film ma napisy po polsku i angielsku. Dźwięk włącza się dopiero po kliknięciu.",
    "case_benefits": [
        ("Cały układ, nie tylko render", "Zmieniasz kamery i oglądasz każdą strefę stoiska."),
        ("Koszt przy każdym elemencie", "Konstrukcja, oświetlenie, multimedia — z podziałem na zakup, wynajem i usługę."),
        ("Warianty przed produkcją", "Porównujesz Economy, Smart i Premium i widzisz, gdzie można oszczędzić."),
    ],
    "case_chapters_title": "Co pokazuje film",
    "case_chapters": [
        "Ogólny widok stoiska", "Zmiana kamery", "Wybór elementu", "Obrót wokół obiektu",
        "Koszt elementu", "Zakup, wynajem czy usługa", "Warianty Economy / Smart / Premium",
        "Koszt oświetlenia", "Kiosk dotykowy", "Prezentacja mikroskopu", "Powrót do stoiska",
        "Potencjalne oszczędności",
    ],
    "case_transcript": "Transkrypcja filmu",
    "case_transcript_body": "<p>{todo:TRANSKRYPCJA — wklej tekst lektora / opis kroków po nagraniu filmu}</p>",
    "case_cta_q": "Chcesz zobaczyć w ten sposób swoje stoisko?",
    "case_cta": "Porozmawiajmy o Twoich targach",

    # ---------- oferta ----------
    "services_label": "Oferta",
    "services_h2": "Trzy obszary, w których mogę pomóc",
    "services_lead": "Możesz zamówić sam projekt z kosztorysem albo cały zakres — "
                     "z realizacją przez wykonawców dobranych do projektu.",
    "services": [
        {
            "key": "expo", "code": "Expo design & cost", "title": "Projekt stoiska i koszty",
            "desc": "Koncepcja, układ i model 3D stoiska — razem ze strukturą kosztów i wariantami do porównania.",
            "items": ["Koncepcja i układ funkcjonalny", "Wizualizacja i model 3D",
                      "Warianty Economy / Smart / Premium", "Porównanie: zakup czy wynajem",
                      "Optymalizacja pod budżet", "Materiały do rozmów z wykonawcami"],
            "who": "Przygotowuję osobiście", "who_type": "own",
            "more": ("Więcej o projekcie stoiska", "expo"), "ask": "Zapytaj o projekt stoiska",
        },
        {
            "key": "3d", "code": "Product 3D & multimedia", "title": "Prezentacje produktów 3D i multimedia",
            "desc": "Pokazujesz, jak działa produkt — także to, czego nie widać z zewnątrz.",
            "items": ["Modele produktowe i animacje", "Widoki rozłożone i przekroje",
                      "Interaktywne prezentacje", "Treści na ekrany dotykowe i kioski",
                      "Materiały do showroomu i sprzedaży"],
            "who": "Przygotowuję osobiście", "who_type": "own",
            "more": ("Więcej o prezentacjach 3D", "3d"), "ask": "Zapytaj o prezentację 3D",
        },
        {
            "key": "delivery", "code": "Delivery & on-site", "title": "Realizacja i wsparcie na miejscu",
            "desc": "Gdy projekt przechodzi do realizacji, dobieram wykonawców do zakresu. Wiesz, kto za co odpowiada.",
            "items": ["Zabudowa i druk", "Multimedia, ekrany, oświetlenie", "Transport, montaż, demontaż",
                      "Personel stoiska — opcjonalnie", "Koordynacja na miejscu — opcjonalnie"],
            "who": "Z wykonawcami dobranymi do projektu", "who_type": "partners",
            "more": None, "ask": "Zapytaj o realizację",
        },
    ],
    "services_note": "Nie każdy element jest potrzebny w każdym projekcie — zakres ustalamy razem.",

    # ---------- koszty ----------
    "costs_label": "Koszty",
    "costs_h2": "Nie tylko render.<br><em>Wiesz, za co płacisz.</em>",
    "costs_lead": "Każdy element stoiska ma w projekcie swój koszt i typ. Rozmawiamy o konkretach, "
                  "a nie o jednej kwocie „za całość”.",
    "costs_sheet_title": "Zestawienie elementów stoiska",
    "costs_sheet_note": "Przykład poglądowy. Elementy i kwoty ustalam dla konkretnego projektu, na podstawie ofert wykonawców.",
    "costs_variant_label": "Porównaj warianty",
    "costs_cols": ("Element", "Typ kosztu", "Co obejmuje"),
    "cost_types": {"buy": "Zakup", "rent": "Wynajem", "service": "Usługa", "buyrent": "Zakup lub wynajem"},
    "costs_rows": [
        ("K-01", "Konstrukcja", "buyrent", ["System modułowy z wynajmu", "System modułowy + własne elementy wielokrotnego użytku", "Zabudowa indywidualna"]),
        ("G-02", "Grafika", "buy", ["Wydruki na ramach systemowych", "Wymienna grafika tekstylna", "Grafika tekstylna, podświetlenia, elementy 3D"]),
        ("O-03", "Oświetlenie", "rent", ["Oświetlenie standardowe + kilka reflektorów", "Reflektory na szynach, akcent na produkt", "Projekt oświetlenia scenicznego"]),
        ("M-04", "Multimedia", "rent", ["Jeden ekran z pętlą wideo", "Ekran + kiosk dotykowy z prezentacją 3D", "Ściana LED + interaktywne stanowiska"]),
        ("F-05", "Meble", "rent", ["Lada i dwa hokery", "Strefa rozmów + lada z magazynkiem", "Meble na wymiar i zaplecze"]),
        ("L-06", "Logistyka", "service", ["Transport z wypożyczalni", "Transport + magazynowanie elementów", "Transport, magazyn i ubezpieczenie"]),
        ("S-07", "Montaż", "service", ["Montaż i demontaż systemu", "Montaż, demontaż i serwis AV", "Ekipa montażowa + technik na targach"]),
    ],
    "costs_legend": [
        ("buy", "Zakup", "zostaje u Ciebie — możesz użyć go ponownie"),
        ("rent", "Wynajem", "płacisz za czas targów"),
        ("service", "Usługa", "praca ludzi: transport, montaż, obsługa"),
    ],
    "costs_get_title": "Co dostajesz",
    "costs_get": ["Model 3D z podziałem na elementy", "Zestawienie: zakup / wynajem / usługa",
                  "Porównanie wariantów", "Wskazanie, gdzie można oszczędzić"],

    # ---------- o mnie ----------
    "about_label": "O mnie",
    "about_h2": "Cześć, jestem Aleks.",
    "about_body": [
        "Na co dzień pracuję z modelami 3D i dokumentacją techniczną — mam doświadczenie w BIM. "
        "W Scenovis wykorzystuję je, żeby pomóc firmom dobrze przygotować się do targów.",
        "Przy projekcie stoiska przygotowuję koncepcję, układ, wizualizację i zestawienie kosztów. "
        "Gdy projekt przechodzi do realizacji, współpracuję z wykonawcami dobranymi do zakresu — "
        "m.in. od zabudowy, multimediów, montażu, logistyki i obsługi.",
        "Rozmawiasz bezpośrednio ze mną, czyli z osobą, która przygotowuje koncepcję.",
    ],
    "about_photo_alt": "Aleks — Scenovis",
    "about_linkedin": "Profil na LinkedIn",
    "about_own_title": "W czym pomagam bezpośrednio",
    "about_own": ["Brief", "Koncepcja", "Układ", "Model 3D", "Koszty", "Prezentacja"],
    "about_partners_title": "Przy realizacji współpracuję z",
    "about_partners": ["Zabudowa", "Druk", "AV i ekrany", "Oświetlenie", "Logistyka",
                       "Montaż i demontaż", "Personel", "Koordynacja na miejscu"],
    "about_partners_note": "To niezależne firmy i specjaliści dobierani do konkretnego projektu, a nie pracownicy Scenovis. "
                           "Przed startem wiesz, kto odpowiada za który element.",

    # ---------- proces ----------
    "process_label": "Współpraca",
    "process_h2": "Jak wygląda współpraca",
    "process": [
        ("Rozmowa i brief", "Targi, termin, powierzchnia, produkt i budżet. Możesz zacząć od jednego zdania."),
        ("Koncepcja i układ", "Strefy, ścieżka odwiedzającego, miejsce na pokaz i rozmowy."),
        ("Model 3D i koszty", "Wizualizacja oraz zestawienie kosztów z wariantami do porównania."),
        ("Prezentacja i decyzja", "Omawiamy projekt razem i wybierasz wariant — wiesz, z czego wynika cena."),
        ("Realizacja — opcjonalnie", "Dobieram wykonawców i pomagam w koordynacji albo przekazuję materiały Twojemu wykonawcy."),
    ],

    # ---------- FAQ ----------
    "faq_label": "FAQ",
    "faq_h2": "Częste pytania",
    "faq": {
        "price": ("Ile kosztuje projekt stoiska targowego?",
                  "<p>Zależy od zakresu: powierzchni, liczby wariantów i tego, czy potrzebujesz prezentacji 3D "
                  "lub multimediów. Wycenę projektu podaję po krótkiej rozmowie, przed rozpoczęciem pracy.</p>"
                  "<p>{todo:FAQ CENA — podaj model wyceny lub widełki „od”, jeśli chcesz je pokazać}</p>"),
        "factors": ("Od czego zależy koszt stoiska?",
                    "<p>Najczęściej od: powierzchni i typu zabudowy (systemowa lub indywidualna), materiałów "
                    "i wykończenia, grafiki, oświetlenia, multimediów, mebli, transportu, montażu i demontażu "
                    "oraz opłat organizatora (np. przyłącza mediów). Dla Twojego projektu rozpisuję to element po elemencie.</p>"),
        "buyrent": ("Co lepiej wynająć, a co kupić?",
                    "<p>To zależy przede wszystkim od tego, ile razy w roku się wystawiasz. Elementy używane wielokrotnie "
                    "— np. konstrukcja systemowa, kiosk czy uniwersalna grafika — często opłaca się kupić. Sprzęt AV "
                    "szybko się starzeje, więc zwykle lepiej go wynająć. W projekcie porównuję oba warianty dla Twojej sytuacji.</p>"),
        "reuse": ("Czy stoisko można wykorzystać na kolejnych targach?",
                  "<p>Tak, jeśli zaplanujemy to od początku: moduły, wymienne grafiki, transport i magazynowanie. "
                  "Pytam o to już na etapie briefu, bo wpływa to na wybór zakup / wynajem.</p>"),
        "materials": ("Jakich materiałów potrzebujesz na start?",
                      "<p>Wystarczy: nazwa targów i termin, powierzchnia i rodzaj stoiska (wyspowe, narożne, rzędowe), "
                      "co chcesz pokazać i orientacyjny budżet. Pomocne będą też: logo lub brandbook, zdjęcia albo modele "
                      "produktu (np. STEP) i regulamin techniczny organizatora.</p>"),
        "delivery": ("Czy Scenovis może pomóc również z realizacją?",
                     "<p>Tak. Do realizacji dobieram wykonawców odpowiednich do zakresu — od zabudowy i druku, przez multimedia "
                     "i oświetlenie, po transport, montaż i obsługę. Możesz też zamówić sam projekt z kosztorysem "
                     "i zrealizować go z własnym wykonawcą.</p>"),
        "area": ("Gdzie działasz?",
                 "<p>{todo:OBSZAR DZIAŁANIA — np. cała Polska / wybrane targi za granicą}</p>"),
        "time": ("Ile wcześniej trzeba zacząć?",
                 "<p>{todo:TERMINY — ile tygodni przed targami najlepiej zacząć projekt i realizację}</p>"),
        "3d_data": ("Jakich danych potrzebujesz do prezentacji 3D produktu?",
                    "<p>Najlepiej pracuje się na modelach CAD (np. STEP) lub rysunkach technicznych. Jeśli ich nie ma, "
                    "zaczniemy od zdjęć, wymiarów i opisu działania — ustalimy razem, jaki poziom szczegółów ma sens.</p>"),
        "3d_hw": ("Na czym działa interaktywna prezentacja?",
                  "<p>{todo:SPRZĘT — na jakim sprzęcie / ekranie działa prezentacja, czy działa offline}</p>"),
        "3d_reuse": ("Czy prezentację można wykorzystać po targach?",
                     "<p>Tak. Model i materiały przygotowane na targi mogą później służyć w sprzedaży, w showroomie "
                     "lub jako film i grafiki na stronę internetową.</p>"),
    },

    # ---------- kontakt ----------
    "contact_label": "Kontakt",
    "contact_h2": "Opowiedz o swoich targach.",
    "contact_lead": "Wystarczy telefon lub e-mail. Odezwę się, żeby ustalić szczegóły.",
    "contact_direct": "Albo napisz lub zadzwoń bezpośrednio",
    "contact_phone_sub": "Zadzwoń",
    "contact_email_sub": "Wyślij brief lub pliki",
    "contact_wa": "Napisz na WhatsApp",
    "contact_brief": "Masz już brief? Wyślij go na {email}.",
    "contact_lang": "Rozmawiam po polsku i angielsku.",
    "form_title": "Szybkie zapytanie",
    "f_contact": "Telefon lub e-mail",
    "f_contact_hint": "Np. +48 500 000 000 lub imie@firma.pl",
    "f_required": "wymagane",
    "f_optional": "opcjonalnie",
    "f_name": "Imię",
    "f_message": "Wiadomość",
    "f_message_ph": "Np. jakie targi, kiedy i co chcesz pokazać",
    "f_more": "Dodaj szczegóły targów",
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
    "f_disclaimer": "Dane wykorzystam do obsługi zapytania i zabezpieczenia formularza. Szczegóły: <a href=\"{privacy}\">polityka prywatności</a>.",
    "f_err_contact": "Wpisz numer telefonu (min. 7 cyfr) albo poprawny adres e-mail.",
    "f_success": "Dziękuję — zapytanie zostało wysłane. Odezwę się najszybciej, jak to możliwe.",
    "f_fail": "Formularz nie został wysłany. Twoja wiadomość jest gotowa — wyślij ją e-mailem lub przez WhatsApp:",
    "f_fail_email": "Wyślij e-mailem",
    "f_fail_wa": "Wyślij przez WhatsApp",
    "f_turnstile_label": "Zabezpieczenie formularza",
    "f_turnstile_wait": "Trwa wczytywanie zabezpieczenia formularza — spróbuj ponownie za chwilę.",
    "f_turnstile_check": "Potwierdź weryfikację bezpieczeństwa formularza i spróbuj ponownie.",
    "f_turnstile_unavailable": "Zabezpieczenie formularza jest chwilowo niedostępne. Wyślij zapytanie e-mailem:",
    "f_preview": "To podgląd lokalny — wysyłka działa po publikacji. Możesz przetestować wysyłkę e-mailem:",
    "mail_subject": "Zapytanie ze strony Scenovis",
    "wa_hello": "Dzień dobry, piszę ze strony Scenovis.",
    "topics": {"expo": "Projekt stoiska i koszty", "3d": "Prezentacja 3D / multimedia",
               "delivery": "Realizacja", "general": "Ogólne"},
    "field_names": {"contact": "Kontakt", "name": "Imię", "message": "Wiadomość", "topic": "Temat",
                    "event": "Targi", "city": "Miasto", "date": "Termin", "area": "Powierzchnia",
                    "budget": "Budżet", "reuse": "Ponowne użycie"},

    # ---------- landing: projekt stoiska ----------
    "expo_slug": "projekt-stoiska-targowego",
    "expo_title": "Projekt stoiska targowego 3D z kosztorysem | Scenovis",
    "expo_desc": "Koncepcja, układ i wizualizacja 3D stoiska targowego. Zestawienie kosztów: zakup, wynajem, "
                 "usługa i warianty Economy / Smart / Premium — przed produkcją.",
    "expo_crumb": "Projekt stoiska targowego",
    "expo_eyebrow": "PROJEKT STOISKA TARGOWEGO",
    "expo_h1": "Projekt stoiska targowego, <em>w którym widać koszty.</em>",
    "expo_lead": "Przygotowuję koncepcję i układ stoiska, model 3D oraz zestawienie kosztów każdego elementu. "
                 "Porównujesz warianty, zanim zamówisz produkcję.",
    "expo_points": ["Koncepcja i układ funkcjonalny", "Wizualizacja i model 3D",
                    "Zakup / wynajem / usługa przy każdym elemencie", "Warianty Economy / Smart / Premium"],
    "expo_cta": "Omówmy Twoje targi",
    "expo_cta2": "Zobacz przykład",
    "expo_get_h2": "Co obejmuje projekt stoiska",
    "expo_get": [
        ("Koncepcja", "Cel stoiska, przekaz i to, co odwiedzający ma zapamiętać."),
        ("Układ funkcjonalny", "Strefy pokazu, rozmów i zaplecza, ruch odwiedzających, ekspozycja produktu."),
        ("Model i wizualizacja 3D", "Widoki z różnych stron i ujęcia do prezentacji w firmie."),
        ("Zestawienie kosztów", "Każdy element opisany jako zakup, wynajem lub usługa."),
        ("Warianty", "Economy / Smart / Premium — z informacją, co zmienia się w każdym z nich."),
        ("Materiały dla wykonawców", "Pakiet do zapytań ofertowych: rzuty, widoki, lista elementów."),
    ],

    # ---------- landing: prezentacje 3D ----------
    "p3d_slug": "prezentacje-produktow-3d",
    "p3d_title": "Prezentacje produktów 3D i multimedia na targi | Scenovis",
    "p3d_desc": "Modele 3D, animacje, widoki rozłożone i przekroje oraz interaktywne prezentacje na ekrany "
                "dotykowe i kioski. Na targi, do showroomu i do sprzedaży.",
    "p3d_crumb": "Prezentacje produktów 3D",
    "p3d_eyebrow": "PREZENTACJE PRODUKTÓW 3D",
    "p3d_h1": "Pokaż, jak działa <em>Twój produkt.</em>",
    "p3d_lead": "Modele 3D, animacje, przekroje i interaktywne prezentacje na ekran dotykowy lub kiosk. "
                "Pomagają wyjaśnić produkt na targach — i później w sprzedaży.",
    "p3d_points": ["Modele i animacje produktu", "Widoki rozłożone i przekroje",
                   "Interaktywna prezentacja na kiosk", "Treści na ekrany targowe"],
    "p3d_cta": "Opowiedz o swoim produkcie",
    "p3d_cta2": "Zobacz przykład",
    "p3d_get_h2": "Co mogę przygotować",
    "p3d_get": [
        ("Model produktu", "Wierny model 3D na podstawie CAD, rysunków lub zdjęć i wymiarów."),
        ("Animacja działania", "Krótki film pokazujący, jak produkt pracuje."),
        ("Widok rozłożony", "Podzespoły rozsunięte w przestrzeni — widać budowę urządzenia."),
        ("Przekrój", "To, czego nie widać z zewnątrz: wnętrze, przepływy, mechanizmy."),
        ("Interaktywna prezentacja", "Odwiedzający sam wybiera element i ogląda go z bliska."),
        ("Ekran dotykowy i kiosk", "Treści przygotowane pod konkretny ekran na stoisku."),
    ],
    "p3d_after_h2": "Targi się kończą. Prezentacja zostaje.",
    "p3d_after": "Model i materiały przygotowane na targi mogą później pracować dla zespołu sprzedaży, "
                 "w showroomie i na stronie internetowej.",
    "p3d_after_tags": ["Targi", "Sprzedaż", "Showroom", "Strona WWW"],

    # ---------- polityka prywatności ----------
    "privacy_slug": "polityka-prywatnosci",
    "privacy_title": "Polityka prywatności | Scenovis",
    "privacy_desc": "Informacja o przetwarzaniu danych osobowych na stronie Scenovis.",
    "privacy_h1": "Polityka prywatności",
    "privacy_draft": "Wersja robocza — dane administratora i dostawców wymagają uzupełnienia przed publikacją.",

    # ---------- 404 ----------
    "nf_title": "Nie znaleziono strony | Scenovis",
    "nf_h1": "Nie ma tu takiej strony.",
    "nf_text": "Adres mógł się zmienić. Przejdź na stronę główną albo napisz do mnie.",
    "nf_home": "Strona główna",
}

EN = {
    "lang_name": "English",
    "skip": "Skip to content",
    "nav_label": "Main navigation",
    "menu_open": "Open menu",
    "menu_close": "Close menu",
    "nav": [("#services", "Services"), ("#example", "Example"), ("#costs", "Costs"),
            ("#about", "About"), ("#faq", "FAQ")],
    "nav_cta": "Contact",
    "lang_switch_label": "Language",
    "home_label": "Scenovis — home",
    "concept_caption": "AI-assisted concept illustration — not a client project.",
    "concept_badge": "Concept (AI)",
    "footer_tagline": "Exhibition stand design, 3D product presentations and multimedia.",
    "footer_privacy": "Privacy policy",
    "footer_location": "Gdańsk, Poland",
    "footer_lang": "Polish and English",
    "breadcrumb_home": "Home",

    "home_title": "Scenovis — exhibition stand design, 3D and cost breakdown",
    "home_desc": "Exhibition stand concept and 3D visualisation with a clear cost breakdown: buy, rent, service. "
                 "3D product presentations and multimedia for trade fairs.",

    "hero_eyebrow": "EXPO • 3D • MULTIMEDIA • COSTS",
    "hero_h1": "Show the product.<br>Understand the stand.<br><em>Control the budget.</em>",
    "hero_lead": "I help you plan your exhibition stand: the layout, a 3D model and a cost breakdown that shows "
                 "what you buy, what you rent and what is a service. For production, multimedia and installation "
                 "I bring in contractors that fit the project.",
    "hero_cta_primary": "See how it works",
    "hero_cta_secondary": "Let’s talk about your trade fair",
    "hero_note": "Based in Gdańsk, Poland {todo:confirm service area} · Polish or English",
    "hero_tags": [
        ("led", "LED wall", "rent"),
        ("light", "Lighting", "rent"),
        ("kiosk", "Touch kiosk", "buy"),
        ("build", "Build & dismantle", "service"),
    ],
    "hero_variant_label": "Option",
    "hero_figure_label": "Example: stand elements labelled by cost type",

    "tldr_title": "Scenovis at a glance",
    "tldr_for": "<strong>Who it’s for:</strong> companies exhibiting at trade fairs — especially with a technical "
                "product that needs explaining.",
    "tldr": [
        ("Concept and layout", "Zones, visitor flow, space for meetings and product demos."),
        ("3D model and visuals", "See the stand from every side before it is built."),
        ("Costs without guesswork", "Every element marked as buy, rent or service. Options to compare."),
        ("Delivery with contractors", "Stand build, AV and installation matched to scope and budget."),
    ],

    "case_label": "Example",
    "case_tag": "Demo project / Scenovis Concept",
    "case_h2": "From stand concept to budget decision",
    "case_lead": "See how a client can explore the stand, check the cost of every element and compare options "
                 "before production.",
    "case_intro": "In the film I operate an interactive presentation built in Blender myself. "
                  "It is a recording of a working tool, not an animation.",
    "video_placeholder_title": "Video coming soon",
    "video_placeholder_text": "A recording of the stand presentation will appear here.",
    "video_todo": "{todo:EXPO VIDEO — MP4 + poster + PL/EN captions, see TODO.md}",
    "video_play": "Play video",
    "video_duration": "Duration",
    "video_captions_note": "Captions are available in Polish and English. Sound plays only after you press play.",
    "case_benefits": [
        ("The whole layout, not just a render", "Switch cameras and look at every zone of the stand."),
        ("A cost on every element", "Structure, lighting, multimedia — split into buy, rent and service."),
        ("Options before production", "Compare Economy, Smart and Premium and see where you can save."),
    ],
    "case_chapters_title": "What the film shows",
    "case_chapters": [
        "Overall stand view", "Camera change", "Selecting an element", "Orbit around an object",
        "Element cost", "Buy, rent or service", "Economy / Smart / Premium options",
        "Lighting cost", "Touch kiosk", "Microscope presentation", "Back to the stand",
        "Potential savings",
    ],
    "case_transcript": "Video transcript",
    "case_transcript_body": "<p>{todo:TRANSCRIPT — paste the narration / step list after recording}</p>",
    "case_cta_q": "Want to see your own stand like this?",
    "case_cta": "Let’s talk about your trade fair",

    "services_label": "Services",
    "services_h2": "Three areas where I can help",
    "services_lead": "Order just the design with a cost breakdown, or the full scope — delivered with contractors "
                     "selected for the project.",
    "services": [
        {
            "key": "expo", "code": "Expo design & cost", "title": "Stand design and costs",
            "desc": "Concept, layout and 3D model of the stand — together with a cost structure and options to compare.",
            "items": ["Concept and functional layout", "3D visualisation and model",
                      "Economy / Smart / Premium options", "Buy vs rent comparison",
                      "Budget optimisation", "Briefing pack for contractors"],
            "who": "I prepare this myself", "who_type": "own",
            "more": ("More about stand design", "expo"), "ask": "Ask about stand design",
        },
        {
            "key": "3d", "code": "Product 3D & multimedia", "title": "3D product presentations and multimedia",
            "desc": "Show how your product works — including what you can’t see from the outside.",
            "items": ["Product models and animations", "Exploded views and cutaways",
                      "Interactive presentations", "Content for touchscreens and kiosks",
                      "Material for showrooms and sales"],
            "who": "I prepare this myself", "who_type": "own",
            "more": ("More about 3D presentations", "3d"), "ask": "Ask about a 3D presentation",
        },
        {
            "key": "delivery", "code": "Delivery & on-site", "title": "Delivery and on-site support",
            "desc": "When the project moves to production, I select contractors for the scope. You know who is responsible for what.",
            "items": ["Stand build and print", "Multimedia, screens, lighting", "Transport, build-up, dismantling",
                      "Stand staff — optional", "On-site coordination — optional"],
            "who": "With contractors selected for the project", "who_type": "partners",
            "more": None, "ask": "Ask about delivery",
        },
    ],
    "services_note": "Not every element is needed in every project — we agree the scope together.",

    "costs_label": "Costs",
    "costs_h2": "Not just a render.<br><em>You know what you pay for.</em>",
    "costs_lead": "Every element of the stand has its own cost and type. We talk about specifics, "
                  "not a single lump sum.",
    "costs_sheet_title": "Stand elements breakdown",
    "costs_sheet_note": "Illustrative example. Elements and amounts are set for each project, based on contractor quotes.",
    "costs_variant_label": "Compare options",
    "costs_cols": ("Element", "Cost type", "What it includes"),
    "cost_types": {"buy": "Buy", "rent": "Rent", "service": "Service", "buyrent": "Buy or rent"},
    "costs_rows": [
        ("K-01", "Structure", "buyrent", ["Hired modular system", "Modular system + own reusable parts", "Custom-built stand"]),
        ("G-02", "Graphics", "buy", ["Prints on system frames", "Replaceable fabric graphics", "Fabric graphics, backlighting, 3D elements"]),
        ("O-03", "Lighting", "rent", ["Standard lighting + a few spotlights", "Track spotlights, product accent", "Stage-style lighting design"]),
        ("M-04", "Multimedia", "rent", ["One screen with a video loop", "Screen + touch kiosk with 3D presentation", "LED wall + interactive stations"]),
        ("F-05", "Furniture", "rent", ["Counter and two stools", "Meeting area + counter with storage", "Custom furniture and back room"]),
        ("L-06", "Logistics", "service", ["Transport from the hire company", "Transport + storage of elements", "Transport, storage and insurance"]),
        ("S-07", "Installation", "service", ["System build-up and dismantling", "Build-up, dismantling and AV service", "Build crew + on-site technician"]),
    ],
    "costs_legend": [
        ("buy", "Buy", "you keep it and can reuse it"),
        ("rent", "Rent", "you pay for the time of the fair"),
        ("service", "Service", "people’s work: transport, installation, staffing"),
    ],
    "costs_get_title": "What you get",
    "costs_get": ["3D model split into elements", "Breakdown: buy / rent / service",
                  "Option comparison", "Where you can save"],

    "about_label": "About",
    "about_h2": "Hi, I’m Aleks.",
    "about_body": [
        "My day-to-day work involves 3D models and technical documentation — I have a background in BIM. "
        "At Scenovis I use that experience to help companies prepare well for trade fairs.",
        "For a stand project I prepare the concept, layout, visualisation and cost breakdown. When the project "
        "moves to production, I work with contractors selected for the scope — including stand builders, "
        "multimedia, installation, logistics and staffing.",
        "You talk directly to me — the person who prepares the concept.",
    ],
    "about_photo_alt": "Aleks — Scenovis",
    "about_linkedin": "LinkedIn profile",
    "about_own_title": "What I help with directly",
    "about_own": ["Brief", "Concept", "Layout", "3D model", "Costs", "Presentation"],
    "about_partners_title": "For delivery I work with",
    "about_partners": ["Stand build", "Print", "AV and screens", "Lighting", "Logistics",
                       "Build-up and dismantling", "Staff", "On-site coordination"],
    "about_partners_note": "These are independent companies and specialists selected for each project, not Scenovis employees. "
                           "Before we start, you know who is responsible for each element.",

    "process_label": "Process",
    "process_h2": "How we work together",
    "process": [
        ("Call and brief", "Fair, dates, floor space, product and budget. One sentence is enough to start."),
        ("Concept and layout", "Zones, visitor route, space for demos and meetings."),
        ("3D model and costs", "Visualisation plus a cost breakdown with options to compare."),
        ("Presentation and decision", "We go through the project together and you choose an option — knowing what drives the price."),
        ("Delivery — optional", "I select contractors and help coordinate, or hand the materials over to your own contractor."),
    ],

    "faq_label": "FAQ",
    "faq_h2": "Frequently asked questions",
    "faq": {
        "price": ("How much does an exhibition stand design cost?",
                  "<p>It depends on the scope: floor space, the number of options and whether you need a 3D presentation "
                  "or multimedia. I quote the design after a short call, before any work starts.</p>"
                  "<p>{todo:FAQ PRICE — add your pricing model or a “from” figure if you want to show it}</p>"),
        "factors": ("What drives the cost of a stand?",
                    "<p>Usually: floor space and build type (modular or custom), materials and finish, graphics, lighting, "
                    "multimedia, furniture, transport, build-up and dismantling, plus organiser fees (e.g. utility connections). "
                    "For your project I break this down element by element.</p>"),
        "buyrent": ("What is better to rent and what to buy?",
                    "<p>Mostly it depends on how often you exhibit. Elements used repeatedly — such as a modular structure, "
                    "a kiosk or universal graphics — are often worth buying. AV equipment dates quickly, so renting it is "
                    "usually better. In the project I compare both options for your situation.</p>"),
        "reuse": ("Can the stand be reused at future fairs?",
                  "<p>Yes, if we plan for it from the start: modules, replaceable graphics, transport and storage. "
                  "I ask about it in the brief, because it affects the buy / rent decision.</p>"),
        "materials": ("What do you need from me to start?",
                      "<p>Enough to start: the fair and its dates, floor space and stand type (island, corner, inline), "
                      "what you want to show and a rough budget. Also helpful: logo or brand guide, product photos or models "
                      "(e.g. STEP) and the organiser’s technical rules.</p>"),
        "delivery": ("Can Scenovis also help with delivery?",
                     "<p>Yes. For delivery I select contractors suited to the scope — from stand build and print, through "
                     "multimedia and lighting, to transport, installation and staffing. You can also order just the design "
                     "with a cost breakdown and build it with your own contractor.</p>"),
        "area": ("Where do you work?",
                 "<p>{todo:SERVICE AREA — e.g. all of Poland / selected fairs abroad}</p>"),
        "time": ("How early should we start?",
                 "<p>{todo:LEAD TIME — how many weeks before the fair to start design and delivery}</p>"),
        "3d_data": ("What data do you need for a 3D product presentation?",
                    "<p>CAD models (e.g. STEP) or technical drawings work best. If you don’t have them, we can start from "
                    "photos, dimensions and a description of how it works — and agree the right level of detail together.</p>"),
        "3d_hw": ("What does the interactive presentation run on?",
                  "<p>{todo:HARDWARE — which device / screen the presentation runs on, whether it works offline}</p>"),
        "3d_reuse": ("Can the presentation be used after the fair?",
                     "<p>Yes. The model and materials prepared for the fair can later support sales, a showroom, "
                     "or be used as video and images on your website.</p>"),
    },

    "contact_label": "Contact",
    "contact_h2": "Tell me about your trade fair.",
    "contact_lead": "A phone number or email is enough. I’ll get back to you to discuss the details.",
    "contact_direct": "Or contact me directly",
    "contact_phone_sub": "Call",
    "contact_email_sub": "Send a brief or files",
    "contact_wa": "Message on WhatsApp",
    "contact_brief": "Already have a brief? Send it to {email}.",
    "contact_lang": "I work in Polish and English.",
    "form_title": "Quick enquiry",
    "f_contact": "Phone or email",
    "f_contact_hint": "E.g. +48 500 000 000 or name@company.com",
    "f_required": "required",
    "f_optional": "optional",
    "f_name": "Name",
    "f_message": "Message",
    "f_message_ph": "E.g. which fair, when, and what you want to show",
    "f_more": "Add trade fair details",
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
    "f_disclaimer": "I use your details to respond to your enquiry and protect the form. Details: <a href=\"{privacy}\">privacy policy</a>.",
    "f_err_contact": "Enter a phone number (at least 7 digits) or a valid email address.",
    "f_success": "Thank you — your enquiry has been sent. I’ll get back to you as soon as I can.",
    "f_fail": "The form wasn’t sent. Your message is ready — send it by email or WhatsApp instead:",
    "f_fail_email": "Send by email",
    "f_fail_wa": "Send via WhatsApp",
    "f_turnstile_label": "Form security check",
    "f_turnstile_wait": "Security check is loading — please try again in a moment.",
    "f_turnstile_check": "Please complete the security check and try again.",
    "f_turnstile_unavailable": "The form’s security check is temporarily unavailable. Please email your enquiry instead:",
    "f_preview": "This is a local preview — sending works once the site is published. You can test sending by email:",
    "mail_subject": "Enquiry from the Scenovis website",
    "wa_hello": "Hello, I’m writing from the Scenovis website.",
    "topics": {"expo": "Stand design and costs", "3d": "3D presentation / multimedia",
               "delivery": "Delivery", "general": "General"},
    "field_names": {"contact": "Contact", "name": "Name", "message": "Message", "topic": "Topic",
                    "event": "Fair", "city": "City", "date": "Dates", "area": "Stand size",
                    "budget": "Budget", "reuse": "Reuse"},

    "expo_slug": "exhibition-stand-design",
    "expo_title": "Exhibition stand design in 3D with cost breakdown | Scenovis",
    "expo_desc": "Exhibition stand concept, layout and 3D visualisation. Cost breakdown by buy, rent and service, "
                 "with Economy / Smart / Premium options — before production.",
    "expo_crumb": "Exhibition stand design",
    "expo_eyebrow": "EXHIBITION STAND DESIGN",
    "expo_h1": "Exhibition stand design <em>with the costs in view.</em>",
    "expo_lead": "I prepare the stand concept and layout, a 3D model and a cost breakdown for every element. "
                 "You compare options before you order production.",
    "expo_points": ["Concept and functional layout", "3D visualisation and model",
                    "Buy / rent / service for every element", "Economy / Smart / Premium options"],
    "expo_cta": "Let’s talk about your trade fair",
    "expo_cta2": "See an example",
    "expo_get_h2": "What stand design includes",
    "expo_get": [
        ("Concept", "The purpose of the stand, the message and what visitors should remember."),
        ("Functional layout", "Demo, meeting and storage zones, visitor flow, product display."),
        ("3D model and visuals", "Views from every side and shots for internal presentations."),
        ("Cost breakdown", "Every element described as buy, rent or service."),
        ("Options", "Economy / Smart / Premium — with what changes in each."),
        ("Contractor pack", "Material for requests for quotation: plans, views, list of elements."),
    ],

    "p3d_slug": "3d-product-presentations",
    "p3d_title": "3D product presentations and trade fair multimedia | Scenovis",
    "p3d_desc": "3D models, animations, exploded views and cutaways, plus interactive presentations for touchscreens "
                "and kiosks. For trade fairs, showrooms and sales.",
    "p3d_crumb": "3D product presentations",
    "p3d_eyebrow": "3D PRODUCT PRESENTATIONS",
    "p3d_h1": "Show how <em>your product works.</em>",
    "p3d_lead": "3D models, animations, cutaways and interactive presentations for a touchscreen or kiosk. "
                "They help explain the product at the fair — and later in sales.",
    "p3d_points": ["Product models and animations", "Exploded views and cutaways",
                   "Interactive kiosk presentation", "Content for trade fair screens"],
    "p3d_cta": "Tell me about your product",
    "p3d_cta2": "See an example",
    "p3d_get_h2": "What I can prepare",
    "p3d_get": [
        ("Product model", "An accurate 3D model based on CAD, drawings, or photos and dimensions."),
        ("Working animation", "A short film showing how the product operates."),
        ("Exploded view", "Components spread out in space — the build of the device becomes clear."),
        ("Cutaway", "What you can’t see from outside: internals, flows, mechanisms."),
        ("Interactive presentation", "Visitors pick an element and look at it up close."),
        ("Touchscreen and kiosk", "Content prepared for the specific screen on your stand."),
    ],
    "p3d_after_h2": "The fair ends. The presentation stays.",
    "p3d_after": "A model and materials prepared for the fair can later work for your sales team, "
                 "in your showroom and on your website.",
    "p3d_after_tags": ["Trade fairs", "Sales", "Showroom", "Website"],

    "privacy_slug": "privacy-policy",
    "privacy_title": "Privacy policy | Scenovis",
    "privacy_desc": "How personal data is processed on the Scenovis website.",
    "privacy_h1": "Privacy policy",
    "privacy_draft": "Draft — controller and provider details must be completed before publication.",

    "nf_title": "Page not found | Scenovis",
    "nf_h1": "This page doesn’t exist.",
    "nf_text": "The address may have changed. Go to the home page or contact me.",
    "nf_home": "Home page",
}

CONTENT = {"pl": PL, "en": EN}
