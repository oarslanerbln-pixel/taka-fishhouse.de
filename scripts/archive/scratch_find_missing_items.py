import json
import re

BASE_DIR = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu'
NEXT_DATA = BASE_DIR + r'\lieferando_next_data.json'
MENU_JS   = BASE_DIR + r'\assets\js\menu-data.js'

with open(NEXT_DATA, 'r', encoding='utf-8') as f:
    data = json.load(f)

raw_items = data['props']['appProps']['preloadedState']['menu']['restaurant']['cdn']['items']

lieferando_items = []
drinks = 0
for item_id, item in raw_items.items():
    name = item.get('name', '').strip()
    desc = item.get('description', '')
    price = item.get('price', 0) / 100
    category = item.get('categoryName', '')
    sources = item.get('imageSources', [])
    image_url = sources[0].get('path', '') if sources else ''
    
    lieferando_items.append({
        'name': name,
        'price': price,
        'image': image_url,
        'id': item_id,
        'category': category
    })
    if 'getränke' in category.lower() or 'drink' in category.lower():
        drinks += 1

print(f"Total Lieferando items: {len(lieferando_items)}")
print(f"Drinks (approx): {drinks}")
print(f"Non-drinks: {len(lieferando_items) - drinks}")

with open(MENU_JS, 'r', encoding='utf-8') as f:
    js_content = f.read()

nameDE_list = re.findall(r'"nameDE":\s*"([^"]+)"', js_content)
print(f"Total items in menu-data.js: {len(nameDE_list)}")

# Normalize helper
def normalize(s):
    s = s.lower().strip()
    return re.sub(r'[^a-z0-9]', '', s)

menu_js_names_normalized = set(normalize(n) for n in nameDE_list)

missing_from_js = []
for item in lieferando_items:
    l_name_norm = normalize(item['name'])
    
    # Try fuzzy substring
    found = False
    for mj in menu_js_names_normalized:
        if l_name_norm in mj or mj in l_name_norm:
            found = True
            break
            
    if not found:
        missing_from_js.append(item)

print(f"Missing from menu-data.js (approx): {len(missing_from_js)}")
print("Sample missing items:")
for m in missing_from_js[:30]:
    print(f" - {m['name']} ({m['price']}€) [Img: {'Yes' if m['image'] else 'No'}]")
