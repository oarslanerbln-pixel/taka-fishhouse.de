import json
import codecs

with codecs.open(r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\scratch\menu_dump.json", "r", "utf-8") as f:
    dump = json.load(f)

items_by_id = {}
for cat in dump:
    for item in cat.get('items', []):
        items_by_id[item['id']] = item['nameTR']

print("IDs in Ana Yemekler:", [61, 62, 63, 'Barbun', 'Uskumru', 67, 68, 71, 72, 73, 74, 75, 76, 77, 78, 80, 81])
for i in [61, 62, 63, 65, 66, 67, 68, 71, 72, 73, 74, 75, 76, 77, 78, 80, 81]:
    print(f"ID {i}: {items_by_id.get(i, 'Not Found')}")
