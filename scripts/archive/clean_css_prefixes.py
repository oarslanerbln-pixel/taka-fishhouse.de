import re
import glob

def dedup_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find duplicate -webkit-backdrop-filter lines
    pattern = r'(-webkit-backdrop-filter:\s*blur\([^)]+\);\s*)\1'
    new_content = re.sub(pattern, r'\1', content)

    # Find duplicate backdrop-filter lines
    pattern2 = r'(backdrop-filter:\s*blur\([^)]+\);\s*)\1'
    new_content = re.sub(pattern2, r'\1', new_content)

    if content != new_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed duplicates in {filepath}")

for css_file in glob.glob('qr-menu/**/*.css', recursive=True):
    dedup_file(css_file)
