import os, shutil
from PIL import Image, ImageEnhance, ImageFilter

SRC = r"C:\Users\oarsl\.gemini\antigravity-ide\brain\6df10031-a5e3-4757-b3ae-0e807e572539"
PRODUCTS = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\img\products"
QR_PRODUCTS = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\img\products"

def copy_to_both(src_path, filename):
    shutil.copy(src_path, os.path.join(PRODUCTS, filename))
    if os.path.exists(QR_PRODUCTS):
        shutil.copy(src_path, os.path.join(QR_PRODUCTS, filename))
    print(f"Copied {filename}")

# 1. ÇITIR KARİDES - copy as-is
citir_src = os.path.join(SRC, "citir_karides_1785773550289.png")
copy_to_both(citir_src, "citir_karides.png")

# 2. ZİNNUR - copy as-is
zinnur_src = os.path.join(SRC, "zinnur_1785773558642.png")
copy_to_both(zinnur_src, "zinnur.png")

# 3. BARBUN - Enhance red/pink colors to make it vibrant
barbun_src = os.path.join(PRODUCTS, "barbun.jpg")
img = Image.open(barbun_src).convert("RGB")

# Boost red channel specifically for the fish color
r, g, b = img.split()
# Increase red channel significantly
r = r.point(lambda x: min(255, int(x * 1.4)))
# Slightly reduce blue to make reds pop more
b = b.point(lambda x: max(0, int(x * 0.85)))
img = Image.merge("RGB", (r, g, b))

# Boost overall saturation + contrast + brightness
img = ImageEnhance.Color(img).enhance(1.6)
img = ImageEnhance.Contrast(img).enhance(1.15)
img = ImageEnhance.Brightness(img).enhance(1.05)
img = ImageEnhance.Sharpness(img).enhance(1.3)

img.save(os.path.join(PRODUCTS, "barbun.jpg"), quality=95)
if os.path.exists(QR_PRODUCTS):
    img.save(os.path.join(QR_PRODUCTS, "barbun.jpg"), quality=95)
print("Barbun enhanced with vivid red colors")

# 4. KARIŞ MAN MEZE TABAGI - Crop to remove wine glasses (zoom in on plate only)
meze_src = os.path.join(PRODUCTS, "karisik-meze-tabagi.jpg.png")
img = Image.open(meze_src).convert("RGB")
w, h = img.size
print(f"Meze image size: {w}x{h}")

# The plate is in the lower portion, glasses are at the top ~30% 
# Crop to focus on the plate: remove top ~30%, keep the rest
# Then crop sides slightly to center on plate
top_crop = int(h * 0.28)  # remove top 28% (where glasses are)
bottom_keep = int(h * 0.05)  # keep a little bottom padding
left_crop = int(w * 0.02)   
right_crop = int(w * 0.02)

cropped = img.crop((left_crop, top_crop, w - right_crop, h - bottom_keep))
# Resize to square for consistent card display
cw, ch = cropped.size
new_size = min(cw, ch)
cx, cy = (cw - new_size) // 2, (ch - new_size) // 2
cropped = cropped.crop((cx, cy, cx + new_size, cy + new_size))

# Enhance to make colors pop
cropped = ImageEnhance.Color(cropped).enhance(1.2)
cropped = ImageEnhance.Contrast(cropped).enhance(1.1)
cropped = ImageEnhance.Brightness(cropped).enhance(1.05)

cropped.save(os.path.join(PRODUCTS, "karisik_meze_tabagi_clean.jpg"), quality=95)
if os.path.exists(QR_PRODUCTS):
    cropped.save(os.path.join(QR_PRODUCTS, "karisik_meze_tabagi_clean.jpg"), quality=95)
print("Meze tabagi cropped (wine glasses removed)")

print("\nAll done!")
