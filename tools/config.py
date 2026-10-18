# -*- coding: utf-8 -*-
"""
SCENOVIS — ustawienia strony. Po zmianie uruchom:  python3 tools/build.py
"""

# Docelowy adres strony, bez ukośnika na końcu (domena podłączona 17.10.2026).
# Używany w canonical, hreflang, sitemap, OpenGraph i danych strukturalnych.
# www.scenovis.com przekierowuje na ten adres (worker/index.js).
SITE_URL = "https://scenovis.com"

# True = tryb roboczy: na stronie widać pomarańczowe znaczniki TODO.
# Produkcja od 17.10.2026. Znaczniki {todo:...} (np. film) są wtedy ukryte.
DRAFT = False

# Telefon / WhatsApp (zaktualizowane 17.10.2026). E-mail jest firmowy.
PHONE_DISPLAY = "+48 734 215 791"
PHONE_TEL = "+48734215791"        # link tel:
WHATSAPP = "48734215791"          # numer w formacie międzynarodowym, bez +
EMAIL = "contact@scenovis.com"

LINKEDIN_ALEKS = "https://www.linkedin.com/in/aleks-malyshka/"

# [TODO: ADRES] Jeżeli podasz adres działalności, dane strukturalne zmienią się
# z Organization na ProfessionalService (LocalBusiness wymaga adresu).
ADDRESS = None
# Przykład:
# ADDRESS = {"streetAddress": "ul. ...", "postalCode": "80-000", "addressLocality": "Gdańsk", "addressCountry": "PL"}

# WARIANTY STOISKA w hero (Economy / Smart / Premium).
# False — dopóki nie ma trzech renderów: hero pokazuje obecny render stoiska, a przełącznik zmienia
#         opis zakresu i zestawienie kosztów (bez punktów, żeby nie opisywać elementów, których nie widać).
# True  — po wgraniu obrazów (python tools/warianty.py FOLDER_Z_PNG): przełącznik zmienia też obraz i punkty.
VARIANT_RENDERS = False

# FILM na podstronie „Prezentacje produktów 3D” (sekcja „Interaktywna prezentacja produktu”).
# Okładka przed odtworzeniem: assets/img/scenovis-obiektywy-okladka-*.webp/.avif (klucz "cover3d" w build.py).
VIDEO_3D = {
    "src": "/assets/video/scenovis-mikroskop-prezentacja.mp4",   # 1920×1080, H.264, bez dźwięku, 18,5 s
    "poster": "/assets/video/scenovis-mikroskop-okladka.jpg",
    "width": 1920, "height": 1080,
    "duration_iso": "PT19S",
    "duration_label": {"pl": "0:19", "en": "0:19"},
    "upload_date": "2026-10-18T13:00:00+02:00",
    "name": {"pl": "Interaktywna prezentacja mikroskopu — Scenovis",
             "en": "Interactive microscope presentation — Scenovis"},
    "captions": {"pl": "/assets/video/scenovis-mikroskop-prezentacja.pl.vtt",
                 "en": "/assets/video/scenovis-mikroskop-prezentacja.en.vtt"},
    "cover": "cover3d",
    "muted": True,
}

# WIDEO w oknie hero na podstronie „Projekt stoiska targowego” (zamiast renderu).
# Krótka pętla bez dźwięku, odtwarzana automatycznie. Przykład:
# EXPO_HERO_VIDEO = {"src": "/assets/video/stoisko-hero.mp4", "poster": "/assets/video/stoisko-hero.jpg",
#                    "width": 1920, "height": 1080}
EXPO_HERO_VIDEO = None

# FILM w sekcji „Zobacz stoisko. Porównaj możliwości.”
# Dopóki VIDEO = None, okno filmu pokazuje okładkę (kadr z kiosku) bez przycisku odtwarzania
# i strona NIE generuje VideoObject JSON-LD. Po nagraniu: wgraj pliki do assets/video/,
# odkomentuj poniższy słownik, popraw nazwy/czas i uruchom: python tools/build.py
# Okno filmu zachowuje ten sam rozmiar co okładka.
VIDEO = None
# Przykład:
# VIDEO = {
#     "src": "/assets/video/scenovis-expo-demo.mp4",      # H.264 (AAC), 1920x1080 — wymagany
#     "src_webm": "/assets/video/scenovis-expo-demo.webm", # VP9/AV1 — opcjonalnie, lżejszy
#     "poster": "/assets/video/scenovis-expo-poster.jpg",  # 1920x1080 JPG/WebP
#     "width": 1920, "height": 1080,
#     "duration_iso": "PT3M20S",                           # ISO 8601
#     "duration_label": {"pl": "3:20", "en": "3:20"},
#     "upload_date": "2026-11-05T12:00:00+01:00",          # data publikacji
#     "captions": {"pl": "/assets/video/scenovis-expo-demo.pl.vtt",
#                  "en": "/assets/video/scenovis-expo-demo.en.vtt"},
#     "name": {"pl": "Zobacz stoisko. Porównaj możliwości. — Scenovis",
#              "en": "See the stand. Compare the options. — Scenovis"},
# }
