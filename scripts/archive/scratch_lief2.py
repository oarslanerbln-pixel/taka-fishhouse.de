import urllib.request
import json

# Try Lieferando public page API
url = "https://www.lieferando.de/en/menu/taka-fisch-haus"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
    # Look for next data / JSON embedded in page
    import re
    matches = re.findall(r'"imageUrl":"(https://[^"]+)"', html)
    print(f"Found {len(matches)} imageUrls in page")
    
    # Also look for __NEXT_DATA__
    nd = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html, re.DOTALL)
    if nd:
        data = json.loads(nd.group(1))
        with open("lieferando_nextdata.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print("Saved __NEXT_DATA__ to lieferando_nextdata.json")
    else:
        print("No __NEXT_DATA__ found")
        # Check what we have
        print(html[:500])
except Exception as e:
    print(f"Error: {e}")
