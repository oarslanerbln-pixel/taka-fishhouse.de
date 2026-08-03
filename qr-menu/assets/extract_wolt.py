import requests
import json
import re

url = "https://wolt.com/de/deu/berlin/restaurant/taka-fish-house-kottbusserdamm"
headers = {"User-Agent": "Mozilla/5.0"}
html = requests.get(url, headers=headers).text

# Extract __NEXT_DATA__
match = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html, re.DOTALL)
if match:
    data = json.loads(match.group(1))
    
    # We need to find items
    # Wolt usually stores menu items somewhere in the state
    with open("wolt_next_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
    print("Saved __NEXT_DATA__")
else:
    print("Could not find NEXT_DATA")
