import re

filepath = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\css\style.css'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the old PREMIUM TITLE SEA ANIMATION block from style.css
# so it doesn't override the new title-sea.css
content = re.sub(
    r'/\* PREMIUM TITLE SEA ANIMATION \*/.*',
    '/* title-sea animation is handled by assets/css/title-sea.css */',
    content,
    flags=re.DOTALL
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed old animation from style.css — title-sea.css now controls it.")
