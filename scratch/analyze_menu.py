import json, codecs, re

content = codecs.open(r'assets\js\menu-data.js', 'r', 'utf-8').read()
match = re.search(r'const menuData = (\[.*?\]);', content, re.DOTALL)
data = json.loads(match.group(1))

with open('scratch/menu_analysis.txt', 'w', encoding='utf-8') as f:
    for cat in data:
        f.write(f"\n[{cat['categoryId']}] {cat['categoryTR']} ({len(cat['items'])} items):\n")
        for item in cat['items']:
            f.write(f"  - {item.get('nameTR', 'No Name')}\n")
