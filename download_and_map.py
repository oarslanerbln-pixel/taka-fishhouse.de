import os
import re
import json
import urllib.request
from urllib.error import URLError

js_file = 'assets/js/menu-data.js'
with open(js_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all images
images = list(set(re.findall(r'"image":\s*"([^"]+)"', content)))

remote_images = [img for img in images if img.startswith('http')]
missing_local = [img for img in images if not img.startswith('http') and not os.path.exists(img.replace('../', ''))]

download_dir = 'assets/img/products'
os.makedirs(download_dir, exist_ok=True)

updates = {}

# Download remote images
for url in remote_images:
    # Generate a filename
    basename = url.split('/')[-1].split('?')[0]
    if not basename.endswith(('.jpg', '.jpeg', '.png')):
        basename += '.jpg'
    
    # Wolt URLs sometimes are just hashes like 69a80af27d25f60394a12d3d
    # Unsplash URLs have lots of params
    if 'unsplash' in url:
        basename = "unsplash_" + url.split('photo-')[1][:10] + '.jpg'
        
    local_path = f"assets/img/products/{basename}"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(local_path, 'wb') as out_file:
            out_file.write(response.read())
        print(f"Downloaded {url} -> {local_path}")
        updates[url] = local_path
    except Exception as e:
        print(f"Failed to download {url}: {e}")

# Handle missing local images by mapping to placeholders or existing
fallback_map = {
    'assets/hamsi_web.jpg': 'assets/img/products/hamsi_tava.png',
    'assets/_DSC4138_web.jpg': 'assets/img/products/karisik_meze.jpg',
    'assets/_DSC4134_web.jpg': 'assets/img/products/taka_spesiyal_deniz_mahsulleri.jpeg',
    'assets/hamsikoy_sutlac_ai.png': 'assets/img/products/sutlac.png',
    'assets/drinks/salgam.png': 'assets/img/products/salgam.jpg' # Assume we have something similar, or just leave it
}

for img in missing_local:
    if img in fallback_map:
        if os.path.exists(fallback_map[img]):
            updates[img] = fallback_map[img]
            print(f"Mapped {img} -> {fallback_map[img]}")

# Update menu-data.js
for old, new in updates.items():
    content = content.replace(f'"image": "{old}"', f'"image": "{new}"')

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Updated {len(updates)} images in menu-data.js")
