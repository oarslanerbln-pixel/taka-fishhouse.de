import re

filepath = 'assets/css/style.css'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the old premium title sea animation block
content = re.sub(r'/\* PREMIUM TITLE SEA ANIMATION \*/.*?(?=\Z)', '', content, flags=re.DOTALL)

# Create a sharper, highly contrasting premium gold gradient without overlay blur
premium_css = """/* PREMIUM TITLE SEA ANIMATION */
.hero-title-premium .title-sea {
    position: relative;
    display: inline-block;
    background: linear-gradient(
        to right, 
        #B38728 0%, 
        #FBF5B7 20%, 
        #D4AF37 40%, 
        #FBF5B7 60%, 
        #B38728 80%,
        #FBF5B7 100%
    );
    background-size: 200% auto;
    color: transparent;
    -webkit-background-clip: text;
    background-clip: text;
    animation: shineGold 4s linear infinite;
    /* Removed heavy text-shadow which causes blur */
    filter: drop-shadow(0px 2px 4px rgba(0, 0, 0, 0.5));
}

@keyframes shineGold {
    to {
        background-position: 200% center;
    }
}
"""

content = content.strip() + "\n\n" + premium_css

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated style.css with sharp premium gold animation.")
