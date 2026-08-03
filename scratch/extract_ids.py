import json
import re

with open(r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\js\menu-data.js', 'r', encoding='utf-8') as f:
    data = f.read()

# Extract items
items = re.findall(r'\"id\":\s*(\d+).*?\"nameTR\":\s*\"([^\"]+)\"', data, re.DOTALL)
for i in items:
    print(f'{i[0]}: {i[1]}')
