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

# [TODO: EXPO VIDEO] Uzupełnij po nagraniu filmu. Dopóki VIDEO = None,
# strona pokazuje estetyczny placeholder i NIE generuje VideoObject JSON-LD.
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
#     "name": {"pl": "Od koncepcji stoiska do decyzji budżetowej — Scenovis",
#              "en": "From stand concept to budget decision — Scenovis"},
# }
