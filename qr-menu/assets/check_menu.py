import json
import re
import codecs

with codecs.open('c:\\Users\\oarsl\\Desktop\\Is Dosyasi\\Taka Fisch Haus\\qr-menu\\assets\\js\\menu-data.js', 'r', 'utf-8') as f:
    content = f.read()

# Let's extract all categoryId using regex
categories = re.findall(r'"categoryId":\s*"([^"]+)"', content)
print("Categories found:", categories)

# Let's check if 'sandwiches' exists
if 'sandwiches' not in categories:
    print("Sandwiches category not found!")
    
# Let's search for soup
soup_match = re.search(r'"categoryId":\s*"suppen"', content)
if soup_match:
    print("Suppen category found!")
    
