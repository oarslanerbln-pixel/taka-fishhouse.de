import json

files = [r'assets\js\menu-data.js', r'qr-menu\assets\js\menu-data.js']
for file_path in files:
    content = open(file_path, encoding='utf-8').read()
    json_str = content.split('const menuData = ')[1].split(';\n')[0]
    if 'window.menuData = menuData;' in json_str:
        json_str = json_str.replace('window.menuData = menuData;', '')
    data = json.loads(json_str)

    found_cacik = False
    found_borulce = False

    for cat in data:
        for item in cat['items']:
            name = item['nameTR']
            if 'Cacık' in name:
                item['image'] = 'assets/img/products/cacik.jpg'
                found_cacik = True
            elif 'Börülcesi' in name:
                item['image'] = 'assets/img/products/deniz-borulcesi.jpg'
                found_borulce = True

    new_js = 'const menuData = ' + json.dumps(data, indent=4, ensure_ascii=False) + ';\n'
    if 'window.menuData = menuData;' in content:
        new_js += '\nwindow.menuData = menuData;\n'
    open(file_path, 'w', encoding='utf-8').write(new_js)
    print(f'Updated {file_path}: Cacik={found_cacik}, Borulce={found_borulce}')
