import os
import time

files_to_update = [
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\index.html",
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\menu.html",
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\index.html"
]

timestamp = str(int(time.time()))

for file_path in files_to_update:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Append cache-buster to css
        content = content.replace('href="assets/css/style.css"', f'href="assets/css/style.css?v={timestamp}"')
        content = content.replace('href="../assets/css/style.css"', f'href="../assets/css/style.css?v={timestamp}"')
        content = content.replace('href="assets/css/menu-page.css"', f'href="assets/css/menu-page.css?v={timestamp}"')
        content = content.replace('href="../assets/css/menu-page.css"', f'href="../assets/css/menu-page.css?v={timestamp}"')
        
        # Append cache-buster to js
        content = content.replace('src="assets/js/menu-data.js"', f'src="assets/js/menu-data.js?v={timestamp}"')
        content = content.replace('src="../assets/js/menu-data.js"', f'src="../assets/js/menu-data.js?v={timestamp}"')
        content = content.replace('src="assets/js/menu-page.js"', f'src="assets/js/menu-page.js?v={timestamp}"')
        content = content.replace('src="../assets/js/menu-page.js"', f'src="../assets/js/menu-page.js?v={timestamp}"')
        content = content.replace('src="assets/js/main.js"', f'src="assets/js/main.js?v={timestamp}"')
        content = content.replace('src="../assets/js/main.js"', f'src="../assets/js/main.js?v={timestamp}"')

        # Eger zaten bir cache buster varsa ustune bir tane daha buster eklendiyse onlemek zor, ama su an temiz oldugunu varsayiyorum.

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

print("Added cache-buster versions.")
