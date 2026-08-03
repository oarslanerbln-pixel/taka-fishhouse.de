import json
content = open(r'assets\js\menu-data.js', encoding='utf-8').read()
json_str = content.split('const menuData = ')[1].split(';\n')[0]
if 'window.menuData' in json_str: json_str = json_str.replace('window.menuData = menuData;', '')
data = json.loads(json_str)
for cat in data:
    if cat['categoryId'] == 'fisch-sandwich-durum':
        for item in cat['items']:
            print(f"{item['nameTR']} -> {item.get('image', 'NONE')}")
