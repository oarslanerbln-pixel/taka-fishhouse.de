import sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
content = open('assets/js/menu-data.js', 'r', encoding='utf8').read()
json_str = content.replace('const menuData = ', '').split('window.menuData = menuData;')[0].strip()
if json_str.endswith(';'): json_str = json_str[:-1]

data = json.loads(json_str)
for cat in data:
    if cat['categoryId'] == 'desserts':
        for i in cat['items']:
            print(f"ID: {i.get('id')}, TR: {i.get('nameTR')}, DE: {i.get('nameDE')}, IMG: {bool(i.get('image'))}")
