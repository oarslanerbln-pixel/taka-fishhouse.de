import os
import re

def fix_encoding(content):
    replacements = {
        'Ã¼': 'ü', 'Ä±': 'ı', 'ÄŸ': 'ğ', 'ÅŸ': 'ş', 'Ã¶': 'ö', 'Ã§': 'ç',
        'Ã‡': 'Ç', 'Åž': 'Ş', 'Ä°': 'İ', 'Ã–': 'Ö', 'Ãœ': 'Ü', 'â‚¬': '€',
        'ðŸ ƒ': '🌿', 'ðŸ Ÿ': '🍤'
    }
    for bad, good in replacements.items():
        content = content.replace(bad, good)
    return content

# 1. FIX HEART HTML ERROR
menu_js_path = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\js\menu-page.js"
with open(menu_js_path, 'r', encoding='utf-8', errors='ignore') as f:
    js_content = fix_encoding(f.read())

if 'const heartHtml =' not in js_content:
    js_content = js_content.replace('const itemName = item.name;', "const itemName = item.name;\n                                            const heartHtml = item.popular ? '<span class=\"favorite-heart\">❤️</span>' : '';")

with open(menu_js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)


# 2. FIX QR MENU HTML (Encoding + Paths + Remove Splash)
qr_path = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\index.html"
with open(qr_path, 'r', encoding='utf-8', errors='ignore') as f:
    qr_content = fix_encoding(f.read())

qr_content = qr_content.replace('../assets/', 'assets/') # Reset to safe state
qr_content = qr_content.replace('"assets/', '"../assets/')
qr_content = qr_content.replace("'assets/", "'../assets/")

# Remove Splash
qr_content = re.sub(r'<!-- Premium Splash Screen -->.*?<div id="premium-splash" class="premium-splash">.*?</div>\s*</div>\s*</div>', '', qr_content, flags=re.DOTALL)

with open(qr_path, 'w', encoding='utf-8') as f:
    f.write(qr_content)


# 3. FIX MENU.HTML ENCODING
menu_html = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\menu.html"
with open(menu_html, 'r', encoding='utf-8', errors='ignore') as f:
    m_content = fix_encoding(f.read())
with open(menu_html, 'w', encoding='utf-8') as f:
    f.write(m_content)


# 4. FIX MAIN INDEX HTML (Encoding + Intro Logo)
index_html = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\index.html"
with open(index_html, 'r', encoding='utf-8', errors='ignore') as f:
    i_content = fix_encoding(f.read())

old_splash = '<span class="splash-text">TAKA FISH HOUSE</span>'
new_splash = '<img src="assets/taka_logo.png" alt="Taka Fisch Haus Logo" style="max-width: 250px; height: auto;">'
i_content = i_content.replace(old_splash, new_splash)

with open(index_html, 'w', encoding='utf-8') as f:
    f.write(i_content)

print("SUPER FIX COMPLETED!")
