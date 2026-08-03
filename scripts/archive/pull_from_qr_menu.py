import os
import urllib.request

urls_to_check = [
    "https://qr-menu-two-delta.vercel.app/index.html",
    "https://qr-menu-two-delta.vercel.app/qr-menu/index.html",
    "https://qr-menu-two-delta.vercel.app/assets/css/style.css",
    "https://qr-menu-two-delta.vercel.app/assets/css/menu-page.css",
    "https://qr-menu-two-delta.vercel.app/menu.html"
]

base_dir = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus"

for url in urls_to_check:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            content = resp.read()
        
        # Save them back
        if "qr-menu/index" in url:
            path = os.path.join(base_dir, "qr-menu", "index.html")
        elif "style.css" in url:
            path = os.path.join(base_dir, "assets", "css", "style.css")
        elif "menu-page.css" in url:
            path = os.path.join(base_dir, "assets", "css", "menu-page.css")
        elif "/menu.html" in url:
            path = os.path.join(base_dir, "menu.html")
        else:
            path = os.path.join(base_dir, "index.html")
            
        with open(path, 'wb') as f:
            f.write(content)
        print(f"KURTARILDI: {url}")
    except Exception as e:
        print(f"CEKILEMEDI: {url} Hata: {e}")

