import sys
import json
import re
import os
import urllib.request
import urllib.error

BASE_DIR = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu'
NEXT_DATA = os.path.join(BASE_DIR, 'lieferando_next_data.json')
MENU_JS = os.path.join(BASE_DIR, r'assets\js\menu-data.js')
IMG_DIR = os.path.join(BASE_DIR, r'assets\lieferando_imgs')
IMG_SIZE = 'w_600,h_400'

os.makedirs(IMG_DIR, exist_ok=True)

with open(NEXT_DATA, 'r', encoding='utf-8') as f:
    data = json.load(f)

raw_items = data['props']['appProps']['preloadedState']['menu']['restaurant']['cdn']['items']

lieferando_items = []
for item_id, item in raw_items.items():
    name = item.get('name', '').strip()
    price = item.get('price', 0) / 100
    category_name = item.get('categoryName', '')
    desc = item.get('description', '')
    sources = item.get('imageSources', [])
    image_url = sources[0].get('path', '').replace('{transformations}', IMG_SIZE) if sources else ''
    
    lieferando_items.append({
        'id': item_id,
        'name': name,
        'price': f"{price:.2f}".replace('.', ','),
        'image': image_url,
        'category': category_name,
        'desc': desc
    })

with open(MENU_JS, 'r', encoding='utf-8') as f:
    js_content = f.read()

nameDE_list = re.findall(r'"nameDE":\s*"([^"]+)"', js_content)

def normalize(s):
    s = s.lower().strip()
    return re.sub(r'[^a-z0-9]', '', s)

menu_js_names_normalized = {normalize(n): n for n in nameDE_list}

missing_from_js = []
for item in lieferando_items:
    l_name_norm = normalize(item['name'])
    found = False
    for mj in menu_js_names_normalized:
        if l_name_norm in mj or mj in l_name_norm:
            found = True
            break
    if not found:
        missing_from_js.append(item)

print(f"Total Lieferando items: {len(lieferando_items)}")
print(f"Missing from menu-data.js: {len(missing_from_js)}")

def safe_filename(name):
    name = name.lower()
    name = re.sub(r'[^a-z0-9]+', '_', name)
    return name.strip('_') + '.jpg'

headers = {'User-Agent': 'Mozilla/5.0'}

new_entries = []
import random

def cat_to_id(lf_cat):
    lf_cat = lf_cat.lower()
    if 'getränk' in lf_cat or 'drink' in lf_cat:
        return 'getranke'
    elif 'salat' in lf_cat or 'supp' in lf_cat:
        return 'suppen-salate'
    elif 'vorspeise' in lf_cat:
        return 'kalte-vorspeisen'
    elif 'sandwich' in lf_cat or 'dürüm' in lf_cat or 'wrap' in lf_cat:
        return 'fisch-sandwich-durum'
    elif 'dessert' in lf_cat or 'nachtisch' in lf_cat or 'eis' in lf_cat:
        return 'desserts'
    else:
        return 'hauptgerichte'

for item in missing_from_js:
    # 1. Download image
    local_path = ""
    rel_path = ""
    if item['image']:
        filename = safe_filename(item['name'])
        local_path = os.path.join(IMG_DIR, filename)
        rel_path = f'assets/lieferando_imgs/{filename}'
        if not os.path.exists(local_path):
            try:
                req = urllib.request.Request(item['image'], headers=headers)
                with urllib.request.urlopen(req, timeout=15) as response:
                    content = response.read()
                with open(local_path, 'wb') as f:
                    f.write(content)
                print(f"Downloaded: {filename}")
            except Exception as e:
                print(f"Failed to download {filename}: {e}")
                rel_path = ""
        else:
            rel_path = f'assets/lieferando_imgs/{filename}'
    
    # Generate ID
    new_id = random.randint(1000, 9999)
    
    # Prepare entry block
    img_line = f',\n                "image": "{rel_path}"' if rel_path else ''
    
    entry = f"""            {{
                "id": {new_id},
                "nameTR": "{item['name']}",
                "nameDE": "{item['name']}",
                "nameEN": "{item['name']}",
                "nameRU": "{item['name']}",
                "nameES": "{item['name']}",
                "nameAR": "{item['name']}",
                "price": "{item['price']}"{img_line}
            }}"""
    
    cat_id = cat_to_id(item['category'])
    new_entries.append((cat_id, entry))

# Inject into menu-data.js
for cat_id, entry_block in new_entries:
    # Find category array
    pattern = r'("categoryId":\s*"' + cat_id + r'".*?"items":\s*\[)'
    js_content = re.sub(pattern, r'\1\n' + entry_block + ',', js_content, flags=re.DOTALL)

with open(MENU_JS, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Added {len(new_entries)} items to menu-data.js")
