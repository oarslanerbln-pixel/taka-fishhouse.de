import os
import re
from PIL import Image

data = open('assets/js/menu-data.js', encoding='utf-8').read()
matches = re.findall(r'"image":\s*"(assets/[^"]+\.JPG)"', data)
unique_jpgs = list(set(matches))

for jpg in unique_jpgs:
    print(f"Optimizing {jpg}...")
    try:
        img_path = jpg
        new_path = jpg.replace(".JPG", "_web.jpg")
        
        with Image.open(img_path) as im:
            # Resize while keeping aspect ratio
            im.thumbnail((800, 800))
            # Convert to RGB in case it's RGBA
            rgb_im = im.convert('RGB')
            rgb_im.save(new_path, "JPEG", quality=80)
            
        data = data.replace(f'"{jpg}"', f'"{new_path}"')
        print(f"Saved {new_path}")
    except Exception as e:
        print(f"Error processing {jpg}: {e}")

open('assets/js/menu-data.js', 'w', encoding='utf-8').write(data)
print("Updated menu-data.js")
