import re
import os
import shutil

BASE = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus'
MENU_JS = os.path.join(BASE, r'qr-menu\assets\js\menu-data.js')
ASSETS = os.path.join(BASE, r'qr-menu\assets')
ARCHIVE = os.path.join(BASE, r'_unused_imgs_archive')

with open(MENU_JS, encoding='utf-8') as f:
    content = f.read()

# Get all image paths used in menu
used_paths = set(re.findall(r'"(assets/[^"]+)"', content))
print(f"Found {len(used_paths)} used images in menu-data.js:")
for p in sorted(used_paths):
    print(f"  {p}")

# Now scan actual asset files (only images, not subdirs with ubereats/lieferando)
IMAGE_EXTS = {'.jpg', '.jpeg', '.png', '.webp', '.gif'}
SCAN_DIRS = ['', 'img']  # root of assets + img subdir

all_files = []
for d in SCAN_DIRS:
    scan_path = os.path.join(ASSETS, d) if d else ASSETS
    if os.path.exists(scan_path):
        for f in os.listdir(scan_path):
            fpath = os.path.join(scan_path, f)
            if os.path.isfile(fpath) and os.path.splitext(f)[1].lower() in IMAGE_EXTS:
                rel = f'assets/{d + "/" if d else ""}{f}'
                all_files.append((rel, fpath))

print(f"\nTotal image files in assets root: {len(all_files)}")

unused = [(rel, path) for rel, path in all_files if rel not in used_paths]
print(f"Unused image files: {len(unused)}")

os.makedirs(ARCHIVE, exist_ok=True)

moved = 0
for rel, fpath in unused:
    fname = os.path.basename(fpath)
    dest = os.path.join(ARCHIVE, fname)
    # don't overwrite if name collision
    if os.path.exists(dest):
        base, ext = os.path.splitext(fname)
        dest = os.path.join(ARCHIVE, f"{base}_dup{ext}")
    shutil.move(fpath, dest)
    print(f"  MOVED: {fname}")
    moved += 1

print(f"\nMoved {moved} unused images to: {ARCHIVE}")
