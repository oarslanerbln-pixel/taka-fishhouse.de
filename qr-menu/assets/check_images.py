import codecs
import re

with codecs.open('c:\\Users\\oarsl\\Desktop\\Is Dosyasi\\Taka Fisch Haus\\qr-menu\\assets\\js\\menu-data.js', 'r', 'utf-8') as f:
    content = f.read()

images = re.findall(r'"image":\s*"([^"]+)"', content)
print("Images used in menu-data.js:")
for img in set(images):
    print(img)
