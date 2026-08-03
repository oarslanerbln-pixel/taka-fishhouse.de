import json
import re

files_to_update = [
    r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\js\menu-data.js',
    r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\js\menu-data.js'
]

updates = {
    "Türk Çayı (Büyük)": "assets/img/products/buyuk-cay.jpg",
    "Türk Çayı (Küçük)": "assets/img/products/kucuk-cay.jpg",
    "Café Latte": "assets/img/products/kaffee-latte.jpeg",
    "Çay (Küçük)": "assets/img/products/kucuk-cay.jpg"
}

for file_path in files_to_update:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for name, new_img in updates.items():
        # Match the block containing the name and replace its image
        pattern = r"(nameTR:\s*['\"]" + re.escape(name) + r"['\"].*?image:\s*['\"])([^'\"]*)(['\"])"
        
        def replacer(match):
            return match.group(1) + new_img + match.group(3)
        
        new_content = re.sub(pattern, replacer, content, flags=re.DOTALL)
        content = new_content
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated menu-data.js files.")
