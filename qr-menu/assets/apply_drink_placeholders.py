import re
import os
import shutil
import codecs

# Image paths
src_cold = r'C:\Users\oarsl\.gemini\antigravity-ide\brain\04e24bd0-ea73-468b-814e-43d4dcc4dca4\placeholder_cold_drink_1782647058905.png'
src_hot = r'C:\Users\oarsl\.gemini\antigravity-ide\brain\04e24bd0-ea73-468b-814e-43d4dcc4dca4\placeholder_hot_drink_1782647073408.png'

dest_dir = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\img'
os.makedirs(dest_dir, exist_ok=True)

dest_cold = os.path.join(dest_dir, 'placeholder_cold_drink.png')
dest_hot = os.path.join(dest_dir, 'placeholder_hot_drink.png')

# Copy files
if os.path.exists(src_cold): shutil.copy(src_cold, dest_cold)
if os.path.exists(src_hot): shutil.copy(src_hot, dest_hot)

# Lists of drinks
cold_drinks = [
    "Stilles Wasser 0,25l", "Mineralwasser mit Kohlensäure 0,25l", "Fritz Cola 0,2l", 
    "Christinen Apfelschorle 0,33l", "7gün Ayran 0,25l", "Capri Sonne 0,2l", 
    "Çamlıca Gazoz 0,2l", "Salgam (Rübensaft) 0,25l", "Tymbark 0,25l", 
    "FuzeTea 0,4l", "Christinen Multivitamin 0,33l", "Durstlöscher 0,5l"
]

hot_drinks = [
    "Türkischer Tee klein", "Verschiedene Teesorten", "Café Cream", 
    "Cappuccino", "Café Latte", "Espresso", "Türkischer Mokka"
]

MENU_DATA_PATH = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\js\menu-data.js'

with codecs.open(MENU_DATA_PATH, 'r', 'utf-8') as f:
    content = f.read()

def apply_placeholder(item_names, image_path, text):
    for item in item_names:
        block_pattern = r'(\{\s*(?:[^{}]|\n)*?"nameDE":\s*"' + re.escape(item) + r'"(?:[^{}]|\n)*?\})'
        
        def replacer(m):
            block = m.group(1)
            if '"image"' in block:
                # Remove existing wrong image if any
                block = re.sub(r',\s*"image":\s*"[^"]+"', '', block)
                block = re.sub(r'"image":\s*"[^"]+",?\s*', '', block)
                
            if '"price"' in block:
                return re.sub(
                    r'("price":\s*"[^"]+"),?',
                    lambda x: x.group(0).rstrip(',') + f',\n                "image": "{image_path}"',
                    block, count=1
                )
            else:
                return re.sub(
                    r'("nameDE":\s*"' + re.escape(item) + r'"),?',
                    lambda x: x.group(0).rstrip(',') + f',\n                "image": "{image_path}"',
                    block, count=1
                )
                
        text = re.sub(block_pattern, replacer, text, flags=re.DOTALL)
    return text

content = apply_placeholder(cold_drinks, "assets/img/placeholder_cold_drink.png", content)
content = apply_placeholder(hot_drinks, "assets/img/placeholder_hot_drink.png", content)

with codecs.open(MENU_DATA_PATH, 'w', 'utf-8') as f:
    f.write(content)

print("Drink placeholders applied successfully!")
