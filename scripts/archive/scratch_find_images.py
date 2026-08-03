import json
import sys

def search_json(filepath, keys):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return

    print(f"\n--- Searching in {filepath} ---")
    for key in keys:
        found = False
        if isinstance(data, list):
            for item in data:
                name = item.get("name", "").lower()
                desc = item.get("description", "").lower()
                if key.lower() in name or key.lower() in desc:
                    img = item.get("imageUrl") or item.get("image")
                    if img:
                        print(f"Found {key}: {item.get('name')} -> {img}")
                        found = True
        elif isinstance(data, dict):
            # Try to handle dict structure if needed
            for k, v in data.items():
                if isinstance(v, dict):
                    name = v.get("name", "").lower()
                    if key.lower() in name:
                        img = v.get("imageUrl") or v.get("image")
                        if img:
                            print(f"Found {key}: {v.get('name')} -> {img}")
                            found = True
        if not found:
            print(f"NOT FOUND: {key}")

keys = ["fritz", "rotbarbe", "hamsi", "octopus", "seezunge"]
search_json("qr-menu/lieferando_data.json", keys)
search_json("qr-menu/assets/wolt_images.json", keys)
