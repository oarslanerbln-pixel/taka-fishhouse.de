import os

files_to_update = [
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\index.html",
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\menu.html",
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\index.html",
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\impressum.html",
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\datenschutz.html"
]

for file_path in files_to_update:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update .com to .de
        content = content.replace("takafishhouse.com", "taka-fishhouse.de")
        content = content.replace("takafishhouse.de", "taka-fishhouse.de") # eger bosluksuz hali kaldiysa
        
        # update canonical
        content = content.replace('href="https://takafishhouse.de/"', 'href="https://taka-fishhouse.de/"')
        
        # OpenGraph image (basic placeholder for SEO)
        if '<meta property="og:type" content="restaurant">' in content and '<meta property="og:image"' not in content:
            og_image = '<meta property="og:image" content="https://taka-fishhouse.de/assets/premium_map.png">\n    <meta property="og:url" content="https://taka-fishhouse.de/">'
            content = content.replace('<meta property="og:type" content="restaurant">', f'<meta property="og:type" content="restaurant">\n    {og_image}')

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

print("SEO domains updated to taka-fishhouse.de")
