import os
import urllib.request
import re

target_dir = r"C:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\drinks"

# Capri Sonne direct URL from the HTML we scraped earlier
capri_url = "https://produkt-handel.de/media/a5/fe/67/1728303601/9872-1.jpg?ts=1782728259"
save_path = os.path.join(target_dir, "caprisonne.jpg")

try:
    req = urllib.request.Request(capri_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as response, open(save_path, 'wb') as out_file:
        out_file.write(response.read())
    print("Downloaded caprisonne.jpg")
except Exception as e:
    print(f"Failed to download Capri Sonne: {e}")

# Inject into menu-data.js
files = [
    "qr-menu/assets/js/menu-data.js",
    "assets/js/menu-data.js"
]

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # ID 141 is Capri Sonne
    pattern = r'("id":\s*141\s*,.*?\})'
    def repl(match):
        block = match.group(1)
        if '"image":' in block:
            return re.sub(r'"image":\s*"[^"]*"', '"image": "assets/drinks/caprisonne.jpg"', block)
        else:
            return re.sub(r'("price":)', '"image": "assets/drinks/caprisonne.jpg",\n                \\1', block)
            
    content = re.sub(pattern, repl, content, flags=re.DOTALL)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
