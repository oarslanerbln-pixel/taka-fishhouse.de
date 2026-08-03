"""
Smart center-crop script for Taka Fisch Haus menu images.
Crops each image to a square, centered on the food subject.
Uses _yeni.jpg originals where available, otherwise originals.
"""
import os, shutil
from PIL import Image, ImageEnhance

PRODUCTS = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\img\products"
QR_PRODUCTS = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\img\products"

def smart_crop(img, cx_pct, cy_pct, zoom=1.0):
    """
    Crop image to square centered at (cx_pct, cy_pct) of original image.
    cx_pct: 0.0=left, 1.0=right  (where the subject center is horizontally)
    cy_pct: 0.0=top, 1.0=bottom  (where the subject center is vertically)
    zoom: 1.0=tightest square, <1.0 keeps more context
    """
    w, h = img.size
    # Square side = min dimension * zoom factor
    side = int(min(w, h) * (1.0 / zoom))
    side = min(side, w, h)  # can't exceed image dimensions
    
    # Desired center in pixels
    cx = int(w * cx_pct)
    cy = int(h * cy_pct)
    
    # Calculate crop box
    left = cx - side // 2
    top = cy - side // 2
    right = left + side
    bottom = top + side
    
    # Clamp to image bounds
    if left < 0:
        right -= left; left = 0
    if top < 0:
        bottom -= top; top = 0
    if right > w:
        left -= (right - w); right = w
    if bottom > h:
        top -= (bottom - h); bottom = h
    
    left = max(0, left); top = max(0, top)
    return img.crop((left, top, right, bottom))

def enhance(img, saturation=1.2, brightness=1.05, contrast=1.1):
    img = ImageEnhance.Color(img).enhance(saturation)
    img = ImageEnhance.Brightness(img).enhance(brightness)
    img = ImageEnhance.Contrast(img).enhance(contrast)
    return img

def save_both(img, filename, quality=92):
    dst1 = os.path.join(PRODUCTS, filename)
    img.save(dst1, quality=quality)
    dst2 = os.path.join(QR_PRODUCTS, filename)
    if os.path.exists(QR_PRODUCTS):
        img.save(dst2, quality=quality)
    print(f"  Saved: {filename}")

def load(filename, prefer_yeni=True):
    """Load image, prefer _yeni version if available"""
    base, ext = os.path.splitext(filename)
    yeni = base + "_yeni" + ext
    yeni_path = os.path.join(PRODUCTS, yeni)
    orig_path = os.path.join(PRODUCTS, filename)
    if prefer_yeni and os.path.exists(yeni_path):
        print(f"  Using: {yeni} (original backup)")
        return Image.open(yeni_path).convert("RGB")
    return Image.open(orig_path).convert("RGB")

print("=== Taka Fisch Haus - Smart Crop & Center ===\n")

# --- URLA MEZE ---
# Food (white rect plate) is bottom-left in frame. 
# Subject center: ~38% from left, ~72% from top
print("Processing: urla_meze.jpg")
img = load("urla_meze.jpg")
img = smart_crop(img, cx_pct=0.38, cy_pct=0.72)
img = enhance(img, saturation=1.3, brightness=1.12, contrast=1.12)
save_both(img, "urla_meze.jpg")

# --- KURU CACIK ---
# White plate with cacık is in left-center to bottom-left. 
# Subject center: ~40% from left, ~65% from top
print("Processing: kuru_cacik.jpg")
img = load("kuru_cacik.jpg")
img = smart_crop(img, cx_pct=0.40, cy_pct=0.65)
img = enhance(img, saturation=1.15, brightness=1.1, contrast=1.1)
save_both(img, "kuru_cacik.jpg")

# --- HAVUÇ TARATOR ---
# Already fairly centered, just slightly high. cx=0.5, cy=0.52
print("Processing: havuc_tarator.jpg")
img = load("havuc_tarator.jpg")
img = smart_crop(img, cx_pct=0.50, cy_pct=0.52)
img = enhance(img, saturation=1.25, brightness=1.1, contrast=1.1)
save_both(img, "havuc_tarator.jpg")

# --- CACIK (kuru_cacik backup / cacik.jpg) ---
# This one is well-centered vertically but has lots of dead space top/bottom
# Subject center: 0.5, 0.55
print("Processing: cacik.jpg")
img = Image.open(os.path.join(PRODUCTS, "cacik.jpg")).convert("RGB")
img = smart_crop(img, cx_pct=0.50, cy_pct=0.52)
img = enhance(img, saturation=1.2, brightness=1.05, contrast=1.08)
save_both(img, "cacik.jpg")

# --- HAMSI WEB ---
# Very wide 16:9, subject fills whole frame nicely centered
# Just crop to square from center: 0.5, 0.5
print("Processing: hamsi_web.jpg")
img = Image.open(os.path.join(PRODUCTS, "hamsi_web.jpg")).convert("RGB")
img = smart_crop(img, cx_pct=0.50, cy_pct=0.50)
img = enhance(img, saturation=1.2, brightness=1.05, contrast=1.1)
save_both(img, "hamsi_web.jpg")

# --- USKUMRU ---
# Plate takes up full width, already centered. Portrait-ish. Just enhance.
print("Processing: uskumru.jpg.jpg")
img = Image.open(os.path.join(PRODUCTS, "uskumru.jpg.jpg")).convert("RGB")
img = smart_crop(img, cx_pct=0.50, cy_pct=0.48)
img = enhance(img, saturation=1.2, brightness=1.05, contrast=1.08)
save_both(img, "uskumru.jpg.jpg")

print("\n=== All images processed successfully! ===")
