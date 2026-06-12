#!/usr/bin/env python3
"""Generate product detail pages for all languages from products.json."""

import json
import os
import shutil

BASE = os.path.dirname(os.path.abspath(__file__))

NAV = {
    "en": {
        "home": "Home", "products": "Products", "gastro": "Gastronomy",
        "private": "Private Household", "cabinet": "Cabinet Smoker",
        "offset": "Offset BBQ &amp; Grill", "brat": "Brat und Backöfen",
        "catering": "Catering", "about": "About Us", "contact": "Contact",
        "privacy": "Privacy Policy", "shipping": "Shipping &amp; Returns",
        "store": "Store Policy", "imprint": "Imprint",
        "footer_nav": "Navigation", "footer_prod": "Products",
        "footer_legal": "Legal", "footer_contact": "Contact",
        "country": "Switzerland", "city": "Winterthur",
        "lang_en": "EN", "lang_fr": "FR", "lang_it": "IT"
    },
    "fr": {
        "home": "Domicile", "products": "Des Produits", "gastro": "La Gastronomie",
        "private": "Ménage Privé", "cabinet": "Armoire Fumeur",
        "offset": "Offset BBQ &amp; Grill", "brat": "Brat und Backöfen",
        "catering": "Catering", "about": "À Propos", "contact": "Contacter",
        "privacy": "Confidentialité", "shipping": "Livraison &amp; Retours",
        "store": "Politique du Magasin", "imprint": "Mentions Légales",
        "footer_nav": "Navigation", "footer_prod": "Produits",
        "footer_legal": "Légal", "footer_contact": "Contacter",
        "country": "Suisse", "city": "Winterthour",
        "lang_en": "EN", "lang_fr": "FR", "lang_it": "IT"
    },
    "it": {
        "home": "Casa", "products": "Prodotti", "gastro": "Gastronomia",
        "private": "Domestico Privato", "cabinet": "Fumatore da Armadio",
        "offset": "Offset BBQ &amp; Grill", "brat": "Brat und Backöfen",
        "catering": "Ristorazione", "about": "Chi Siamo", "contact": "Contatto",
        "privacy": "Privacy", "shipping": "Spedizione &amp; Resi",
        "store": "Politica del Negozio", "imprint": "Impronta",
        "footer_nav": "Navigazione", "footer_prod": "Prodotti",
        "footer_legal": "Legale", "footer_contact": "Contatto",
        "country": "Svizzera", "city": "Winterthur",
        "lang_en": "EN", "lang_fr": "FR", "lang_it": "IT"
    }
}

SITE_NAME = "GrillCraft BBQ"
LOGO = "https://static.wixstatic.com/media/21445d_4a755b26d6f849c284dfb430a6860859~mv2.png"
FB_ICON = "https://static.wixstatic.com/media/e316f544f9094143b9eac01f1f19e697.png"
IG_ICON = "https://static.wixstatic.com/media/9f9c321c774844b793180620472aa4f1.png"
FB_URL = "https://www.facebook.com/bbqitboxschweiz"
IG_URL = "https://www.instagram.com/bbqpitboxschweiz/"
IMG_BASE = "https://static.wixstatic.com/media/"

