import codecs
import re

file_path = 'c:\\Users\\oarsl\\Desktop\\Is Dosyasi\\Taka Fisch Haus\\qr-menu\\assets\\js\\menu-data.js'
with codecs.open(file_path, 'r', 'utf-8') as f:
    content = f.read()

updates = {
    "Lachs Sandwich": "assets/lachs_sandwich_ai.png",
    "Dorade Sandwich": "assets/dorade_sandwich_ai.png",
    "Makrele Sandwich": "assets/makrele_sandwich_ai.png",
    "Sardine Sandwich": "assets/sardine_sandwich_ai.png",
    "Garnele Sandwich": "assets/garnele_sandwich_ai.png",
    "Lachs Dürüm": "assets/lachs_durum_ai.png",
    "Dorade Dürüm": "assets/dorade_durum_ai.png",
    "Makrele Dürüm": "assets/makrele_durum_ai.png",
    "Sardine Dürüm": "assets/sardine_durum_ai.png",
    "Garnele Dürüm": "assets/garnele_durum_ai.png",
    "Lachssuppe": "assets/lachssuppe_ai.png"
}

def replacer(match):
    name = match.group(1)
    if name in updates:
        return match.group(0).replace(match.group(2), updates[name])
    return match.group(0)

# Pattern matches nameDE block then image block
pattern = re.compile(r'("nameDE"\s*:\s*"([^"]+)".*?"image"\s*:\s*")([^"]+)(")', re.DOTALL)
new_content = pattern.sub(replacer, content)

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(new_content)

print("Updated menu-data.js with new AI images.")
