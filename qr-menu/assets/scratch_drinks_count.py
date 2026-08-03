import re
js = open('qr-menu/assets/js/menu-data.js', encoding='utf-8').read()
drinks = re.findall(r'"categoryId"\s*:\s*"getranke"[\s\S]*?\]', js)
items = re.findall(r'"nameDE"', drinks[0]) if drinks else []
print('Drinks count:', len(items))
