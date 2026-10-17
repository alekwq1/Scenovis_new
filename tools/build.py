# -*- coding: utf-8 -*-
"""
SCENOVIS — generator statycznych stron (bez zależności, czysty Python 3.9+).

    python3 tools/build.py

Tworzy: /pl/..., /en/..., /index.html, /404.html, /sitemap.xml, /robots.txt
Treści: tools/content.py   Ustawienia: tools/config.py
Wynik jest zwykłym HTML — hosting nie potrzebuje żadnego procesu budowania.
"""
import hashlib
import html
import json
import os
import re
import sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import config as C  # noqa: E402
from content import CONTENT  # noqa: E402

# Polska typografia: pojedyncze litery (w, z, i, o, a, u) nie zostają na końcu wiersza.
_ORPHAN = re.compile(r"(?<![\w</-])([aiouwzAIOUWZ]) ")


def _nbsp(v):
    if isinstance(v, str):
        return v if v.startswith(("/", "http", "#")) else _ORPHAN.sub("\\1\u00a0", v)
    if isinstance(v, list):
        return [_nbsp(x) for x in v]
    if isinstance(v, tuple):
        return tuple(_nbsp(x) for x in v)
    if isinstance(v, dict):
        return {k: (x if k.endswith("_slug") else _nbsp(x)) for k, x in v.items()}
    return v


CONTENT["pl"] = _nbsp(CONTENT["pl"])

LANGS = ["pl", "en"]
OG_LOCALE = {"pl": "pl_PL", "en": "en_GB"}

# Identyfikatory sekcji (kotwice) w każdym języku
IDS = {
    "pl": {"services": "oferta", "case": "przyklad", "costs": "koszty", "about": "o-mnie",
           "process": "wspolpraca", "faq": "faq", "contact": "kontakt", "get": "zakres"},
    "en": {"services": "services", "case": "example", "costs": "costs", "about": "about",
           "process": "process", "faq": "faq", "contact": "contact", "get": "scope"},
}

TODO_RE = re.compile(r"\{todo:([^}]*)\}")


def esc(s):
    return html.escape(s, quote=True)


def todo(text):
    """Zamienia {todo:...} na znacznik widoczny tylko w trybie roboczym."""
    # W produkcji (DRAFT=False) znacznik w ogóle nie trafia do HTML — Google nie zobaczy go w kodzie strony.
    if not C.DRAFT:
        return TODO_RE.sub("", text)
    return TODO_RE.sub(lambda m: f'<span class="todo">[TODO: {esc(m.group(1))}]</span>', text)


def version():
    h = hashlib.sha1()
    for p in ("assets/css/site.css", "assets/js/site.js"):
        with open(os.path.join(ROOT, p), "rb") as f:
            h.update(f.read())
    return h.hexdigest()[:8]


VER = version()


# ---------------------------------------------------------------- URL-e stron
def page_path(lang, page):
    t = CONTENT[lang]
    return {
        "home": f"/{lang}/",
        "expo": f"/{lang}/{t['expo_slug']}/",
        "3d": f"/{lang}/{t['p3d_slug']}/",
        "privacy": f"/{lang}/{t['privacy_slug']}/",
    }[page]


def abs_url(path):
    return C.SITE_URL + path


