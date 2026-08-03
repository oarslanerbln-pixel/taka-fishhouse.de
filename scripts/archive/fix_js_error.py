import os
import re

js_path = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\js\menu-page.js"
with open(js_path, 'r', encoding='utf-8', errors='ignore') as f:
    js_content = f.read()

# Fix heartHtml error
# We will insert let heartHtml = ''; right before const priceHtml
js_content = js_content.replace('const priceHtml', "let heartHtml = '';\n                        const priceHtml")

# Try to fix weird encoding in js too (like we did in HTML)
replacements = {
    'Ã¼': 'ü',
    'Ä±': 'ı',
    'ÄŸ': 'ğ',
    'ÅŸ': 'ş',
    'Ã¶': 'ö',
    'Ã§': 'ç',
    'Ã‡': 'Ç',
    'Åž': 'Ş',
    'Ä°': 'İ',
    'Ã–': 'Ö',
    'Ãœ': 'Ü',
    'â‚¬': '€',
    'ðŸ ƒ': '🌿',
    'ðŸ Ÿ': '🍤'
}
for bad, good in replacements.items():
    js_content = js_content.replace(bad, good)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("menu-page.js FIXED!")

data_path = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\js\menu-data.js"
if os.path.exists(data_path):
    with open(data_path, 'r', encoding='utf-8', errors='ignore') as f:
        data_c = f.read()
    for bad, good in replacements.items():
        data_c = data_c.replace(bad, good)
    with open(data_path, 'w', encoding='utf-8') as f:
        f.write(data_c)
    print("menu-data.js FIXED!")

