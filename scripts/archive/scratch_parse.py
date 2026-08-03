import json
import re

with open("lieferando_nextdata.json", "r", encoding="utf-8") as f:
    data = json.load(f)

text = json.dumps(data)

# Find fritz items with images
for term in ["fritz", "rotbarbe", "hamsi", "oktopus", "seezunge", "barbun"]:
    idxs = [m.start() for m in re.finditer(term, text, re.IGNORECASE)]
    if idxs:
        print(f"\n=== Found {term} at {len(idxs)} places ===")
        for idx in idxs[:2]:  # max 2
            chunk = text[max(0,idx-100):idx+400]
            # Find imageUrl near this
            img = re.search(r'"imageUrl":\s*"([^"]+)"', chunk)
            name = re.search(r'"name":\s*"([^"]+)"', chunk)
            print(f"  name: {name.group(1) if name else 'N/A'}")
            print(f"  img: {img.group(1) if img else 'N/A'}")
    else:
        print(f"NOT FOUND: {term}")
