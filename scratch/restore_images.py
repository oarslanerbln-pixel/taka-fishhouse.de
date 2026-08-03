import os
from PIL import Image, ImageEnhance
import shutil

def restore_and_enhance(src_path, dst_path):
    if not os.path.exists(src_path):
        return
    # Restore from the backup (_yeni.jpg)
    shutil.copy(src_path, dst_path)
    
    img = Image.open(dst_path)
    
    # Enhance Color (Saturation)
    enhancer_color = ImageEnhance.Color(img)
    img = enhancer_color.enhance(1.25)
    
    # Enhance Brightness
    enhancer_brightness = ImageEnhance.Brightness(img)
    img = enhancer_brightness.enhance(1.1)
    
    # Enhance Contrast
    enhancer_contrast = ImageEnhance.Contrast(img)
    img = enhancer_contrast.enhance(1.1)
    
    # Save WITHOUT cropping (keeps 16:9)
    img.save(dst_path)

files = [
    ('havuc_tarator_yeni.jpg', 'havuc_tarator.jpg'),
    ('urla_meze_yeni.jpg', 'urla_meze.jpg'),
    ('kuru_cacik_yeni.jpg', 'kuru_cacik.jpg')
]

dirs = [
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\img\products",
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\img\products"
]

for d in dirs:
    for src, dst in files:
        src_path = os.path.join(d, src)
        dst_path = os.path.join(d, dst)
        restore_and_enhance(src_path, dst_path)

print("Images restored and enhanced (without crop).")
