import json
import re
import codecs

file_path = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\js\menu-data.js"
with codecs.open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

match = re.search(r"const menuData = (\[.*?\]);\s*window\.menuData", content, re.DOTALL)
if match:
    data_str = match.group(1)
    data = json.loads(data_str)
    
    with codecs.open(r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\scratch\menu_dump.json", "w", encoding="utf-8") as out:
        json.dump(data, out, indent=2, ensure_ascii=False)
