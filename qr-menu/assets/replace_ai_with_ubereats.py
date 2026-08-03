import os
import json
import urllib.request
import re
import codecs
import unicodedata

BASE_DIR = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu'
MENU_JS = os.path.join(BASE_DIR, r'assets\js\menu-data.js')
IMG_DIR = os.path.join(BASE_DIR, r'assets\ubereats_imgs')
os.makedirs(IMG_DIR, exist_ok=True)

url = "https://www.ubereats.com/de/store/taka-restaurant/LFSSR2wyU9ylHG_P4cVDaQ?diningMode=PICKUP"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept-Language": "en-US,en;q=0.9,de;q=0.8"
}

print("Fetching UberEats page...")
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as response:
    html = response.read().decode('utf-8')

pattern = r'\\u0022imageUrl\\u0022:\\u0022(.*?)\\u0022.*?\\u0022title\\u0022:\\u0022(.*?)\\u0022'
matches = re.findall(pattern, html)

uber_images = {}
for img, title in matches:
    try:
        title_decoded = title.encode('utf-8').decode('unicode_escape')
        img_decoded = img.encode('utf-8').decode('unicode_escape')
        uber_images[title_decoded] = img_decoded
    except:
        pass

manual_mappings = {
    "Tarator": "Tarator",
    "Acılı Ezme": "Scharfes PaprikapÃ¼ree",
    "Humus": "Hummus",
    "Köpoğlu": "KÃ¶poglu",
    "Narlı Dilberiye": "Narli Dilberiye",
    "Oktopus Salat": "Gegrillter Oktopus", # Wait, DE name for ahtapot salatasi
    "Oktopus mit Speck": "Oktopus mit Speck",
    "Fisch auf Auberginenpüreebett": "Fisch Auf AuberginenpÃ¼reebett",
    "Hummus mit Speck": "Hummus mit Speck",
    "Warmer Grieß - Halva mit Eis": "Warmer GrieÃŸ â€“ Halva mit Eis",
    "Gebackener „Kneipen“ Halva": "Gebackener â€žKneipenâ€\x9d Halva",
    "Fava": "Fava",
    "Apfelportulak": "Apfelportulak",
    "Immun Elixier": "Immun Elixier",
    "Überbackener Garnelenauflauf": "Ãœberbackener Garnelenauflauf",
    "Gegrillte Jumbo Garnelen": "Gegrillte Jumbo Garnelen",
    "Gegrillte Champignons": "Gegrillte Champignons",
    "Überbackener Brokkoli": "Ãœberbackener Brokkoli",
    "Gebratenes eingelegtes Gemüse": "Gebratenes Eingelegtes GemÃ¼se",
    "Hamsi auf Zwiebelbett": "Hamsi Auf Zwiebelbett",
    "Hausgemachte panierte Kalamarsringe": "Hausgemachte Panierte Kalamarsringe",
    "Gemischter Taka Spezial-Teller": "Gemischter Taka Spezial-Teller",
    "Garnelenpfanne in Tomatensoße": "Garnelenpfanne in TomatensoÃŸe",
    "Gegrillter Oktopus": "Gegrillter Oktopus",
    "Fischauflauf": "Fischauflauf",
    "Nudeln mit Lachsfilet": "Nudeln mit Lachsfilet",
    "Nudeln mit Garnelen": "Nudeln mit Garnelen",
}

def safe_filename(name):
    name = name.lower()
    name = re.sub(r'[^a-z0-9]+', '_', name)
    return name.strip('_') + '.jpg'

download_map = {}

def get_url_for_mapped_title(mapped_title):
    for ukey, uval in uber_images.items():
        if mapped_title == ukey: return uval
    for ukey, uval in uber_images.items():
        clean_mapped = re.sub(r'[^a-zA-Z]', '', mapped_title).lower()
        clean_ukey = re.sub(r'[^a-zA-Z]', '', ukey).lower()
        if clean_mapped and clean_mapped in clean_ukey or clean_ukey in clean_mapped:
            return uval
    return None

print("Downloading new images...")
for de_name, uber_title in manual_mappings.items():
    url = get_url_for_mapped_title(uber_title)
    if not url: continue
    filename = safe_filename(uber_title)
    local_path = os.path.join(IMG_DIR, filename)
    rel_path = f'assets/ubereats_imgs/{filename}'
    if os.path.exists(local_path):
        download_map[de_name] = rel_path
        continue
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as response:
            with open(local_path, 'wb') as f:
                f.write(response.read())
        download_map[de_name] = rel_path
        print(f"  OK: {filename}")
    except:
        pass

with codecs.open(MENU_JS, 'r', 'utf-8') as f:
    js_content = f.read()

def replace_or_add_image(content, de_name, image_path):
    def replacer_fuzzy(match):
        block = match.group(1)
        block_de = re.search(r'"nameDE":\s*"([^"]+)"', block).group(1)
        
        # We also want to replace AI images (anything not containing 'ubereats' or 'lieferando')
        if re.sub(r'[^a-zA-Z]', '', block_de.lower()) == re.sub(r'[^a-zA-Z]', '', de_name.lower()):
            # check if current image is an AI image (e.g. ends with _ai.png or just has a custom name)
            if '"image"' in block:
                curr_img = re.search(r'"image":\s*"([^"]+)"', block).group(1)
                # We always overwrite because the user wants UberEats originals over AI ones!
                return re.sub(r'"image":\s*"[^"]+"', f'"image": "{image_path}"', block)
            else:
                return block.replace(
                    f'"nameDE": "{block_de}",',
                    f'"nameDE": "{block_de}",\n                "image": "{image_path}",'
                )
        return block
    
    new_content = re.sub(r'("nameDE":\s*"[^"]+".*?\})', replacer_fuzzy, content, flags=re.DOTALL)
    return new_content

updated = js_content
for de_name, rel_path in download_map.items():
    updated = replace_or_add_image(updated, de_name, rel_path)

with codecs.open(MENU_JS, 'w', 'utf-8') as f:
    f.write(updated)

print(f"Updated {len(download_map)} items using UberEats data.")