def nav_header(lang, active_path, active_lang):
    t = NAV[lang]
    def l(href, code):
        cls = ' class="active"' if code == active_lang else ""
        return f'<a href="/{href}/"{cls}>{t["lang_" + code]}</a>'
    return f'''<header class="header"><div class="header-inner">
<a href="/{lang}/" class="logo"><img src="{LOGO}" alt="{SITE_NAME}"></a>
<button class="mobile-toggle" aria-label="Menu"><span></span><span></span><span></span></button>
<nav class="nav">
<a href="/{lang}/">{t["home"]}</a>
<div class="dropdown">
<a href="/{lang}/produkte" class="dropbtn">{t["products"]}</a>
<div class="dropdown-content"><a href="/{lang}/gastronomie">{t["gastro"]}</a><a href="/{lang}/private-haushalt">{t["private"]}</a></div>
</div>
<a href="/{lang}/cabinet-smoker">{t["cabinet"]}</a>
<a href="/{lang}/offset-bbq-grill">{t["offset"]}</a>
<a href="/{lang}/brat-und-backoefen">{t["brat"]}</a>
<a href="/{lang}/catering">{t["catering"]}</a>
<div class="dropdown">
<a href="/{lang}/uber-uns" class="dropbtn">{t["about"]}</a>
<div class="dropdown-content"><a href="/{lang}/contact">{t["contact"]}</a></div>
</div>
<div class="lang-switcher">{l("en", "en")}{l("fr", "fr")}{l("it", "it")}</div>
</nav></div></header>'''

def footer(lang):
    t = NAV[lang]
    return f'''<footer class="footer"><div class="container"><div class="footer-grid">
<div><h4>{t["footer_nav"]}</h4>
<a href="/{lang}/">{t["home"]}</a><a href="/{lang}/produkte">{t["products"]}</a><a href="/{lang}/cabinet-smoker">{t["cabinet"]}</a>
<a href="/{lang}/offset-bbq-grill">{t["offset"]}</a><a href="/{lang}/catering">{t["catering"]}</a>
<a href="/{lang}/uber-uns">{t["about"]}</a><a href="/{lang}/contact">{t["contact"]}</a></div>
<div><h4>{t["footer_prod"]}</h4>
<a href="/{lang}/gastronomie">{t["gastro"]}</a><a href="/{lang}/private-haushalt">{t["private"]}</a>
<a href="/{lang}/brat-und-backoefen">{t["brat"]}</a></div>
<div><h4>{t["footer_legal"]}</h4>
<a href="/{lang}/datenschutzerklarung">{t["privacy"]}</a><a href="/{lang}/shipping-and-returns">{t["shipping"]}</a>
<a href="/{lang}/store-policy">{t["store"]}</a><a href="/{lang}/impressum">{t["imprint"]}</a></div>
<div class="footer-contact"><h4>{t["footer_contact"]}</h4>
<p>KLERED GmbH</p><p>Stadthausstrasse 10b</p><p>8400 {t["city"]}, {t["country"]}</p>
<p>Phone: +41 52 203 1111</p>
<p><a href="mailto:info@bbqpitbox.com">info@bbqpitbox.com</a></p>
<div class="social"><a href="{FB_URL}" target="_blank" rel="noopener"><img src="{FB_ICON}" alt="Facebook"></a>
<a href="{IG_URL}" target="_blank" rel="noopener"><img src="{IG_ICON}" alt="Instagram"></a></div></div></div>
<div class="footer-bottom"><p>&copy; 2021 BY KLERED GmbH &ndash; Winterthur {t["country"]}</p></div></div></footer>'''

def page_template(lang, title, desc, content, active_lang):
    return f'''<!DOCTYPE html><html lang="{lang}"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | {SITE_NAME}</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/png" href="{LOGO}">
<link rel="stylesheet" href="/assets/css/style.css">
</head><body>
{nav_header(lang, "", active_lang)}
<section class="content-page"><div class="container">
{content}
</div></section>
{footer(lang)}
<script src="/assets/js/script.js"></script>
</body></html>'''

