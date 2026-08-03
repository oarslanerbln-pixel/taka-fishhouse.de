import os
import re

css_path = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\assets\css\style.css"
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()
    
bordo_mavi_css = '''
.title-sea {
    background: linear-gradient(90deg, #800000, #000080, #800000);
    background-size: 200% auto;
    color: transparent;
    -webkit-background-clip: text;
    background-clip: text;
    animation: gradientMove 3s linear infinite;
    display: inline-block;
}

@keyframes gradientMove {
    0% { background-position: 0% center; }
    100% { background-position: 200% center; }
}
'''
if '.title-sea' not in css_content:
    css_content += "\n" + bordo_mavi_css
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_content)

index_path = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\index.html"
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

# Eski "Karadeniz Esintisi" HTML'sini bul ve degistir.
# Kreuzberg'te Karadeniz Esintisi -> Kreuzberg'te <span class="title-sea">Karadeniz</span> Esintisi
if 'class="title-sea"' not in index_content:
    index_content = re.sub(r"Kreuzberg'te(.*?)Karadeniz Esintisi", r"Kreuzberg'te\1<span class=\"title-sea\">Karadeniz</span> Esintisi", index_content, flags=re.IGNORECASE)
    
    # Eger hic match olmadıysa ve direkt <h1 ...>Karadeniz... </h1> varsa
    index_content = index_content.replace('Karadeniz Esintisi', '<span class="title-sea">Karadeniz</span> Esintisi')
    
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_content)

print("Bordo-Mavi Animasyon ve Karadeniz yazisi eklendi.")
