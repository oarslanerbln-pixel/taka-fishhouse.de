import json
import re

# Read menu-data.js
with open(r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\js\menu-data.js", "r", encoding="utf-8") as f:
    content = f.read()

# Extract json
json_str = content[content.find('['):content.rfind(']')+1]
try:
    # Need to handle javascript object format without quotes around keys sometimes
    # Since it might be hard to parse raw js, let's just count items and check missing images
    items = []
    current_item = {}
    for line in json_str.split('\n'):
        if '"id":' in line:
            current_item = {"id": line.split(':')[1].strip().replace(',', '')}
        elif '"nameDE":' in line:
            current_item["nameDE"] = line.split(':')[1].strip().strip('",')
        elif '"image":' in line:
            current_item["image"] = line.split(':')[1].strip().strip('",')
        elif '},' in line or '}' in line:
            if current_item.get("id"):
                items.append(current_item)
                current_item = {}
    
    missing_images = []
    has_images = []
    for item in items:
        if "image" not in item or not item["image"] or "placeholder" in item["image"]:
            missing_images.append(item)
        else:
            has_images.append(item)
            
    print(f"Total items found: {len(items)}")
    print(f"Items with images: {len(has_images)}")
    print(f"Items missing images: {len(missing_images)}")
    
    print("\nMissing Images List:")
    for item in missing_images:
        print(f"ID: {item.get('id')} - {item.get('nameDE')}")

except Exception as e:
    print(f"Error parsing: {e}")