def build_series_page(lang, s, active_lang):
    img_url = f"{IMG_BASE}{s['image']}"
    badge_html = f'<div class="badge">{s["badge"]}</div>' if s["badge"] else ""
    variants_html = ""
    if s["variants"]:
        variants_html = '<div class="grid-2" style="margin-top:30px"><h3 style="grid-column:1/-1">Models</h3>'
        for v in s["variants"]:
            vimg = f"{IMG_BASE}{v['image']}"
            variants_html += f'''
<div class="prod-card">
<img src="{vimg}" alt="{v['name']}" loading="lazy">
<div class="prod-card-body">
<h3>{v['name']}</h3>
<div class="badge" style="font-size:14px;color:var(--text-light);margin:8px 0">Out of stock</div>
<a href="/{lang}/product-page/{v['slug']}" class="btn btn-sm">More Info</a>
</div>
</div>'''
        variants_html += "</div>"

    content = f'''
<div class="breadcrumb"><a href="/{lang}/">{NAV[lang]["home"]}</a> <span>/ <a href="/{lang}/produkte">{NAV[lang]["products"]}</a> / {s['name']}</span></div>
<div class="prod-detail">
<div><img src="{img_url}" alt="{s['name']}" loading="lazy"></div>
<div>
{badge_html}
<h1>{s['name']}</h1>
<p style="font-size:1.1rem;color:var(--text-light);margin:8px 0">{s['tagline']}</p>
<div class="badge" style="font-size:14px;color:var(--text-light);margin:8px 0">Out of stock</div>
<div class="desc"><p>{s['description']}</p></div>
<div class="meta"><p><strong>Category:</strong> {s['category']}</p><p><strong>Capacity:</strong> {s['capacity']}</p></div>
</div>
</div>
{variants_html}'''
    return content

def build_individual_page(lang, p, active_lang):
    img_url = f"{IMG_BASE}{p['image']}"
    content = f'''
<div class="breadcrumb"><a href="/{lang}/">{NAV[lang]["home"]}</a> <span>/ <a href="/{lang}/produkte">{NAV[lang]["products"]}</a> / {p['name']}</span></div>
<div class="prod-detail">
<div><img src="{img_url}" alt="{p['name']}" loading="lazy"></div>
<div>
<h1>{p['name']}</h1>
<div class="badge" style="font-size:14px;color:var(--text-light);margin:8px 0">Out of stock</div>
<div class="desc"><p>{p['description']}</p></div>
<div class="meta"><p><strong>Category:</strong> {p['category']}</p><p><strong>Capacity:</strong> {p['capacity']}</p></div>
</div>
</div>'''
    return content

def main():
    with open(os.path.join(BASE, "products.json")) as f:
        data = json.load(f)

    for lang in ["en", "fr", "it"]:
        pp_dir = os.path.join(BASE, lang, "product-page")
        os.makedirs(pp_dir, exist_ok=True)

        t = NAV[lang]
        active_lang = lang

        # Generate series pages
        for s in data["series"]:
            content = build_series_page(lang, s, active_lang)
            title = s["name"]
            desc = s["description"][:150]
            html = page_template(lang, title, desc, content, active_lang)
            path = os.path.join(pp_dir, f"{s['slug']}.html")
            with open(path, "w") as f:
                f.write(html)
            print(f"  Created: {path}")

            # Generate variant pages for this series
            for v in s["variants"]:
                individual_data = {
                    "slug": v["slug"],
                    "name": v["name"],
                    "category": s["category"],
                    "capacity": v["capacity"],
                    "image": v["image"] if v["image"] else s["image"],
                    "description": f"The {v['name']} is a model from the {s['name']} series. {s['description']}"
                }
                content = build_individual_page(lang, individual_data, active_lang)
                html = page_template(lang, v["name"], individual_data["description"][:150], content, active_lang)
                path = os.path.join(pp_dir, f"{v['slug']}.html")
                with open(path, "w") as f:
                    f.write(html)
                print(f"  Created: {path}")

        # Generate individual product pages
        for p in data["individuals"]:
            content = build_individual_page(lang, p, active_lang)
            html = page_template(lang, p["name"], p["description"][:150], content, active_lang)
            path = os.path.join(pp_dir, f"{p['slug']}.html")
            with open(path, "w") as f:
                f.write(html)
            print(f"  Created: {path}")

        print(f"Done generating {lang} product pages!\n")

if __name__ == "__main__":
    main()
