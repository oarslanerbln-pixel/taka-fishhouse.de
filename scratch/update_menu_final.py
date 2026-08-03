import json
import re
import shutil
import os

# 1. Copy image
brain_dir = r"C:\Users\oarsl\.gemini\antigravity-ide\brain\0ef7b752-cec1-4f33-8c81-3f6f4460c05e"
src_img = os.path.join(brain_dir, "taka_meze_vibrant_1783348454716.png")
dst_img = r"C:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\img\taka_meze_vibrant.png"

try:
    shutil.copy(src_img, dst_img)
    print("Image copied successfully.")
except Exception as e:
    print(f"Error copying image: {e}")

# 2. Update menu-data.js
file_path = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\js\menu-data.js"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

match = re.search(r"const menuData = (\[.*?\]);\s*window\.menuData", content, re.DOTALL)
if match:
    data_str = match.group(1)
    data = json.loads(data_str)
    
    for cat in data:
        new_items = []
        for item in cat.get('items', []):
            if item['id'] in [36, 37]:
                print(f"Removed item {item['id']}")
                continue # Remove Zinnur and Enginar
            
            if item['id'] == 10:
                print("Updating item 10")
                item['nameTR'] = "Karışık Meze Tabağı"
                item['nameDE'] = "Gemischter Vorspeisenteller"
                item['nameEN'] = "Mixed Appetizer Platter"
                item['nameES'] = "Plato de Aperitivos Mixtos"
                item['nameRU'] = "Смешанная Тарелка Закусок"
                item['nameAR'] = "مقبلات مشكلة"
                item['image'] = "assets/img/taka_meze_vibrant.png"
            
            new_items.append(item)
        
        cat['items'] = new_items

    # 3. Write back
    new_data_str = json.dumps(data, indent=4, ensure_ascii=False)
    # The original file has double quotes. Let's make sure it matches format
    final_content = f"const menuData = {new_data_str};\n\nwindow.menuData = menuData;\n"
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_content)
        
    print("Menu updated successfully.")
    
    # 4. Print Ana Yemekler
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    for cat in data:
        if cat['category'] == 'Ana Yemekler':
            print("\n--- ANA YEMEKLER SIRALAMASI ---")
            for idx, item in enumerate(cat['items']):
                print(f"{idx+1}. {item['nameTR']}")
