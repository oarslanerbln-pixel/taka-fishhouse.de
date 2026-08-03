import json

files = [r'assets\js\menu-data.js', r'qr-menu\assets\js\menu-data.js']
for file_path in files:
    content = open(file_path, encoding='utf-8').read()
    json_str = content.split('const menuData = ')[1].split(';\n')[0]
    if 'window.menuData = menuData;' in json_str:
        json_str = json_str.replace('window.menuData = menuData;', '')
    data = json.loads(json_str)

    for cat in data:
        if cat['categoryId'] == 'getranke':
            # Remove logical duplicates
            to_remove_names = ['Çay (Küçük)', 'Çeşitli Çaylar', 'Cappucino']
            items = [it for it in cat['items'] if it['nameTR'] not in to_remove_names]
            
            # Define logical order keywords
            order_map = {
                'Su (0,25l)': 1,
                'Maden Suyu (0,25l)': 2,
                'Coca Cola (0,2l)': 3,
                'Coca Cola Zero (0,2l)': 4,
                'Coca-Cola Zero Sugar 0,2l': 4,
                'Fanta (0,2l)': 5,
                'Sprite (0,2l)': 6,
                'Mezzo Mix (0,2l)': 7,
                'Uludag Gazoz 0,25l': 8,
                'Çamlıca Gazoz (0,2l)': 9,
                '7gün Ayran (0,25l)': 10,
                'Şalgam Suyu (0,25l)': 11,
                'Fritz Cola (0,2l)': 12,
                'Fritz Cola Zero (0,2l)': 13,
                'Fritz Orange (0,2l)': 14,
                'FuzeTea (0,4l)': 15,
                'FuzeTea Pfirsich 0,4l': 15,
                'Schweppes (0,2l)': 16,
                'Christinen Elma Suyu (0,33l)': 17,
                'Christinen Multivitamin (0,33l)': 18,
                'Capri Sonne (0,2l)': 19,
                'Tymbark (0,25l)': 20,
                'Durstlöscher (0,5l)': 21,
                # Hot drinks at the end
                'Türk Çayı (Küçük)': 50,
                'Türk Çayı (Büyük)': 51,
                'Çay Çeşitleri': 52,
                'Türk Kahvesi': 53,
                'Espresso': 54,
                'Café Cream': 55,
                'Cappuccino': 56,
                'Café Latte': 57
            }
            
            # Deduplicate one more time just to be safe (e.g. FuzeTea vs FuzeTea Pfirsich)
            seen_names = set()
            dedup_items = []
            for it in items:
                name = it['nameTR']
                if name == 'FuzeTea (0,4l)' and 'FuzeTea' in str(seen_names):
                    continue
                if name == 'Coca-Cola Zero Sugar 0,2l' and 'Coca Cola Zero (0,2l)' in str(seen_names):
                    continue
                seen_names.add(name)
                dedup_items.append(it)
                
            def get_sort_key(item):
                return order_map.get(item['nameTR'], 99)
                
            dedup_items.sort(key=get_sort_key)
            cat['items'] = dedup_items

    new_js = 'const menuData = ' + json.dumps(data, indent=4, ensure_ascii=False) + ';\n'
    if 'window.menuData = menuData;' in content:
        new_js += '\nwindow.menuData = menuData;\n'
    open(file_path, 'w', encoding='utf-8').write(new_js)
    print(f'Reordered and cleaned drinks in {file_path}')
