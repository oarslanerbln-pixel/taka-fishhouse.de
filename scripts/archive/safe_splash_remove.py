import re

html_path = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    c = f.read()

# Sadece Splash ekranini temizle, baska HICBIR SEYE DOKUNMA!
c = re.sub(r'(?s)<!-- Premium Splash Screen -->.*?</div>\s*</div>\s*</div>', '<!-- Splash Removed -->', c)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(c)
print("Splash removed safely.")
