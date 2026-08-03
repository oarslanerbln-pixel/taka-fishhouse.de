import re
import os

html_file = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\index.html"
css_file = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\css\style.css"
trans_files = [
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\js\translations.js",
    r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\js\translations.js"
]

# 1. Update index.html
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace iframe wrapper
iframe_block = """            <div class="map-embed-wrapper premium-map">
                <iframe
                    src="https://maps.google.com/maps?q=Kottbusser%20Damm%2035%20Berlin&t=&z=15&ie=UTF8&iwloc=&output=embed"
                    width="100%"
                    height="100%"
                    class="map-iframe"
                    allowfullscreen=""
                    loading="lazy"
                    title="Taka Fish House – Kottbusser Damm 35, Berlin">
                </iframe>
            </div>"""

new_map_block = """            <div class="map-embed-wrapper premium-static-map">
                <img src="assets/premium_map.png" alt="Taka Fisch Haus Location" class="static-map-img">
                <div class="static-map-overlay">
                    <a href="https://maps.app.goo.gl/wSrxzL8Txhw2Fm3d8" target="_blank" class="map-open-btn">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
                        <span data-i18n="map-open-btn">Google Haritalar'da Aç</span>
                    </a>
                </div>
            </div>"""

html = html.replace(iframe_block, new_map_block)

# Remove gsap-fade-up from reservation right side
html = html.replace('<div class="map-res-right gsap-fade-up">', '<div class="map-res-right">')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Update style.css
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

new_css = """
/* Static Map Overrides */
.premium-static-map {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #060a0f;
}
.static-map-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    opacity: 0.8;
}
.static-map-overlay {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(6,10,15,0.3);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s ease;
}
.premium-static-map:hover .static-map-overlay {
    background: rgba(6,10,15,0.1);
}
.map-open-btn {
    background: rgba(6,10,15,0.85);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.15);
    color: var(--text-light);
    padding: 16px 28px;
    border-radius: 30px;
    display: inline-flex;
    align-items: center;
    gap: 12px;
    font-size: 1.05rem;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.3s ease;
    box-shadow: 0 15px 30px rgba(0,0,0,0.5);
}
.map-open-btn:hover {
    background: #e6b350;
    color: #1a1a1a;
    transform: translateY(-3px);
    box-shadow: 0 20px 40px rgba(230, 179, 80, 0.3);
}
"""

if ".static-map-img" not in css:
    with open(css_file, 'a', encoding='utf-8') as f:
        f.write("\n" + new_css)


# 3. Update translations.js
for tf in trans_files:
    if not os.path.exists(tf): continue
    with open(tf, 'r', encoding='utf-8') as f:
        t_content = f.read()
    
    if '"map-open-btn"' not in t_content:
        t_content = re.sub(r'(tr:\s*\{)(.*?)(\n\s*// Menu Page Specific|\n\s*\},)', r'\1\2\n        "map-open-btn": "Google Haritalar\'da Aç",\3', t_content, flags=re.DOTALL)
        t_content = re.sub(r'(de:\s*\{)(.*?)(\n\s*// Menu Page Specific|\n\s*\},)', r'\1\2\n        "map-open-btn": "In Google Maps öffnen",\3', t_content, flags=re.DOTALL)
        t_content = re.sub(r'(en:\s*\{)(.*?)(\n\s*// Menu Page Specific|\n\s*\},|\n\s*\})', r'\1\2\n        "map-open-btn": "Open in Google Maps",\3', t_content, flags=re.DOTALL)
        with open(tf, 'w', encoding='utf-8') as f:
            f.write(t_content)

print("Replacement complete.")
