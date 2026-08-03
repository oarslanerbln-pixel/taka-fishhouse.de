import re

with open('c:/Users/oarsl/Desktop/Is Dosyasi/Taka Fisch Haus/assets/js/menu-data.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
with open('c:/Users/oarsl/Desktop/Is Dosyasi/Taka Fisch Haus/scratch/meze_lines.txt', 'w', encoding='utf-8') as out:
    for i, line in enumerate(lines):
        if 'soguk-mezeler' in line:
            out.write(f"Soguk mezeler category at line {i}\n")
        if 'Karı' in line or 'Kar\u0131' in line or 'Havuç' in line or 'Urla' in line or 'Cacık' in line or 'Meze' in line:
            out.write(f"Found something at line {i}: {line.strip()}\n")
