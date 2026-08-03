# -*- coding: utf-8 -*-
"""
PLAN:
1. Load lieferando_next_data.json → extract {name: image_url} map
2. Load menu-data.js → find all nameDE values
3. Match nameDE to lieferando name (fuzzy, case-insensitive)
4. Download matched images to assets/lieferando_imgs/
5. Update menu-data.js with new image paths

Token efficient: do it all in one script.
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

import json
import re
import os
import urllib.request
import unicodedata

# ─── CONFIG ───────────────────────────────────────────────────────────────────
BASE_DIR = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu'
NEXT_DATA = os.path.join(BASE_DIR, 'lieferando_next_data.json')
MENU_JS   = os.path.join(BASE_DIR, r'assets\js\menu-data.js')
IMG_DIR   = os.path.join(BASE_DIR, r'assets\lieferando_imgs')
IMG_SIZE  = 'w_600,h_400'   # Cloudinary transformation for download

os.makedirs(IMG_DIR, exist_ok=True)

# ─── 1. LOAD LIEFERANDO ITEMS ─────────────────────────────────────────────────
with open(NEXT_DATA, 'r', encoding='utf-8') as f:
    data = json.load(f)

raw_items = data['props']['appProps']['preloadedState']['menu']['restaurant']['cdn']['items']

lieferando = {}
for item_id, item in raw_items.items():
    name = item.get('name', '').strip()
    sources = item.get('imageSources', [])
    if name and sources:
        template = sources[0].get('path', '')
        # Replace {transformations} with actual size
        url = template.replace('{transformations}', IMG_SIZE)
        lieferando[name] = url

print(f"Lieferando items with images: {len(lieferando)}")
for n, u in list(lieferando.items())[:5]:
    print(f"  {n!r}: {u[:80]}...")

# ─── 2. LOAD menu-data.js & EXTRACT nameDE values ─────────────────────────────
with open(MENU_JS, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Pattern to capture nameDE
nameDE_list = re.findall(r'"nameDE":\s*"([^"]+)"', js_content)
print(f"\nmenu-data.js nameDE entries: {len(nameDE_list)}")

# ─── 3. FUZZY MATCH ───────────────────────────────────────────────────────────
def normalize(s):
    # lowercase, remove accents, collapse spaces
    s = s.lower().strip()
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return s

lief_normalized = {normalize(k): (k, v) for k, v in lieferando.items()}

matches = {}     # nameDE -> (lieferando_name, url)
no_match = []    # nameDE entries we couldn't match

# Build word sets for smarter matching
lieferando_words = {}
for lkey, (lname, lurl) in lief_normalized.items():
    words = set(re.split(r'[\s,()]+', lkey)) - {''}
    lieferando_words[lkey] = (words, lname, lurl)

for de_name in nameDE_list:
    key = normalize(de_name)
    de_words = set(re.split(r'[\s,()]+', key)) - {''}
    # Remove common filler words that don't discriminate
    stop = {'oder', 'und', 'der', 'die', 'das', 'in', 'mit', 'gegrillt',
            'gebraten', 'scharf', 'mehrweg', 'teller', 'pfanne'}
    de_core = de_words - stop
    
    # Try exact
    if key in lief_normalized:
        matches[de_name] = lief_normalized[key]
        continue
    
    # Try substring containment
    found = None
    for lkey, (lname, lurl) in lief_normalized.items():
        if key in lkey or lkey in key:
            found = (lname, lurl)
            break
    if found:
        matches[de_name] = found
        continue

    # Try word overlap: if de_core words mostly appear in lieferando name
    best_score = 0
    best_match = None
    for lkey, (lwords, lname, lurl) in lieferando_words.items():
        lcore = lwords - stop
        if not de_core or not lcore:
            continue
        common = de_core & lcore
        # score = how many de_core words matched / total de_core words
        score = len(common) / len(de_core)
        if score > best_score and score >= 0.6:
            best_score = score
            best_match = (lname, lurl)
    
    if best_match:
        matches[de_name] = best_match
    else:
        no_match.append(de_name)

print(f"\nMatched: {len(matches)}")
print(f"No match: {len(no_match)}")
print("\nMatched pairs:")
for de, (lf, url) in matches.items():
    print(f"  DE: {de!r:40s} <- Lieferando: {lf!r}")
if no_match:
    print("\nNo match found for:")
    for n in no_match:
        print(f"  {n!r}")

# ─── 4. DOWNLOAD IMAGES ───────────────────────────────────────────────────────
def safe_filename(name):
    name = name.lower()
    name = re.sub(r'[^a-z0-9]+', '_', name)
    return name.strip('_') + '.jpg'

print("\nDownloading images...")
download_map = {}  # nameDE -> local relative path

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

for de_name, (lf_name, url) in matches.items():
    filename = safe_filename(lf_name)
    local_path = os.path.join(IMG_DIR, filename)
    rel_path = f'assets/lieferando_imgs/{filename}'
    
    if os.path.exists(local_path):
        print(f"  SKIP (exists): {filename}")
        download_map[de_name] = rel_path
        continue
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as response:
            content = response.read()
        with open(local_path, 'wb') as f:
            f.write(content)
        size_kb = len(content) // 1024
        print(f"  OK ({size_kb}KB): {filename}")
        download_map[de_name] = rel_path
    except Exception as e:
        print(f"  FAIL: {filename} - {e}")

print(f"\nDownloaded: {len(download_map)} images")

# ─── 5. UPDATE menu-data.js ───────────────────────────────────────────────────
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

updated_content = js_content
update_count = 0
for de_name, rel_path in download_map.items():
    new_content = replace_image_for_de(updated_content, de_name, rel_path)
    if new_content != updated_content:
        update_count += 1
    updated_content = new_content

with open(MENU_JS, 'w', encoding='utf-8') as f:
    f.write(updated_content)

print(f"\nUpdated {update_count} image paths in menu-data.js")
print("DONE!")
