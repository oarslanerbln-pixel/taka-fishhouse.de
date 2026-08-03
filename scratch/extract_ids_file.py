import json
import re

with open(r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\js\menu-data.js', 'r', encoding='utf-8') as f:
    data = f.read()

items = re.findall(r'\"id\":\s*(\d+).*?\"nameTR\":\s*\"([^\"]+)\"', data, re.DOTALL)
with open(r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\scratch\items.txt', 'w', encoding='utf-8') as f:
    for i in items:
        f.write(f'{i[0]}: {i[1]}\n')
