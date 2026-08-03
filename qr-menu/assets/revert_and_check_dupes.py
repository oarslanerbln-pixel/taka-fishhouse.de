import re
import codecs
from collections import defaultdict

MENU_DATA_PATH = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\js\menu-data.js'

with codecs.open(MENU_DATA_PATH, 'r', 'utf-8') as f:
    content = f.read()

# 1. Revert placeholders
content = re.sub(r',\s*"image":\s*"assets/img/placeholder_cold_drink\.png"', '', content)
content = re.sub(r',\s*"image":\s*"assets/img/placeholder_hot_drink\.png"', '', content)

with codecs.open(MENU_DATA_PATH, 'w', 'utf-8') as f:
    f.write(content)

# 2. Check for duplicate images
item_blocks = re.findall(r'(\{\s*(?:[^{}]|\n)*?"nameDE":\s*"[^"]+"(?:[^{}]|\n)*?\})', content, re.DOTALL)

image_to_items = defaultdict(list)
for block in item_blocks:
    name_match = re.search(r'"nameDE":\s*"([^"]+)"', block)
    img_match = re.search(r'"image":\s*"([^"]+)"', block)
    
    if name_match and img_match:
        name = name_match.group(1)
        img = img_match.group(1)
        image_to_items[img].append(name)

print("DUPLICATE IMAGES DETECTED:")
found_dupes = False
for img, items in image_to_items.items():
    if len(items) > 1:
        found_dupes = True
        print(f"\nImage: {img} is used by {len(items)} items:")
        for i in items:
            print(f"  - {i}")

if not found_dupes:
    print("No duplicates found!")
