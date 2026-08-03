import os

js_path = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\js\main.js"
with open(js_path, 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

bad_code = '''//
    if (splash) {
        setTimeout(() => {
            splash.classList.add('hidden');
        }, 2800); // CSS animasyon 2.1s + 0.7s fade = 2.8s total
    }'''

c = c.replace(bad_code, "")

# in case it has different spaces:
import re
c = re.sub(r'if\s*\(\s*splash\s*\)\s*\{\s*setTimeout\(\s*\(\s*\)\s*=>\s*\{\s*splash\.classList\.add\(\'hidden\'\);\s*\}\s*,\s*2800\);\s*//.*?\s*\}', '', c, flags=re.DOTALL)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(c)

print("main.js SPLASH IS NOT DEFINED bug fixed!")
