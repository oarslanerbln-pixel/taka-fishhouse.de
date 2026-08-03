import json

MENU_JS = r'qr-menu\assets\js\menu-data.js'

content = open(MENU_JS, encoding='utf-8').read()
json_str = content.split('const menuData = ')[1].split(';\n\nwindow')[0]
data = json.loads(json_str)

# Show ALL categories and item counts
for c in data:
    print(f"\n=== {c['categoryId']} ({len(c['items'])} items) ===")
    for item in c['items']:
        print(f"  id={item['id']} | {item.get('nameDE', '')[:50]} | {item.get('price','')}")
