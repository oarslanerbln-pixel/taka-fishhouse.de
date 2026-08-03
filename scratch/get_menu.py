import re

with open('c:/Users/oarsl/Desktop/Is Dosyasi/Taka Fisch Haus/assets/js/menu-data.js', 'r', encoding='utf-8') as f:
    data = f.read()
    
items = re.findall(r'\"nameTR\"\s*:\s*\"([^\"]+)\".*?\"image\"\s*:\s*\"([^\"]+)\"', data, re.DOTALL)
for name, img in items:
    print(f"{name}: {img}")
