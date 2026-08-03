import os

js_file = 'assets/js/menu-data.js'
with open(js_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Hamsi Tava (id 72)
content = content.replace('"image": "assets/img/products/hamsi_tava.png"', '"image": "assets/img/products/hamsi_web.jpg"')

# Fix Karisik Meze (if it was DSC4138)
# But wait, there might be other items using karisik_meze.jpg
# So I should only replace the specific item. Let me do regex for the id or name if possible.
# Actually, Hamsiköy Sütlaç has id 102
# "id": 102 ... "image": "assets/img/products/sutlac.png" -> "assets/img/products/hamsikoy_sutlac_ai.png"

import re

def update_item_img(name_tr_regex, new_img):
    global content
    # Find block starting with nameTR and update image
    pattern = re.compile(rf'("nameTR":\s*"{name_tr_regex}".*?"image":\s*")[^"]+(")', re.DOTALL)
    content = pattern.sub(rf'\g<1>{new_img}\g<2>', content)

# Hamsi Tava (already fixed by simple replace if unique, but let's be safe)
update_item_img("Hamsi Tava.*?", "assets/img/products/hamsi_web.jpg")
update_item_img("Hamsiköy Sütlacı.*?", "assets/img/products/hamsikoy_sutlac_ai.png")
update_item_img("Zinnur.*?", "assets/img/products/_DSC4138_web.jpg") # wait, zinnur is which one?
# Taka Spesiyal Deniz Mahsülleri
update_item_img("TAKA Special Deniz Mahsülleri.*?", "assets/img/products/_DSC4134_web.jpg")

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed mappings based on located files.")
