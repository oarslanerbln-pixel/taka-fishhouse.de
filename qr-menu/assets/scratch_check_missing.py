import json
import re

js = open('qr-menu/assets/js/menu-data.js', encoding='utf-8').read()
names = re.findall(r'"nameDE"\s*:\s*"([^"]+)"', js)
names_lower = [n.lower() for n in names]

mapping = json.load(open('qr-menu/assets/wolt_item_mapping.json', encoding='utf-8'))
missing = mapping.get('unmatched', [])

not_in_js = []
for m in missing:
    if m.lower() not in names_lower:
        # Check partial match
        found = any(m.lower() in n or n in m.lower() for n in names_lower)
        if not found:
            not_in_js.append(m)

print(f"Total in JS: {len(names)}")
print(f"Total in unmatched list: {len(missing)}")
print(f"Not in JS: {len(not_in_js)}")
for m in not_in_js:
    print(f" - {m}")
