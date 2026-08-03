import requests
import json

url = "https://restaurant-api.wolt.com/v3/menus/slug/taka-fish-house-kottbusserdamm"
headers = {"User-Agent": "Mozilla/5.0"}
res = requests.get(url, headers=headers)
print("Status:", res.status_code)
if res.status_code == 200:
    with open("wolt_menu.json", "w", encoding="utf-8") as f:
        json.dump(res.json(), f, indent=2, ensure_ascii=False)
