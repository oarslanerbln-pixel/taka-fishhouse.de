import codecs
import re

file_path = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\js\menu-data.js'

with codecs.open(file_path, 'r', 'utf-8') as f:
    content = f.read()

manual_map = {
    "Sardine Sandwich": "assets/lieferando_imgs/sardinen_sandwich.jpg",
    "Garnele Sandwich": "assets/lieferando_imgs/garnelen_sandwich.jpg",
    "Dorade Dürüm": "assets/lieferando_imgs/d_r_m_doraden.jpg",
    "Makrele Dürüm": "assets/lieferando_imgs/d_r_m_makrelen.jpg",
    "Sardine Dürüm": "assets/lieferando_imgs/d_r_m_sardinen.jpg",
    "Garnele Dürüm": "assets/lieferando_imgs/d_r_m_garnelen.jpg",
    "Lachssuppe": "assets/lieferando_imgs/lachsuppe.jpg"
}

def replace_image_for_de(content, de_name, image_path):
    pattern = r'("nameDE":\s*"' + re.escape(de_name) + r'".*?\})'
    
    def replacer(match):
        block = match.group(1)
        if '"image"' in block:
            return re.sub(r'"image":\s*"[^"]+"', f'"image": "{image_path}"', block)
        else:
            return block.replace(
                f'"nameDE": "{de_name}",',
                f'"nameDE": "{de_name}",\n                "image": "{image_path}",'
            )
    
    return re.sub(pattern, replacer, content, flags=re.DOTALL)

for de_name, rel_path in manual_map.items():
    content = replace_image_for_de(content, de_name, rel_path)

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(content)

print("Applied manual overrides successfully.")
