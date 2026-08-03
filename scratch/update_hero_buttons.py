import codecs
import re

html_path = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\index.html"
css_path = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\css\style.css"

# Update index.html
with codecs.open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

old_buttons = """        <div class="hero-actions">
            <a href="qr-menu/" class="btn btn-dark-blue-pulse" data-i18n="hero-cta-menu">Menüyü Gör</a>
            <a href="#about" class="btn btn-ghost" data-i18n="hero-cta-story">Hikayemiz</a>
        </div>"""

new_buttons = """        <div class="hero-actions premium-hero-actions">
            <a href="qr-menu/" class="btn-neon-premium" data-i18n="hero-cta-menu">
                <span class="btn-text">Menüyü Gör</span>
                <span class="btn-glow"></span>
            </a>
            <a href="tel:+493026349486" class="btn-neon-outline" data-i18n="nav-reservation">
                <span class="btn-text">Rezervasyon Yap</span>
                <span class="btn-glow"></span>
            </a>
        </div>"""

html_content = html_content.replace(old_buttons, new_buttons)

with codecs.open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

# Update style.css
with codecs.open(css_path, "a", encoding="utf-8") as f:
    f.write("""
/* ==========================================================
   PREMIUM NEON ANIMATED BUTTONS (HERO SECTION)
   ========================================================== */
.premium-hero-actions {
    display: flex;
    gap: 20px;
    margin-top: 30px;
    align-items: center;
    justify-content: center;
}

@media (max-width: 768px) {
    .premium-hero-actions {
        flex-direction: column;
        width: 100%;
        gap: 15px;
        padding: 0 20px;
    }
}

/* Neon Premium (Main Action) */
.btn-neon-premium {
    position: relative;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    padding: 16px 36px;
    font-family: var(--font-primary), sans-serif;
    font-weight: 600;
    font-size: 1.1rem;
    color: #ffffff;
    text-transform: uppercase;
    letter-spacing: 2px;
    text-decoration: none;
    border-radius: 50px;
    background: linear-gradient(135deg, #001f3f, #004080);
    border: 2px solid #00e6b8;
    overflow: hidden;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    box-shadow: 0 0 15px rgba(0, 230, 184, 0.4), inset 0 0 10px rgba(0, 230, 184, 0.2);
    z-index: 1;
}

.btn-neon-premium .btn-text {
    position: relative;
    z-index: 2;
    text-shadow: 0 0 8px rgba(255, 255, 255, 0.6);
}

.btn-neon-premium .btn-glow {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 0;
    height: 0;
    background: rgba(0, 230, 184, 0.3);
    border-radius: 50%;
    z-index: 0;
    transition: width 0.6s ease, height 0.6s ease;
    filter: blur(10px);
}

.btn-neon-premium:hover {
    color: #0a1118;
    background: #00e6b8;
    box-shadow: 0 0 30px rgba(0, 230, 184, 0.8), inset 0 0 15px rgba(255, 255, 255, 0.5);
    transform: translateY(-3px);
}

.btn-neon-premium:hover .btn-glow {
    width: 300px;
    height: 300px;
}

/* Neon Outline (Secondary Action) */
.btn-neon-outline {
    position: relative;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    padding: 16px 36px;
    font-family: var(--font-primary), sans-serif;
    font-weight: 600;
    font-size: 1.1rem;
    color: #00e6b8;
    text-transform: uppercase;
    letter-spacing: 2px;
    text-decoration: none;
    border-radius: 50px;
    background: rgba(0, 31, 63, 0.3);
    border: 2px solid rgba(0, 230, 184, 0.5);
    overflow: hidden;
    backdrop-filter: blur(10px);
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    z-index: 1;
}

.btn-neon-outline .btn-text {
    position: relative;
    z-index: 2;
}

.btn-neon-outline .btn-glow {
    position: absolute;
    top: 0;
    left: -100%;
    width: 50%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(0, 230, 184, 0.4), transparent);
    transform: skewX(-20deg);
    animation: neon-shine 3s infinite linear;
    z-index: 0;
}

@keyframes neon-shine {
    0% { left: -100%; }
    20% { left: 200%; }
    100% { left: 200%; }
}

.btn-neon-outline:hover {
    color: #ffffff;
    border-color: #00e6b8;
    background: rgba(0, 230, 184, 0.15);
    box-shadow: 0 0 20px rgba(0, 230, 184, 0.5);
    transform: translateY(-3px);
}

/* Pulse animation for the premium button to draw attention */
.btn-neon-premium {
    animation: premium-btn-pulse 2s infinite ease-in-out alternate;
}

@keyframes premium-btn-pulse {
    0% { box-shadow: 0 0 15px rgba(0, 230, 184, 0.4), inset 0 0 10px rgba(0, 230, 184, 0.2); }
    100% { box-shadow: 0 0 25px rgba(0, 230, 184, 0.7), inset 0 0 15px rgba(0, 230, 184, 0.4); }
}
""")

print("SUCCESS")
