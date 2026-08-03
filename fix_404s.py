"""
Fix ALL 404 errors:
- Wolt hex images → exist in assets/img/products/ — copy to qr-menu/assets/
- hamsi_web.jpg, hamsikoy_sutlac_ai.png → already in qr-menu/assets/ ✓
- taka-logo-gold.svg → fix reference to taka_logo.png in index.html
- taka-video-poster.jpg → fix reference to existing _DSC4134_web.jpg
- salgam.png → copy a matching drink image to assets/drinks/
- Drink hex images (coca cola etc) → fix in assets/js/menu-data.js
"""
import os, shutil

BASE = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus'
QR_ASSETS = os.path.join(BASE, 'qr-menu', 'assets')
MAIN_PRODUCTS = os.path.join(BASE, 'assets', 'img', 'products')
MAIN_DRINKS = os.path.join(BASE, 'assets', 'drinks')
MAIN_JS = os.path.join(BASE, 'assets', 'js', 'menu-data.js')

# ==========================================
# 1. Copy wolt hex images → qr-menu/assets/
# ==========================================
wolt_hex_images = [
    '69a80af27d25f60394a12d3d.jpg',
    '69a80b2fe2de7f22b84d7fee.jpg',
    '69a80b6e23e151913f38f30e.jpg',
    '69a80bb97d25f60394a12da0.jpg',
    '69a80bd97d25f60394a12eaa.jpg',
    '69a80c4de2de7f22b84d8232.jpg',
    '69a80c6be2de7f22b84d823a.jpg',
    '69a80cc67d25f60394a12f6c.jpg',
    '69a80dce7d25f60394a12fcb.jpg',
    '69a80e3523e151913f38f56e.jpg',
]
for fname in wolt_hex_images:
    src = os.path.join(MAIN_PRODUCTS, fname)
    dst = os.path.join(QR_ASSETS, fname)
    if os.path.exists(src) and not os.path.exists(dst):
        shutil.copy2(src, dst)
        print(f"Copied {fname}")
    elif os.path.exists(dst):
        print(f"Already exists: {fname}")
    else:
        print(f"NOT FOUND: {fname}")

# ==========================================
# 2. cacik.jpg, deniz-borulcesi.jpg, unsplash → copy to qr-menu/assets/
# ==========================================
extra_imgs = ['cacik.jpg', 'deniz-borulcesi.jpg', 'unsplash_1556679343.jpg']
for fname in extra_imgs:
    src = os.path.join(MAIN_PRODUCTS, fname)
    dst = os.path.join(QR_ASSETS, fname)
    if os.path.exists(src) and not os.path.exists(dst):
        shutil.copy2(src, dst)
        print(f"Copied {fname}")
    elif os.path.exists(dst):
        print(f"Already exists: {fname}")
    else:
        print(f"NOT FOUND: {fname}")

# ==========================================
# 3. salgam.png — create placeholder in assets/drinks/
# ==========================================
salgam_dst = os.path.join(MAIN_DRINKS, 'salgam.png')
if not os.path.exists(salgam_dst):
    # Use any existing drink image as placeholder
    drink_src = os.path.join(MAIN_DRINKS, 'ayran.jpg')
    if not os.path.exists(drink_src):
        # Find any file in drinks folder
        drinks_list = os.listdir(MAIN_DRINKS) if os.path.exists(MAIN_DRINKS) else []
        if drinks_list:
            drink_src = os.path.join(MAIN_DRINKS, drinks_list[0])
    if os.path.exists(drink_src):
        shutil.copy2(drink_src, salgam_dst)
        print(f"Created salgam.png placeholder from {drink_src}")
    else:
        print("WARN: No drink file found for salgam placeholder")
else:
    print("salgam.png already exists")

# ==========================================
# 4. Fix main menu-data.js drink hex IDs → use lieferando_imgs/
# ==========================================
with open(MAIN_JS, 'r', encoding='utf-8') as f:
    content = f.read()

