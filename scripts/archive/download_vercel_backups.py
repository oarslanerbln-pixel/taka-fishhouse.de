import os
import urllib.request

urls = [
    "https://taka-fisch-haus-ggasmhxl2-oarslanerbln-pixels-projects.vercel.app",
    "https://taka-fisch-haus-ggasmhxl2-oarslanerbln-pixels-projects.vercel.app/qr-menu/",
    "https://taka-fisch-haus-p7wlsr3nv-oarslanerbln-pixels-projects.vercel.app",
    "https://taka-fisch-haus-pivevabp1-oarslanerbln-pixels-projects.vercel.app"
]

out_dir = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\scratch_old_vercel"
os.makedirs(out_dir, exist_ok=True)

for i, url in enumerate(urls):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            filename = os.path.join(out_dir, f"backup_{i}.html")
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Saved {url} to {filename} (Length: {len(html)})")
    except Exception as e:
        print(f"Failed {url}: {e}")

