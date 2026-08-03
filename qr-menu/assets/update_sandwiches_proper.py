import codecs

file_path = 'c:\\Users\\oarsl\\Desktop\\Is Dosyasi\\Taka Fisch Haus\\qr-menu\\assets\\js\\menu-data.js'
with codecs.open(file_path, 'r', 'utf-8') as f:
    lines = f.readlines()

updates = {
    "Lachs Sandwich": "assets/lachs_sandwich_v2_ai.png",
    "Dorade Sandwich": "assets/dorade_sandwich_v2_ai.png",
    "Makrele Sandwich": "assets/makrele_sandwich_v2_ai.png",
    "Sardine Sandwich": "assets/sardine_sandwich_v2_ai.png",
    "Garnele Sandwich": "assets/garnele_sandwich_v2_ai.png",
    "Lachs Dürüm": "assets/lachs_durum_ai.png",
    "Dorade Dürüm": "assets/dorade_durum_ai.png",
    "Makrele Dürüm": "assets/makrele_durum_ai.png",
    "Sardine Dürüm": "assets/sardine_durum_ai.png",
    "Garnele Dürüm": "assets/garnele_durum_ai.png",
    "Lachssuppe": "assets/lachssuppe_ai.png"
}

current_name = None
for i in range(len(lines)):
    line = lines[i]
    if '"nameDE"' in line:
        # Extract nameDE value
        parts = line.split('"')
        if len(parts) >= 4:
            current_name = parts[3]
    elif '"image"' in line and current_name in updates:
        # Replace image path
        parts = line.split('"')
        if len(parts) >= 4:
            old_image = parts[3]
            new_image = updates[current_name]
            lines[i] = line.replace(old_image, new_image)
        # Reset current_name after replacing image for this item
        current_name = None

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.writelines(lines)

print("Updated menu-data.js successfully.")
