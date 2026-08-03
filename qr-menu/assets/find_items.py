import json
import codecs

with codecs.open('c:\\Users\\oarsl\\Desktop\\Is Dosyasi\\Taka Fisch Haus\\qr-menu\\assets\\js\\menu-data.js', 'r', 'utf-8') as f:
    content = f.read()
    
# Find the string `const menuData = [` and `];` and parse it
start = content.find('const menuData = [')
end = content.rfind('];') + 1
if start != -1 and end != -1:
    json_str = content[start + 17:end]
    # In JS, properties are unquoted sometimes, but here they seem to be quoted.
    try:
        import js2py
        # Actually js2py is probably not available.
    except:
        pass
        
import re
items = re.findall(r'"nameTR":\s*"([^"]+)",\s*"nameDE":\s*"([^"]+)"', content)
for tr, de in items:
    if 'Sand' in de or 'Sand' in tr or 'Sup' in de or 'Çorba' in tr or 'Lachs' in de:
        print(f"TR: {tr} | DE: {de}")
