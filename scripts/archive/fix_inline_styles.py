import re

html_file = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\index.html"
css_file = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\css\style.css"

with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Line 73
html_content = html_content.replace(
    '<a href="tel:+493026349486" class="btn btn-primary sm-hidden" style="padding: 10px 22px; font-size: 0.85rem;" data-i18n="nav-reservation">Reservieren</a>',
    '<a href="tel:+493026349486" class="btn btn-primary sm-hidden header-res-btn" data-i18n="nav-reservation">Reservieren</a>'
)

# Line 282 iframe
html_content = html_content.replace(
    'style="border:0;"',
    'class="map-iframe"'
)

# Line 320
html_content = html_content.replace(
    '<div class="story-section-badge" style="display:inline-flex; margin-bottom:20px;">',
    '<div class="story-section-badge res-badge-inline">'
)

# Line 565 (footer link or something)
html_content = html_content.replace(
    'style="color: var(--accent-color); font-weight: 500;"',
    'class="accent-link-bold"'
)

# Line 601 and 602
html_content = html_content.replace(
    '<div style="font-size: 0.85rem; margin-top: 15px;">',
    '<div class="footer-impressum-wrap">'
)
html_content = html_content.replace(
    'style="color: var(--accent-color); text-decoration: none;"',
    'class="footer-impressum-link"'
)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

# Now inject these new classes to style.css
new_css = """
/* Auto-extracted inline styles */
.brand-logo-img { height: 50px; width: auto; object-fit: contain; filter: drop-shadow(0px 2px 4px rgba(0,0,0,0.5)); }
.header-res-btn { padding: 10px 22px; font-size: 0.85rem; }
.map-iframe { border: 0; }
.res-badge-inline { display: inline-flex; margin-bottom: 20px; }
.accent-link-bold { color: var(--accent-color); font-weight: 500; }
.footer-impressum-wrap { font-size: 0.85rem; margin-top: 15px; }
.footer-impressum-link { color: var(--accent-color); text-decoration: none; }
"""

with open(css_file, 'a', encoding='utf-8') as f:
    f.write("\n" + new_css)

print("Inline styles cleaned up!")
