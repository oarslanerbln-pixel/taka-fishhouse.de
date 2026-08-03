import urllib.request
import json

urls = [
    "https://takeaway.com/api/restaurant/by-restaurant-slug/taka-fisch-haus-berlin",
    "https://api.lieferando.de/api/restaurant/by-restaurant-slug/taka-fisch-haus-berlin",
]

for url in urls:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"OK: {url}, status={resp.status}")
            break
    except Exception as e:
        print(f"FAIL: {url} -> {e}")

# Check if we have cached lieferando_data.json from before
import os
if os.path.exists("qr-menu/lieferando_data.json"):
    with open("qr-menu/lieferando_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"\nCached lieferando data type: {type(data)}")
    if isinstance(data, dict):
        print(f"Keys: {list(data.keys())[:10]}")
    elif isinstance(data, list):
        print(f"List len: {len(data)}")
        if data:
            print(f"First item keys: {list(data[0].keys())[:10]}")
