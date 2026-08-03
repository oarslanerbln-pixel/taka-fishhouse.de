import requests
import re

links = {
    "buyuk_cay": "https://share.google/1Fzr2ZLYNFIg5WgQZ",
    "kucuk_cay": "https://share.google/vHPLEFKeMLn1aIdbk",
    "ayran_7gun": "https://share.google/iGyx73OdnyOMmKKhI",
    "kaffee_crema": "https://share.google/dtEUiBIgtWj5RCqLn",
    "kaffee_latte": "https://share.google/lbNdpibrFFxfYGe1e",
    "turk_mokka": "https://share.google/vMswTF9rHtC9IDd9J",
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

for name, url in links.items():
    try:
        r = requests.get(url, headers=headers, allow_redirects=True)
        html = r.text
        match = re.search(r'<meta[^>]*property="og:image"[^>]*content="([^"]+)"', html, re.IGNORECASE)
        if match:
            print(f"{name}: {match.group(1)}")
        else:
            print(f"{name}: No og:image found")
    except Exception as e:
        print(f"Error {name}: {e}")
