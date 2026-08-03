import json
import re

with open('lieferando_nextdata.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# The menu items are in data['props']['appProps']['preloadedState']['menu']['restaurant']['menu']['items']
try:
    items_lief = data['props']['appProps']['preloadedState']['menu']['restaurant']['menu']['items']
except KeyError:
    items_lief = {}

print(f'Total extracted Lieferando items: {len(items_lief)}')

with open('qr-menu/assets/js/menu-data.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

names_in_js = re.findall(r'"nameDE"\s*:\s*"([^"]+)"', js_content)
names_in_js_lower = [n.strip().lower() for n in names_in_js]

missing = []
for k, item in items_lief.items():
    name = item.get('name', '').strip()
    price = item.get('price', 0) / 100
    img = item.get('imageUrl', '')
    if name.lower() not in names_in_js_lower:
        found = any(name.lower() in n or n in name.lower() for n in names_in_js_lower)
        if not found:
            missing.append((name, price, img))

print(f'Missing from JS ({len(missing)}):')
for m in missing:
    print(f' - {m[0]} (Price: {m[1]} EUR) [Image: {bool(m[2])}]')
