import re
import os
import codecs
import time
import urllib.request
from duckduckgo_search import DDGS

# Ensure encoding for prints
import sys
sys.stdout.reconfigure(encoding='utf-8')

MENU_DATA_PATH = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\js\menu-data.js'
AUTO_IMGS_DIR = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\auto_imgs'

os.makedirs(AUTO_IMGS_DIR, exist_ok=True)

# 1. Read menu data
with codecs.open(MENU_DATA_PATH, 'r', 'utf-8') as f:
    content = f.read()

# Fix Fritz Cola if wrongly matched
content = re.sub(
    r'("nameDE":\s*"Fritz Cola 0,2l",.*?)\n\s*"image":\s*"assets/lieferando_imgs/coca_cola_0_2l_mehrweg\.jpg"',
    r'\1',
    content,
    flags=re.DOTALL
)

# Extract blocks and find missing images
item_blocks = re.findall(r'(\{\s*(?:[^{}]|\n)*?"nameDE":\s*"[^"]+"(?:[^{}]|\n)*?\})', content, re.DOTALL)

missing_items = []
for block in item_blocks:
    if '"image"' not in block:
        name_match = re.search(r'"nameDE":\s*"([^"]+)"', block)
        if name_match:
            missing_items.append(name_match.group(1))

print(f"Toplam {len(missing_items)} ürün için görsel aranacak...")

ddgs = DDGS()
updated_count = 0

for item_name in missing_items:
    print(f"\n🔍 Aranıyor: {item_name}")
    
    # Improve search queries for better results
    search_query = f"{item_name}"
    if "0,2" in item_name or "0,3" in item_name or "0,5" in item_name:
        search_query += " flasche getränk" # Add bottle/drink context for drinks
    
    if item_name == "Kuru Cacik (traditioneller türkischer Joghurt Gurken-Dip)":
        search_query = "Kuru Cacik Haydari"
        
    try:
        results = list(ddgs.images(search_query, max_results=3))
        if results:
            img_url = results[0]['image']
            print(f"   Bulundu: {img_url[:60]}...")
            
            # Format filename
            safe_name = re.sub(r'[^\w\s-]', '', item_name.lower())
            safe_name = re.sub(r'\s+', '_', safe_name.strip())[:50]
            ext = img_url.split('.')[-1][:4] if '.' in img_url[-6:] else 'jpg'
            # Clean up extension
            ext = "".join([c for c in ext if c.isalpha()])
            if not ext: ext = 'jpg'
            
            filename = f"{safe_name}.{ext}"
            filepath = os.path.join(AUTO_IMGS_DIR, filename)
            
            # Download image
            req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
            try:
                with urllib.request.urlopen(req, timeout=10) as response:
                    with open(filepath, 'wb') as f:
                        f.write(response.read())
                
                rel_path = f"assets/auto_imgs/{filename}"
                print(f"   ✅ İndirildi: {rel_path}")
                
                # Update content string
                block_pattern = r'(\{\s*(?:[^{}]|\n)*?"nameDE":\s*"' + re.escape(item_name) + r'"(?:[^{}]|\n)*?\})'
                
                def replacer(m):
                    block = m.group(1)
                    if '"price"' in block:
                        return re.sub(
                            r'("price":\s*"[^"]+"),?',
                            lambda x: x.group(0).rstrip(',') + f',\n                "image": "{rel_path}"',
                            block, count=1
                        )
                    else:
                        return re.sub(
                            r'("nameDE":\s*"' + re.escape(item_name) + r'"),?',
                            lambda x: x.group(0).rstrip(',') + f',\n                "image": "{rel_path}"',
                            block, count=1
                        )
                
                content = re.sub(block_pattern, replacer, content, flags=re.DOTALL)
                updated_count += 1
                
            except Exception as e:
                print(f"   ❌ İndirme hatası: {e}")
                
        else:
            print("   ❌ Görsel bulunamadı.")
            
    except Exception as e:
        print(f"   ❌ Arama hatası: {e}")
        
    time.sleep(1.5) # Be gentle to DDG

if updated_count > 0:
    with codecs.open(MENU_DATA_PATH, 'w', 'utf-8') as f:
        f.write(content)
    print(f"\n🎉 Toplam {updated_count} ürün otomatik görselleriyle eklendi!")
else:
    print("\n⚠️ Hiç görsel güncellenemedi.")
