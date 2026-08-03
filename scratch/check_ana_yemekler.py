import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

file_path = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\js\menu-data.js"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

match = re.search(r"const menuData = (\[.*?\]);\s*window\.menuData", content, re.DOTALL)
if match:
    data_str = match.group(1)
    data = json.loads(data_str)
    
    for cat in data:
        if cat.get('categoryId') == 'ana-yemekler':
            print("\n--- ANA YEMEKLER SIRALAMASI ---")
            for idx, item in enumerate(cat['items']):
                print(f"{idx+1}. {item['nameTR']}")
