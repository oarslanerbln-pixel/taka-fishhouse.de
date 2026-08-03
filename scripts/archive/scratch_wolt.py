import urllib.request
import json

# Try alternate Wolt API endpoints
urls = [
    "https://restaurant-api.wolt.com/v3/venues/slug/taka-fish-house-kottbusserdamm",
    "https://restaurant-api.wolt.com/v3/menus/slug/taka-fisch-haus",
    "https://consumer-api.wolt.com/v2/venues/slug/taka-fish-house-kottbusserdamm/menu",
    "https://restaurant-api.wolt.com/v3/venues/slug/taka-fisch-haus",
]
for url in urls:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"OK: {url}")
            data = json.load(resp)
            print(f"Top keys: {list(data.keys())[:5]}")
            with open("wolt_menu.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            break
    except Exception as e:
        print(f"FAIL: {url} -> {e}")
