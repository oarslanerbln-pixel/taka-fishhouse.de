import json
import re
import os
import urllib.request
import random

BASE_DIR = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu'
WOLT_IMAGES = os.path.join(BASE_DIR, r'assets\wolt_images.json')
WOLT_MAPPING = os.path.join(BASE_DIR, r'assets\wolt_item_mapping.json')
MENU_JS = os.path.join(BASE_DIR, r'assets\js\menu-data.js')
IMG_DIR = os.path.join(BASE_DIR, r'assets\wolt_imgs')

os.makedirs(IMG_DIR, exist_ok=True)

# Define known drinks and mapping to possible image keywords
drinks = {
    "Stilles Wasser 0,25l": ("3,00", "wasser"),
    "Mineralwasser mit Kohlensäure 0,25l": ("3,00", "mineral"),
    "Fritz Cola 0,2l": ("3,50", "fritz_kola"),
    "Fritz Cola Zero 0,2l": ("3,50", "superzero"),
    "Fritz Orange 0,2l": ("3,50", "orange__21"),
    "Christinen Apfelschorle 0,33l": ("3,50", "apfelschorle"),
    "7gün Ayran 0,25l": ("2,50", "ayran"),
    "Capri Sonne 0,2l": ("2,00", "capri"),
    "Çamlıca Gazoz 0,2l": ("3,00", "gazoz"),
    "Uludag Gazoz 0,25l": ("3,00", "uludag"),
    "Salgam (Rübensaft) 0,25l": ("3,00", "salgam"),
    "Tymbark 0,25l": ("3,00", "tymbark"),
    "FuzeTea Pfirsich 0,4l": ("4,00", "fuzetea"),
    "Christinen Multivitamin 0,33l": ("3,50", "multivitamin"),
    "Durstlöscher 0,5l": ("2,50", "durst"),
    "Türkischer Tee klein": ("2,00", "tee"),
    "Verschiedene Teesorten": ("3,00", "tee"),
    "Café Cream": ("3,50", "cafe"),
    "Cappuccino": ("4,00", "cappuccino"),
    "Café Latte": ("4,50", "latte"),
    "Espresso": ("2,50", "espresso"),
    "Türkischer Mokka": ("3,50", "mokka"),
    "Coca-Cola 0,2l": ("3,50", "cocacola_0_2"),
    "Coca-Cola Zero Sugar 0,2l": ("3,50", "cocacola_zero_0_2"),
    "Sprite 0,2l": ("3,50", "sprite_0_2"),
    "Fanta 0,2l": ("3,50", "fanta_0_2")
}

with open(WOLT_IMAGES, 'r', encoding='utf-8') as f:
    wolt_data = json.load(f)

img_urls = [img['src'] for img in wolt_data['imgs']]

# Match drinks to urls
drink_to_url = {}
for d_name, (d_price, keyword) in drinks.items():
    matched_url = ""
    for url in img_urls:
        if keyword in url.lower():
            matched_url = url
            break
    drink_to_url[d_name] = (d_price, matched_url)

with open(MENU_JS, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Make sure Getranke category exists, if not we will inject it
if '"categoryId": "getranke"' not in js_content:
    print("WARNING: getranke category not found in menu-data.js")
    # Actually it might be "getranke"
    
def safe_filename(name):
    name = name.lower()
    name = re.sub(r'[^a-z0-9]+', '_', name)
    return name.strip('_') + '.jpg'

new_entries = []
headers = {'User-Agent': 'Mozilla/5.0'}

nameDE_list = re.findall(r'"nameDE":\s*"([^"]+)"', js_content)
existing = {re.sub(r'[^a-z0-9]', '', n.lower()): n for n in nameDE_list}

for d_name, (d_price, url) in drink_to_url.items():
    norm_name = re.sub(r'[^a-z0-9]', '', d_name.lower())
    if norm_name in existing:
        continue # Already there

    rel_path = ""
    if url:
        filename = safe_filename(d_name)
        local_path = os.path.join(IMG_DIR, filename)
        rel_path = f'assets/wolt_imgs/{filename}'
        if not os.path.exists(local_path):
            try:
                req = urllib.request.Request(url, headers=headers)
                with urllib.request.urlopen(req, timeout=15) as response:
                    content = response.read()
                with open(local_path, 'wb') as f:
                    f.write(content)
                print(f"Downloaded: {filename}")
            except Exception as e:
                print(f"Failed to download {filename}: {e}")
                rel_path = ""
                
    new_id = random.randint(2000, 9999)
    img_line = f',\n                "image": "{rel_path}"' if rel_path else ''
    
    entry = f"""            {{
                "id": {new_id},
                "nameTR": "{d_name}",
                "nameDE": "{d_name}",
                "nameEN": "{d_name}",
                "nameRU": "{d_name}",
                "nameES": "{d_name}",
                "nameAR": "{d_name}",
                "price": "{d_price}"{img_line}
            }}"""
    new_entries.append(entry)

if new_entries:
    # Inject into getranke category
    pattern = r'("categoryId":\s*"getranke".*?"items":\s*\[)'
    if re.search(pattern, js_content, flags=re.DOTALL):
        joined_entries = ",\n".join(new_entries)
        js_content = re.sub(pattern, r'\1\n' + joined_entries + ',', js_content, flags=re.DOTALL)
        with open(MENU_JS, 'w', encoding='utf-8') as f:
            f.write(js_content)
        print(f"Added {len(new_entries)} drinks to menu-data.js")
    else:
        print("Could not find getranke category block to inject")
else:
    print("No new drinks to add.")
