import codecs
import re

file_path = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\js\menu-data.js'

with codecs.open(file_path, 'r', 'utf-8') as f:
    content = f.read()

# We need to remove the "image" line for specific items:
# "Pommes frites"
# "Ruccolasalat", "Lachssalat", "Garnelensalat", "Hamsisalat"

items_to_clear = [
    "Pommes frites",
    "Ruccolasalat",
    "Lachssalat",
    "Garnelensalat",
    "Hamsisalat"
]

def remove_image_for_de(content, de_name):
    # Regex to find the item block by nameDE and remove the "image": "..." line
    pattern = r'("nameDE":\s*"' + re.escape(de_name) + r'".*?\})'
    
    def replacer(match):
        block = match.group(1)
        # Remove the image line and any preceding comma and whitespace
        # Sometimes it's `,\n                "image": "..."`
        block = re.sub(r',\s*"image":\s*"[^"]+"', '', block)
        # Or if it's the first one without a comma before it
        block = re.sub(r'"image":\s*"[^"]+",\s*', '', block)
        block = re.sub(r'"image":\s*"[^"]+"\s*', '', block)
        return block
    
    return re.sub(pattern, replacer, content, flags=re.DOTALL)

for item in items_to_clear:
    content = remove_image_for_de(content, item)

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(content)

print("Removed incorrect images successfully.")
