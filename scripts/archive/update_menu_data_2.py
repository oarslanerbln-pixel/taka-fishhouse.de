import re

def add_image_to_menu(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find id: 109 and insert image after it
    pattern = r'("id": 109,\s*"nameTR": "Balık Köfte Menü",\s*"nameDE": "[^"]*",)'
    replacement = r'\1\n      "image": "assets/img/products/balik_kofte_menu.jpg",'
    
    new_content = re.sub(pattern, replacement, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"No match found or already updated in {filepath}")

add_image_to_menu(r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\js\menu-data.js")
add_image_to_menu(r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\js\menu-data.js")
