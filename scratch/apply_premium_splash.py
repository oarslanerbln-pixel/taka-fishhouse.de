import codecs
import re
import os

root_dir = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu"
css_file = os.path.join(root_dir, "assets", "css", "menu-page.css")
js_file = os.path.join(root_dir, "assets", "js", "menu-page.js")

# --- Update menu-page.css ---
with codecs.open(css_file, "r", encoding="utf-8") as f:
    css_content = f.read()

# Remove the old .splash-logo-container and its keyframes completely, up to the end
css_content = re.sub(
    r"\.splash-logo-container\s*\{.*?\@keyframes\s+splash-logo-fade-in\s*\{.*?\n\}\n",
    "",
    css_content,
    flags=re.DOTALL
)

# Replace the .premium-splash transition
css_content = css_content.replace(
    "transition: opacity 0.4s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.4s;",
    "transition: opacity 1.2s cubic-bezier(0.16, 1, 0.3, 1), transform 1.2s cubic-bezier(0.16, 1, 0.3, 1), filter 1.2s cubic-bezier(0.16, 1, 0.3, 1), visibility 1.2s;"
)

# Append the new premium styles at the end
new_css = """
/* ===== PREMIUM SPLASH ENHANCEMENTS ===== */
.premium-splash.is-exiting {
    opacity: 0;
    transform: scale(1.15);
    filter: blur(15px);
    visibility: hidden;
    pointer-events: none;
}

.splash-logo-container {
    position: relative;
    z-index: 2;
    animation: 
        splash-logo-enter 1.5s cubic-bezier(0.16, 1, 0.3, 1) forwards,
        splash-neon-pulse 2s infinite ease-in-out alternate forwards;
    animation-delay: 0s, 1.5s; /* Neon starts after entry */
}

@keyframes splash-logo-enter {
    0% { opacity: 0; transform: scale(0.6) translateY(30px) rotateX(-20deg); filter: drop-shadow(0 0 0 rgba(0,0,0,0)); }
    100% { opacity: 1; transform: scale(1) translateY(0) rotateX(0deg); filter: drop-shadow(0 0 15px rgba(0, 150, 255, 0.4)); }
}

@keyframes splash-neon-pulse {
    0% { filter: drop-shadow(0 0 15px rgba(0, 150, 255, 0.6)) drop-shadow(0 0 30px rgba(0, 150, 255, 0.3)); transform: scale(1); }
    100% { filter: drop-shadow(0 0 25px rgba(0, 230, 184, 0.9)) drop-shadow(0 0 50px rgba(0, 230, 184, 0.7)) drop-shadow(0 0 90px rgba(0, 230, 184, 0.5)); transform: scale(1.05); }
}
"""
css_content += new_css

with codecs.open(css_file, "w", encoding="utf-8") as f:
    f.write(css_content)

# --- Update menu-page.js ---
with codecs.open(js_file, "r", encoding="utf-8") as f:
    js_content = f.read()

old_js_block = """    // ===== Premium Splash Screen Logic =====
    const premiumSplash = document.getElementById('premium-splash');
    if (premiumSplash) {
        // Prevent scrolling during splash
        document.body.style.overflow = 'hidden';
        
        // Max 2 seconds total experience
        setTimeout(() => {
            premiumSplash.style.opacity = '0';
            premiumSplash.style.visibility = 'hidden';
            
            // Allow scrolling again
            document.body.style.overflow = '';
            
            // Remove from DOM to keep things clean
            setTimeout(() => {
                premiumSplash.remove();
            }, 400);
        }, 2500);
    }"""

new_js_block = """    // ===== Ultra-Premium Splash Screen Logic =====
    const premiumSplash = document.getElementById('premium-splash');
    if (premiumSplash) {
        document.body.style.overflow = 'hidden';
        
        // Let the neon pulse for a bit before exiting (total time ~3s)
        setTimeout(() => {
            premiumSplash.classList.add('is-exiting');
            
            // Allow scrolling immediately as the splash transitions out smoothly
            document.body.style.overflow = '';
            
            // Remove after transition completes (matches 1.2s transition in CSS)
            setTimeout(() => {
                premiumSplash.remove();
            }, 1200);
        }, 3200);
    }"""

js_content = js_content.replace(old_js_block, new_js_block)

with codecs.open(js_file, "w", encoding="utf-8") as f:
    f.write(js_content)

print("SUCCESS: Splash screen updated")