# ---------------------------------------------------------------- elementy wspólne
def picture(name, widths, w, h, alt, sizes, eager=False, cls=""):
    avif = ", ".join(f"/assets/img/{name}-{x}.avif {x}w" for x in widths)
    webp = ", ".join(f"/assets/img/{name}-{x}.webp {x}w" for x in widths)
    mid = widths[len(widths) // 2]
    load = 'fetchpriority="high" decoding="async"' if eager else 'loading="lazy" decoding="async"'
    return (f'<picture><source type="image/avif" srcset="{avif}" sizes="{sizes}">'
            f'<source type="image/webp" srcset="{webp}" sizes="{sizes}">'
            f'<img class="{cls}" src="/assets/img/{name}-{mid}.webp" width="{w}" height="{h}" alt="{esc(alt)}" {load}>'
            f'</picture>')


def icon(name):
    paths = {
        "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
        "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
        "wa": '<path d="M3.5 20.5 5 16a8.5 8.5 0 1 1 3 3z"/><path d="M9 9.5c.3 2 2.3 4.2 4.5 5l1.3-1.3 2 1-.3 1.3c-3.3.6-7.6-3.4-7.8-7.2l1.3-.6 1 2z"/>',
        "check": '<path d="m5 12.5 4.5 4.5L19 7.5"/>',
        "play": '<path d="M8 5.5v13l11-6.5z"/>',
        "arrow": '<path d="M5 12h14m-5-5 5 5-5 5"/>',
        "linkedin": '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 10.5V16m0-8v.01M12 16v-5.5m0 2.5c0-1.5 1-2.5 2.3-2.5S16 11.5 16 13v3"/>',
    }
    return (f'<svg class="icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
            f'{paths[name]}</svg>')


def head(lang, page, title, desc, alternates, robots="index,follow", jsonld=None):
    t = CONTENT[lang]
    canonical = abs_url(page_path(lang, page)) if page else None
    links = []
    if canonical:
        links.append(f'<link rel="canonical" href="{canonical}">')
    if alternates:
        for l in LANGS:
            links.append(f'<link rel="alternate" hreflang="{l}" href="{abs_url(alternates[l])}">')
        links.append(f'<link rel="alternate" hreflang="x-default" href="{abs_url(alternates["en"])}">')
    og_img = abs_url(f"/assets/og/og-{lang}.jpg")
    og = [
        '<meta property="og:type" content="website">',
        '<meta property="og:site_name" content="Scenovis">',
        f'<meta property="og:locale" content="{OG_LOCALE[lang]}">',
        f'<meta property="og:locale:alternate" content="{OG_LOCALE["en" if lang == "pl" else "pl"]}">',
        f'<meta property="og:title" content="{esc(title)}">',
        f'<meta property="og:description" content="{esc(desc)}">',
        f'<meta property="og:image" content="{og_img}">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        f'<meta property="og:image:alt" content="{esc(t["home_title"])}">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{esc(title)}">',
        f'<meta name="twitter:description" content="{esc(desc)}">',
        f'<meta name="twitter:image" content="{og_img}">',
    ]
    if canonical:
        og.append(f'<meta property="og:url" content="{canonical}">')
    ld = ""
    if jsonld:
        ld = ('<script type="application/ld+json">'
              + json.dumps(jsonld, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
              + "</script>")
    return f"""<!doctype html>
<html lang="{lang}" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="{robots}">
{chr(10).join(links)}
<meta name="theme-color" content="#121617">
<meta name="color-scheme" content="dark">
<link rel="preload" href="/assets/fonts/inter-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/site.css?v={VER}">
<script src="/assets/js/site.js?v={VER}" defer></script>
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/assets/icons/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/icons/apple-touch-icon.png">
{chr(10).join(og)}
{ld}
</head>"""


def header(lang, page, alternates, nav=True):
    t = CONTENT[lang]
    ids = IDS[lang]
    home = page_path(lang, "home")
    prefix = "" if page == "home" else home
    nav_html = ""
    if nav:
        def nav_href(href):
            # "@expo" / "@3d" = podstrona usługi, "#..." = sekcja strony głównej
            return page_path(lang, href[1:]) if href.startswith("@") else prefix + href
        items = "".join(f'<li><a href="{nav_href(href)}">{esc(label)}</a></li>' for href, label in t["nav"])
        nav_html = (f'<nav class="nav" id="site-nav" aria-label="{esc(t["nav_label"])}">'
                    f'<ul>{items}</ul></nav>')
    contact_href = f"#{ids['contact']}" if page != "privacy" else f"{home}#{ids['contact']}"
    lang_links = []
    for l in LANGS:
        cur = ' aria-current="true"' if l == lang else ""
        lang_links.append(f'<a href="{alternates[l]}" hreflang="{l}" lang="{l}"{cur} '
                          f'title="{esc(CONTENT[l]["lang_name"])}">{l.upper()}</a>')
    toggle = ""
    if nav:
        toggle = (f'<button class="menu-toggle" type="button" aria-controls="site-nav" aria-expanded="false" '
                  f'aria-label="{esc(t["menu_open"])}" data-label-open="{esc(t["menu_open"])}" '
                  f'data-label-close="{esc(t["menu_close"])}"><span></span><span></span></button>')
    return f"""<body class="{'is-draft' if C.DRAFT else ''}" data-page="{page}" data-lang="{lang}">
<a class="skip-link" href="#main">{esc(t['skip'])}</a>
<header class="site-header">
<div class="wrap header-inner">
<a class="brand" href="{home}" aria-label="{esc(t['home_label'])}"><img src="/assets/icons/logo.svg" width="172" height="50" alt="Scenovis"></a>
{nav_html}
<div class="header-actions">
<div class="lang-switch" role="group" aria-label="{esc(t['lang_switch_label'])}">{''.join(lang_links)}</div>
<a class="button button-primary button-small header-cta" href="{contact_href}">{esc(t['nav_cta'])}</a>
{toggle}
</div>
</div>
<div class="scroll-progress" aria-hidden="true"><span></span></div>
</header>
<main id="main" tabindex="-1">"""


def footer(lang):
    t = CONTENT[lang]
    year = date.today().year
    return f"""</main>
<footer class="site-footer">
<div class="wrap footer-inner">
<div class="footer-brand">
<img src="/assets/icons/logo.svg" width="138" height="40" alt="Scenovis" loading="lazy">
<p>{esc(t['footer_tagline'])}</p>
</div>
<ul class="footer-links">
<li><a href="{page_path(lang, 'expo')}">{esc(t['expo_crumb'])}</a></li>
<li><a href="{page_path(lang, '3d')}">{esc(t['p3d_crumb'])}</a></li>
<li><a href="tel:{C.PHONE_TEL}" data-track="phone_click">{esc(C.PHONE_DISPLAY)}</a></li>
<li><a href="mailto:{C.EMAIL}" data-track="email_click">{esc(C.EMAIL)}</a></li>
<li><a href="{page_path(lang, 'privacy')}">{esc(t['footer_privacy'])}</a></li>
</ul>
<p class="footer-meta">{esc(t['footer_location'])} · {esc(t['footer_lang'])} · © {year} Scenovis</p>
</div>
</footer>
</body>
</html>
"""


def section_head(label, h2, lead=None, h2_id=None, extra=""):
    lead_html = f'<p class="section-lead">{todo(lead)}</p>' if lead else ""
    hid = f' id="{h2_id}"' if h2_id else ""
    return (f'<div class="section-head"><p class="section-label">{esc(label)}</p>{extra}'
            f'<h2{hid}>{h2}</h2>{lead_html}</div>')


# ---------------------------------------------------------------- sekcje
def hero_home(lang):
    t = CONTENT[lang]
    ids = IDS[lang]
    tags = []
    for key, name, typ in t["hero_tags"]:
        tkey = {"wynajem": "rent", "rent": "rent", "zakup": "buy", "buy": "buy",
                "usługa": "service", "service": "service"}[typ]
        tags.append(f'<li class="tag tag--{key}"><span class="tag-label"><span class="tag-name">{esc(name)}</span>'
                    f'<span class="chip chip--{tkey}">{esc(typ)}</span></span></li>')
    paths = "".join(f'<li><a class="hero-path" href="{page_path(lang, key)}" data-track="hero_service_{key}">'
                    f'<span>{esc(label)}</span>{icon("arrow")}</a></li>' for key, label in t["hero_paths"])
    return f"""<section class="hero" aria-labelledby="hero-title">
<div class="wrap hero-grid">
<div class="hero-copy">
<p class="eyebrow">{esc(t['hero_eyebrow'])}</p>
<h1 id="hero-title">{t['hero_h1']}</h1>
<p class="lead">{esc(t['hero_lead'])}</p>
<div class="cta-row">
<a class="button button-primary" href="#{ids['contact']}" data-topic="general" data-track="hero_cta_contact">{esc(t['hero_cta_primary'])}</a>
</div>
<nav class="hero-paths" aria-label="{esc(t['hero_paths_label'])}"><ul>{paths}</ul></nav>
<p class="hero-note">{todo(esc(t['hero_note']).replace('{todo:', '{todo:'))}</p>
</div>
<figure class="hero-figure">
<div class="annotated">
{picture('stoisko-koncepcja', [640, 960, 1280, 1660], 1660, 934, t['concept_caption'],
         '(min-width: 1000px) 58vw, 100vw', eager=True, cls='annotated-img')}
<ul class="tags" aria-label="{esc(t['hero_figure_label'])}">{''.join(tags)}</ul>
<div class="variant-pill" aria-hidden="true"><span>{esc(t['hero_variant_label'])}</span><b>Economy</b><b class="is-on">Smart</b><b>Premium</b></div>
<span class="concept-badge">{esc(t['concept_badge'])}</span>
</div>
<figcaption>{esc(t['concept_caption'])}</figcaption>
</figure>
</div>
</section>"""


def hero_landing(lang, kind):
    t = CONTENT[lang]
    ids = IDS[lang]
    p = "expo" if kind == "expo" else "p3d"
    points = "".join(f'<li>{icon("check")}{esc(x)}</li>' for x in t[f"{p}_points"])
    if kind == "expo":
        pic = picture('stoisko-koncepcja', [640, 960, 1280, 1660], 1660, 934, t['concept_caption'],
                      '(min-width: 1000px) 55vw, 100vw', eager=True)
    else:
        pic = picture('produkt-3d-koncepcja', [640, 960, 1280, 1536], 1536, 1024, t['concept_caption'],
                      '(min-width: 1000px) 55vw, 100vw', eager=True)
    crumbs = (f'<nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="{page_path(lang, "home")}">'
              f'{esc(t["breadcrumb_home"])}</a></li><li aria-current="page">{esc(t[p + "_crumb"])}</li></ol></nav>')
    return f"""<section class="hero hero--landing" aria-labelledby="hero-title">
<div class="wrap">{crumbs}</div>
<div class="wrap hero-grid">
<div class="hero-copy">
<p class="eyebrow">{esc(t[p + '_eyebrow'])}</p>
<h1 id="hero-title">{t[p + '_h1']}</h1>
<p class="lead">{esc(t[p + '_lead'])}</p>
<ul class="check-list">{points}</ul>
<div class="cta-row">
<a class="button button-primary" href="#{ids['contact']}" data-topic="{kind}" data-track="hero_cta_contact">{esc(t[p + '_cta'])}</a>
<a class="button button-ghost" href="#{ids['case']}" data-track="hero_cta_case">{esc(t[p + '_cta2'])}</a>
</div>
</div>
<figure class="hero-figure hero-figure--plain">
<div class="annotated">{pic}<span class="concept-badge">{esc(t['concept_badge'])}</span></div>
<figcaption>{esc(t['concept_caption'])}</figcaption>
</figure>
</div>
</section>"""


def tldr(lang):
    t = CONTENT[lang]
    items = "".join(f'<li><h3>{esc(a)}</h3><p>{esc(b)}</p></li>' for a, b in t["tldr"])
    return f"""<section class="tldr" aria-labelledby="tldr-title">
<div class="wrap">
<h2 class="visually-hidden" id="tldr-title">{esc(t['tldr_title'])}</h2>
<p class="tldr-for">{t['tldr_for']}</p>
<ul class="tldr-list">{items}</ul>
</div>
</section>"""


def player(lang):
    t = CONTENT[lang]
    v = C.VIDEO
    if not v:
        return f"""<div class="player is-placeholder" role="img" aria-label="{esc(t['video_placeholder_title'])}">
<div class="player-ph">
<span class="play-ring" aria-hidden="true">{icon('play')}</span>
<p class="player-ph-title">{esc(t['video_placeholder_title'])}</p>
<p>{esc(t['video_placeholder_text'])}</p>
{('<p>' + todo(t['video_todo']) + '</p>') if C.DRAFT else ''}
</div>
</div>"""
    tracks = ""
    for l in LANGS:
        if v.get("captions", {}).get(l):
            default = " default" if l == lang else ""
            tracks += (f'<track kind="captions" srclang="{l}" label="{esc(CONTENT[l]["lang_name"])}" '
                       f'src="{v["captions"][l]}"{default}>')
    dur = v.get("duration_label", {}).get(lang, "")
    webm = f'<source src="{v["src_webm"]}" type="video/webm">' if v.get("src_webm") else ""
    return f"""<div class="player">
<video id="case-video" controls preload="none" playsinline poster="{v['poster']}" width="{v['width']}" height="{v['height']}" data-video-name="expo_case">
{webm}<source src="{v['src']}" type="video/mp4">{tracks}
</video>
<button class="player-play" type="button" aria-label="{esc(t['video_play'])}">{icon('play')}<span>{esc(t['video_play'])}{(' · ' + esc(dur)) if dur else ''}</span></button>
</div>
<p class="player-meta">{esc(t['video_duration'])}: {esc(dur)} · {esc(t['video_captions_note'])}</p>"""


def case(lang, kind="expo"):
    """Sekcja „Przykład”. kind="expo" — demonstrator stoiska (strona główna, projekt stoiska);
    kind="3d" — ten sam projekt demonstracyjny opisany z perspektywy prezentacji produktu."""
    t = CONTENT[lang]
    ids = IDS[lang]
    k = "case3d" if kind == "3d" else "case"
    intro = t[k + "_intro"] if C.VIDEO else t[k + "_intro_pending"]
    benefits = "".join(f'<li><h3>{esc(a)}</h3><p>{esc(b)}</p></li>' for a, b in t[k + "_benefits"])
    tag = f'<p class="demo-tag">{esc(t[k + "_tag"])}</p>'
    cta = f"""<div class="case-cta">
<p>{esc(t[k + '_cta_q'])}</p>
<a class="button button-primary" href="#{ids['contact']}" data-topic="{kind}" data-track="case_cta_click">{esc(t[k + '_cta'])}</a>
</div>"""
    if kind == "3d":
        bottom = f'<div class="case-bottom case-bottom--single">{cta}</div>'
    else:
        chapters = "".join(f'<li>{esc(c)}</li>' for c in t["case_chapters"])
        transcript = (f'<details class="transcript"><summary>{esc(t["case_transcript"])}</summary>'
                      f'{todo(t["case_transcript_body"])}</details>') if C.VIDEO else ""
        bottom = f"""<div class="case-bottom">
<div class="chapters">
<h3>{esc(t['case_chapters_title'])}</h3>
<ol>{chapters}</ol>
{transcript}
</div>
{cta}
</div>"""
    return f"""<section class="section case" id="{ids['case']}" aria-labelledby="case-title">
<div class="wrap">
{section_head(t['case_label'], esc(t[k + '_h2']), t[k + '_lead'], 'case-title', tag)}
<div class="case-stage">
{player(lang)}
</div>
<p class="case-intro">{esc(intro)}</p>
<ul class="benefits">{benefits}</ul>
{bottom}
</div>
</section>"""


def services(lang):
    t = CONTENT[lang]
    ids = IDS[lang]
    cards = []
    for s in t["services"]:
        items = "".join(f'<li>{icon("check")}{esc(x)}</li>' for x in s["items"])
        more = ""
        if s["more"]:
            label, target = s["more"]
            more = f'<a class="text-link" href="{page_path(lang, target)}">{esc(label)}{icon("arrow")}</a>'
        cards.append(f"""<article class="service service--{s['who_type']}">
<p class="service-code">{esc(s['code'])}</p>
<h3>{esc(s['title'])}</h3>
<p class="service-desc">{esc(s['desc'])}</p>
<ul class="service-list">{items}</ul>
<p class="who who--{s['who_type']}">{esc(s['who'])}</p>
<div class="service-actions">
<a class="button button-ghost button-small" href="#{ids['contact']}" data-topic="{s['key']}">{esc(s['ask'])}</a>
{more}
</div>
</article>""")
    return f"""<section class="section services" id="{ids['services']}" aria-labelledby="services-title">
<div class="wrap">
{section_head(t['services_label'], esc(t['services_h2']), t['services_lead'], 'services-title')}
<div class="services-grid">{''.join(cards)}</div>
<p class="services-note">{esc(t['services_note'])}</p>
</div>
</section>"""


def costs(lang):
    t = CONTENT[lang]
    ids = IDS[lang]
    variants = ["economy", "smart", "premium"]
    tabs = "".join(
        f'<button type="button" role="tab" id="tab-{v}" aria-controls="cost-sheet" '
        f'aria-selected="{"true" if v == "smart" else "false"}" tabindex="{"0" if v == "smart" else "-1"}" '
        f'data-variant="{v}">{v.capitalize()}</button>' for v in variants)
    rows = []
    for code, name, typ, descs in t["costs_rows"]:
        d = "".join(f'<span class="v v-{v}">{esc(x)}</span>' for v, x in zip(variants, descs))
        rows.append(f'<tr><td class="c-code">{code}</td><th scope="row">{esc(name)}</th>'
                    f'<td><span class="chip chip--{typ}">{esc(t["cost_types"][typ])}</span></td><td class="c-desc">{d}</td></tr>')
    c1, c2, c3 = t["costs_cols"]
    legend = "".join(f'<li><span class="chip chip--{k}">{esc(a)}</span> {esc(b)}</li>' for k, a, b in t["costs_legend"])
    get = "".join(f'<li>{icon("check")}{esc(x)}</li>' for x in t["costs_get"])
    return f"""<section class="section costs" id="{ids['costs']}" aria-labelledby="costs-title">
<div class="wrap costs-grid">
<div class="costs-copy">
{section_head(t['costs_label'], t['costs_h2'], t['costs_lead'], 'costs-title')}
<ul class="legend">{legend}</ul>
<h3 class="small-h">{esc(t['costs_get_title'])}</h3>
<ul class="check-list">{get}</ul>
</div>
<div class="sheet" data-variant="smart">
<div class="sheet-top">
<p class="sheet-title">{esc(t['costs_sheet_title'])}</p>
<div class="seg" role="tablist" aria-label="{esc(t['costs_variant_label'])}">{tabs}</div>
</div>
<div class="sheet-body" id="cost-sheet" role="tabpanel" aria-labelledby="tab-smart" tabindex="0">
<table>
<thead><tr><th scope="col" class="c-code"><span class="visually-hidden">ID</span></th><th scope="col">{esc(c1)}</th><th scope="col">{esc(c2)}</th><th scope="col">{esc(c3)}</th></tr></thead>
<tbody>{''.join(rows)}</tbody>
</table>
</div>
<p class="sheet-note">{esc(t['costs_sheet_note'])}</p>
</div>
</div>
</section>"""


def about(lang):
    t = CONTENT[lang]
    ids = IDS[lang]
    body = "".join(f"<p>{esc(p)}</p>" for p in t["about_body"])
    own = "".join(f"<li>{esc(x)}</li>" for x in t["about_own"])
    partners = "".join(f"<li>{esc(x)}</li>" for x in t["about_partners"])
    pic = picture('aleks', [400, 600, 800], 800, 1067, t['about_photo_alt'], '(min-width: 900px) 320px, 60vw')
    return f"""<section class="section about" id="{ids['about']}" aria-labelledby="about-title">
<div class="wrap">
<div class="about-grid">
<div class="about-photo">{pic}</div>
<div class="about-copy">
<p class="section-label">{esc(t['about_label'])}</p>
<h2 id="about-title">{esc(t['about_h2'])}</h2>
<div class="about-body">{body}</div>
<a class="text-link" href="{C.LINKEDIN_ALEKS}" rel="noopener" target="_blank">{icon('linkedin')}{esc(t['about_linkedin'])}</a>
</div>
</div>
<div class="roles">
<div class="role role--own"><h3>{esc(t['about_own_title'])}</h3><ol class="flow">{own}</ol></div>
<div class="role role--partners"><h3>{esc(t['about_partners_title'])}</h3><ul class="pills">{partners}</ul>
<p>{esc(t['about_partners_note'])}</p></div>
</div>
</div>
</section>"""


def process(lang):
    t = CONTENT[lang]
    ids = IDS[lang]
    steps = "".join(f'<li><h3>{esc(a)}</h3><p>{esc(b)}</p></li>' for a, b in t["process"])
    return f"""<section class="section process" id="{ids['process']}" aria-labelledby="process-title">
<div class="wrap">
{section_head(t['process_label'], esc(t['process_h2']), None, 'process-title')}
<ol class="steps">{steps}</ol>
</div>
</section>"""


def faq(lang, keys):
    t = CONTENT[lang]
    ids = IDS[lang]
    items = []
    for k in keys:
        q, a = t["faq"][k]
        items.append(f'<details class="faq-item"><summary>{esc(q)}</summary><div class="faq-a">{todo(a)}</div></details>')
    return f"""<section class="section faq" id="{ids['faq']}" aria-labelledby="faq-title">
<div class="wrap faq-grid">
{section_head(t['faq_label'], esc(t['faq_h2']), None, 'faq-title')}
<div class="faq-list">{''.join(items)}</div>
</div>
</section>"""


def get_grid(lang, kind):
    t = CONTENT[lang]
    ids = IDS[lang]
    p = "expo" if kind == "expo" else "p3d"
    items = "".join(f'<li><h3>{esc(a)}</h3><p>{esc(b)}</p></li>' for a, b in t[f"{p}_get"])
    label = t["services_label"]
    return f"""<section class="section get" id="{ids['get']}" aria-labelledby="get-title">
<div class="wrap">
{section_head(label, esc(t[p + '_get_h2']), None, 'get-title')}
<ul class="get-grid">{items}</ul>
</div>
</section>"""


def after_fair(lang):
    t = CONTENT[lang]
    tags = "".join(f"<li>{esc(x)}</li>" for x in t["p3d_after_tags"])
    return f"""<section class="section after">
<div class="wrap after-inner">
<h2>{esc(t['p3d_after_h2'])}</h2>
<div><p>{esc(t['p3d_after'])}</p><ul class="pills">{tags}</ul></div>
</div>
</section>"""


def cross(lang, kind):
    """Odnośnik do drugiej, równorzędnej usługi (na podstronach usług)."""
    t = CONTENT[lang]
    k = "cross_expo" if kind == "expo" else "cross_3d"
    target = "3d" if kind == "expo" else "expo"
    return f"""<section class="section after cross" aria-labelledby="cross-title">
<div class="wrap after-inner">
<h2 id="cross-title">{esc(t[k + '_h2'])}</h2>
<div><p>{esc(t[k + '_text'])}</p>
<a class="text-link" href="{page_path(lang, target)}">{esc(t[k + '_link'])}{icon('arrow')}</a></div>
</div>
</section>"""


def contact(lang, page, topic="general"):
    t = CONTENT[lang]
    ids = IDS[lang]
    reuse = "".join(f'<option value="{esc(v)}">{esc(l)}</option>' for v, l in t["f_reuse_opts"])
    topics = "".join(f'<option value="{k}"{" selected" if k == topic else ""}>{esc(v)}</option>'
                     for k, v in t["topics"].items())
    h2 = t.get(f"contact_h2_{page}", t["contact_h2"])
    privacy = page_path(lang, "privacy")
    brief = esc(t["contact_brief"]).replace("{email}", f'<a href="mailto:{C.EMAIL}" data-track="email_click">{esc(C.EMAIL)}</a>')
    i18n = {k: t[k] for k in ("f_err_contact", "f_err_empty", "f_err_email", "f_success", "f_fail", "f_fail_email", "f_fail_wa",
                              "f_preview", "f_sending", "f_submit", "f_turnstile_wait", "f_turnstile_check", "f_turnstile_unavailable", "mail_subject", "wa_hello")}
    i18n["topics"] = t["topics"]
    i18n["fields"] = t["field_names"]
    opt = f'<span class="opt">({esc(t["f_optional"])})</span>'
    return f"""<section class="section contact" id="{ids['contact']}" aria-labelledby="contact-title">
<div class="wrap contact-grid">
<div class="contact-copy">
{section_head(t['contact_label'], esc(h2), t['contact_lead'], 'contact-title')}
<p class="direct-title">{esc(t['contact_direct'])}</p>
<ul class="direct">
<li><a href="tel:{C.PHONE_TEL}" data-track="phone_click">{icon('phone')}<span><strong>{esc(C.PHONE_DISPLAY)}</strong><small>{esc(t['contact_phone_sub'])}</small></span></a></li>
<li><a href="mailto:{C.EMAIL}" data-track="email_click">{icon('mail')}<span><strong>{esc(C.EMAIL)}</strong><small>{esc(t['contact_email_sub'])}</small></span></a></li>
</ul>
<p class="wa-line"><a class="text-link" href="https://wa.me/{C.WHATSAPP}?text={html.escape(__import__('urllib.parse').parse.quote(t['wa_hello']))}" rel="noopener" target="_blank" data-track="whatsapp_click">{icon('wa')}{esc(t['contact_wa'])}</a></p>
<p class="contact-small">{brief}<br>{esc(t['contact_lang'])}</p>
</div>
<div class="form-panel">
<h3 class="form-title">{esc(t['form_title'])}</h3>
<form id="lead-form" class="lead-form" action="/api/lead" method="post" novalidate>
<input type="hidden" name="lang" value="{lang}">
<input type="hidden" name="page" value="{page}">
<div class="hp" aria-hidden="true" inert><input type="text" name="website" id="f-website" tabindex="-1" autocomplete="off" aria-hidden="true"></div>
<div class="field">
<label for="f-contact">{esc(t['f_contact'])} <span class="req">({esc(t['f_required'])})</span></label>
<input id="f-contact" name="contact" type="text" required maxlength="140" autocomplete="on" spellcheck="false" autocapitalize="off" autocorrect="off" enterkeyhint="next" aria-describedby="f-contact-hint f-error">
<p class="hint" id="f-contact-hint">{esc(t['f_contact_hint'])}</p>
</div>
<div class="field-row">
<div class="field">
<label for="f-topic">{esc(t['f_topic'])}</label>
<select id="f-topic" name="topic">{topics}</select>
</div>
<div class="field">
<label for="f-name">{esc(t['f_name'])} {opt}</label>
<input id="f-name" name="name" type="text" maxlength="80" autocomplete="name">
</div>
</div>
<div class="field">
<label for="f-message">{esc(t['f_message'])} {opt}</label>
<textarea id="f-message" name="message" rows="3" maxlength="2000" placeholder="{esc(t['f_message_ph'])}"></textarea>
</div>
<details class="more-fields">
<summary>{esc(t['f_more'])} {opt}</summary>
<div class="more-grid">
<div class="field"><label for="f-event">{esc(t['f_event'])}</label><input id="f-event" name="event" type="text" maxlength="120"></div>
<div class="field"><label for="f-city">{esc(t['f_city'])}</label><input id="f-city" name="city" type="text" maxlength="80" autocomplete="address-level2"></div>
<div class="field"><label for="f-date">{esc(t['f_date'])}</label><input id="f-date" name="date" type="text" maxlength="60" placeholder="{esc(t['f_date_ph'])}"></div>
<div class="field"><label for="f-area">{esc(t['f_area'])}</label><input id="f-area" name="area" type="text" inputmode="decimal" maxlength="20"></div>
<div class="field"><label for="f-budget">{esc(t['f_budget'])}</label><input id="f-budget" name="budget" type="text" maxlength="80" placeholder="{esc(t['f_budget_ph'])}"></div>
<div class="field"><label for="f-reuse">{esc(t['f_reuse'])}</label><select id="f-reuse" name="reuse">{reuse}</select></div>
</div>
</details>
<div class="turnstile-holder" id="turnstile-container" aria-label="{esc(t['f_turnstile_label'])}"></div>
<p class="form-error" id="f-error" role="alert"></p>
<button class="button button-primary button-block" type="submit">{esc(t['f_submit'])}</button>
<div class="form-status" id="f-status" role="status" aria-live="polite" tabindex="-1"></div>
<p class="form-note">{t['f_disclaimer'].replace('{privacy}', privacy)}</p>
</form>
<script type="application/json" id="form-i18n">{json.dumps(i18n, ensure_ascii=False)}</script>
<script type="application/json" id="form-config">{json.dumps({"email": C.EMAIL, "wa": C.WHATSAPP})}</script>
</div>
</div>
</section>"""


# ---------------------------------------------------------------- dane strukturalne
def org_node():
    node = {
        "@type": "ProfessionalService" if C.ADDRESS else "Organization",
        "@id": abs_url("/#organization"),
        "name": "Scenovis",
        "url": abs_url("/"),
        "logo": abs_url("/assets/icons/icon-512.png"),
        "image": abs_url("/assets/og/og-pl.jpg"),
        "email": C.EMAIL,
        "telephone": C.PHONE_TEL,
        "knowsLanguage": ["pl", "en"],
        "founder": {"@id": abs_url("/#aleks")},
        "contactPoint": {"@type": "ContactPoint", "contactType": "customer service",
                         "telephone": C.PHONE_TEL, "email": C.EMAIL, "availableLanguage": ["Polish", "English"]},
    }
    if C.ADDRESS:
        node["address"] = dict({"@type": "PostalAddress"}, **C.ADDRESS)
    return node


def person_node():
    return {"@type": "Person", "@id": abs_url("/#aleks"), "name": "Aleks",
            "jobTitle": "3D / BIM — exhibition stand design and 3D product presentations", "worksFor": {"@id": abs_url("/#organization")},
            "sameAs": [C.LINKEDIN_ALEKS]}


def website_node():
    return {"@type": "WebSite", "@id": abs_url("/#website"), "url": abs_url("/"), "name": "Scenovis",
            "inLanguage": ["pl", "en"], "publisher": {"@id": abs_url("/#organization")}}


def video_node(lang, page="home"):
    v = C.VIDEO
    if not v:
        return None
    t = CONTENT[lang]
    return {"@type": "VideoObject", "@id": abs_url(page_path(lang, page) + "#video"),
            "name": v["name"][lang], "description": t["case_lead"],
            "thumbnailUrl": [abs_url(v["poster"])], "uploadDate": v["upload_date"],
            "duration": v["duration_iso"], "contentUrl": abs_url(v["src"]), "inLanguage": lang,
            "creator": {"@id": abs_url("/#organization")}}


def graph(lang, page, title, desc, extra=None):
    nodes = [org_node(), website_node()]
    url = abs_url(page_path(lang, page))
    wp = {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": title, "description": desc,
          "inLanguage": lang, "isPartOf": {"@id": abs_url("/#website")}, "about": {"@id": abs_url("/#organization")}}
    nodes.append(wp)
    if page == "home":
        nodes.append(person_node())
    for n in (extra or []):
        if n:
            nodes.append(n)
    return {"@context": "https://schema.org", "@graph": nodes}


def service_node(lang, kind):
    t = CONTENT[lang]
    p = "expo" if kind == "expo" else "p3d"
    return {"@type": "Service", "@id": abs_url(page_path(lang, kind)) + "#service", "name": t[p + "_crumb"],
            "description": t[p + "_desc"], "provider": {"@id": abs_url("/#organization")},
            "serviceType": t[p + "_crumb"], "url": abs_url(page_path(lang, kind))}


def breadcrumb_node(lang, kind):
    t = CONTENT[lang]
    p = "expo" if kind == "expo" else "p3d"
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": t["breadcrumb_home"], "item": abs_url(page_path(lang, "home"))},
        {"@type": "ListItem", "position": 2, "name": t[p + "_crumb"], "item": abs_url(page_path(lang, kind))}]}


