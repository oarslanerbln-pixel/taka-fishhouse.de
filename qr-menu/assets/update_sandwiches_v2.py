import codecs
import re

file_path = 'c:\\Users\\oarsl\\Desktop\\Is Dosyasi\\Taka Fisch Haus\\qr-menu\\assets\\js\\menu-data.js'
with codecs.open(file_path, 'r', 'utf-8') as f:
    content = f.read()

updates = {
    "Lachs Sandwich": "assets/lachs_sandwich_v2_ai.png",
    "Dorade Sandwich": "assets/dorade_sandwich_v2_ai.png",
    "Makrele Sandwich": "assets/makrele_sandwich_v2_ai.png",
    "Sardine Sandwich": "assets/sardine_sandwich_v2_ai.png",
    "Garnele Sandwich": "assets/garnele_sandwich_v2_ai.png"
}

def replacer(match):
    name = match.group(1)
    if name in updates:
        return match.group(0).replace(match.group(2), updates[name])
    return match.group(0)

pattern = re.compile(r'("nameDE"\s*:\s*"([^"]+)".*?"image"\s*:\s*")([^"]+)(")', re.DOTALL)
new_content = pattern.sub(replacer, content)

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(new_content)

print("Updated menu-data.js with v2 sandwich images.")
