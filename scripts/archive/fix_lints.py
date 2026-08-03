import re
import glob
import os

def fix_css_prefixes(filepath):
    if not os.path.exists(filepath):
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content

    # 1. Fix user-select
    # Replace standalone user-select (that doesn't have -webkit- prefix before it)
    # We'll just do a global replace for common cases
    content = re.sub(r'(?<!-webkit-)(user-select:\s*[^;]+;)', r'-webkit-user-select: \1\n    \1', content)
    # The regex above might duplicate if we run it multiple times blindly, so let's be careful.
    # A safer approach is to find all blocks and process line by line.

    # 2. Fix backdrop-filter ordering and missing prefixes
    # We want:
    # -webkit-backdrop-filter: blur(...);
    # backdrop-filter: blur(...);
    
    # First, let's remove ALL backdrop-filter and -webkit-backdrop-filter lines 
    # and replace them with a single marker temporarily, then put the correct pair back.
    # Actually, simpler: just find any backdrop filter line and ensure the pair exists.
    
    lines = content.split('\n')
    new_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # User-select fix
        if 'user-select:' in line and '-webkit-user-select' not in line and 'none' in line.lower():
             # Check if previous line had webkit
             if i == 0 or '-webkit-user-select' not in lines[i-1]:
                 indent = line[:len(line) - len(line.lstrip())]
                 val = line.split(':')[1].strip()
                 new_lines.append(f"{indent}-webkit-user-select: {val}")
        
        # Backdrop-filter fix
        if 'backdrop-filter:' in line:
            indent = line[:len(line) - len(line.lstrip())]
            val = line.split('backdrop-filter:')[1].strip()
            
            # Skip if we already added it (handling consecutive duplicates that our previous dedup missed, or if we process the webkit one first)
            if 'webkit' in line:
                # It's a webkit line. 
                # Let's peek ahead to see if the standard one is next. If not, add it.
                new_lines.append(line)
                if i + 1 >= len(lines) or 'backdrop-filter:' not in lines[i+1] or '-webkit-' in lines[i+1]:
                    new_lines.append(f"{indent}backdrop-filter: {val}")
            else:
                # It's a standard line.
                # Check if previous line was webkit. If yes, we are good (it's in right order).
                # If previous was webkit but AFTER standard, that's wrong order.
                if i > 0 and '-webkit-backdrop-filter:' in new_lines[-1]:
                    new_lines.append(line) # Correct order
                else:
                    # Missing webkit or wrong order.
                    # Let's see if next line is webkit (wrong order).
                    if i + 1 < len(lines) and '-webkit-backdrop-filter:' in lines[i+1]:
                        # Swap them
                        val_webkit = lines[i+1].split('backdrop-filter:')[1].strip()
                        new_lines.append(f"{indent}-webkit-backdrop-filter: {val_webkit}")
                        new_lines.append(line)
                        i += 1 # skip the next line
                    else:
                        # Just missing webkit
                        new_lines.append(f"{indent}-webkit-backdrop-filter: {val}")
                        new_lines.append(line)
            i += 1
            continue
            
        new_lines.append(line)
        i += 1

    final_content = '\n'.join(new_lines)
    
    # Clean up any potential triple duplicates if the logic above got confused by existing mess
    final_content = re.sub(r'(\s*-webkit-backdrop-filter:[^\n]+\n)\1+', r'\1', final_content)
    final_content = re.sub(r'(\s*backdrop-filter:[^\n]+\n)\1+', r'\1', final_content)

    if final_content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(final_content)
        print(f"Fixed lint errors in {filepath}")

css_files = [
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\css\style.css",
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\css\style.css",
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\css\menu-page.css",
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\css\menu-page.css"
]

for f in css_files:
    fix_css_prefixes(f)

