import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\js\menu-data.js', encoding='utf-8') as f:
    content = f.read()

# Find all item blocks
items = re.findall(r'\{[^{}]+\}', content, re.DOTALL)

missing = []
has_image = []

for item in items:
    name_match = re.search(r'"nameDE":\s*"([^"]+)"', item)
    if name_match:
        name = name_match.group(1)
        if '"image"' not in item:
            missing.append(name)
        else:
            img_match = re.search(r'"image":\s*"([^"]+)"', item)
            img = img_match.group(1) if img_match else "?"
            has_image.append((name, img))

print(f"=== Items WITHOUT image ({len(missing)}) ===")
for n in missing:
    print(f"  MISSING: {n}")

print(f"\n=== Items WITH image ({len(has_image)}) ===")
for n, img in has_image:
    print(f"  OK: {n} -> {img}")
