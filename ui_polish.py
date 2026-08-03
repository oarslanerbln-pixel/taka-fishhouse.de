import os

def polish_css(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add overflow-x and touch-action if not fully present
    # We will just append them at the end for global overrides
    
    polish = """
/* UI POLISH & BUG HUNT FIXES */
html, body {
    overflow-x: hidden;
    width: 100%;
}

a, button, .btn, .category-btn {
    touch-action: manipulation; /* Removes 300ms tap delay on mobile */
    -webkit-tap-highlight-color: transparent;
}

/* Ensure images don't overflow */
img, video {
    max-width: 100%;
    height: auto;
}
"""
    if '/* UI POLISH' not in content:
        content += "\n" + polish
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Polished {filepath}")

polish_css('assets/css/style.css')
polish_css('qr-menu/assets/css/menu-page.css')
