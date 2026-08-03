"""
The QR menu runs from qr-menu/ directory.
When it loads menu-data.js images with paths like 'assets/img/products/xxx.jpg',
it looks for them at: qr-menu/assets/img/products/xxx.jpg

But the files are in: assets/img/products/xxx.jpg (main site folder)

Solution: Copy ALL missing files to qr-menu/assets/ structure
"""
import os, shutil

BASE = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus'
QR_ASSETS = os.path.join(BASE, 'qr-menu', 'assets')

# Create target directories
dirs_to_create = [
    os.path.join(QR_ASSETS, 'img', 'products'),
    os.path.join(QR_ASSETS, 'drinks'),
    os.path.join(QR_ASSETS, 'lieferando_imgs'),
    os.path.join(QR_ASSETS, 'ubereats_imgs'),
]
for d in dirs_to_create:
    os.makedirs(d, exist_ok=True)

# Copy img/products/ 
src_products = os.path.join(BASE, 'assets', 'img', 'products')
dst_products = os.path.join(QR_ASSETS, 'img', 'products')
copied = 0
for fname in os.listdir(src_products):
    src = os.path.join(src_products, fname)
    dst = os.path.join(dst_products, fname)
    if not os.path.exists(dst):
        shutil.copy2(src, dst)
        copied += 1
print(f"Copied {copied} files to qr-menu/assets/img/products/")

# Copy drinks/
src_drinks = os.path.join(BASE, 'assets', 'drinks')
dst_drinks = os.path.join(QR_ASSETS, 'drinks')
copied = 0
for fname in os.listdir(src_drinks):
    src = os.path.join(src_drinks, fname)
    dst = os.path.join(dst_drinks, fname)
    if os.path.isfile(src) and not os.path.exists(dst):
        shutil.copy2(src, dst)
        copied += 1
print(f"Copied {copied} files to qr-menu/assets/drinks/")

# Copy top-level assets (hamsi_web.jpg, etc.)
top_level_files = [
    'hamsi_web.jpg', 'hamsikoy_sutlac_ai.png', 'levrek_marin_ai.png',
    'dil_baligi.png', '_DSC4134_web.jpg', '_DSC4138_web.jpg',
    'taka_logo.png'
]
copied = 0
for fname in top_level_files:
    src = os.path.join(BASE, 'assets', fname)
    if not os.path.exists(src):
        src = os.path.join(BASE, 'qr-menu', 'assets', fname)
    dst = os.path.join(QR_ASSETS, fname)
    if os.path.exists(src) and not os.path.exists(dst):
        shutil.copy2(src, dst)
        copied += 1
    elif os.path.exists(dst):
        pass
    else:
        print(f"NOT FOUND: {fname}")
print(f"Copied {copied} top-level asset files")

# Also copy lieferando and ubereats from main assets if they exist there
for subfolder in ['lieferando_imgs', 'ubereats_imgs']:
    src_dir = os.path.join(BASE, 'assets', subfolder)
    dst_dir = os.path.join(QR_ASSETS, subfolder)
    if os.path.exists(src_dir):
        copied = 0
        for fname in os.listdir(src_dir):
            src = os.path.join(src_dir, fname)
            dst = os.path.join(dst_dir, fname)
            if os.path.isfile(src) and not os.path.exists(dst):
                shutil.copy2(src, dst)
                copied += 1
        print(f"Copied {copied} files to qr-menu/assets/{subfolder}/")

print("\nDone! All assets mirrored to qr-menu/assets/")
