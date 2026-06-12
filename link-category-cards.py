#!/usr/bin/env python3
"""Add 'More Info' links to product cards in category listing pages."""

import os
import re

BASE = "/home/v/bbq/grillcraftbbq.com"

# Maps (normalized product name) -> (slug)
# We normalize by lowercasing, stripping punctuation, collapsing whitespace
NAME_TO_SLUG = {}

# From products.json series + individuals
PRODUCT_MAP = {
    # Gastronomy page products
    "BBQ Pit Box Compact Smoker \u2013 Size XXS": "compact-smoker-xxs",
    "Yakitori BBQ Grill \u2013 SIZE S": "yakitori-bbq-grill-s",
    "BBQ Pit Box Compact Smoker \u2013 Size XXS Plus": "compact-smoker-xxs-plus",
    "BBQ Pit Box Compact Smoker \u2013 Size XS": "compact-smoker-xs",
    "BBQ Pit Box Smoker \u2013 Size S": "smoker-size-s",
    "BBQ Pit Box Duck Oven \u2013 Size XS": "duck-oven-xs",
    "ASADO Grill Mobile Fire Pit \u2013 SIZE S": "asado-grill-s",
    "Yakitori BBQ Grill \u2013 SIZE M": "yakitori-bbq-grill-m",
    "BBQ Pit Box Compact Smoker \u2013 Size S": "compact-smoker-s",
    # Cabinet Smoker page
    "BYH Cadet XS": "byh-cadet-xs",
    "BYH Junior XXS": "byh-junior-xxs",
    "Compact Smoker XXS": "compact-smoker-xxs",
    "Duck Oven XS": "duck-oven-xs",
    "Compact Smoker XS": "compact-smoker-xs",
    "Smoker Size S": "smoker-size-s",
    "Compact Smoker XXS Plus": "compact-smoker-xxs-plus",
    "Duck Oven XS Plus": "duck-oven-xs-plus",
    "Compact Smoker S": "compact-smoker-s",
    # Offset BBQ & Grill page
    "NYP BBQ Regular Offset XS": "nyp-regular-offset-xs",
    "NYP BBQ Regular Offset S": "nyp-regular-offset-s",
    "ASADO Grill Mobile Fire Pit - SIZE S": "asado-grill-s",
    "Yakitori BBQ Grill - SIZE S": "yakitori-bbq-grill-s",
    "Offset BBQ Grill - SIZE S": "offset-bbq-grill-s",
    "Offset BBQ Grill - SIZE L": "offset-bbq-grill-l",
    "Yakitori BBQ Grill - SIZE L": "yakitori-bbq-grill-l",
    "Duck Oven Size L": "duck-oven-l",
    "Whole Hog BBQ Grill": "whole-hog-monster",
    # Brat und Backöfen page
    "Duck Oven Size XS Plus": "duck-oven-xs-plus",
    "Duck Oven Size S": "duck-oven-s",
    "Duck Oven Size M": "duck-oven-m",
    "Duck Oven Size L": "duck-oven-l",
    "Duck Oven Size XS": "duck-oven-xs",
    "B Oven S": "b-oven-s",
    # Private Household page
    "NYP BBQ Regular Offset XS": "nyp-regular-offset-xs",
    "NYP BBQ Regular Offset S": "nyp-regular-offset-s",
    "BBQ Pit Box B Oven S": "b-oven-s",
    "BYH Cadet XS": "byh-cadet-xs",
    "BYH Junior XXS": "byh-junior-xxs",
    "BBQ Pit Box Compact Smoker Size XS": "compact-smoker-xs",
    "ASADO Grill Mobile Fire Pit SIZE S": "asado-grill-s",
    "BBQ Pit Box Compact Smoker Size XXS": "compact-smoker-xxs",
    "BBQ Pit Box Smoker Size S": "smoker-size-s",
}

# Build normalized map for fuzzy matching
def norm(s):
    return re.sub(r'[^a-z0-9]', '', s.lower())

for name, slug in PRODUCT_MAP.items():
    NAME_TO_SLUG[norm(name)] = slug

def find_slug(h3_text):
    n = norm(h3_text)
    # Exact normalized match first
    if n in NAME_TO_SLUG:
        return NAME_TO_SLUG[n]
    # Try substring matching
    for key, slug in NAME_TO_SLUG.items():
        if key in n or n in key:
            return slug
    return None

def process_file(filepath, lang):
    with open(filepath) as f:
        content = f.read()
    
    # Find all prod-card blocks
    pattern = re.compile(
        r'(<div class="prod-card">.*?<div class="prod-card-body">.*?<h3>(.*?)</h3>.*?</div>\s*</div>)',
        re.DOTALL
    )
    
    def add_link(match):
        block = match.group(1)
        h3_text = match.group(2)
        # Strip HTML entities for matching
        h3_clean = h3_text.replace('&amp;', '&').replace('&ndash;', '-').replace('\u2013', '-').strip()
        slug = find_slug(h3_clean)
        
        if slug:
            # Check if there's already a More Info link
            if 'More Info' in block and 'btn' in block:
                return block  # already has a link
            # Insert More Info link right after </h3>
            link_html = f'\n          <a href="/{lang}/product-page/{slug}" class="btn btn-sm" style="margin-top:8px">More Info</a>'
            block = block.replace(f'</h3>', f'</h3>{link_html}', 1)
        return block
    
    new_content = pattern.sub(add_link, content)
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        return True
    return False

def main():
    pages = [
        "gastronomie", "private-haushalt", "cabinet-smoker",
        "offset-bbq-grill", "brat-und-backoefen"
    ]
    for lang in ["en", "fr", "it"]:
        for page in pages:
            fp = os.path.join(BASE, lang, f"{page}.html")
            if os.path.exists(fp):
                changed = process_file(fp, lang)
                print(f"{'MODIFIED' if changed else 'UNCHANGED'}: {fp}")

if __name__ == "__main__":
    main()
