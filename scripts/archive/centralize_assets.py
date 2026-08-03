import re

filepath = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace src="assets/ with src="../assets/
content = re.sub(r'src="assets/', 'src="../assets/', content)

# Replace href="assets/ with href="../assets/
content = re.sub(r'href="assets/', 'href="../assets/', content)

# Replace url('assets/ with url('../assets/
content = re.sub(r"url\('assets/", "url('../assets/", content)
content = re.sub(r'url\("assets/', 'url("../assets/', content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated qr-menu/index.html to use centralized assets.")
