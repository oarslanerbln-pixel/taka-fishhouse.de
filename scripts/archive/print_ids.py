import json
import re

with open('qr-menu/assets/js/menu-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'const menuData = (\[[\s\S]*\]);', content)
if match:
    data = eval(match.group(1).replace('\n', '').replace('\r', ''))
    with open('output_ids.txt', 'w', encoding='utf-8') as out:
        for cat in data:
            for item in cat.get('items', []):
                name = item.get('nameTR', '').lower()
                if 'enginar' in name or 'zinnur' in name or 'sandviç' in name or 'dürüm' in name or 'ekmek' in name:
                    out.write(f"{item.get('id')} - {item.get('nameTR')} - {item.get('image')}\n")
