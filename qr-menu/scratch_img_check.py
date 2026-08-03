import re, os
path = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\js\menu-data.js'
with open(path, 'r', encoding='utf-8') as f:
    data = f.read()
imgs = re.findall(r'"image":\s*"(.*?)"', data)
for img in imgs:
    full_path = os.path.join(r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu', img)
    if not os.path.exists(full_path):
        print("Missing:", img)
