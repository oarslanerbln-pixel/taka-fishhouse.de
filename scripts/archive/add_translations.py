import re
import os

new_keys = {
    'tr': """
        "hero-title-city": "Kreuzberg'te",
        "hero-title-breeze": "Karadeniz Esintisi",
        "sig-badge": "İmza Lezzetlerimiz",
        "sig-title": "Tabakta Bir Başyapıt",
        "sig-subtitle": "Karadeniz'in en taze mahsulleriyle, sıfır katkı maddesiyle hazırlanan özel tariflerimiz.",
        "form-name": "Ad Soyad",
        "form-phone": "Telefon",
        "form-date": "Tarih",
        "form-time": "Saat",
        "form-guests": "Kişi Sayısı",
        "form-guests-label": "kişi",
        "form-note": "Not (isteğe bağlı)",
        "res-submit": "Telefon ile Rezervasyon",
        "res-note-text": "Formu doldurup ararsanız daha hızlı hizmet alırsınız.",
""",
    'de': """
        "hero-title-city": "In Kreuzberg",
        "hero-title-breeze": "Schwarzmeer-Brise",
        "sig-badge": "Unsere Spezialitäten",
        "sig-title": "Ein Meisterwerk auf dem Teller",
        "sig-subtitle": "Unsere besonderen Rezepte, zubereitet mit den frischesten Zutaten und ganz ohne Zusatzstoffe.",
        "form-name": "Vor- und Nachname",
        "form-phone": "Telefon",
        "form-date": "Datum",
        "form-time": "Uhrzeit",
        "form-guests": "Personenanzahl",
        "form-guests-label": "Personen",
        "form-note": "Notiz (optional)",
        "res-submit": "Telefonisch reservieren",
        "res-note-text": "Füllen Sie das Formular aus und rufen Sie uns an für einen schnelleren Service.",
""",
    'en': """
        "hero-title-city": "In Kreuzberg",
        "hero-title-breeze": "Black Sea Breeze",
        "sig-badge": "Signature Dishes",
        "sig-title": "A Masterpiece on the Plate",
        "sig-subtitle": "Our special recipes prepared with the freshest ingredients and absolutely zero additives.",
        "form-name": "Full Name",
        "form-phone": "Phone",
        "form-date": "Date",
        "form-time": "Time",
        "form-guests": "Number of Guests",
        "form-guests-label": "people",
        "form-note": "Note (optional)",
        "res-submit": "Reserve via Phone",
        "res-note-text": "Fill out the form and call us for faster service.",
"""
}

files_to_update = [
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\js\translations.js",
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\js\translations.js"
]

for filepath in files_to_update:
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already added
    if '"form-name"' in content:
        print(f"Keys already exist in {filepath}")
        continue

    # Insert into tr block
    content = re.sub(r'(tr:\s*\{)(.*?)(\n\s*// Menu Page Specific|\n\s*\},)', r'\1\2' + new_keys['tr'].replace('\\', '\\\\') + r'\3', content, flags=re.DOTALL)
    
    # Insert into de block
    content = re.sub(r'(de:\s*\{)(.*?)(\n\s*// Menu Page Specific|\n\s*\},)', r'\1\2' + new_keys['de'].replace('\\', '\\\\') + r'\3', content, flags=re.DOTALL)
    
    # Insert into en block
    content = re.sub(r'(en:\s*\{)(.*?)(\n\s*// Menu Page Specific|\n\s*\},|\n\s*\})', r'\1\2' + new_keys['en'].replace('\\', '\\\\') + r'\3', content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        print(f"Updated {filepath}")
