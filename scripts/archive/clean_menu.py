import json

MENU_JS = r'qr-menu\assets\js\menu-data.js'

content = open(MENU_JS, encoding='utf-8').read()
json_str = content.split('const menuData = ')[1].split(';\n\nwindow')[0]
data = json.loads(json_str)

# Clean up: remove items with price 0,00 or empty price from all categories
# These are Lieferando scrape artifacts that got into wrong categories
removed_total = 0
for c in data:
    original_count = len(c['items'])
    c['items'] = [
        item for item in c['items']
        if item.get('price', '0,00') not in ('0,00', '', '0.00')
    ]
    removed = original_count - len(c['items'])
    if removed > 0:
        print(f"Removed {removed} zero-price items from '{c['categoryId']}'")
    removed_total += removed

print(f"\nTotal removed: {removed_total}")
print("\nCategories after cleanup:")
for c in data:
    print(f"  {c['categoryId']}: {len(c['items'])} items")

# Write back
new_js = f"const menuData = {json.dumps(data, indent=4, ensure_ascii=False)};\n\nwindow.menuData = menuData;\n"
open(MENU_JS, 'w', encoding='utf-8').write(new_js)
print("\nDone! menu-data.js updated.")
