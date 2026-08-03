import re

file_path = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\js\menu-data.js'
with open(file_path, 'r', encoding='utf-8') as f:
    data = f.read()

# Extract items
citir_regex = r'\{\s*\"id\": 9991,.*?(?=\n\s*\},|\n\s*\}\n)\n\s*\}'
zinnur_regex = r'\{\s*\"id\": 9993,.*?(?=\n\s*\},|\n\s*\}\n)\n\s*\}'

citir_match = re.search(citir_regex, data, re.DOTALL)
zinnur_match = re.search(zinnur_regex, data, re.DOTALL)

if not citir_match or not zinnur_match:
    print("Items not found.")
    exit(1)

citir_str = citir_match.group(0)
zinnur_str = zinnur_match.group(0)

# Remove items from their original place
# We need to handle the comma after the item if it exists
data = re.sub(citir_regex + r',?', '', data, flags=re.DOTALL)
data = re.sub(zinnur_regex + r',?', '', data, flags=re.DOTALL)

# Find the end of deniz-mahsulleri items array
# Look for "categoryId": "deniz-mahsulleri", and its "items": [ array
dm_regex = r'(\"categoryId\":\s*\"deniz-mahsulleri\",.*?\"items\":\s*\[)(.*?)(\n\s*\])'
dm_match = re.search(dm_regex, data, re.DOTALL)

if dm_match:
    # Append the items before the closing bracket of deniz-mahsulleri items array
    # add a comma to the last item if it doesn't have one
    items_content = dm_match.group(2)
    if not items_content.strip().endswith(','):
        items_content += ','
    
    new_items_content = items_content + '\n' + citir_str + ',\n' + zinnur_str
    
    data = data[:dm_match.start(2)] + new_items_content + data[dm_match.end(2):]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(data)
    print("Items moved successfully.")
else:
    print("Deniz mahsulleri category not found.")
