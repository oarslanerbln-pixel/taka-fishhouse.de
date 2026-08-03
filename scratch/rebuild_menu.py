import json
import codecs

# 1. Load the dump
with codecs.open(r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\scratch\menu_dump.json", "r", "utf-8") as f:
    dump = json.load(f)

items_by_id = {}
for cat in dump:
    for item in cat.get('items', []):
        items_by_id[item['id']] = item

# Also need to find by name for the ones with string IDs or whatever
def find_item(query):
    if isinstance(query, int) or (isinstance(query, str) and query.isdigit()):
        return items_by_id.get(int(query))
    # Otherwise search by nameTR
    for it in items_by_id.values():
        if it['nameTR'] == query:
            return it
    return None

def create_item(id, nameTR, nameDE, price, image=""):
    return {
        "id": id,
        "nameTR": nameTR,
        "nameDE": nameDE,
        "nameEN": nameEN if 'nameEN' in locals() else nameDE,
        "price": price,
        "image": image,
        "allergens": ""
    }

# Build categories
corbalar = []
salatalar = []
soguk_mezeler = []
ara_sicaklar = []
spezialitaten = []
hauptgerichte = []
deniz_mahsulleri = []
tava_guvecler = []
balik_ekmek = []
cocuk_menusu = []
tatlilar = []
soguk_icecekler = []
sicak_icecekler = []

# Distribute items
for cat in dump:
    cat_id = cat.get('categoryId')
    for item in cat.get('items', []):
        name = item.get('nameTR', '').lower()
        if cat_id == 'suppen-salate':
            if 'çorba' in name or 'suppe' in item.get('nameDE', '').lower():
                corbalar.append(item)
            else:
                salatalar.append(item)
        elif cat_id == 'kalte-vorspeisen':
            soguk_mezeler.append(item)
        elif cat_id == 'warme-zwischengerichte':
            if any(x in name for x in ['karides', 'kalamar', 'midye', 'ahtapot', 'hamsi kuşu']):
                deniz_mahsulleri.append(item)
            else:
                ara_sicaklar.append(item)
        elif cat_id == 'hauptgerichte':
            # physical menu has Spezialitaten, Hauptgerichte, Deniz Mahsulleri, Tava
            if any(x in name for x in ['kalkan', 'lagos', 'kılıç', 'yılan']):
                spezialitaten.append(item)
            elif 'güveç' in name or 'kavurma' in name or 'buğulama' in name or 'tereyağında' in name:
                tava_guvecler.append(item)
            elif any(x in name for x in ['karides', 'kalamar', 'midye', 'ahtapot']):
                deniz_mahsulleri.append(item)
            else:
                hauptgerichte.append(item)
        elif cat_id == 'fisch-sandwich-durum':
            balik_ekmek.append(item)
        elif cat_id == 'kindermenu':
            cocuk_menusu.append(item)
        elif cat_id == 'desserts':
            if 'dondurma' in name and 'kızarmış' in name:
                continue # user asked to skip or update it, I will manually add the correct one later
            tatlilar.append(item)
        elif cat_id == 'getranke':
            if 'çay' in name or 'kahve' in name or 'espresso' in name or 'cream' in name:
                sicak_icecekler.append(item)
            else:
                soguk_icecekler.append(item)

# Add missing items
citir_karides = {
    "id": 9991, "nameTR": "Çıtır Karides", "nameDE": "Crispy Garnellen", "nameEN": "Crispy Shrimp", 
    "nameRU": "Хрустящие Креветки", "nameES": "Camarones Crujientes", "nameAR": "جمبري مقرمش",
    "price": "22,50", "image": "assets/img/placeholder.jpg" # Use placeholder if no image exists
}
deniz_mahsulleri.append(citir_karides)

taka_spesiyal_deniz = {
    "id": 9992, "nameTR": "Taka Deniz Mahsülleri Spesiyal", "nameDE": "Taka Meeresfrüchte Spezial", 
    "nameEN": "Taka Seafood Special", "nameRU": "Така Спешл Морепродукты", "nameES": "Especial Mariscos Taka", "nameAR": "طبق تاكا البحري الخاص",
    "price": "35,00", "image": "assets/img/placeholder.jpg"
}
deniz_mahsulleri.append(taka_spesiyal_deniz)

# The single portion fried ice cream:
fried_icecream = {
    "id": 121, "nameTR": "Kızarmış Dondurma (Tek Kişilik)", "nameDE": "Gebackenes Eis (Einzelportion)",
    "nameEN": "Fried Ice Cream (Single Portion)", "nameRU": "Жареное мороженое", "nameES": "Helado frito", "nameAR": "آيس كريم مقلي",
    "price": "8,50", "image": "assets/img/fried-ice-cream.jpg"
}
tatlilar.append(fried_icecream)

new_categories = [
    {"categoryId": "corbalar", "categoryTR": "Çorbalar", "categoryDE": "Suppen", "icon": "fa-bowl-food", "items": corbalar},
    {"categoryId": "salatalar", "categoryTR": "Salatalar", "categoryDE": "Salate", "icon": "fa-leaf", "items": salatalar},
    {"categoryId": "soguk-mezeler", "categoryTR": "Soğuk Mezeler", "categoryDE": "Kalte Vorspeisen", "icon": "fa-plate-wheat", "items": soguk_mezeler},
    {"categoryId": "ara-sicaklar", "categoryTR": "Ara Sıcaklar", "categoryDE": "Warme Zwischengerichte", "icon": "fa-fire-burner", "items": ara_sicaklar},
    {"categoryId": "spezialitaten", "categoryTR": "Taka Spesiyal", "categoryDE": "Spezialität des Hauses", "icon": "fa-star", "items": spezialitaten},
    {"categoryId": "hauptgerichte", "categoryTR": "Ana Yemekler", "categoryDE": "Hauptgerichte", "icon": "fa-fish-fins", "items": hauptgerichte},
    {"categoryId": "deniz-mahsulleri", "categoryTR": "Deniz Mahsülleri", "categoryDE": "Meeresfrüchte", "icon": "fa-shrimp", "items": deniz_mahsulleri},
    {"categoryId": "tava-guvecler", "categoryTR": "Tava ve Güveçler", "categoryDE": "Pfannen & Schmortöpfe", "icon": "fa-fire", "items": tava_guvecler},
    {"categoryId": "balik-ekmek", "categoryTR": "Balık Sandviç / Dürüm", "categoryDE": "Fisch Sandwich / Dürüm", "icon": "fa-hotdog", "items": balik_ekmek},
    {"categoryId": "cocuk-menusu", "categoryTR": "Çocuk Menüsü", "categoryDE": "Kindermenü", "icon": "fa-child", "items": cocuk_menusu},
    {"categoryId": "tatlilar", "categoryTR": "Tatlılar", "categoryDE": "Desserts", "icon": "fa-ice-cream", "items": tatlilar},
    {"categoryId": "soguk-icecekler", "categoryTR": "Soğuk İçecekler", "categoryDE": "Kalte Getränke", "icon": "fa-glass-water", "items": soguk_icecekler},
    {"categoryId": "sicak-icecekler", "categoryTR": "Sıcak İçecekler", "categoryDE": "Warme Getränke", "icon": "fa-mug-hot", "items": sicak_icecekler}
]

js_out = f"const menuData = {json.dumps(new_categories, indent=4, ensure_ascii=False)};\\n\\nwindow.menuData = menuData;\\n"

with codecs.open(r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\js\menu-data.js", "w", "utf-8") as f:
    f.write(js_out)

print("Menu successfully rebuilt!")
