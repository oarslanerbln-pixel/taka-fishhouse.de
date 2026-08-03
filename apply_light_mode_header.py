import os

css_path = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\css\style.css'

with open(css_path, 'r', encoding='utf-8') as f:
    content = f.read()

if '/* --- PREMIUM QR LIGHT MODE OVERRIDES --- */' not in content:
    light_mode_fixes = """
/* --- PREMIUM QR LIGHT MODE OVERRIDES --- */
html[data-theme="light"] header.scrolled {
    background: rgba(255, 255, 255, 0.95);
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.05);
    border-bottom: 1px solid rgba(0, 0, 0, 0.05);
}
html[data-theme="light"] header .nav-links a {
    color: var(--text-main);
}
"""
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(content + '\n' + light_mode_fixes)
    print("Light mode header fixes appended to style.css")
else:
    print("Already applied.")
