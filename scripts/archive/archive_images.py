import os
import shutil

html_files = [os.path.join(r, f) for r, d, files in os.walk('.') if '.git' not in r and '.vercel' not in r for f in files if f.endswith('.html')]
js_files = [os.path.join(r, f) for r, d, files in os.walk('.') if '.git' not in r and '.vercel' not in r for f in files if f.endswith('.js')]

content = ''
for f in html_files + js_files:
    try:
        content += open(f, 'r', encoding='utf-8', errors='ignore').read()
    except Exception as e:
        print(f"Error reading {f}: {e}")

archive_dir = '_unused_imgs_archive/products'
os.makedirs(archive_dir, exist_ok=True)

# Function to process an image directory
def process_img_dir(base_dir):
    if not os.path.exists(base_dir):
        return
    img_files = [f for f in os.listdir(base_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.svg'))]
    moved = 0
    for img in img_files:
        if img not in content:
            source = os.path.join(base_dir, img)
            dest = os.path.join(archive_dir, f"{os.path.basename(base_dir)}_{img}")
            try:
                shutil.move(source, dest)
                moved += 1
                print(f"Moved {source} to {dest}")
            except Exception as e:
                print(f"Error moving {img}: {e}")
    print(f"Total moved from {base_dir}: {moved}")

process_img_dir('assets/img/products')
process_img_dir('qr-menu/assets/img/products')
