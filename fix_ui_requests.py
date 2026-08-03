import os
import re

# 1. Update main.js splash duration
main_js = 'assets/js/main.js'
with open(main_js, 'r', encoding='utf-8') as f:
    main_content = f.read()

main_content = main_content.replace('}, 2200);', '}, 800);')
with open(main_js, 'w', encoding='utf-8') as f:
    f.write(main_content)
print("Updated splash duration.")

# 2. Update translations.js
trans_js = 'assets/js/translations.js'
with open(trans_js, 'r', encoding='utf-8') as f:
    trans_content = f.read()

# Replace TR
trans_content = re.sub(r'("hero-title":\s*")Kreuzberg\'de.*?(")', r'\1Kreuzberg\'de <br><span class=\\"title-sea\\">Karadeniz</span> Esintisi\2', trans_content)
# Replace DE (might be Bosphorus-Brise)
trans_content = re.sub(r'("hero-title":\s*")Bosphorus-Brise.*?(")', r'\1<span class=\\"title-sea\\">Schwarzmeer</span>-Brise <br>in Kreuzberg\2', trans_content)
# Replace EN
trans_content = re.sub(r'("hero-title":\s*")Bosphorus Breeze.*?(")', r'\1<span class=\\"title-sea\\">Black Sea</span> Breeze <br>in Kreuzberg\2', trans_content)

# The inject_translations we ran might have "Бриз Босфора <br>в Кройцберге" for RU, "Brisa del Bósforo <br>en Kreuzberg" for ES, "نسيم البوسفور <br>في كرويتزبيرغ" for AR
trans_content = trans_content.replace("Бриз Босфора <br>в Кройцберге", "<span class=\\\"title-sea\\\">Черноморский</span> Бриз <br>в Кройцберге")
trans_content = trans_content.replace("Brisa del Bósforo <br>en Kreuzberg", "Brisa del <span class=\\\"title-sea\\\">Mar Negro</span> <br>en Kreuzberg")
trans_content = trans_content.replace("نسيم البوسفور <br>في كرويتزبيرغ", "نسيم <span class=\\\"title-sea\\\">البحر الأسود</span> <br>في كرويتزبيرغ")

with open(trans_js, 'w', encoding='utf-8') as f:
    f.write(trans_content)
print("Updated translations.")

# 3. Update style.css
style_css = 'assets/css/style.css'
with open(style_css, 'r', encoding='utf-8') as f:
    style_content = f.read()

premium_css = """
/* PREMIUM TITLE SEA ANIMATION */
.hero-title-premium .title-sea {
    position: relative;
    display: inline-block;
    color: transparent;
    background: linear-gradient(
        110deg,
        #00cca3 0%,
        #00a884 25%,
        #ffae00 50%,
        #00cca3 75%,
        #00a884 100%
    );
    background-size: 300% 100%;
    -webkit-background-clip: text;
    background-clip: text;
    animation: premiumWave 8s ease-in-out infinite alternate;
    text-shadow: 0 0 40px rgba(0, 204, 163, 0.4);
}

.hero-title-premium .title-sea::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(
        90deg,
        rgba(255, 255, 255, 0) 0%,
        rgba(255, 255, 255, 0.8) 50%,
        rgba(255, 255, 255, 0) 100%
    );
    background-size: 200% 100%;
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    animation: shinePass 6s infinite linear;
    mix-blend-mode: overlay;
}

@keyframes premiumWave {
    0% { background-position: 0% 50%; }
    100% { background-position: 100% 50%; }
}

@keyframes shinePass {
    0% { background-position: 200% 50%; opacity: 0; }
    20% { opacity: 0; }
    50% { opacity: 0.5; }
    80% { opacity: 0; }
    100% { background-position: -200% 50%; opacity: 0; }
}
"""

# Replace old .title-sea block if it exists
if '.title-sea {' in style_content or '.hero-title-premium .title-sea' in style_content:
    # Just remove old blocks
    style_content = re.sub(r'\.title-sea\s*{[^}]*}', '', style_content)
    style_content = re.sub(r'\.hero-title-premium\s*\.title-sea\s*{[^}]*}', '', style_content)
    style_content = re.sub(r'@keyframes gradientMove\s*{[^}]*}', '', style_content)
    # We will just append the new one at the end
    style_content += "\n" + premium_css
    
    with open(style_css, 'w', encoding='utf-8') as f:
        f.write(style_content)
    print("Updated style.css.")
else:
    print("Could not find .title-sea in style.css. Appending anyway.")
    with open(style_css, 'a', encoding='utf-8') as f:
        f.write("\n" + premium_css)

