import re
import json

data_path = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\js\menu-data.js"

with open(data_path, "r", encoding="utf-8") as f:
    content = f.read()

# Extract JSON from menuData variable
json_str = content.split("const menuData = ")[1].rsplit("];", 1)[0] + "]"

try:
    menu = json.loads(json_str)
except Exception as e:
    print("Error parsing json:", e)
    # try evaluating somehow
    exit(1)

# 1. Check for 'Kızarmış Dondurma'
count_dondurma = 0
for cat in menu:
    for item in cat.get("items", []):
        name = item.get("nameTR", "").lower()
        if "kızarmış dondurma" in name or "kizarmis" in name:
            count_dondurma += 1
            print(f"Found '{item.get('nameTR')}' in category '{cat.get('categoryId')}' (ID: {item.get('id')})")

print(f"Total Kızarmış Dondurma found: {count_dondurma}")

# 2. Check all categories
print("\n--- Categories in menu-data.js ---")
for cat in menu:
    print(f"ID: {cat.get('categoryId')} | TR: {cat.get('categoryTR')} | DE: {cat.get('categoryDE')}")

# 3. Path fixing preview
print("\n--- Image Path Issues Preview ---")
missing_count = 0
for cat in menu:
    for item in cat.get("items", []):
        img = item.get("image", "")
        if img and not img.startswith("http") and not img.startswith("assets/img/products/"):
            # Preview how we could fix it
            if "lieferando_imgs" in img:
                new_img = img.replace("assets/lieferando_imgs/", "assets/img/products/lieferando_imgs/")
            elif "ubereats_imgs" in img:
                new_img = img.replace("assets/ubereats_imgs/", "assets/img/products/ubereats_imgs/")
            elif "wolt_imgs" in img:
                new_img = img.replace("assets/wolt_imgs/", "assets/img/products/wolt_imgs/")
            elif "drinks" in img:
                new_img = img.replace("assets/drinks/", "assets/img/products/")
            else:
                new_img = img.replace("assets/", "assets/img/products/")
            print(f"Will change: {img} -> {new_img}")
            missing_count += 1
print(f"Total paths to fix: {missing_count}")
