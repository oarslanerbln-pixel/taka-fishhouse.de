import urllib.request
import json

# Try UberEats API / feed endpoint
urls = [
    "https://www.ubereats.com/api/getStoreV1?storeUuid=f1c3afad-bda0-480f-a821-94dcbe7078bb",
    "https://api.uber.com/v2/eats/stores/f1c3afad-bda0-480f-a821-94dcbe7078bb/menus",
]

# Try Lieferando API 
lieferando_urls = [
    "https://cst.lieferando.de/api/v3/restaurant/by-restaurant-slug/taka-fisch-haus-berlin?lat=52.4946&lng=13.4272",
    "https://cst.lieferando.de/api/v3/restaurant/by-restaurant-slug/taka-fisch-haus?lat=52.4946&lng=13.4272",
]

print("=== Trying Lieferando ===")
for url in lieferando_urls:
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
    })
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"OK: {url}")
            data = json.load(resp)
            print(f"Top keys: {list(data.keys())[:5]}")
            # Search for fritz, hamsi etc
            text = json.dumps(data)
            for term in ["fritz", "rotbarbe", "hamsi", "oktopus", "seezunge"]:
                if term.lower() in text.lower():
                    print(f"  FOUND: {term}")
            with open("lieferando_fresh.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            break
    except Exception as e:
        print(f"FAIL: {url} -> {e}")