# ---------------------------------------------------------------- strony
def alts(page):
    return {l: page_path(l, page) for l in LANGS}


def build_home(lang):
    t = CONTENT[lang]
    a = alts("home")
    ld = graph(lang, "home", t["home_title"], t["home_desc"], [video_node(lang, "home")])
    return (head(lang, "home", t["home_title"], t["home_desc"], a, jsonld=ld)
            + header(lang, "home", a)
            + hero_home(lang) + tldr(lang) + services(lang) + case(lang, "expo") + costs(lang)
            + about(lang) + process(lang)
            + faq(lang, ["price", "expo_process", "delivery", "3d_forms", "3d_data", "3d_nofair", "area", "time"])
            + contact(lang, "home") + footer(lang))


def build_expo(lang):
    t = CONTENT[lang]
    a = alts("expo")
    ld = graph(lang, "expo", t["expo_title"], t["expo_desc"],
               [service_node(lang, "expo"), breadcrumb_node(lang, "expo"), video_node(lang, "expo")])
    return (head(lang, "expo", t["expo_title"], t["expo_desc"], a, jsonld=ld)
            + header(lang, "expo", a, nav=False)
            + hero_landing(lang, "expo") + get_grid(lang, "expo") + case(lang, "expo") + costs(lang) + process(lang)
            + cross(lang, "expo")
            + faq(lang, ["expo_process", "price", "factors", "buyrent", "reuse", "materials", "delivery", "time"])
            + contact(lang, "expo", topic="expo") + footer(lang))


