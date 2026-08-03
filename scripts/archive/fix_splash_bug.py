import os
import re

js_path = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\js\main.js"
with open(js_path, 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

# Replace the wrong splash ID
# from const splash = document.getElementById('karadenizSplash');
# to a code that checks for BOTH possible IDs:

fix_code = '''
    const splash1 = document.getElementById('premium-splash');
    if (splash1) {
        setTimeout(() => splash1.classList.add('hidden'), 2800);
    }
    const splash2 = document.getElementById('karadenizSplash');
    if (splash2) {
        setTimeout(() => splash2.classList.add('hidden'), 2800);
    }
'''

# we can just inject this at the top of DOMContentLoaded
if 'premium-splash' not in c:
    c = c.replace("const splash = document.getElementById('karadenizSplash');", fix_code + "\n//")

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(c)

print("main.js SPLASH BUG FIXED!")

