import os
import re

# 1. FIX INDEX.HTML INTRO
index_path = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\index.html"
with open(index_path, 'r', encoding='utf-8', errors='ignore') as f:
    index_content = f.read()

old_splash = '<span class="splash-text">TAKA FISH HOUSE</span>'
new_splash = '<img src="assets/taka_logo.png" alt="Taka Fisch Haus Logo" style="max-width: 250px; height: auto;">'

if old_splash in index_content:
    index_content = index_content.replace(old_splash, new_splash)
else:
    # try regex just in case
    index_content = re.sub(r'<span class="splash-text">[^<]*</span>', new_splash, index_content)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_content)
    
print("index.html INTRO LOGO EKLENDI.")

# 2. REMOVE INTRO FROM QR-MENU/INDEX.HTML
qr_path = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\index.html"
with open(qr_path, 'r', encoding='utf-8', errors='ignore') as f:
    qr_content = f.read()

# remove the whole <div id="premium-splash" class="premium-splash"> ... </div>
qr_content = re.sub(r'<!-- Premium Splash Screen -->.*?<div id="premium-splash" class="premium-splash">.*?</div>\s*</div>\s*</div>', '', qr_content, flags=re.DOTALL)

with open(qr_path, 'w', encoding='utf-8') as f:
    f.write(qr_content)

print("qr-menu/index.html INTRO KALDIRILDI.")
