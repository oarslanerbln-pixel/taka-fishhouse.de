import json

MENU_JS = r'qr-menu\assets\js\menu-data.js'

content = open(MENU_JS, encoding='utf-8').read()
json_str = content.split('const menuData = ')[1].split(';\n\nwindow')[0]
data = json.loads(json_str)

# Show structure of hauptgerichte category - first 10 items
for c in data:
    if c['categoryId'] == 'hauptgerichte':
        print(f"hauptgerichte has {len(c['items'])} items")
        for item in c['items'][:15]:
            print(f"  id={item['id']} | {item.get('nameDE', '')[:60]} | {item.get('price', '')}")
        break
