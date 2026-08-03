import os
import re
import urllib.request

log_dir = r"c:\Users\oarsl\.gemini\antigravity-ide\brain\0ef7b752-cec1-4f33-8c81-3f6f4460c05e\.system_generated\tasks"
urls = set()

# Bütün task loglarindan Vercel Production URL'lerini cikar
for root, _, files in os.walk(log_dir):
    for f in files:
        if f.endswith('.log'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as logfile:
                content = logfile.read()
                found = re.findall(r'https://taka-fisch-haus-[a-z0-9]+-oarslanerbln-pixels-projects\.vercel\.app', content)
                for u in found:
                    urls.add(u)

print("Bulunan Deploy URL'leri:", urls)

# Her bir URL'den index.html cek ve "Karadeniz Esintisi" varsa MUKEMMEL SURUMDUR!
perfect_url = None
for u in urls:
    try:
        req = urllib.request.Request(u + "/index.html", headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            if 'title-sea' in html or 'Kreuzberg' in html: # Kreuzberg'te Karadeniz Esintisi
                print(f"BULDUM!! MUKEMMEL SURUM BU: {u}")
                perfect_url = u
                break
    except:
        pass

if perfect_url:
    # Simdi bu mukemmel surumden dosyalari gercekten geri cekelim!
    files_to_recover = {
        "index.html": "/index.html",
        "menu.html": "/menu.html",
        "qr-menu/index.html": "/qr-menu/index.html",
        "assets/css/style.css": "/assets/css/style.css",
        "assets/css/menu-page.css": "/assets/css/menu-page.css",
        "datenschutz.html": "/datenschutz.html",
        "impressum.html": "/impressum.html"
    }
    
    base_dir = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus"
    for file_path, url_path in files_to_recover.items():
        try:
            url = perfect_url + url_path
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                content = response.read() # As bytes, to avoid encoding errors!
                
            full_path = os.path.join(base_dir, file_path)
            with open(full_path, 'wb') as f: # Write as bytes! No encoding corruption!
                f.write(content)
            print(f"GERI YUKLENDI: {file_path}")
        except Exception as e:
            print(f"CEKILEMEDI {file_path}: {e}")
else:
    print("MUKEMMEL SURUM BULUNAMADI!")