def build_3d(lang):
    t = CONTENT[lang]
    a = alts("3d")
    ld = graph(lang, "3d", t["p3d_title"], t["p3d_desc"],
               [service_node(lang, "3d"), breadcrumb_node(lang, "3d"), video_node(lang, "3d")])
    return (head(lang, "3d", t["p3d_title"], t["p3d_desc"], a, jsonld=ld)
            + header(lang, "3d", a, nav=False)
            + hero_landing(lang, "3d") + get_grid(lang, "3d") + case(lang, "3d") + after_fair(lang)
            + cross(lang, "3d")
            + faq(lang, ["3d_forms", "3d_data", "3d_hw", "3d_reuse", "3d_nofair", "price"])
            + contact(lang, "3d", topic="3d") + footer(lang))


PRIVACY = {
    "pl": """
<h2>1. Administrator danych</h2>
<p>Administratorem danych osobowych jest Aliaksei Malyshka, prowadzący działalność pod marką Scenovis, ul. Przytulna 26, 80-176 Gdańsk. Kontakt w sprawach danych osobowych: <a href="mailto:{email}">{email}</a>, tel. {phone}.</p>
<h2>2. Jakie dane przetwarzam i po co</h2>
<p>Gdy wysyłasz zapytanie przez formularz, przetwarzam podany telefon lub e-mail, wybrany temat, a jeśli je podasz — imię, treść wiadomości i informacje o projekcie (wydarzenie, miasto, termin, powierzchnia, budżet, ponowne użycie stoiska). Do wiadomości dołączana jest data otrzymania, język i podstrona, z której wysłano formularz, oraz kraj połączenia ustalony przez Cloudflare. Gdy piszesz e-mail, dzwonisz lub korzystasz z WhatsApp, przetwarzam dane, które sam przekażesz.</p>
<p>Cel: odpowiedź na zapytanie i rozmowy o możliwej współpracy oraz ochrona formularza przed spamem i nadużyciami. Podstawa prawna: prawnie uzasadniony interes administratora (art. 6 ust. 1 lit. f RODO) lub — gdy prosisz o ofertę — działania przed zawarciem umowy (art. 6 ust. 1 lit. b RODO).</p>
<h2>3. Jak działa formularz i kto jest odbiorcą danych</h2>
<p>Strona jest hostowana w Cloudflare (Cloudflare, Inc.). Formularz trafia do mechanizmu Cloudflare Workers, który sprawdza dane i przekazuje je dalej jako wiadomość e-mail — <strong>strona nie zapisuje zapytań w bazie danych</strong>. Do ochrony formularza przed nadużyciami służy Cloudflare Turnstile (weryfikacja może przetwarzać dane techniczne przeglądarki i połączenia, w tym adres IP). Wiadomość wysyła usługa Resend, a odbiera ją skrzynka Namecheap Private Email pod adresem {email}. Dostawcy mogą przechowywać kopie wiadomości i logi techniczne zgodnie ze swoimi zasadami.</p>
<p>Część dostawców może przetwarzać dane poza Europejskim Obszarem Gospodarczym — w takim przypadku na podstawie mechanizmów przewidzianych w RODO (np. standardowe klauzule umowne lub decyzja o adekwatności).</p>
<p>Kliknięcie linku do WhatsApp otwiera usługę WhatsApp (Meta), w której obowiązują jej własne zasady prywatności.</p>
<h2>4. Jak długo przechowuję dane</h2>
<p>Zapytania, które nie prowadzą do współpracy, usuwam najpóźniej po 6 miesiącach od ostatniego kontaktu. Jeśli dojdzie do współpracy, korespondencję przechowuję przez czas jej trwania, a następnie przez okres wymagany przepisami (np. podatkowymi) lub potrzebny do ustalenia, dochodzenia albo obrony roszczeń. Kopie wiadomości i logi techniczne u dostawców (Cloudflare, Resend, Namecheap) są usuwane zgodnie z ich zasadami.</p>
<h2>5. Twoje prawa</h2>
<p>Masz prawo dostępu do danych, ich sprostowania, usunięcia lub ograniczenia przetwarzania, prawo do przenoszenia danych oraz prawo sprzeciwu wobec przetwarzania opartego na uzasadnionym interesie. Możesz też złożyć skargę do Prezesa Urzędu Ochrony Danych Osobowych. Podanie kontaktu jest dobrowolne, ale bez niego nie mogę odpowiedzieć. Dane nie służą do profilowania ani automatycznego podejmowania decyzji.</p>
<h2>6. Pliki cookies, analityka i zasoby zewnętrzne</h2>
<p>Strona nie używa plików cookies analitycznych ani reklamowych i nie ma zainstalowanej analityki. Formularz wczytuje zewnętrzny skrypt Cloudflare Turnstile w celu ochrony przed spamem. Czcionki i pliki strony są serwowane z tego samego serwera. Hosting może zapisywać techniczne logi serwera (np. adres IP, czas żądania) w celu zapewnienia bezpieczeństwa i działania strony.</p>
<p>Jeżeli w przyszłości dodam analitykę (np. Google Analytics), tagi reklamowe (np. Google Ads) lub osadzone treści zewnętrzne (np. YouTube), ta polityka zostanie zaktualizowana, a narzędzia te zostaną uruchomione dopiero po uzyskaniu Twojej zgody.</p>
<h2>7. Zmiany</h2>
<p>Aktualna wersja polityki jest zawsze dostępna na tej stronie. Ostatnia aktualizacja: 17 października 2026 r.</p>
""",
    "en": """
<h2>1. Data controller</h2>
<p>The controller of personal data is Aliaksei Malyshka, operating under the Scenovis brand, ul. Przytulna 26, 80-176 Gdańsk, Poland. Contact for data protection matters: <a href="mailto:{email}">{email}</a>, phone {phone}.</p>
<h2>2. What data I process and why</h2>
<p>When you send an enquiry through the form, I process the phone number or email you provide, the selected topic and, if you give them, your name, message and project details (event, city, dates, stand size, budget, reuse). The message also includes the time it was received, the language and page the form was sent from, and the connection country determined by Cloudflare. When you email, call or use WhatsApp, I process the data you choose to share.</p>
<p>Purpose: to answer your enquiry, discuss possible cooperation and protect the form against spam and abuse. Legal basis: the controller’s legitimate interests (Art. 6(1)(f) GDPR) or — if you ask for a quote — steps taken before entering into a contract (Art. 6(1)(b) GDPR).</p>
<h2>3. How the form works and who receives the data</h2>
<p>The website is hosted by Cloudflare (Cloudflare, Inc.). The form is handled by Cloudflare Workers, which checks the data and forwards it as an email — <strong>the website does not store enquiries in a database</strong>. Cloudflare Turnstile protects the form against abuse (verification may process technical browser and connection data, including the IP address). The message is sent through Resend and received in a Namecheap Private Email mailbox at {email}. Providers may keep copies of messages and technical logs under their own terms.</p>
<p>Some providers may process data outside the European Economic Area — in that case on the basis of GDPR transfer mechanisms (e.g. standard contractual clauses or an adequacy decision).</p>
<p>Clicking the WhatsApp link opens WhatsApp (Meta), where its own privacy terms apply.</p>
<h2>4. Retention</h2>
<p>Enquiries that do not lead to cooperation are deleted no later than 6 months after the last contact. If we work together, correspondence is kept for the duration of the cooperation and then for the period required by law (e.g. tax regulations) or needed to establish, pursue or defend legal claims. Copies of messages and technical logs held by providers (Cloudflare, Resend, Namecheap) are deleted under their own terms.</p>
<h2>5. Your rights</h2>
<p>You have the right to access, rectify, erase or restrict the processing of your data, to data portability and to object to processing based on legitimate interests. You may also lodge a complaint with the Polish supervisory authority (Prezes UODO). Providing contact details is voluntary, but I can’t reply without them. The data is not used for profiling or automated decision-making.</p>
<h2>6. Cookies, analytics and external resources</h2>
<p>This website does not use analytics or advertising cookies and has no analytics installed. The contact form loads a third-party Cloudflare Turnstile script to protect against spam. Fonts and site files are served from the same server. The host may keep technical server logs (e.g. IP address, request time) for security and operation of the site.</p>
<p>If analytics (e.g. Google Analytics), advertising tags (e.g. Google Ads) or external embeds (e.g. YouTube) are added in future, this policy will be updated and those tools will run only after you give consent.</p>
<h2>7. Changes</h2>
<p>The current version of this policy is always available on this page. Last updated: 17 October 2026.</p>
""",
}


