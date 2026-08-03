import json, codecs, re

content = codecs.open(r'assets\js\menu-data.js', 'r', 'utf-8').read()
match = re.search(r'const menuData = (\[.*?\]);', content, re.DOTALL)
data = json.loads(match.group(1))

def find_category(cid):
    for c in data:
        if c['categoryId'] == cid:
            return c
    return None

spezialitaten = find_category('spezialitaten')
tava = find_category('tava-guvecler')

def move_item(item, source_cat_id, target_cat):
    # Remove from all
    for c in data:
        c['items'] = [i for i in c['items'] if i['id'] != item['id']]
    # Add to target
    target_cat['items'].append(item)

# Let's iterate over a copy of all items to find ones that need moving
all_items = []
for c in data:
    for i in c['items']:
        all_items.append((i, c['categoryId']))

for item, cat_id in all_items:
    name = item.get('nameTR', '').lower()
    
    # 1. Taka Spesiyal items
    if 'spesiyal' in name or 'özel' in name:
        if cat_id != 'spezialitaten':
            move_item(item, cat_id, spezialitaten)
            continue
            
    # 2. Tava ve Güveçler items
    if 'tavası' in name or 'tava' in name or 'güveç' in name or 'kavurma' in name or 'buğulama' in name:
        # Exclude 'Hamsi Tava' if it's just plain fried fish? Or include it?
        # Physical menus usually keep basic fried fish in "Ana Yemekler" or "Balıklar". 
        # "Tava ve Güveçler" usually refers to shrimp pan (karides tava), etc.
        if 'hamsi' in name or 'istavrit' in name or 'mezgit' in name or 'barbun' in name or 'çipura' in name or 'levrek' in name:
            pass # Keep in Ana Yemekler or whatever
        elif cat_id != 'tava-guvecler':
            move_item(item, cat_id, tava)
            continue

js_out = f'const menuData = {json.dumps(data, indent=4, ensure_ascii=False)};\n\nwindow.menuData = menuData;\n'
with codecs.open(r'assets\js\menu-data.js', 'w', 'utf-8') as f:
    f.write(js_out)

print("Reorganized menu successfully.")
