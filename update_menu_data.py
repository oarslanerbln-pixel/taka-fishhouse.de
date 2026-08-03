import re

filepath = 'assets/js/menu-data.js'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove Çıtır Deniz Mahsülleri Sarması and Peynir Dolgulu Enginar
# We need to remove the whole object `{ ... }` from the items array.
# The safest way using regex without breaking syntax:
# Find the object start `{` all the way to `},` or `}` that contains the name.
# Using a loop to find and replace.

def remove_item_by_name(name):
    global content
    pattern = re.compile(r'\{[^{}]*"nameTR":\s*"' + name + r'".*?\},?\s*', re.DOTALL)
    content = pattern.sub('', content)
    print("Removed an item")

remove_item_by_name("Çıtır Deniz Mahsülleri Sarması")
remove_item_by_name("Peynir Dolgulu Enginar")

# 2. Update sandwich images
def update_sandwich_img(name_tr_regex, new_img):
    global content
    pattern = re.compile(rf'("nameTR":\s*"{name_tr_regex}".*?"image":\s*")[^"]+(")', re.DOTALL)
    content = pattern.sub(rf'\g<1>{new_img}\g<2>', content)

# typical sandwiches
update_sandwich_img("Çipura Sandviç.*?", "assets/lieferando_imgs/dorade_sandwich.jpg")
update_sandwich_img("Uskumru Sandviç.*?", "assets/lieferando_imgs/makrele_sandwich.jpg")
update_sandwich_img("Somon Sandviç.*?", "assets/lieferando_imgs/lachs_sandwich.jpg")
update_sandwich_img("Karides Sandviç.*?", "assets/lieferando_imgs/garnelen_sandwich.jpg")
update_sandwich_img("Sardalya Sandviç.*?", "assets/lieferando_imgs/sardinen_sandwich.jpg")
update_sandwich_img("Hamsi Sandviç.*?", "assets/lieferando_imgs/sardinen_sandwich.jpg") # Fallback if hamsi sandwich uses sardine pic

# durums (wraps) if needed
update_sandwich_img("Somon Dürüm.*?", "assets/lieferando_imgs/lachs_sandwich.jpg")
update_sandwich_img("Karides Dürüm.*?", "assets/lieferando_imgs/garnelen_sandwich.jpg")
update_sandwich_img("Çipura Dürüm.*?", "assets/lieferando_imgs/dorade_sandwich.jpg")
update_sandwich_img("Uskumru Dürüm.*?", "assets/lieferando_imgs/makrele_sandwich.jpg")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Menu data updated successfully.")