def build_privacy(lang):
    t = CONTENT[lang]
    a = alts("privacy")
    body = todo(PRIVACY[lang].replace("{email}", C.EMAIL).replace("{phone}", C.PHONE_DISPLAY))
    # Baner widoczny zawsze, dopóki polityka zawiera niewypełnione pola {todo:...} — nawet gdy DRAFT=False.
    draft = f'<p class="policy-draft">{esc(t["privacy_draft"])}</p>' if (C.DRAFT or "{todo:" in PRIVACY[lang]) else ""
    return (head(lang, "privacy", t["privacy_title"], t["privacy_desc"], a, robots="noindex,follow")
            + header(lang, "privacy", a, nav=False)
            + f'<section class="section policy"><div class="wrap narrow"><h1>{esc(t["privacy_h1"])}</h1>{draft}{body}</div></section>'
            + footer(lang))


def build_404():
    t = CONTENT["pl"]
    e = CONTENT["en"]
    a = alts("home")
    return (head("pl", None, t["nf_title"], t["nf_text"], None, robots="noindex")
            + header("pl", "privacy", a, nav=False)
            + f"""<section class="section notfound"><div class="wrap narrow">
<p class="section-label">404</p>
<h1>{esc(t['nf_h1'])}</h1><p class="lead">{esc(t['nf_text'])}</p>
<div class="cta-row"><a class="button button-primary" href="/pl/">{esc(t['nf_home'])}</a></div>
<hr>
<h2 lang="en">{esc(e['nf_h1'])}</h2><p lang="en">{esc(e['nf_text'])}</p>
<div class="cta-row"><a class="button button-ghost" href="/en/" lang="en">{esc(e['nf_home'])}</a></div>
</div></section>""" + footer("pl"))


