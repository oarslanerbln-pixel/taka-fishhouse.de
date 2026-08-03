import json
import codecs
import sys

# Ensure utf-8 output to avoid charmap errors
sys.stdout.reconfigure(encoding='utf-8')

with codecs.open('c:\\Users\\oarsl\\Desktop\\Is Dosyasi\\Taka Fisch Haus\\qr-menu\\assets\\js\\menu-data.js', 'r', 'utf-8') as f:
    content = f.read()

import re
items = re.findall(r'"nameTR":\s*"([^"]+)",\s*"nameDE":\s*"([^"]+)"', content)
for tr, de in items:
    if 'Sup' in de or 'Corba' in tr or 'Çorba' in tr:
        print(f"TR: {tr} | DE: {de}")
