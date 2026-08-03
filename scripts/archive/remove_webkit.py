import re
import os

css_files = [
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\css\style.css",
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\css\menu-page.css",
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\css\style.css",
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\css\menu-page.css"
]

for filepath in css_files:
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove -webkit-backdrop-filter completely
    content = re.sub(r'^[ \t]*-webkit-backdrop-filter:[^\n]+\n', '', content, flags=re.MULTILINE)
    
    # Remove -webkit-user-select completely
    content = re.sub(r'^[ \t]*-webkit-user-select:[^\n]+\n', '', content, flags=re.MULTILINE)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        print(f"Removed webkit prefixes from {filepath}")
