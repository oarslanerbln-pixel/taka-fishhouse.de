import os
import shutil
import json
import codecs
import re

brain_dir = r"C:\Users\oarsl\.gemini\antigravity-ide\brain\0ef7b752-cec1-4f33-8c81-3f6f4460c05e"
root_dir = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus"
img_dir = os.path.join(root_dir, "assets", "img")

# Define copies
copies = [
    ("media__1783423472954.jpg", "karisik_meze_tabagi_user.jpg"),
    ("media__1783423479754.jpg", "deniz_mahsulleri_soguk_user.jpg"),
    ("kizarmis_dondurma_tek_top_1783419644203.png", "kizarmis_dondurma.png")
]

for src, dst in copies:
    src_path = os.path.join(brain_dir, src)
    dst_path = os.path.join(img_dir, dst)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
    else:
        print(f"File not found: {src_path}")

# Now update menu-data.js
menu_file = os.path.join(root_dir, "assets", "js", "menu-data.js")
with codecs.open(menu_file, "r", encoding="utf-8") as f:
    content = f.read()

match = re.search(r"const menuData = (\[.*?\]);\s*window\.menuData", content, re.DOTALL)
if match:
    data_str = match.group(1)
    data = json.loads(data_str)
    
    # 1. Update Karışık Meze Tabağı (ID 10)
    # 2. Update Deniz Mahsülleri (ID 17)
    # 3. Add Kızarmış Dondurma (ID 121) to tatlilar
    
    for cat in data:
        for item in cat.get('items', []):
            if item.get('id') == 10:
                item['image'] = "assets/img/karisik_meze_tabagi_user.jpg"
            if item.get('id') == 17:
                item['image'] = "assets/img/deniz_mahsulleri_soguk_user.jpg"
        
        if cat.get('categoryId') == "tatlilar":
            # Check if 121 is already there
            exists = any(i.get('id') == 121 for i in cat.get('items', []))
            if not exists:
                cat['items'].insert(0, {
                    "id": 121,
                    "nameTR": "Kızarmış Dondurma",
                    "nameDE": "Fritierte Eiscreme",
                    "nameEN": "Fried Ice Cream",
                    "nameES": "Helado Frito",
                    "nameRU": "Жареное Мороженое",
                    "nameAR": "آيس كريم مقلي",
                    "descTR": "",
                    "descDE": "",
                    "descEN": "",
                    "descES": "",
                    "descRU": "",
                    "descAR": "",
                    "price": 9.00,
                    "image": "assets/img/kizarmis_dondurma.png"
                })

    new_data_str = json.dumps(data, indent=4, ensure_ascii=False)
    final_content = f"const menuData = {new_data_str};\n\nwindow.menuData = menuData;\n"

    with codecs.open(menu_file, "w", encoding="utf-8") as f:
        f.write(final_content)
    print("SUCCESS: Updated menu-data.js")
else:
    print("Failed to match JSON array in menu-data.js")
