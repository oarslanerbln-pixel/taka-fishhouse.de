import json
import re
import urllib.request
import os

path = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\js\menu-data.js'
with open(path, 'r', encoding='utf-8') as f:
    data = f.read()

imgs = re.findall(r'"image":\s*"(.*?)"', data)

for img in imgs:
    if img.startswith('http'):
        try:
            req = urllib.request.Request(img, headers={'User-Agent': 'Mozilla/5.0'})
            response = urllib.request.urlopen(req, timeout=3)
            length = response.headers.get('Content-Length')
            content = response.read()
            if len(content) == 15705 or (length and int(length) == 15705):
                print(f"Placeholder Wolt icon found: {img}")
        except Exception as e:
            print(f"Error fetching {img}: {e}")
    else:
        full_path = os.path.join(r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu', img)
        if not os.path.exists(full_path):
            print(f"Local file missing: {img}")