def build_root():
    # Rezerwowa strona główna "/" (np. gdy Worker nie jest aktywny).
    # Worker Cloudflare odpowiada na "/" przekierowaniem 302: polski w przeglądarce → /pl/, inny język → /en/.
    return f"""<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Scenovis</title>
<meta name="robots" content="noindex,follow">
<link rel="canonical" href="{abs_url('/pl/')}">
<script src="/assets/js/root.js"></script>
<meta http-equiv="refresh" content="0; url=/pl/">
<style>body{{background:#121617;color:#f1efe8;font:16px/1.6 system-ui,sans-serif;display:grid;place-items:center;min-height:100vh;margin:0}}a{{color:#ffb28e}}</style>
</head>
<body><p><a href="/pl/" lang="pl">Scenovis — polski</a> · <a href="/en/" lang="en">Scenovis — English</a></p></body>
</html>
"""


def legacy_privacy():
    return f"""<!doctype html>
<html lang="pl"><head><meta charset="utf-8"><title>Scenovis</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="{abs_url('/pl/polityka-prywatnosci/')}">
<meta http-equiv="refresh" content="0; url=/pl/polityka-prywatnosci/"></head>
<body><a href="/pl/polityka-prywatnosci/">Polityka prywatności</a> · <a href="/en/privacy-policy/">Privacy policy</a></body></html>
"""


