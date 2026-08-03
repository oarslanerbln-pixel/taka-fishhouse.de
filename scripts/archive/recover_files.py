import urllib.request
import os

base_url = "https://taka-fisch-haus-evjl4i3ha-oarslanerbln-pixels-projects.vercel.app"
files_to_recover = {
    "index.html": "/",
    "menu.html": "/menu.html",
    "qr-menu/index.html": "/qr-menu/",
    "assets/css/style.css": "/assets/css/style.css"
}

base_dir = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus"

for file_path, url_path in files_to_recover.items():
    try:
        url = base_url + url_path
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
            
        full_path = os.path.join(base_dir, file_path)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"RECOVERED: {file_path}")
    except Exception as e:
        print(f"FAILED to recover {file_path}: {e}")

