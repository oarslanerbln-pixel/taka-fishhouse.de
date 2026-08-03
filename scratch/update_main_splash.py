import codecs
import os

root_dir = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus"
html_file = os.path.join(root_dir, "index.html")
css_file = os.path.join(root_dir, "assets", "css", "style.css")
js_file = os.path.join(root_dir, "assets", "js", "main.js")

# --- Update index.html ---
with codecs.open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

old_splash = """<!-- ============================
     PREMIUM LOGO SPLASH (INTRO)
     ============================ -->
<div id="premium-splash" class="premium-splash">
    <div class="splash-logo-container">
        <img src="assets/taka_logo.png" alt="TAKA Fish House Logo" class="splash-logo">
    </div>
</div>"""

new_splash = """<!-- ============================
     PREMIUM VIDEO SPLASH (INTRO)
     ============================ -->
<div id="premium-splash" class="premium-splash">
    <video class="splash-bg-video" autoplay muted playsinline>
        <source src="assets/videos/main-splash-intro.mp4" type="video/mp4">
    </video>
    <div class="splash-logo-container">
        <img src="assets/taka_logo.png" alt="TAKA Fish House Logo" class="splash-logo">
    </div>
</div>"""

html_content = html_content.replace(old_splash, new_splash)

with codecs.open(html_file, "w", encoding="utf-8") as f:
    f.write(html_content)


# --- Update style.css ---
with codecs.open(css_file, "a", encoding="utf-8") as f:
    f.write("""
/* ==========================================================
   PREMIUM SPLASH INTRO (MAIN PAGE)
   ========================================================== */
.premium-splash {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: radial-gradient(circle at center, #0a1118 0%, #020304 100%);
    z-index: 9999;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    transition: opacity 1.2s cubic-bezier(0.16, 1, 0.3, 1), transform 1.2s cubic-bezier(0.16, 1, 0.3, 1), filter 1.2s cubic-bezier(0.16, 1, 0.3, 1), visibility 1.2s;
}

.splash-bg-video {
    position: absolute;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    object-fit: cover;
    z-index: 1;
    opacity: 0.6; /* Slight darkness to make logo pop */
}

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
    animation-delay: 0s, 1.5s;
}

.splash-logo {
    max-width: 180px;
    height: auto;
}

@keyframes splash-logo-enter {
    0% { opacity: 0; transform: scale(0.6) translateY(30px) rotateX(-20deg); filter: drop-shadow(0 0 0 rgba(0,0,0,0)); }
    100% { opacity: 1; transform: scale(1) translateY(0) rotateX(0deg); filter: drop-shadow(0 0 15px rgba(0, 150, 255, 0.4)); }
}

@keyframes splash-neon-pulse {
    0% { filter: drop-shadow(0 0 15px rgba(0, 150, 255, 0.6)) drop-shadow(0 0 30px rgba(0, 150, 255, 0.3)); transform: scale(1); }
    100% { filter: drop-shadow(0 0 25px rgba(0, 230, 184, 0.9)) drop-shadow(0 0 50px rgba(0, 230, 184, 0.7)) drop-shadow(0 0 90px rgba(0, 230, 184, 0.5)); transform: scale(1.05); }
}
""")


# --- Update main.js ---
# We need to make sure the splash screen logic in main.js handles this video duration. The trimmed video is 3.5 seconds long (6.0 - 2.5).
# So we should transition out around 3.2s.

with codecs.open(js_file, "r", encoding="utf-8") as f:
    js_content = f.read()

# Let's replace the existing splash logic in main.js.
# Existing logic in main.js:
# setTimeout(() => {
#     const premiumSplash = document.getElementById('premium-splash');
#     if(premiumSplash) { ... }
# }, 2000); // 2 second display

import re
js_content = re.sub(
    r"setTimeout\(\(\) => \{\s*const premiumSplash.*?2000\);", 
    """// ===== Ultra-Premium Cinematic Splash Logic =====
    setTimeout(() => {
        const premiumSplash = document.getElementById('premium-splash');
        if(premiumSplash) {
            premiumSplash.classList.add('is-exiting');
            document.body.style.overflow = '';
            
            setTimeout(() => {
                premiumSplash.remove();
            }, 1200);
        }
    }, 3200); // Display for 3.2 seconds to match the 3.5s video""",
    js_content,
    flags=re.DOTALL
)

with codecs.open(js_file, "w", encoding="utf-8") as f:
    f.write(js_content)

print("SUCCESS")