def sitemap():
    today = date.today().isoformat()
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for page in ("home", "expo", "3d"):
        for lang in LANGS:
            out.append("<url>")
            out.append(f"<loc>{abs_url(page_path(lang, page))}</loc>")
            out.append(f"<lastmod>{today}</lastmod>")
            for l in LANGS:
                out.append(f'<xhtml:link rel="alternate" hreflang="{l}" href="{abs_url(page_path(l, page))}"/>')
            out.append(f'<xhtml:link rel="alternate" hreflang="x-default" href="{abs_url(page_path("en", page))}"/>')
            out.append("</url>")
    out.append("</urlset>\n")
    return "\n".join(out)


def robots():
    return f"User-agent: *\nAllow: /\nDisallow: /api/\n\nSitemap: {abs_url('/sitemap.xml')}\n"


def write(path, content):
    full = os.path.join(ROOT, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    return path


def check_keys():
    pl, en = set(CONTENT["pl"]), set(CONTENT["en"])
    if pl != en:
        raise SystemExit(f"Brak kluczy — tylko PL: {sorted(pl - en)} / tylko EN: {sorted(en - pl)}")
    if set(CONTENT["pl"]["faq"]) != set(CONTENT["en"]["faq"]):
        raise SystemExit("FAQ PL/EN mają różne klucze")


def main():
    check_keys()
    written = []
    for lang in LANGS:
        written.append(write(page_path(lang, "home") + "index.html", build_home(lang)))
        written.append(write(page_path(lang, "expo") + "index.html", build_expo(lang)))
        written.append(write(page_path(lang, "3d") + "index.html", build_3d(lang)))
        written.append(write(page_path(lang, "privacy") + "index.html", build_privacy(lang)))
    written.append(write("/404.html", build_404()))
    written.append(write("/index.html", build_root()))
    written.append(write("/privacy.html", legacy_privacy()))
    written.append(write("/sitemap.xml", sitemap()))
    written.append(write("/robots.txt", robots()))
    print(f"OK ({'DRAFT' if C.DRAFT else 'PRODUKCJA'}, v={VER}, {C.SITE_URL})")
    for w in written:
        print("  ", w)


if __name__ == "__main__":
    main()
