import os

# Append premium CSS overrides to qr-menu/assets/css/menu-page.css
css_path = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\css\menu-page.css'

with open(css_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove any previous premium overrides if they exist so we don't duplicate
if '/* --- PREMIUM QR MENU HERO OVERRIDES --- */' in content:
    content = content.split('/* --- PREMIUM QR MENU HERO OVERRIDES --- */')[0]

premium_css = """/* --- PREMIUM QR MENU HERO OVERRIDES --- */
/* Completely revamp the hero section to look embedded and professional */
.menu-hero {
    position: relative !important;
    background: transparent !important;
    min-height: auto !important;
    height: auto !important;
    padding-bottom: 0 !important;
    margin-bottom: 20px;
    border-radius: 0 0 24px 24px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    z-index: 1;
}

/* Make the video absolute within the hero, NOT fixed to the viewport */
.menu-hero .hero-video-container {
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    width: 100% !important;
    height: 100% !important;
    z-index: 0 !important;
    background: var(--bg-primary) !important;
    transform: none !important;
}

.menu-hero .hero-video-container video {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    mask-image: none !important;
    -webkit-mask-image: none !important;
    opacity: 0.8;
}

/* Remove the dirty black gradients from bottom */
.menu-hero::after,
.hero-gradient-bottom {
    display: none !important;
}

/* Standalone text block inside the hero */
.standalone-text-block {
    position: relative !important;
    z-index: 2 !important;
    margin-top: 0 !important;
    padding: 80px 20px 60px !important;
    background: linear-gradient(to bottom, rgba(0,0,0,0.4) 0%, rgba(0,0,0,0.7) 100%) !important;
    text-align: center;
    border-radius: 0 0 24px 24px;
}

/* Light mode specifics for the text */
html[data-theme="light"] .standalone-text-block {
    background: linear-gradient(to bottom, rgba(255,255,255,0.2) 0%, rgba(255,255,255,0.8) 100%) !important;
}
html[data-theme="light"] .standalone-text-block h1 {
    color: var(--text-main) !important;
    text-shadow: none !important;
    background: none !important;
    -webkit-text-fill-color: var(--text-main) !important;
}
html[data-theme="light"] .standalone-text-block p {
    color: var(--text-secondary) !important;
}
html[data-theme="light"] .section-badge.glass-badge {
    background: rgba(255, 255, 255, 0.5) !important;
    color: var(--text-main) !important;
    border-color: rgba(0, 0, 0, 0.1) !important;
}

/* Sticky Categories Menu */
.menu-categories {
    position: sticky !important;
    top: 75px !important; /* Header is ~75px */
    z-index: 1000 !important;
    background: var(--bg-primary) !important;
    margin-top: 0 !important;
    padding: 10px 0 !important;
    border-radius: 0 !important;
    border-bottom: 1px solid var(--border-color) !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05) !important;
}

/* Light mode specific categories */
html[data-theme="light"] .menu-categories {
    background: rgba(255, 255, 255, 0.95) !important;
    -webkit-backdrop-filter: blur(10px);
    backdrop-filter: blur(10px);
}
"""

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(content + '\n' + premium_css)

print("Premium CSS overrides appended.")
