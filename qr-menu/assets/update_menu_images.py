import codecs
import re

with codecs.open('c:\\Users\\oarsl\\Desktop\\Is Dosyasi\\Taka Fisch Haus\\qr-menu\\assets\\js\\menu-data.js', 'r', 'utf-8') as f:
    content = f.read()

def replace_image_for_de(content, de_name, image_path):
    # Regex to find the item block by nameDE and insert/replace "image": "..."
    # A block looks like:
    # "nameDE": "Lachs Sandwich",\n                ... \n            }
    
    pattern = r'("nameDE":\s*"' + de_name + r'".*?\})'
    
    def replacer(match):
        block = match.group(1)
        if '"image"' in block:
            # Replace existing image
            return re.sub(r'"image":\s*"[^"]+"', f'"image": "{image_path}"', block)
        else:
            # Add image before the last closing brace
            # Usually the last field before } doesn't have a comma, so we need to be careful
            # We can just insert it after nameDE
            return block.replace(f'"nameDE": "{de_name}",', f'"nameDE": "{de_name}",\n                "image": "{image_path}",')
    
    return re.sub(pattern, replacer, content, flags=re.DOTALL)

content = replace_image_for_de(content, 'Lachs Sandwich', 'assets/wolt_lachs_sandwich.jpg')
content = replace_image_for_de(content, 'Dorade Sandwich', 'assets/wolt_dorade_sandwich.jpg')
content = replace_image_for_de(content, 'Makrele Sandwich', 'assets/wolt_makrele_sandwich.jpg')
content = replace_image_for_de(content, 'Lachssuppe', 'assets/wolt_lachsuppe.jpg')

with codecs.open('c:\\Users\\oarsl\\Desktop\\Is Dosyasi\\Taka Fisch Haus\\qr-menu\\assets\\js\\menu-data.js', 'w', 'utf-8') as f:
    f.write(content)
