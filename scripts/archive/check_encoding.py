import json

content = open('qr-menu/assets/js/menu-data.js', encoding='utf-8').read()
json_str = content.split('const menuData = ')[1].split(';\n\nwindow')[0]
data = json.loads(json_str)

# Check all items for encoding problems
issues = 0
for c in data:
    for item in c['items']:
        for key in ['nameTR', 'nameDE']:
            val = item.get(key, '')
            if '\u01ec' in val or '\u01cc' in val or '\ufffd' in val:
                issues += 1
                cat = c['categoryId']
                print(f'{cat}: {val[:60]}')
                break

print(f'Total issues found: {issues}')
