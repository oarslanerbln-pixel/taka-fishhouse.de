import re, sys, io
from collections import defaultdict

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open("qr-menu/assets/js/menu-data.js", "r", encoding="utf-8") as f:
    content = f.read()

desserts_match = re.search(r'"categoryId":\s*"desserts".*?"items":\s*\[(.*?)\]\s*\}', content, re.DOTALL)
drinks_match = re.search(r'"categoryId":\s*"getranke".*?"items":\s*\[(.*?)\]\s*\}', content, re.DOTALL)

def get_remove_ids(items_raw):
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

    to_remove = []
    for name, dupes in by_name.items():
        if len(dupes) > 1:
            has_img_items = [d for d in dupes if d["has_image"]]
            no_img_items = [d for d in dupes if not d["has_image"]]
            if has_img_items:
                # Remove all without image
                for item in no_img_items:
                    to_remove.append(item["id"])
            else:
                # All have no image, keep first, remove rest
                for item in dupes[1:]:
                    to_remove.append(item["id"])
    return to_remove

all_remove = []
if desserts_match:
    all_remove += get_remove_ids(desserts_match.group(1))
if drinks_match:
    all_remove += get_remove_ids(drinks_match.group(1))

print("Removing IDs:", all_remove)

# For each ID to remove, remove the entire item block from content
# Item blocks start with { "id": X and end with the closing }
for item_id in all_remove:
    # Match the item object (non-greedy, from id to closing brace)
    pattern = r',?\s*\{\s*"id":\s*' + str(item_id) + r'\s*,.*?\}'
    new_content = re.sub(pattern, '', content, flags=re.DOTALL)
    if new_content != content:
        print("  Removed ID {}".format(item_id))
        content = new_content
    else:
        print("  WARN: Could not remove ID {}".format(item_id))

# Clean up orphaned commas (e.g. ,  , or [  ,)
content = re.sub(r',\s*,', ',', content)
content = re.sub(r'\[\s*,', '[', content)
content = re.sub(r',\s*\]', ']', content)

for file_path in ["qr-menu/assets/js/menu-data.js", "assets/js/menu-data.js"]:
    with open(file_path.replace("qr-menu/assets/js/menu-data.js", "qr-menu/assets/js/menu-data.js"), "w", encoding="utf-8") as f:
        f.write(content)

# Also update main assets
with open("assets/js/menu-data.js", "r", encoding="utf-8") as f:
    main_content = f.read()

for item_id in all_remove:
    pattern = r',?\s*\{\s*"id":\s*' + str(item_id) + r'\s*,.*?\}'
    new_main = re.sub(pattern, '', main_content, flags=re.DOTALL)
    if new_main != main_content:
        main_content = new_main

main_content = re.sub(r',\s*,', ',', main_content)
main_content = re.sub(r'\[\s*,', '[', main_content)
main_content = re.sub(r',\s*\]', ']', main_content)

with open("assets/js/menu-data.js", "w", encoding="utf-8") as f:
    f.write(main_content)

print("Done! Both files updated.")