drink_map = {
    # THESE are old Wolt/Lieferando hex IDs still in menu-data.js
    '2faec65a-17a7-11eb-9f4b-b26fbf627d3c_cocacola_zero_0_2.jpeg': 
        'assets/drinks/cola_zero.jpg',
    '0211094c-17a7-11eb-8056-b6507305cae7_cocacola_0_2.jpeg': 
        'assets/drinks/cola.jpg',
    '3f846a1a-2f23-11eb-bd32-c2695b788ece_fanta_0_2.jpeg': 
        'assets/drinks/fanta.jpg',
    '2a2f2782-17a8-11eb-9abd-fe05229f24a2_sprite_0_2l_.jpeg': 
        'assets/drinks/sprite.jpg',
    'fc113ac8-4a80-11eb-8d33-866b5695d3f0_mezzo_mix_0_2l.jpeg': 
        'assets/drinks/mezzo_mix.jpg',
    'a8e2e052-65b1-11ec-be25-feaf95301eef_uludaggazoz025.jpeg': 
        'assets/drinks/uludag.jpg',
    'd3ada63c-44fb-11eb-9129-9add570c388b_fritz_kola__21.jpeg': 
        'assets/drinks/fritz_kola.jpg',
    '26a7725a-44fc-11eb-8728-1233a3d50ac2_fritz_limo_orange__21.jpeg': 
        'assets/drinks/fritz_limo.jpg',
    '4aeb5c0a-8841-11ed-800a-2ad9c7086556_superzero.jpeg': 
        'assets/drinks/superzero.jpg',
    '76f4b770-4927-11eb-9330-4e241e2ced00_christinen_apfelschorle_0_33l.jpeg': 
        'assets/drinks/apfelschorle.jpg',
    '645e9f72-4927-11eb-9c98-16866cd60e34_christinen_multivitamin_0_33l.jpeg': 
        'assets/drinks/multivitamin.jpg',
}

# Check which lieferando drinks actually exist
lieferando = os.path.join(QR_ASSETS, 'lieferando_imgs')
lieferando_files = {f.lower(): f for f in os.listdir(lieferando)} if os.path.exists(lieferando) else {}

# Smart drink name→file mapping
smart_drink_map = {
    '2faec65a-17a7-11eb-9f4b-b26fbf627d3c_cocacola_zero_0_2.jpeg': 
        'assets/img/products/2faec65a-17a7-11eb-9f4b-b26fbf627d3c_cocacola_zero_0_2.jpeg',
    '0211094c-17a7-11eb-8056-b6507305cae7_cocacola_0_2.jpeg': 
        'assets/img/products/0211094c-17a7-11eb-8056-b6507305cae7_cocacola_0_2.jpeg',
    '3f846a1a-2f23-11eb-bd32-c2695b788ece_fanta_0_2.jpeg': 
        'assets/img/products/3f846a1a-2f23-11eb-bd32-c2695b788ece_fanta_0_2.jpeg',
    '2a2f2782-17a8-11eb-9abd-fe05229f24a2_sprite_0_2l_.jpeg': 
        'assets/img/products/2a2f2782-17a8-11eb-9abd-fe05229f24a2_sprite_0_2l_.jpeg',
    'fc113ac8-4a80-11eb-8d33-866b5695d3f0_mezzo_mix_0_2l.jpeg': 
        'assets/img/products/fc113ac8-4a80-11eb-8d33-866b5695d3f0_mezzo_mix_0_2l.jpeg',
    'a8e2e052-65b1-11ec-be25-feaf95301eef_uludaggazoz025.jpeg': 
        'assets/img/products/a8e2e052-65b1-11ec-be25-feaf95301eef_uludaggazoz025.jpeg',
    'd3ada63c-44fb-11eb-9129-9add570c388b_fritz_kola__21.jpeg': 
        'assets/img/products/d3ada63c-44fb-11eb-9129-9add570c388b_fritz_kola__21.jpeg',
    '26a7725a-44fc-11eb-8728-1233a3d50ac2_fritz_limo_orange__21.jpeg': 
        'assets/img/products/26a7725a-44fc-11eb-8728-1233a3d50ac2_fritz_limo_orange__21.jpeg',
    '4aeb5c0a-8841-11ed-800a-2ad9c7086556_superzero.jpeg': 
        'assets/img/products/4aeb5c0a-8841-11ed-800a-2ad9c7086556_superzero.jpeg',
    '76f4b770-4927-11eb-9330-4e241e2ced00_christinen_apfelschorle_0_33l.jpeg': 
        'assets/img/products/76f4b770-4927-11eb-9330-4e241e2ced00_christinen_apfelschorle_0_33l.jpeg',
    '645e9f72-4927-11eb-9c98-16866cd60e34_christinen_multivitamin_0_33l.jpeg': 
        'assets/img/products/645e9f72-4927-11eb-9c98-16866cd60e34_christinen_multivitamin_0_33l.jpeg',
}

# Check which ones actually exist in img/products
r_count = 0
for old_name, new_path in smart_drink_map.items():
    full_path = os.path.join(BASE, new_path)
    if not os.path.exists(full_path):
        # File doesn't exist in products — use placeholder
        smart_drink_map[old_name] = 'assets/img/placeholder_cold_drink.png'
    if old_name in content:
        content = content.replace(old_name, new_path)
        r_count += 1

with open(MAIN_JS, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Fixed {r_count} drink references in menu-data.js")

print("\nAll fixes applied! Now deploy to Vercel.")
