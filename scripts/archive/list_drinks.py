import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('assets/js/menu-data.js', 'r', encoding='utf-8') as f:
    raw = f.read()

# Find getranke category block
idx = raw.find('"getranke"')
if idx == -1:
    print('getranke bulunamadi')
    exit()

# Get the items array for getranke
block = raw[idx:]
items_start = block.find('"items"')
items_block = block[items_start:]

# Extract individual items as objects
item_blocks = re.findall(r'\{[^{}]*\}', items_block[:50000])

print('=== ICECEKLER (Getranke) ===')
seen_names = {}
duplicates = []

for i, item in enumerate(item_blocks):
    name = re.search(r'"nameTR"\s*:\s*"([^"]+)"', item)
    image = re.search(r'"image"\s*:\s*"([^"]+)"', item)
    price = re.search(r'"price"\s*:\s*"([^"]+)"', item)
    id_ = re.search(r'"id"\s*:\s*(\d+)', item)
    
    if name:
        n = name.group(1)
        img = image.group(1) if image else 'NO_IMAGE'
        p = price.group(1) if price else '?'
        id_val = id_.group(1) if id_ else '?'
        
        marker = ''
        if n in seen_names:
            marker = '  <-- DUPLIKAT!'
            duplicates.append(n)
        seen_names[n] = True
        
        print(f'{i+1:2}. [{id_val}] {n:<38} {p:<12} {img[:50]}{marker}')

print(f'\nTOPLAM: {len(item_blocks)} icecek')
print(f'DUPLIKAT: {duplicates}')
