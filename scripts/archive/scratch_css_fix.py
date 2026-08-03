import re

files = [
    r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\css\style.css',
    r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\css\menu-page.css',
    r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\css\menu-page.css',
]

def fix_css_prefixes(content):
    lines = content.split('\n')
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.lstrip()
        indent = line[:len(line) - len(stripped)]
        
        # Check if this line is a bare backdrop-filter (without -webkit- prefix)
        if re.match(r'\s*backdrop-filter\s*:', line) and not re.match(r'\s*-webkit-backdrop-filter\s*:', line):
            # Check if previous line already has -webkit-backdrop-filter
            prev_stripped = result[-1].strip() if result else ''
            if not prev_stripped.startswith('-webkit-backdrop-filter'):
                # Add webkit prefix before this line
                webkit_line = indent + '-webkit-' + stripped
                result.append(webkit_line)
        
        # Check if this line is a bare user-select (without -webkit- prefix)
        elif re.match(r'\s*user-select\s*:', line) and not re.match(r'\s*-webkit-user-select\s*:', line):
            prev_stripped = result[-1].strip() if result else ''
            if not prev_stripped.startswith('-webkit-user-select'):
                webkit_line = indent + '-webkit-' + stripped
                result.append(webkit_line)
        
        result.append(line)
        i += 1
    
    return '\n'.join(result)

for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        fixed = fix_css_prefixes(content)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(fixed)
        
        print(f"Fixed: {f}")
    except FileNotFoundError:
        print(f"NOT FOUND: {f}")

print("Done.")
