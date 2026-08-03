import re
import codecs

MENU_DATA_PATH = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\js\menu-data.js'

with codecs.open(MENU_DATA_PATH, 'r', 'utf-8') as f:
    content = f.read()

# Fix specific wrong assignments

# 1. Meeresfrüchte Taka Spezial -> Remove image
content = re.sub(
    r'("nameDE":\s*"Meeresfrüchte Taka Spezial",.*?)\n\s*"image":\s*"assets/lieferando_imgs/taka_spezial_teller\.jpg",?',
    r'\1',
    content,
    flags=re.DOTALL
)

# 2. Gegrillte Champions mit Käse überbacken -> Set to gegrillte_champignons.jpg
content = re.sub(
    r'("nameDE":\s*"Gegrillte Champions mit Käse überbacken",.*?)\n\s*"image":\s*"assets/lieferando_imgs/broccoli\.jpg"',
    r'\1\n                "image": "assets/ubereats_imgs/gegrillte_champignons.jpg"',
    content,
    flags=re.DOTALL
)

# 3. Gemischter grüner Salat -> Set to gemischter_salat.jpg
content = re.sub(
    r'("nameDE":\s*"Gemischter grüner Salat",.*?)\n\s*"image":\s*"assets/ubereats_imgs/bauernsalat\.jpg"',
    r'\1\n                "image": "assets/lieferando_imgs/gemischter_salat.jpg"',
    content,
    flags=re.DOTALL
)

# 4. Fritz Cola Zero 0,2l -> Remove image
content = re.sub(
    r'("nameDE":\s*"Fritz Cola Zero 0,2l",.*?)\n\s*"image":\s*"assets/lieferando_imgs/coca_cola_zero_sugar_0_2l_mehrweg\.jpg",?',
    r'\1',
    content,
    flags=re.DOTALL
)

# 5. Fritz Orange 0,2l -> Remove image
content = re.sub(
    r'("nameDE":\s*"Fritz Orange 0,2l",.*?)\n\s*"image":\s*"assets/lieferando_imgs/fanta_orange_0_2l_mehrweg\.jpg",?',
    r'\1',
    content,
    flags=re.DOTALL
)

# 6. Schweppes 0,2l -> Remove image
content = re.sub(
    r'("nameDE":\s*"Schweppes 0,2l",.*?)\n\s*"image":\s*"assets/lieferando_imgs/sprite_0_2l_mehrweg\.jpg",?',
    r'\1',
    content,
    flags=re.DOTALL
)

with codecs.open(MENU_DATA_PATH, 'w', 'utf-8') as f:
    f.write(content)

print("Duplicates fixed successfully!")
