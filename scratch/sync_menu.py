import json
import codecs

with codecs.open(r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\scratch\menu_dump.json", "r", encoding="utf-8") as f:
    data = json.load(f)

all_items = []
for cat in data:
    for item in cat.get('items', []):
        all_items.append(item)

def find_item_by_name(name_tr):
    for item in all_items:
        if item.get('nameTR') == name_tr:
            return item.copy()
    return None

def find_item_by_id(item_id):
    for item in all_items:
        if item.get('id') == item_id:
            return item.copy()
    return None

ordered_categories = [
    {
        "categoryId": "corbalar", "categoryTR": "Çorbalar", "categoryDE": "Suppen", "categoryEN": "Soups", "categoryES": "Sopas", "categoryRU": "Супы", "categoryAR": "الشوربات", "icon": "fa-bowl-food",
        "items": [
            find_item_by_id(1)
        ]
    },
    {
        "categoryId": "salatalar", "categoryTR": "Salatalar", "categoryDE": "Salate", "categoryEN": "Salads", "categoryES": "Ensaladas", "categoryRU": "Салаты", "categoryAR": "سلطات", "icon": "fa-leaf",
        "items": [
            find_item_by_id(4), find_item_by_id(5), find_item_by_id(6), find_item_by_id(7), find_item_by_id(8), find_item_by_id(9)
        ]
    },
    {
        "categoryId": "soguk-mezeler", "categoryTR": "Soğuk Mezeler", "categoryDE": "Kalte Vorspeisen", "categoryEN": "Cold Appetizers", "categoryES": "Aperitivos Fríos", "categoryRU": "Холодные Закуски", "categoryAR": "مقبلات باردة", "icon": "fa-plate-wheat",
        "items": [
            find_item_by_id(13), find_item_by_id(14), find_item_by_id(15), find_item_by_id(16), find_item_by_id(17), find_item_by_id(18), find_item_by_id(19), find_item_by_id(21), find_item_by_id(22), find_item_by_id(23), find_item_by_id(27), find_item_by_id(30), find_item_by_id(31), find_item_by_id(32), find_item_by_id(35), find_item_by_id(10)
        ]
    },
    {
        "categoryId": "ara-sicaklar", "categoryTR": "Ara Sıcaklar", "categoryDE": "Warme Zwischengerichte", "categoryEN": "Hot Appetizers", "categoryES": "Aperitivos Calientes", "categoryRU": "Горячие Закуски", "categoryAR": "مقبلات ساخنة", "icon": "fa-fire-burner",
        "items": [
            {
                "id": 24, "nameTR": "Çıtır Karides", "nameDE": "Crispy Garnellen", "nameEN": "Crispy Shrimp", "nameES": "Camarones Crujientes", "nameRU": "Хрустящие Креветки", "nameAR": "جمبري مقرمش",
                "descTR": "", "descDE": "", "descEN": "", "descES": "", "descRU": "", "descAR": "",
                "price": 22.50, "image": ""
            },
            find_item_by_id(38), find_item_by_id(39), find_item_by_id(41), find_item_by_id(42), find_item_by_id(43), find_item_by_id(44), find_item_by_id(45), find_item_by_id(46), find_item_by_id(47), find_item_by_id(49), find_item_by_id(50)
        ]
    },
    {
        "categoryId": "ana-yemekler", "categoryTR": "Ana Yemekler", "categoryDE": "Hauptgerichte", "categoryEN": "Main Courses", "categoryES": "Platos Principales", "categoryRU": "Главные Блюда", "categoryAR": "الأطباق الرئيسية", "icon": "fa-fish-fins",
        "items": [
            find_item_by_id(61), find_item_by_id(62), find_item_by_id(63), find_item_by_name("Barbun"), find_item_by_name("Uskumru"), find_item_by_id(67), find_item_by_id(68), find_item_by_id(71), find_item_by_id(72), find_item_by_id(73), find_item_by_id(74), find_item_by_id(75), find_item_by_id(76), find_item_by_id(77), find_item_by_id(78), find_item_by_id(80), find_item_by_id(81)
        ]
    },
    {
        "categoryId": "balik-ekmek", "categoryTR": "Balık Sandviç / Dürüm", "categoryDE": "Fisch Sandwich / Dürüm", "categoryEN": "Fish Sandwich / Wrap", "categoryES": "Sándwich de Pescado / Wrap", "categoryRU": "Рыбный Сэндвич / Шаурма", "categoryAR": "ساندويتش سمك / دوروم", "icon": "fa-hotdog",
        "items": [
            find_item_by_id(90), find_item_by_id(91), find_item_by_id(92), find_item_by_id(93), find_item_by_id(94), find_item_by_id(98), find_item_by_id(99), find_item_by_id(100), find_item_by_id(101), find_item_by_id(102)
        ]
    },
    {
        "categoryId": "cocuk-menusu", "categoryTR": "Çocuk Menüsü & Makarnalar", "categoryDE": "Kindermenü & Nudeln", "categoryEN": "Kids Menu & Pastas", "categoryES": "Menú Infantil y Pastas", "categoryRU": "Детское Меню и Пасты", "categoryAR": "قائمة الأطفال والمعكرونة", "icon": "fa-child",
        "items": [
            find_item_by_name("Balık Burger, Kızarmış Patates, İçecek"),
            find_item_by_name("Balık Köfte, Kızarmış Patates veya Pilav, İçecek"),
            find_item_by_id(112), find_item_by_id(113)
        ]
    },
    {
        "categoryId": "tatlilar", "categoryTR": "Tatlılar", "categoryDE": "Desserts", "categoryEN": "Desserts", "categoryES": "Postres", "categoryRU": "Десерты", "categoryAR": "حلويات", "icon": "fa-ice-cream",
        "items": [
            find_item_by_id(116), find_item_by_id(118), find_item_by_id(122), find_item_by_id(120)
        ]
    },
    {
        "categoryId": "soguk-icecekler", "categoryTR": "Soğuk İçecekler", "categoryDE": "Kalte Getränke", "categoryEN": "Cold Drinks", "categoryES": "Bebidas Frías", "categoryRU": "Холодные Напитки", "categoryAR": "مشروبات باردة", "icon": "fa-glass-water",
        "items": [
            find_item_by_id(130), find_item_by_id(131), find_item_by_id(132), find_item_by_id(4816), find_item_by_id(134), find_item_by_id(135), find_item_by_id(136), find_item_by_id(137), find_item_by_id(138), find_item_by_id(139), find_item_by_id(141), find_item_by_id(143), find_item_by_id(144), find_item_by_id(7892), find_item_by_id(147), find_item_by_id(148), find_item_by_id(142), find_item_by_id(140), find_item_by_id(9584), find_item_by_id(145)
        ]
    },
    {
        "categoryId": "sicak-icecekler", "categoryTR": "Sıcak İçecekler", "categoryDE": "Warme Getränke", "categoryEN": "Hot Drinks", "categoryES": "Bebidas Calientes", "categoryRU": "Горячие Напитки", "categoryAR": "مشروبات ساخنة", "icon": "fa-mug-hot",
        "items": [
            find_item_by_id(91), find_item_by_id(911), find_item_by_id(92), find_item_by_id(97), find_item_by_id(163), find_item_by_id(164), find_item_by_id(165), find_item_by_id(167)
        ]
    }
]

# Ensure no Nones are in the list
for cat in ordered_categories:
    cat['items'] = [item for item in cat['items'] if item is not None]

# Fix the duplicate IDs for Barbun and Balık Burger
for item in ordered_categories[6]['items']:
    if item['nameTR'] == "Balık Burger, Kızarmış Patates, İçecek":
        item['id'] = 650
    if item['nameTR'] == "Balık Köfte, Kızarmış Patates veya Pilav, İçecek":
        item['id'] = 660

for item in ordered_categories[4]['items']:
    if item['nameTR'] == "Barbun":
        item['id'] = 65
    if item['nameTR'] == "Uskumru":
        item['id'] = 66

new_data_str = json.dumps(ordered_categories, indent=4, ensure_ascii=False)
final_content = f"const menuData = {new_data_str};\n\nwindow.menuData = menuData;\n"

file_path = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\js\menu-data.js"
with codecs.open(file_path, "w", encoding="utf-8") as f:
    f.write(final_content)

print("SUCCESS")
