import re, os

BASE = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus'
MAIN_JS = os.path.join(BASE, 'assets', 'js', 'menu-data.js')

with open(MAIN_JS, 'r', encoding='utf-8') as f:
    content = f.read()

imgs = re.findall(r'"image":\s*"([^"]+)"', content)
# Show first 30 to understand the pattern
for img in imgs[:30]:
    print(img)
print(f"\nTotal image refs: {len(imgs)}")

# Check if any of the 404 filenames appear
test_names = ['cocacola', 'fanta', 'sprite', 'mezzo', 'uludag', 'fritz', 'superzero', 'christinen', 'salgam']
for name in test_names:
    matches = [i for i in imgs if name in i]
    if matches:
        print(f"\nFOUND {name}: {matches}")
    else:
        print(f"\nNot found: {name}")
