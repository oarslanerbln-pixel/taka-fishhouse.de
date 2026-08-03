import re

def clean_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Index.html specific fixes
    content = re.sub(r'style="height:\s*50px;\s*width:\s*auto;\s*object-fit:\s*contain;\s*filter:\s*drop-shadow\(0px\s*2px\s*4px\s*rgba\(0,0,0,0\.5\)\);"', '', content)
    content = re.sub(r'style="padding:\s*10px\s*22px;\s*font-size:\s*0\.85rem;"', '', content)
    content = re.sub(r'class="btn btn-outline-dark"\s*style="margin-top:2rem;"', 'class="btn btn-outline-dark mt-8"', content)
    content = re.sub(r'style="font-size:\s*0\.85rem;\s*margin-top:\s*15px;"', 'class="footer-impressum-container"', content)
    content = re.sub(r'style="color:\s*var\(--accent-color\);\s*text-decoration:\s*none;"', 'class="footer-impressum-link"', content)
    content = re.sub(r'style="border:0;"', '', content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

clean_file('index.html')
try:
    clean_file('qr-menu/index.html')
except:
    pass
