import json
import os
import sys

# Try to find the 121 items source
sources = [
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\wolt_images.json",
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\lieferando_nextdata.json",
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\lieferando_next_data.json"
]

def analyze_json(path):
    if not os.path.exists(path):
        return
    with open(path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            # Try to see if it's lieferando nextdata
            if 'props' in data:
                menu_data = data['props']['initialState']['menu']['menu']['products']
                print(f"{os.path.basename(path)} has {len(menu_data)} products.")
                
                # Check how many are drinks
                drinks = 0
                for pid, p in menu_data.items():
                    # Lieferando has categories, we can check category names if we have them
                    pass
            elif isinstance(data, list):
                print(f"{os.path.basename(path)} has {len(data)} items (List).")
            elif isinstance(data, dict):
                print(f"{os.path.basename(path)} has {len(data)} keys (Dict).")
        except Exception as e:
            print(f"Error parsing {path}: {e}")

for s in sources:
    analyze_json(s)

