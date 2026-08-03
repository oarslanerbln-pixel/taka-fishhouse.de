import os
import re

def fix_encoding_and_paths():
    files = [
        r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\index.html",
        r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\menu.html",
        r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\index.html"
    ]
    
    for file_path in files:
        if not os.path.exists(file_path): continue
        
        # Oku (ANSI'den UTF-8'e cevirerek bozulmus karakterleri kurtar)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        try:
            # Eger dosya gercekten double-encoded olduysa:
            fixed_content = content.encode('latin1').decode('utf-8')
        except:
            fixed_content = content # Encode hatasi verirse zaten duzgundur.
            
        # qr-menu icindeyse pathleri duzelt
        if "qr-menu" in file_path:
            # Script yollari
            fixed_content = re.sub(r'src="assets/js/', 'src="../assets/js/', fixed_content)
            # Image yollari (logo vs) eger "assets/" ile basliyorsa
            fixed_content = re.sub(r'src="assets/img/', 'src="../assets/img/', fixed_content)
            fixed_content = re.sub(r'src="assets/taka_logo', 'src="../assets/taka_logo', fixed_content)
            
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(fixed_content)

fix_encoding_and_paths()
print("Encoding and paths fixed.")
