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
    "nav": [("@expo", "Stoiska EXPO"), ("@3d", "Prezentacje 3D"), ("#koszty", "Koszty"),
            ("#o-mnie", "O mnie"), ("#faq", "FAQ")],
    "nav_cta": "Kontakt",
    "lang_switch_label": "Wersja językowa",
    "home_label": "Scenovis — strona główna",
    "concept_caption": "Ilustracja koncepcyjna wygenerowana z pomocą AI — nie jest realizacją dla klienta.",
    "concept_badge": "Koncepcja (AI)",
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
    "hero_lead": "Projektuję stoiska targowe z modelem 3D i zestawieniem kosztów oraz interaktywne "
                 "prezentacje 3D produktów technicznych. Każdą usługę możesz zamówić osobno lub razem.",
    "hero_cta_primary": "Opowiedz o swoim projekcie",
    "hero_paths_label": "Usługi",
    "hero_paths": [("expo", "Projekt stoiska targowego"), ("3d", "Prezentacje produktów 3D")],
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
    "tldr_for": "<strong>Dla kogo:</strong> dla firm z produktem technicznym — przygotowujących stoisko na targi "
                "albo szukających czytelnego sposobu, by pokazać, jak działa ich produkt.",
    "tldr": [
        ("Projekt stoiska", "Koncepcja, układ i model 3D — oglądasz stoisko, zanim powstanie."),
        ("Koszty pod kontrolą", "Każdy element jako zakup, wynajem lub usługa. Warianty do porównania."),
        ("Prezentacje produktów 3D", "Budowa, mechanizmy i działanie urządzenia — interaktywnie lub jako animacja."),
        ("Wykonawcy dobrani do zakresu", "Produkcję i montaż realizują współpracujące firmy. Wiesz, kto za co odpowiada."),
    ],

    # ---------- case study / film (strona główna i projekt stoiska) ----------
    "case_label": "Przykład",
    "case_tag": "Projekt demonstracyjny / Scenovis Concept",
    "case_h2": "Od koncepcji stoiska do decyzji budżetowej",
    "case_lead": "Projekt demonstracyjny: jak obejrzeć stoisko, sprawdzić koszt każdego elementu "
                 "i porównać warianty przed produkcją.",
    "case_intro": "Na filmie sam steruję interaktywną prezentacją zbudowaną w Blenderze. "
                  "To zapis działającego narzędzia, a nie animacja.",
    "case_intro_pending": "Nagranie jest w przygotowaniu. Pokaże interaktywną prezentację zbudowaną w Blenderze, "
                          "którą steruję samodzielnie — to koncepcja demonstracyjna, nie realizacja dla klienta.",
    "video_placeholder_title": "Film w przygotowaniu",
    "video_placeholder_text": "Tutaj pojawi się nagranie projektu demonstracyjnego.",
    "video_todo": "{todo:EXPO VIDEO — MP4 + poster + napisy PL/EN, zob. TODO.md}",
    "video_play": "Odtwórz film",
    "video_duration": "Czas trwania",
    "video_captions_note": "Film ma napisy po polsku i angielsku. Dźwięk włącza się dopiero po kliknięciu.",
    "case_benefits": [
        ("Cały układ, nie tylko render", "Zmieniasz kamery i oglądasz każdą strefę stoiska."),
        ("Koszt przy każdym elemencie", "Konstrukcja, oświetlenie, multimedia — z podziałem na zakup, wynajem i usługę."),
        ("Warianty przed produkcją", "Porównujesz Economy, Smart i Premium i widzisz, z czego wynikają różnice w kosztach."),
    ],
    "case_chapters_title": "Co pokaże film",
    "case_chapters": [
        "Ogólny widok stoiska", "Zmiana kamery", "Wybór elementu", "Obrót wokół obiektu",
        "Koszt elementu", "Zakup, wynajem czy usługa", "Warianty Economy / Smart / Premium",
        "Koszt oświetlenia", "Kiosk dotykowy", "Prezentacja mikroskopu", "Powrót do stoiska",
        "Porównanie kosztów wariantów",
    ],
    "case_transcript": "Transkrypcja filmu",
    "case_transcript_body": "<p>{todo:TRANSKRYPCJA — wklej tekst lektora / opis kroków po nagraniu filmu}</p>",
    "case_cta_q": "Chcesz zobaczyć w ten sposób swoje stoisko?",
    "case_cta": "Omów projekt stoiska",

    # ---------- przykład na podstronie prezentacji 3D ----------
    "case3d_tag": "Projekt demonstracyjny / Scenovis Concept",
    "case3d_h2": "Interaktywna prezentacja produktu",
    "case3d_lead": "Projekt demonstracyjny Scenovis: prezentacja urządzenia technicznego (mikroskopu) przygotowana "
                   "w Blenderze. To koncepcja, nie realizacja dla klienta.",
    "case3d_intro": "Na nagraniu sam steruję prezentacją — wybieram elementy urządzenia i pokazuję je z bliska.",
    "case3d_intro_pending": "Nagranie jest w przygotowaniu. Poniżej zakres, który może obejmować prezentacja produktu tego typu.",
    "case3d_benefits": [
        ("Budowa urządzenia", "Podzespoły i mechanizmy pokazane w przestrzeni — także te ukryte w obudowie."),
        ("Element po elemencie", "Odwiedzający lub handlowiec wybiera część i ogląda ją z każdej strony."),
        ("Działanie produktu", "Animacja pokazuje, jak pracuje mechanizm — bez demontażu i transportu urządzenia."),
    ],
    "case3d_cta_q": "Chcesz w ten sposób pokazać swój produkt?",
    "case3d_cta": "Porozmawiajmy o prezentacji produktu",

    # ---------- oferta ----------
    "services_label": "Oferta",
    "services_h2": "Dwie usługi — osobno lub razem",
    "services_lead": "Projekt stoiska i prezentację produktu 3D możesz zamówić niezależnie od siebie. "
                     "Każdy projekt wyceniam indywidualnie, według uzgodnionego zakresu.",
    "services": [
        {
            "key": "expo", "code": "Usługa · EXPO", "title": "Projekt stoiska targowego",
            "desc": "Przemyślana przestrzeń targowa i decyzje podjęte przed produkcją — na podstawie modelu 3D "
                    "i zestawienia kosztów.",
            "items": ["Koncepcja stoiska", "Układ funkcjonalny i ergonomia", "Model i wizualizacje 3D",
                      "Dobór wyposażenia i technologii", "Analiza: zakup, wynajem czy własne elementy",
                      "Zestawienie elementów i szacunek kosztów", "Wsparcie w wyborze wykonawców"],
            "who": "Przygotowuję osobiście", "who_type": "own",
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
            "who": "Przygotowuję osobiście", "who_type": "own",
            "more": ("Więcej o prezentacjach 3D", "3d"), "ask": "Porozmawiajmy o prezentacji",
        },
        {
            "key": "delivery", "code": "Opcjonalnie", "title": "Koordynacja realizacji",
            "desc": "Produkcję, montaż i obsługę wykonują współpracujące firmy. Pomagam je dobrać, a jeśli tak "
                    "ustalimy — koordynuję realizację.",
            "items": ["Zabudowa i druk", "Multimedia, ekrany, oświetlenie", "Transport, montaż, demontaż",
                      "Personel stoiska", "Koordynacja na miejscu"],
            "who": "Przez współpracujących wykonawców", "who_type": "partners",
            "more": None, "ask": "Zapytaj o realizację",
        },
    ],
    "services_note": "Zakres każdego projektu ustalamy razem — bez sztywnych pakietów.",

    # ---------- koszty ----------
    "costs_label": "Koszty stoiska",
    "costs_h2": "Nie tylko render.<br><em>Wiesz, za co płacisz.</em>",
    "costs_lead": "W projekcie stoiska każdy element ma swój koszt i typ. Rozmawiamy o konkretach, "
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
                  "Porównanie wariantów", "Miejsca, w których można ograniczyć koszty"],

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
    "about_own_title": "Co robię samodzielnie",
    "about_own": ["Brief", "Koncepcja", "Analiza funkcjonalna", "Modele 3D", "Prezentacje techniczne", "Zestawienia kosztów"],
    "about_partners_title": "Co realizują współpracujący wykonawcy",
    "about_partners": ["Zabudowa", "Druk", "AV i ekrany", "Oświetlenie", "Logistyka",
                       "Montaż i demontaż", "Personel", "Koordynacja na miejscu"],
    "about_partners_note": "To niezależne firmy i specjaliści dobierani do konkretnego projektu, a nie pracownicy Scenovis. "
                           "Przed startem wiesz, kto odpowiada za który element.",

    # ---------- proces ----------
    "process_label": "Współpraca",
    "process_h2": "Jak wygląda współpraca",
    "process": [
        ("Rozmowa i brief", "Cel, termin, zakres i budżet. Na start wystarczy jedno zdanie."),
        ("Koncepcja", "Układ stoiska albo scenariusz prezentacji produktu."),
        ("Model 3D i zestawienie", "Wizualizacje, prezentacja lub zestawienie kosztów — zależnie od usługi."),
        ("Omówienie i decyzja", "Przechodzimy przez wynik razem i ustalamy kolejne kroki."),
        ("Realizacja — opcjonalnie", "Wykonawcy dobrani do zakresu albo przekazanie materiałów Twojemu zespołowi."),
    ],

    # ---------- FAQ ----------
    "faq_label": "FAQ",
    "faq_h2": "Częste pytania",
    "faq": {
        "price": ("Jak wyceniasz projekt?",
                  "<p>Każdy projekt wyceniam indywidualnie — nie mam sztywnych pakietów. Wycena zależy od zakresu: "
                  "przy stoisku m.in. od powierzchni i liczby wariantów, przy prezentacji 3D od złożoności produktu "
                  "i formy prezentacji. Wycenę podaję po krótkiej rozmowie, przed rozpoczęciem pracy.</p>"),
        "expo_process": ("Jak wygląda projektowanie stoiska?",
                         "<p>Zaczynamy od briefu: targi, termin, powierzchnia, cel i budżet. Potem przygotowuję koncepcję "
                         "i układ funkcjonalny, model 3D oraz zestawienie elementów z typem kosztu. Omawiamy warianty "
                         "i dopiero wtedy decydujesz, co zamówić u wykonawców.</p>"),
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
        "delivery": ("Kto wykonuje i montuje stoisko?",
                     "<p>Produkcję, montaż, multimedia i logistykę realizują niezależni wykonawcy. Mogę pomóc w ich wyborze "
                     "i — jeśli tak ustalimy — w koordynacji. Możesz też zamówić sam projekt z zestawieniem kosztów "
                     "i zrealizować go z własnym wykonawcą.</p>"),
        "area": ("Gdzie działasz?",
                 "<p>{todo:OBSZAR DZIAŁANIA — np. cała Polska / wybrane targi za granicą}</p>"),
        "time": ("Ile wcześniej trzeba zacząć?",
                 "<p>Im wcześniej, tym więcej czasu na porównanie wariantów i ofert wykonawców. "
                 "Konkretny harmonogram ustalamy po briefie.</p>"
                 "<p>{todo:TERMINY — ile tygodni przed targami najlepiej zacząć projekt i realizację}</p>"),
        "3d_forms": ("W jakiej formie może powstać prezentacja 3D?",
                     "<p>Zależnie od potrzeb: jako interaktywna prezentacja, w której użytkownik sam wybiera elementy "
                     "produktu, jako animacja lub film albo jako zestaw wizualizacji i przekrojów. Formę dobieramy do "
                     "miejsca użycia — stoiska, showroomu, spotkania handlowego lub strony internetowej.</p>"),
        "3d_data": ("Jakich danych potrzebujesz do prezentacji 3D produktu?",
                    "<p>Najlepiej pracuje się na modelach CAD (np. STEP) lub rysunkach technicznych. Jeśli ich nie ma, "
                    "zaczniemy od zdjęć, wymiarów i opisu działania — ustalimy razem, jaki poziom szczegółów ma sens.</p>"),
        "3d_hw": ("Na jakich urządzeniach działa interaktywna prezentacja?",
                  "<p>Urządzenie ustalamy na początku projektu — np. ekran dotykowy, kiosk, laptop handlowca lub duży "
                  "ekran na stoisku. Wymagania techniczne sprawdzamy przed rozpoczęciem pracy.</p>"
                  "<p>{todo:SPRZĘT — na jakim sprzęcie / ekranie działa prezentacja, czy działa offline}</p>"),
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
    "f_disclaimer": "Dane wykorzystam do obsługi zapytania i zabezpieczenia formularza. Szczegóły: <a href=\"{privacy}\">polityka prywatności</a>.",
    "f_err_empty": "Podaj numer telefonu lub adres e-mail.",
    "f_err_email": "Sprawdź adres e-mail — powinien wyglądać np. tak: imie@firma.pl.",
    "f_err_contact": "Wpisz numer telefonu albo adres e-mail.",
    "f_success": "Dziękuję — zapytanie zostało wysłane. Odezwę się najszybciej, jak to możliwe.",
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
               "delivery": "Koordynacja realizacji"},
    "field_names": {"contact": "Kontakt", "name": "Imię", "message": "Wiadomość", "topic": "Temat",
                    "event": "Targi", "city": "Miasto", "date": "Termin", "area": "Powierzchnia",
                    "budget": "Budżet", "reuse": "Ponowne użycie"},

    # ---------- landing: projekt stoiska ----------
    "expo_slug": "projekt-stoiska-targowego",
    "expo_title": "Projekt stoiska targowego 3D z zestawieniem kosztów | Scenovis",
    "expo_desc": "Koncepcja, układ funkcjonalny i wizualizacja 3D stoiska targowego. Zestawienie elementów "
                 "i kosztów (zakup, wynajem, usługa) oraz porównanie wariantów przed produkcją.",
    "expo_crumb": "Projekt stoiska targowego",
    "expo_eyebrow": "PROJEKT STOISKA TARGOWEGO",
    "expo_h1": "Projekt stoiska targowego, <em>w którym widać koszty.</em>",
    "expo_lead": "Przygotowuję koncepcję i układ stoiska, model 3D oraz zestawienie elementów z kosztami. "
                 "Porównujesz rozwiązania i podejmujesz decyzje, zanim zamówisz produkcję.",
    "expo_points": ["Koncepcja i układ funkcjonalny", "Model i wizualizacje 3D",
                    "Zakup / wynajem / usługa przy każdym elemencie", "Warianty do porównania przed realizacją"],
    "expo_cta": "Omów projekt stoiska",
    "expo_cta2": "Zobacz przykład",
    "expo_get_h2": "Co obejmuje projekt stoiska",
    "expo_get": [
        ("Koncepcja", "Cel stoiska, przekaz i to, co odwiedzający ma zapamiętać."),
        ("Układ i ergonomia", "Strefy pokazu, rozmów i zaplecza, ruch odwiedzających, ekspozycja produktu."),
        ("Model i wizualizacje 3D", "Widoki z różnych stron i ujęcia do omówienia projektu w firmie."),
        ("Wyposażenie i technologia", "Dobór mebli, multimediów i oświetlenia do celu stoiska."),
        ("Zestawienie i warianty", "Elementy opisane jako zakup, wynajem lub usługa — z wariantami do porównania."),
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
    "p3d_cta2": "Zobacz przykład",
    "p3d_get_h2": "Co mogę przygotować",
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
    "nf_text": "Adres mógł się zmienić. Przejdź na stronę główną albo napisz do mnie.",
    "nf_home": "Strona główna",
}

