import re
import os

css_files = [
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\css\style.css",
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\css\menu-page.css",
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\css\style.css",
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\css\menu-page.css"
]

for filepath in css_files:
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove all backdrop-filter (without webkit) completely to start fresh
    content = re.sub(r'^[ \t]*backdrop-filter:[^\n]+\n', '', content, flags=re.MULTILINE)
    
    # Now for every -webkit-backdrop-filter, add the standard one right after it
    # We capture the leading whitespace to maintain indentation
    content = re.sub(r'^([ \t]*)-webkit-backdrop-filter:([^\n]+)', r'\1-webkit-backdrop-filter:\2\n\1backdrop-filter:\2', content, flags=re.MULTILINE)

    # Clean up user-select similarly
    content = re.sub(r'^[ \t]*user-select:[^\n]+\n', '', content, flags=re.MULTILINE)
    content = re.sub(r'^([ \t]*)-webkit-user-select:([^\n]+)', r'\1-webkit-user-select:\2\n\1user-select:\2', content, flags=re.MULTILINE)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        print(f"Fixed {filepath}")
