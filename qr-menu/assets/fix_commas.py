import re, codecs
path = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\js\menu-data.js'
with codecs.open(path, 'r', 'utf-8') as f:
    content = f.read()
# Bul: "image": "..." (virgül yok), ardından boşluk ve başka bir JSON keyi ("allergens": gibi)
content = re.sub(r'("image":\s*"[^"]+")\s*\n(\s*"[^"]+":)', r'\1,\n\2', content)
with codecs.open(path, 'w', 'utf-8') as f:
    f.write(content)
print("Virgüller eklendi!")
