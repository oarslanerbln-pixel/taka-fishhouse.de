import sys
from PIL import Image, ImageEnhance
import os

def enhance_image(input_path, output_path):
    try:
        img = Image.open(input_path)
        
        # Convert to RGB if it's not
        if img.mode != 'RGB':
            img = img.convert('RGB')
            
        # Enhance Color (Vibrance)
        color_enhancer = ImageEnhance.Color(img)
        img = color_enhancer.enhance(1.4) # Increase color saturation by 40%
        
        # Enhance Contrast
        contrast_enhancer = ImageEnhance.Contrast(img)
        img = contrast_enhancer.enhance(1.15) # Increase contrast by 15%
        
        # Enhance Brightness
        brightness_enhancer = ImageEnhance.Brightness(img)
        img = brightness_enhancer.enhance(1.05) # Increase brightness by 5%
        
        # Enhance Sharpness
        sharpness_enhancer = ImageEnhance.Sharpness(img)
        img = sharpness_enhancer.enhance(1.2) # Increase sharpness by 20%
        
        # Save
        img.save(output_path, quality=95)
        print(f"Successfully saved enhanced image to {output_path}")
        
    except Exception as e:
        print(f"Error enhancing image: {e}")
        sys.exit(1)

if __name__ == "__main__":
    input_file = r"C:\Users\oarsl\.gemini\antigravity-ide\brain\0ef7b752-cec1-4f33-8c81-3f6f4460c05e\media__1783359538566.jpg"
    
    out_dir1 = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\img\products"
    out_dir2 = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\img\products"
    
    os.makedirs(out_dir1, exist_ok=True)
    os.makedirs(out_dir2, exist_ok=True)
    
    out1 = os.path.join(out_dir1, "balik_kofte_menu.jpg")
    out2 = os.path.join(out_dir2, "balik_kofte_menu.jpg")
    
    enhance_image(input_file, out1)
    
    # Also save to qr-menu
    import shutil
    shutil.copy2(out1, out2)
    print(f"Copied to {out2}")
