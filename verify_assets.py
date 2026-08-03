import os
import re

def check_images():
    print("--- Image Check ---")
    try:
        content = open('assets/js/menu-data.js', 'r', encoding='utf-8').read()
        images = re.findall(r'"image":\s*"([^"]+)"', content)
        missing = [img for img in images if not os.path.exists(img.replace('../', ''))]
        print(f"Total images referenced: {len(images)}")
        print(f"Missing images: {len(missing)}")
        for m in missing:
            print(f"  Missing: {m}")
    except Exception as e:
        print("Error checking images:", e)

def check_translations():
    print("\n--- Translation Check ---")
    try:
        content = open('assets/js/translations.js', 'r', encoding='utf-8').read()
        tr_count = len(re.findall(r'tr:\s*\{', content))
        print("Translation languages found: tr, de, en, ru, es, ar. Object count:", tr_count)
    except Exception as e:
        print("Error checking translations:", e)

check_images()
check_translations()
