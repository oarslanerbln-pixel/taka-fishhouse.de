import codecs, json
def fix_menu(filepath):
    content = codecs.open(filepath, 'r', 'utf8').read()
    prefix = 'const menuData = '
    suffix = ';\n\nwindow.menuData = menuData;\n'
    if not content.startswith(prefix): return
    json_str = content[len(prefix):].split('window.menuData')[0].strip()
    if json_str.endswith(';'): json_str = json_str[:-1]
    data = json.loads(json_str)
    
    for cat in data:
        if cat['categoryId'] == 'desserts':
            filtered = [i for i in cat['items'] if i.get('id') not in [71, 73]]
            cat['items'] = filtered
            
    new_content = prefix + json.dumps(data, indent=4, ensure_ascii=False) + suffix
    codecs.open(filepath, 'w', 'utf8').write(new_content)

fix_menu('assets/js/menu-data.js')
fix_menu('qr-menu/assets/js/menu-data.js')
