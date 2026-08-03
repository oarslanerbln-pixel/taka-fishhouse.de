import os
import urllib.request
import re

links = {
    "buyuk_cay": "https://share.google/1Fzr2ZLYNFIg5WgQZ",
    "kucuk_cay": "https://share.google/vHPLEFKeMLn1aIdbk",
    "ayran_7gun": "https://share.google/iGyx73OdnyOMmKKhI",
    "kaffee_crema": "https://share.google/dtEUiBIgtWj5RCqLn",
    "kaffee_latte": "https://share.google/lbNdpibrFFxfYGe1e",
    "turk_mokka": "https://share.google/vMswTF9rHtC9IDd9J",
}

for name, url in links.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8', errors='ignore')
            
        match = re.search(r'<meta[^>]*property="og:image"[^>]*content="([^"]+)"', html, re.IGNORECASE)
        if match:
            print(f"{name} og:image -> {match.group(1)}")
        else:
            print(f"{name} -> No og:image found. HTML snippet: {html[:200]}")
    except Exception as e:
        print(f"Error fetching {name}: {e}")

# Also check capri sonne
capri_path = r"C:\Users\oarsl\Desktop\capri-sun-orange-40-x-0-2l.htm"
if os.path.exists(capri_path):
    with open(capri_path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    imgs = re.findall(r'<img[^>]*src=["\'](http[^"\']+)["\']', html, re.IGNORECASE)
    print(f"\nCapri Sonne images found:")
    for img in set(imgs):
        if not img.endswith('.svg') and 'logo' not in img.lower():
            print(img)
