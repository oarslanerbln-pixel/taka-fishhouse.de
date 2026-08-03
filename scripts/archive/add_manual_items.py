import json
import os

MENU_JS = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\js\menu-data.js'

new_items = [
    {
        "cat_id": "kindermenu",
        "nameTR": "Balık Burger, Kızarmış Patates, İçecek",
        "nameDE": "Fisch-Burger, Pommes, Getränk nach Wahl",
        "price": "16,00",
        "id": 65
    },
    {
        "cat_id": "kindermenu",
        "nameTR": "Balık Köfte, Kızarmış Patates veya Pilav, İçecek",
        "nameDE": "Fisch-Bouletten, Pommes oder Reis, Getränk nach Wahl",
        "price": "16,00",
        "id": 66
    },
    {
        "cat_id": "hauptgerichte",
        "nameTR": "Somonlu Makarna, özel sos ile",
        "nameDE": "Nudeln mit Lachsfilet in hausgemachter Soße",
        "price": "20,00",
        "id": 67
    },
    {
        "cat_id": "hauptgerichte",
        "nameTR": "Karidesli Makarna, özel sos ile",
        "nameDE": "Nudeln mit Garnelen in hausgemachter Soße",
        "price": "20,00",
        "id": 68
    },
    {
        "cat_id": "desserts",
        "nameTR": "Kızarmış Dondurma",
        "nameDE": "Fritierte Eiscreme",
        "price": "9,00",
        "id": 69
    },
    {
        "cat_id": "desserts",
        "nameTR": "Dondurmalı İrmik Helvası",
        "nameDE": "Warmer Grieß-Halva mit Eis",
        "price": "9,00",
        "id": 70
    },
    {
        "cat_id": "desserts",
        "nameTR": "Fırında 'Meyhane' Helvası",
        "nameDE": "Gebackener 'Kneipen' Halva",
        "price": "7,90",
        "id": 71
    },
    {
        "cat_id": "desserts",
        "nameTR": "Çilekli Magnolia",
        "nameDE": "Erdbeer Magnolia",
        "price": "5,90",
        "id": 72
    },
    {
        "cat_id": "desserts",
        "nameTR": "Hamsiköy Sütlacı (Fırın Sütlaç)",
        "nameDE": "Türkischer Milchreis aus dem Ofen",
        "price": "5,90",
        "id": 73
    }
]

hot_drinks = [
    {
        "cat_id": "getranke",
        "nameTR": "Türk Çayı (Küçük)",
        "nameDE": "Türkischer Tee klein",
        "price": "1,50",
        "id": 91
    },
    {
        "cat_id": "getranke",
        "nameTR": "Türk Çayı (Büyük)",
        "nameDE": "Türkischer Tee groß",
        "price": "2,50",
        "id": 911
    },
    {
        "cat_id": "getranke",
        "nameTR": "Çay Çeşitleri",
        "nameDE": "Verschiedene Teesorten",
        "price": "2,50",
        "id": 92
    },
    {
        "cat_id": "getranke",
        "nameTR": "Café Cream",
        "nameDE": "Café Cream",
        "price": "3,50",
        "id": 94
    },
    {
        "cat_id": "getranke",
        "nameTR": "Cappucino",
        "nameDE": "Cappucino",
        "price": "3,50",
        "id": 95
    },
    {
        "cat_id": "getranke",
        "nameTR": "Café Latte",
        "nameDE": "Café latte",
        "price": "3,50",
        "id": 96
    },
    {
        "cat_id": "getranke",
        "nameTR": "Espresso",
        "nameDE": "Espresso",
        "price": "3,00",
        "id": 97
    },
    {
        "cat_id": "getranke",
        "nameTR": "Türk Kahvesi",
        "nameDE": "Türkischer Mokka",
        "price": "3,00",
        "id": 98
    }
]

new_items.extend(hot_drinks)

with open(MENU_JS, 'r', encoding='utf-8') as f:
    js_content = f.read()

json_str = js_content.split('const menuData = ')[1].split(';\n\nwindow.menuData')[0]
data = json.loads(json_str)

for cat in data:
    cat_items = cat['items']
    existing_ids = [str(item.get('id', '')) for item in cat_items]
    
    for new_item in new_items:
        if new_item['cat_id'] == cat['categoryId'] and str(new_item['id']) not in existing_ids:
            # We copy nameDE to EN, RU, ES, AR for now, the UI uses DE by default or we can translate later.
            cat_items.append({
                "id": new_item["id"],
                "nameTR": new_item["nameTR"],
                "nameDE": new_item["nameDE"],
                "nameEN": new_item["nameDE"],
                "nameRU": new_item["nameDE"],
                "nameES": new_item["nameDE"],
                "nameAR": new_item["nameDE"],
                "price": new_item["price"]
            })

new_js = f"const menuData = {json.dumps(data, indent=4, ensure_ascii=False)};\n\nwindow.menuData = menuData;\n"

with open(MENU_JS, 'w', encoding='utf-8') as f:
    f.write(new_js)

print("Added manual items using JSON parse.")
