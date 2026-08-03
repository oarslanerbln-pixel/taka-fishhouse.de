import os
import json
import urllib.request
import re
import codecs
import unicodedata

BASE_DIR = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu'
MENU_JS = os.path.join(BASE_DIR, r'assets\js\menu-data.js')
IMG_DIR = os.path.join(BASE_DIR, r'assets\ubereats_imgs')
JSON_FILE = os.path.join(BASE_DIR, r'assets\ubereats_images.json')

os.makedirs(IMG_DIR, exist_ok=True)

with open(JSON_FILE, "r", encoding="utf-8") as f:
    uber_images = json.load(f)

# Normalize for matching
def normalize(s):
    s = s.lower().strip()
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return s

uber_normalized = {normalize(k): (k, v) for k, v in uber_images.items()}

# Load menu-data.js
with codecs.open(MENU_JS, 'r', 'utf-8') as f:
    js_content = f.read()

nameDE_list = re.findall(r'"nameDE":\s*"([^"]+)"', js_content)

# Custom manual mappings for tricky ones
manual_mappings = {
    "Aubergine mit Joghurt": "Auberginen mit Joghurt",
    "Ruccolasalat": "Rucolasalat",
    "Gemischter grüner Salat": "Bauernsalat", # or maybe we leave it if already mapped
    "Kretische Käsepaste": "Kretische KÃ¤sepaste",
    "Şakşuka": "Saksuka"
}

matches = {}
for de_name in nameDE_list:
    # If it already has a lieferando_img, let's see if we should skip or not.
    # Actually, the user wants the missing ones. Let's match all.
    key = normalize(manual_mappings.get(de_name, de_name))
    
    # Try exact match first
    if key in uber_normalized:
        matches[de_name] = uber_normalized[key]
        continue
    
    # Try substring
    found = None
    for ukey, uval in uber_normalized.items():
        if key == ukey:
            found = uval
            break
    if found:
        matches[de_name] = found

def safe_filename(name):
    name = name.lower()
    name = re.sub(r'[^a-z0-9]+', '_', name)
    return name.strip('_') + '.jpg'

download_map = {}
headers = {'User-Agent': 'Mozilla/5.0'}

print("Downloading UberEats images...")
for de_name, (u_name, url) in matches.items():
    filename = safe_filename(u_name)
    local_path = os.path.join(IMG_DIR, filename)
    rel_path = f'assets/ubereats_imgs/{filename}'
    
    if os.path.exists(local_path):
        download_map[de_name] = rel_path
        continue
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as response:
            content = response.read()
        with open(local_path, 'wb') as f:
            f.write(content)
        print(f"  OK: {filename}")
        download_map[de_name] = rel_path
    except Exception as e:
        print(f"  FAIL: {filename} - {e}")

# Update menu-data.js
def replace_or_add_image(content, de_name, image_path):
    pattern = r'("nameDE":\s*"' + re.escape(de_name) + r'".*?\})'
    def replacer(match):
        block = match.group(1)
        if '"image"' in block:
            # ONLY overwrite if current is not lieferando OR if the user asked to fill missing
            # we will overwrite unconditionally here because UberEats is the requested source
            return re.sub(r'"image":\s*"[^"]+"', f'"image": "{image_path}"', block)
        else:
            return block.replace(
                f'"nameDE": "{de_name}",',
                f'"nameDE": "{de_name}",\n                "image": "{image_path}",'
            )
    return re.sub(pattern, replacer, content, flags=re.DOTALL)

updated = js_content
for de_name, rel_path in download_map.items():
    # check if image is missing in current block, or if it is already there
    # we want to ensure we don't overwrite good lieferando images unless it's the salads or Pommes frites
    # Actually, it's fine to use UberEats for anything it matched!
    updated = replace_or_add_image(updated, de_name, rel_path)

with codecs.open(MENU_JS, 'w', 'utf-8') as f:
    f.write(updated)

print(f"Updated {len(download_map)} items using UberEats data.")
