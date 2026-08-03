import re

def update_html():
    html_file = 'qr-menu/index.html'
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove sm-hidden from nav-links
    content = content.replace('<div class="nav-links sm-hidden">', '<div class="nav-links">')
    
    # Remove hero-top-bar
    content = re.sub(r'<div class="hero-top-bar"[\s\S]*?</div>', '', content)

    # Enhance hero-video-container by adding an overlay
    # Wait, there's a hero-gradient-bottom already. Let's keep it but enhance CSS.
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

def update_css():
    css_file = 'qr-menu/assets/css/menu-page.css'
    with open(css_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Enhance .menu-hero
    content = re.sub(r'\.premium-hero\s*{[^}]*}', '', content)
    
    hero_css = """
/* ENHANCED VIDEO HERO */
.premium-hero {
    position: relative;
    height: 40vh; /* Better proportion */
    min-height: 350px;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    margin-top: 0;
}

.premium-hero .hero-video-container {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 1;
}

.premium-hero video {
    width: 100%;
    height: 100%;
    object-fit: cover;
    filter: brightness(0.85) contrast(1.1); /* Vibrant but readable */
}

/* Multi-layer gradient for depth */
.premium-hero .hero-gradient-bottom {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(to bottom, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.6) 60%, var(--bg-dark, #111) 100%);
    z-index: 2;
}

.standalone-text-block {
    position: relative;
    z-index: 3;
    text-align: center;
    padding: 0 20px;
    transform: translateY(20px);
}

.standalone-text-block h1 {
    font-size: 3rem;
    color: #fff;
    margin-bottom: 10px;
    text-shadow: 0 4px 15px rgba(0,0,0,0.8);
    font-family: 'Playfair Display', serif;
}

.standalone-text-block p {
    font-size: 1.1rem;
    color: rgba(255,255,255,0.9);
    text-shadow: 0 2px 10px rgba(0,0,0,0.8);
    max-width: 600px;
    margin: 0 auto;
}

/* Fix sticky category bar */
.menu-categories {
    position: sticky;
    top: 70px; /* Adjusted for header height */
    z-index: 999;
    background: var(--bg-dark, #111);
    box-shadow: 0 4px 20px rgba(0,0,0,0.5);
    border-bottom: 1px solid rgba(255,255,255,0.1);
    margin-top: -20px;
    padding: 10px 0;
    transition: background-color 0.3s ease;
}

/* Ensure body doesn't cause sticky issues */
body {
    overflow-x: hidden;
}
"""
    # Append the new css
    content += "\n" + hero_css
    
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(content)

update_html()
update_css()
print("Updated UI elements successfully.")
