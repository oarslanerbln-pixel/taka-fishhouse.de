import codecs
import re

with codecs.open('c:\\Users\\oarsl\\Desktop\\Is Dosyasi\\Taka Fisch Haus\\qr-menu\\assets\\js\\menu-data.js', 'r', 'utf-8') as f:
    content = f.read()

sandwiches = re.findall(r'"nameDE":\s*"([^"]+)",[\s\S]*?"image":\s*"([^"]+)"', content)
for name, img in sandwiches:
    if "Sandwich" in name or "Dürüm" in name or "Wrap" in name:
        print(f"{name} -> {img}")
