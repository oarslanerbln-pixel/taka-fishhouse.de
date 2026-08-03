import re
import os
import codecs
import sys

sys.stdout.reconfigure(encoding='utf-8')

MENU_DATA_PATH = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\js\menu-data.js'
BASE_DIR = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets'

SEARCH_DIRS = [
    'ubereats_imgs',
    'lieferando_imgs',
    'img'
]

def normalize(text):
    text = text.lower().strip()
    text = text.replace('ü', 'u').replace('ö', 'o').replace('ä', 'a').replace('ß', 'ss')
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', '_', text).strip('_')
    return text

def get_all_local_images():
    images = {}
    for folder in SEARCH_DIRS:
        folder_path = os.path.join(BASE_DIR, folder)
        if not os.path.exists(folder_path): continue
        for file in os.listdir(folder_path):
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                name_norm = normalize(os.path.splitext(file)[0])
                # Prefer ubereats over lieferando if same name
                if name_norm not in images or folder == 'ubereats_imgs':
                    images[name_norm] = f"assets/{folder}/{file}"
    return images

def find_best_match(menu_name, local_images):
    menu_norm = normalize(menu_name)
    menu_words = set(menu_norm.split('_'))
    
    best_match = None
    best_score = 0
    
    for img_norm, rel_path in local_images.items():
        img_words = set(img_norm.split('_'))
        
        if menu_norm == img_norm:
            return rel_path, 1.0
            
        if menu_words and img_words:
            intersection = menu_words & img_words
            union = menu_words | img_words
            score = len(intersection) / len(union)
            
            # Substring match if score is low but string is contained
            if score < 1.0 and (menu_norm in img_norm or img_norm in menu_norm):
                score += 0.4
                
            if score > best_score:
                best_score = score
                best_match = rel_path
                
    return best_match, best_score

with codecs.open(MENU_DATA_PATH, 'r', 'utf-8') as f:
    content = f.read()

local_images = get_all_local_images()
item_blocks = re.findall(r'(\{\s*(?:[^{}]|\n)*?"nameDE":\s*"[^"]+"(?:[^{}]|\n)*?\})', content, re.DOTALL)

updated_count = 0

for block in item_blocks:
    if '"image"' not in block:
        name_match = re.search(r'"nameDE":\s*"([^"]+)"', block)
        if name_match:
            de_name = name_match.group(1)
            match_path, score = find_best_match(de_name, local_images)
            
            if match_path and score > 0.4:
                print(f"✅ Eşleşti: '{de_name}' -> {match_path} (Skor: {score:.2f})")
                
                if '"price"' in block:
                    new_block = re.sub(
                        r'("price":\s*"[^"]+"),?',
                        lambda x: x.group(0).rstrip(',') + f',\n                "image": "{match_path}"',
                        block, count=1
                    )
                else:
                    new_block = re.sub(
                        r'("nameDE":\s*"' + re.escape(de_name) + r'"),?',
                        lambda x: x.group(0).rstrip(',') + f',\n                "image": "{match_path}"',
                        block, count=1
                    )
                
                content = content.replace(block, new_block)
                updated_count += 1
            else:
                print(f"❌ Bulunamadı: '{de_name}'")

if updated_count > 0:
    with codecs.open(MENU_DATA_PATH, 'w', 'utf-8') as f:
        f.write(content)
    print(f"\n🎉 Toplam {updated_count} ürünün görseli güncellendi!")
else:
    print("\n⚠️ Güncellenecek ürün bulunamadı.")
