import shutil
import os

files_to_copy = [
    (r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\_unused_imgs_archive\uskumru_enhanced.png",
     r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\img\products\uskumru_enhanced.png"),
    (r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\_unused_imgs_archive\uskumru_enhanced.png",
     r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\img\products\uskumru_enhanced.png"),
    (r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\img\karisik_meze_tabagi_user.jpg",
     r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\img\karisik_meze_tabagi_user.jpg")
]

for src, dst in files_to_copy:
    if os.path.exists(src):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        print(f"Başarıyla kopyalandı: {os.path.basename(src)}")
    else:
        print(f"Bulunamadı: {src}")