EN = {
    "lang_name": "English",
    "skip": "Skip to content",
    "nav_label": "Main navigation",
    "menu_open": "Open menu",
    "menu_close": "Close menu",
    "nav": [("@expo", "Exhibition stands"), ("@3d", "3D presentations"), ("#costs", "Costs"),
            ("#about", "About"), ("#faq", "FAQ")],
    "nav_cta": "Contact",
    "lang_switch_label": "Language",
    "home_label": "Scenovis — home",
    "concept_caption": "AI-assisted concept illustration — not a client project.",
    "concept_badge": "Concept (AI)",
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
    "hero_lead": "I design exhibition stands with a 3D model and a cost breakdown, and build interactive 3D "
                 "presentations of technical products. Order either service on its own or both together.",
    "hero_cta_primary": "Tell me about your project",
    "hero_paths_label": "Services",
    "hero_paths": [("expo", "Exhibition stand design"), ("3d", "3D product presentations")],
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
    "tldr_for": "<strong>Who it’s for:</strong> companies with a technical product — preparing a trade fair stand "
                "or looking for a clear way to show how their product works.",
    "tldr": [
        ("Stand design", "Concept, layout and 3D model — see the stand before it is built."),
        ("Costs in view", "Every element marked as buy, rent or service. Options to compare."),
        ("3D product presentations", "The build, mechanisms and operation of a device — interactive or animated."),
        ("Contractors matched to scope", "Production and installation by partner companies. You know who does what."),
    ],

    "case_label": "Example",
    "case_tag": "Demo project / Scenovis Concept",
    "case_h2": "From stand concept to budget decision",
    "case_lead": "A demo project: how to explore the stand, check the cost of every element and compare options "
                 "before production.",
    "case_intro": "In the film I operate an interactive presentation built in Blender myself. "
                  "It is a recording of a working tool, not an animation.",
    "case_intro_pending": "The recording is in preparation. It will show an interactive presentation built in Blender, "
                          "operated by me — a demo concept, not a client project.",
    "video_placeholder_title": "Video coming soon",
    "video_placeholder_text": "A recording of the demo project will appear here.",
    "video_todo": "{todo:EXPO VIDEO — MP4 + poster + PL/EN captions, see TODO.md}",
    "video_play": "Play video",
    "video_duration": "Duration",
    "video_captions_note": "Captions are available in Polish and English. Sound plays only after you press play.",
    "case_benefits": [
        ("The whole layout, not just a render", "Switch cameras and look at every zone of the stand."),
        ("A cost on every element", "Structure, lighting, multimedia — split into buy, rent and service."),
        ("Options before production", "Compare Economy, Smart and Premium and see what drives the cost differences."),
    ],
    "case_chapters_title": "What the film will show",
    "case_chapters": [
        "Overall stand view", "Camera change", "Selecting an element", "Orbit around an object",
        "Element cost", "Buy, rent or service", "Economy / Smart / Premium options",
        "Lighting cost", "Touch kiosk", "Microscope presentation", "Back to the stand",
        "Comparing option costs",
    ],
    "case_transcript": "Video transcript",
    "case_transcript_body": "<p>{todo:TRANSCRIPT — paste the narration / step list after recording}</p>",
    "case_cta_q": "Want to see your own stand like this?",
    "case_cta": "Discuss your stand design",

    "case3d_tag": "Demo project / Scenovis Concept",
    "case3d_h2": "An interactive product presentation",
    "case3d_lead": "A Scenovis demo project: a presentation of a technical device (a microscope) built in Blender. "
                   "It is a concept, not a client project.",
    "case3d_intro": "In the recording I operate the presentation myself — selecting parts of the device and showing them up close.",
    "case3d_intro_pending": "The recording is in preparation. Below is what a product presentation of this kind can cover.",
    "case3d_benefits": [
        ("How the device is built", "Components and mechanisms shown in space — including those hidden inside the housing."),
        ("Part by part", "A visitor or sales rep picks a part and looks at it from every side."),
        ("How the product works", "An animation shows the mechanism in action — without dismantling or shipping the device."),
    ],
    "case3d_cta_q": "Want to present your product like this?",
    "case3d_cta": "Let’s talk about your product presentation",

    "services_label": "Services",
    "services_h2": "Two services — separately or together",
    "services_lead": "You can order stand design and a 3D product presentation independently of each other. "
                     "Every project is quoted individually, based on the agreed scope.",
    "services": [
        {
            "key": "expo", "code": "Service · EXPO", "title": "Exhibition stand design",
            "desc": "A well-planned stand and decisions made before production — based on a 3D model and a cost breakdown.",
            "items": ["Stand concept", "Functional layout and ergonomics", "3D model and visuals",
                      "Choice of furniture and technology", "Analysis: buy, rent or use your own elements",
                      "List of elements and cost estimate", "Help choosing contractors"],
            "who": "I prepare this myself", "who_type": "own",
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
            "who": "I prepare this myself", "who_type": "own",
            "more": ("More about 3D presentations", "3d"), "ask": "Talk about a presentation",
        },
        {
            "key": "delivery", "code": "Optional", "title": "Delivery coordination",
            "desc": "Production, installation and staffing are carried out by partner companies. I help you choose them "
                    "and, if agreed, coordinate the delivery.",
            "items": ["Stand build and print", "Multimedia, screens, lighting", "Transport, build-up, dismantling",
                      "Stand staff", "On-site coordination"],
            "who": "Through partner contractors", "who_type": "partners",
            "more": None, "ask": "Ask about delivery",
        },
    ],
    "services_note": "We agree the scope of each project together — no fixed packages.",

    "costs_label": "Stand costs",
    "costs_h2": "Not just a render.<br><em>You know what you pay for.</em>",
    "costs_lead": "In a stand design every element has its own cost and type. We talk about specifics, "
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
                  "Option comparison", "Where costs can be reduced"],

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
    "about_own_title": "What I do myself",
    "about_own": ["Brief", "Concept", "Functional analysis", "3D models", "Technical presentations", "Cost breakdowns"],
    "about_partners_title": "What partner contractors deliver",
    "about_partners": ["Stand build", "Print", "AV and screens", "Lighting", "Logistics",
                       "Build-up and dismantling", "Staff", "On-site coordination"],
    "about_partners_note": "These are independent companies and specialists selected for each project, not Scenovis employees. "
                           "Before we start, you know who is responsible for each element.",

    "process_label": "Process",
    "process_h2": "How we work together",
    "process": [
        ("Call and brief", "Goal, dates, scope and budget. One sentence is enough to start."),
        ("Concept", "A stand layout or a storyline for the product presentation."),
        ("3D model and breakdown", "Visuals, a presentation or a cost breakdown — depending on the service."),
        ("Review and decision", "We go through the result together and agree the next steps."),
        ("Delivery — optional", "Contractors matched to the scope, or a hand-over of materials to your own team."),
    ],

    "faq_label": "FAQ",
    "faq_h2": "Frequently asked questions",
    "faq": {
        "price": ("How do you price a project?",
                  "<p>Every project is quoted individually — there are no fixed packages. The quote depends on the scope: "
                  "for a stand, for example, on floor space and the number of options; for a 3D presentation, on the "
                  "complexity of the product and the format. I give you a quote after a short call, before any work starts.</p>"),
        "expo_process": ("What does the stand design process look like?",
                         "<p>We start with a brief: the fair, dates, floor space, goal and budget. I then prepare the concept "
                         "and functional layout, a 3D model and a list of elements with their cost type. We go through the "
                         "options, and only then do you decide what to order from contractors.</p>"),
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
        "delivery": ("Who builds and installs the stand?",
                     "<p>Production, installation, multimedia and logistics are delivered by independent contractors. I can help "
                     "you choose them and, if agreed, coordinate the work. You can also order just the design with a cost "
                     "breakdown and build it with your own contractor.</p>"),
        "area": ("Where do you work?",
                 "<p>{todo:SERVICE AREA — e.g. all of Poland / selected fairs abroad}</p>"),
        "time": ("How early should we start?",
                 "<p>The earlier, the more time there is to compare options and contractor quotes. "
                 "We agree a specific schedule after the brief.</p>"
                 "<p>{todo:LEAD TIME — how many weeks before the fair to start design and delivery}</p>"),
        "3d_forms": ("What form can a 3D presentation take?",
                     "<p>Depending on your needs: an interactive presentation where the user picks parts of the product, "
                     "an animation or film, or a set of visuals and cutaways. We choose the format for where it will be "
                     "used — a stand, a showroom, a sales meeting or a website.</p>"),
        "3d_data": ("What data do you need for a 3D product presentation?",
                    "<p>CAD models (e.g. STEP) or technical drawings work best. If you don’t have them, we can start from "
                    "photos, dimensions and a description of how it works — and agree the right level of detail together.</p>"),
        "3d_hw": ("Which devices does the interactive presentation run on?",
                  "<p>We agree the device at the start of the project — e.g. a touchscreen, a kiosk, a sales rep’s laptop "
                  "or a large screen on the stand. Technical requirements are checked before work begins.</p>"
                  "<p>{todo:HARDWARE — which device / screen the presentation runs on, whether it works offline}</p>"),
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
    "f_disclaimer": "I use your details to respond to your enquiry and protect the form. Details: <a href=\"{privacy}\">privacy policy</a>.",
    "f_err_empty": "Please enter a phone number or an email address.",
    "f_err_email": "Please check the email address — it should look like name@company.com.",
    "f_err_contact": "Enter a phone number or an email address.",
    "f_success": "Thank you — your enquiry has been sent. I’ll get back to you as soon as I can.",
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
               "delivery": "Delivery coordination"},
    "field_names": {"contact": "Contact", "name": "Name", "message": "Message", "topic": "Topic",
                    "event": "Fair", "city": "City", "date": "Dates", "area": "Stand size",
                    "budget": "Budget", "reuse": "Reuse"},

    "expo_slug": "exhibition-stand-design",
    "expo_title": "Exhibition stand design in 3D with cost breakdown | Scenovis",
    "expo_desc": "Exhibition stand concept, functional layout and 3D visualisation. A list of elements and costs "
                 "(buy, rent, service) and an option comparison before production.",
    "expo_crumb": "Exhibition stand design",
    "expo_eyebrow": "EXHIBITION STAND DESIGN",
    "expo_h1": "Exhibition stand design <em>with the costs in view.</em>",
    "expo_lead": "I prepare the stand concept and layout, a 3D model and a list of elements with their costs. "
                 "You compare solutions and make decisions before you order production.",
    "expo_points": ["Concept and functional layout", "3D model and visuals",
                    "Buy / rent / service for every element", "Options to compare before delivery"],
    "expo_cta": "Discuss your stand design",
    "expo_cta2": "See an example",
    "expo_get_h2": "What stand design includes",
    "expo_get": [
        ("Concept", "The purpose of the stand, the message and what visitors should remember."),
        ("Layout and ergonomics", "Demo, meeting and storage zones, visitor flow, product display."),
        ("3D model and visuals", "Views from every side and shots for discussing the project internally."),
        ("Furniture and technology", "Choosing furniture, multimedia and lighting to fit the stand’s purpose."),
        ("Breakdown and options", "Elements described as buy, rent or service — with options to compare."),
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
    "p3d_cta2": "See an example",
    "p3d_get_h2": "What I can prepare",
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
    "nf_text": "The address may have changed. Go to the home page or contact me.",
    "nf_home": "Home page",
}

CONTENT = {"pl": PL, "en": EN}
