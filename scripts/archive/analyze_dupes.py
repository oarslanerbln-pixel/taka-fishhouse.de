import re, sys, io
from collections import defaultdict

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open("qr-menu/assets/js/menu-data.js", "r", encoding="utf-8") as f:
    content = f.read()

desserts_match = re.search(r'"categoryId":\s*"desserts".*?"items":\s*\[(.*?)\]\s*\}', content, re.DOTALL)
drinks_match = re.search(r'"categoryId":\s*"getranke".*?"items":\s*\[(.*?)\]\s*\}', content, re.DOTALL)

def analyze_items(items_raw, section_name):
    print("=== {} ===".format(section_name))
    raw_blocks = re.split(r'(?=\s*\{\s*"id":)', items_raw)

    items = []
    for block in raw_blocks:
        id_match = re.search(r'"id":\s*(\d+)', block)
        name_match = re.search(r'"nameTR":\s*"([^"]+)"', block)
        has_img = '"image":' in block
        if id_match:
            items.append({
                "id": int(id_match.group(1)),
                "name": name_match.group(1) if name_match else "?",
                "has_image": has_img,
            })

    by_name = defaultdict(list)
    for item in items:
        by_name[item["name"]].append(item)

    print("Total items: {}".format(len(items)))
    to_remove = []

    for name, dupes in by_name.items():
        if len(dupes) > 1:
            has_img_items = [d for d in dupes if d["has_image"]]
            no_img_items = [d for d in dupes if not d["has_image"]]
            ids = [str(d["id"]) for d in dupes]
            print("  DUPE [{}]: IDs {}".format(name[:30], ", ".join(ids)))
            if has_img_items:
                for item in no_img_items:
                    to_remove.append(item["id"])
                    print("    REMOVE ID {} (no image, keeping {})".format(
                        item["id"], has_img_items[0]["id"]))
            else:
                for item in dupes[1:]:
                    to_remove.append(item["id"])
                    print("    REMOVE ID {} (keep first)".format(item["id"]))
    return to_remove

desserts_remove = analyze_items(desserts_match.group(1), "DESSERTS") if desserts_match else []
print("")
drinks_remove = analyze_items(drinks_match.group(1), "DRINKS") if drinks_match else []

all_remove = desserts_remove + drinks_remove
print("\nTotal IDs to remove: {}".format(len(all_remove)))
print("IDs: {}".format(all_remove))
