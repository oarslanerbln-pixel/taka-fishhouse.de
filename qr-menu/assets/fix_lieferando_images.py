# -*- coding: utf-8 -*-
"""
Manual fix script:
1. Correct bad matches from previous run
2. Add manual mappings for items we know match
3. Re-download + update menu-data.js
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

import json, re, os, urllib.request, unicodedata

BASE_DIR = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu'
NEXT_DATA = os.path.join(BASE_DIR, 'lieferando_next_data.json')
MENU_JS   = os.path.join(BASE_DIR, r'assets\js\menu-data.js')
IMG_DIR   = os.path.join(BASE_DIR, r'assets\lieferando_imgs')
IMG_SIZE  = 'w_600,h_400'

os.makedirs(IMG_DIR, exist_ok=True)

# Load Lieferando items
with open(NEXT_DATA, 'r', encoding='utf-8') as f:
    data = json.load(f)

raw_items = data['props']['appProps']['preloadedState']['menu']['restaurant']['cdn']['items']

lieferando = {}
for item_id, item in raw_items.items():
    name = item.get('name', '').strip()
    sources = item.get('imageSources', [])
    if name and sources:
        template = sources[0].get('path', '')
        url = template.replace('{transformations}', IMG_SIZE)
        # Use first occurrence (avoid duplicates)
        if name not in lieferando:
            lieferando[name] = url

# ─── MANUAL MAPPING: menu-data.js nameDE  ->  Lieferando name ─────────────────
# Only entries that need correction or were missed by fuzzy match
MANUAL_MAP = {
    # Main dishes
    'Dorade (gegrillt oder gebraten)':           'Dorade Teller',
    'Wolfsbarsch (gegrillt oder gebraten)':      'Wolfsbarsch Teller',
    'Makrele':                                   'Makrele Teller',       # was wrongly matched to Dürüm Makrelen
    'Forelle':                                   'Forelle Teller',
    'Hamsi – gebraten':                          None,                   # No Lieferando image available
    'Rotbarbe':                                  None,
    'Lachsfilet':                                'Lachs Teller',
    'Hausgemachte panierte Kalamaresringe':      'Kalamar Teller',
    'Garnelenpfanne in Butter':                  'Garnelen Pfanne',
    'Garnelenpfanne in Tomatensoße, scharf':     'Garnelen Pfanne',
    'Garnelenpfanne TAKA Spezial':               'Großgarnelen Pfanne',
    'Gegrillter Octopus':                        None,
    'Seezunge':                                  None,
    'Gemischter Taka Spezial Teller':            'Taka Spezial Teller',
    'Meeresfrüchte Taka Spezial':                'Taka Spezial Teller',
    'Bratkartoffel Taka Spezial':                'Bratkartoffeln',        # was wrongly matched to Taka Spezial Teller
    'TAKA Spezial Vorspeisenteller':             'Taka Spezial Teller',

    # Starters / meze
    'Humus':                                     None,
    'Wolfsbarsch Marin':                         None,
    'Meeresfrüchte':                             None,
    'Tarator – Joghurt, Möhren':                 None,
    'Scharfes Paprikapüree':                     None,
    'Şakşuka':                                   None,
    'Kretische Käsepaste':                       None,
    'Geröstete Aubergine, Paprika, Joghurt mit Knoblauch': None,
    'Oktopussalat':                              None,
    'Grüner Salat mit Granatapfel, Petersilie, Frühlingszwiebel': None,
    'Urla Meze':                                 None,
    'Aubergine mit Joghurt':                     None,
    'Kuru Cacik (traditioneller türkischer Joghurt Gurken-Dip)': None,
    'Rote Beete mit Joghurt und Knoblauch':      None,
    'Seespargel':                                None,
    'Überbackener Garnelenauflauf':              'Großgarnelen Pfanne',
    'Gegrillte Jumbo Garnelen (3 Stück)':        'Großgarnelen Teller',
    'Oktopus mit Pastırma':                      None,
    'Fisch auf Augerberginenpüreebett':          None,
    'Geschnetzelte Fischpfanne':                 None,
    'Gegrillte Champions mit Käse überbacken':   'Broccoli',
    'Überbackene Brokkoli':                      'Broccoli',
    'Humus mit Pastırma':                        None,
    'Pommes frites':                             'Bratkartoffeln',

    # Sandwiches / Dürüm
    'Sardine Sandwich':                          'Sardinen Sandwich',
    'Garnele Sandwich':                          'Garnelen Sandwich',
    'Dorade Dürüm':                              'Dürüm Doraden',
    'Makrele Dürüm':                             'Dürüm Makrelen',
    'Sardine Dürüm':                             'Dürüm Sardinen',
    'Garnele Dürüm':                             'Dürüm Garnelen',
    'Lachs Dürüm':                               'Dürüm Lachs',

    # Soups / Salads
    'Lachssuppe':                                'Lachsuppe',
    'Ruccolasalat':                              'Gemischter Salat',
    'Lachssalat':                                'Gemischter Salat',
    'Garnelensalat':                             'Gemischter Salat',
    'Hamsisalat':                                'Gemischter Salat',
    'Gemischter grüner Salat':                   'Gemischter Salat',

    # Drinks - only correct false matches, skip Fritz Cola etc (no images on Lieferando)
    'Cola Zero 0,2l':                            'Coca-Cola Zero Sugar 0,2l (MEHRWEG)',
    'Fanta 0,2l':                                'Fanta Orange 0,2l (MEHRWEG)',
    'Sprite 0,2l':                               'Sprite 0,2l (MEHRWEG)',
    'Mezzo Mix 0,2l':                            'Mezzo Mix 0,2l (MEHRWEG)',
    'Coca Cola 0,2l':                            'Coca-Cola 0,2l (MEHRWEG)',
    # Fritz Cola → no Lieferando image, remove bad match
    'Fritz Cola Zero 0,2l':                      None,
    'Fritz Orange 0,2l':                         None,
    'Schweppes 0,2l':                            None,
}

print(f"Lieferando items available: {len(lieferando)}")
print("\nBuilding download list...")

def safe_filename(name):
    name = name.lower()
    name = re.sub(r'[^a-z0-9]+', '_', name)
    return name.strip('_') + '.jpg'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

download_map = {}  # nameDE -> local relative path

for de_name, lf_name in MANUAL_MAP.items():
    if lf_name is None:
        continue  # No image available; skip
    
    url = lieferando.get(lf_name)
    if not url:
        print(f"  WARNING: '{lf_name}' not found in Lieferando data")
        continue
    
    filename = safe_filename(lf_name)
    local_path = os.path.join(IMG_DIR, filename)
    rel_path = f'assets/lieferando_imgs/{filename}'
    
    if not os.path.exists(local_path):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as response:
                content = response.read()
            with open(local_path, 'wb') as f:
                f.write(content)
            size_kb = len(content) // 1024
            print(f"  DL ({size_kb}KB): {filename}")
        except Exception as e:
            print(f"  FAIL: {filename} → {e}")
            continue
    
    download_map[de_name] = rel_path

print(f"\nReady to update: {len(download_map)} mappings")

# Update menu-data.js
with open(MENU_JS, 'r', encoding='utf-8') as f:
    js_content = f.read()

def replace_image_for_de(content, de_name, image_path):
    pattern = r'("nameDE":\s*"' + re.escape(de_name) + r'".*?\})'
    def replacer(match):
        block = match.group(1)
        if '"image"' in block:
            return re.sub(r'"image":\s*"[^"]+"', f'"image": "{image_path}"', block)
        else:
            return block.replace(
                f'"nameDE": "{de_name}",',
                f'"nameDE": "{de_name}",\n                "image": "{image_path}",'
            )
    return re.sub(pattern, replacer, content, flags=re.DOTALL)

def remove_image_for_de(content, de_name):
    """Remove bad image assignments for items with no Lieferando match."""
    # We won't remove existing intentionally placed AI images, just skip
    return content

updated = js_content
update_count = 0

# Also handle None entries — revert to keeping existing images (do nothing)
for de_name, rel_path in download_map.items():
    new = replace_image_for_de(updated, de_name, rel_path)
    if new != updated:
        update_count += 1
    updated = new

with open(MENU_JS, 'w', encoding='utf-8') as f:
    f.write(updated)

print(f"Updated {update_count} image entries in menu-data.js")
print("\nFinal match summary:")
for de_name, lf_name in MANUAL_MAP.items():
    status = "→ " + download_map.get(de_name, '[kept existing]') if lf_name else '✗ no Lieferando image'
    print(f"  {de_name[:45]:45s}  {status}")

print("\nDONE!")
