import os
from PIL import Image, ImageEnhance
import shutil

src_ai_image = r"C:\Users\oarsl\.gemini\antigravity-ide\brain\6df10031-a5e3-4757-b3ae-0e807e572539\karisik_meze_tabagi_ai_1785772134438.png"
dst_img1 = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\img\products\karisik_meze_tabagi_ai.png"
dst_img2 = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\img\products\karisik_meze_tabagi_ai.png"

if os.path.exists(src_ai_image):
    shutil.copy(src_ai_image, dst_img1)
    if os.path.exists(os.path.dirname(dst_img2)):
        shutil.copy(src_ai_image, dst_img2)

def enhance_and_crop(img_path):
    if not os.path.exists(img_path):
        return
    img = Image.open(img_path)
    # Crop to 1:1 (Center)
    width, height = img.size
    new_size = min(width, height)
    left = (width - new_size) / 2
    top = (height - new_size) / 2
    right = (width + new_size) / 2
    bottom = (height + new_size) / 2
    img = img.crop((left, top, right, bottom))
    
    # Enhance Color (Saturation)
    enhancer_color = ImageEnhance.Color(img)
    img = enhancer_color.enhance(1.25)
    
    # Enhance Brightness
    enhancer_brightness = ImageEnhance.Brightness(img)
    img = enhancer_brightness.enhance(1.1)
    
    # Enhance Contrast
    enhancer_contrast = ImageEnhance.Contrast(img)
    img = enhancer_contrast.enhance(1.1)
    
    # Overwrite the original
    img.save(img_path)

images_to_edit = ['havuc_tarator.jpg', 'urla_meze.jpg', 'kuru_cacik.jpg']
dirs = [
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\img\products",
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\img\products"
]

for d in dirs:
    for filename in images_to_edit:
        path = os.path.join(d, filename)
        enhance_and_crop(path)

print("Images successfully processed.")
