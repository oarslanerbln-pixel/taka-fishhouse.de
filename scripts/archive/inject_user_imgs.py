import re

DRINK_IMAGES = {
    # Çamlıca Gazoz 
    142: "https://www.uzunoglusu.com/wp-content/uploads/2024/02/camlica-uzunoglu.jpg",
    # Schweppes 0.2l
    147: "https://we-deliver-drinks.es/wp-content/uploads/2024/04/Schweppes-02L-Variante.webp",  # Changed 2026 to 2024 if it was a typo, wait, the script found 2026. Let's stick to what we downloaded locally!
    # Durstlöscher 
    149: "https://sbunion.shop/wp-content/uploads/2023/03/101189_104104_104107_506050Durstloescher500mlGruppe.png",
    # Şalgam
    143: "https://image.hurimg.com/i/hurriyet/90/0x0/68fa2ae3b34cd2371d88e3c1.jpg",
    # Tymbark
    145: "http://bier-berlin.com/cdn/shop/files/Photoroom-20240411_133323.png?v=1757421400",
    # Verschiedene Teesorten
    162: "http://oznatur.de/cdn/shop/articles/teearten-welche-gibt-es.png?v=1782211008",
    92:  "http://oznatur.de/cdn/shop/articles/teearten-welche-gibt-es.png?v=1782211008",
    
    # Mineralwasser mit Kohlensäure - let's find a reliable classic sparkling water bottle (e.g. San Pellegrino or generic mineral water with bubbles)
    # The current one was: https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=400&q=80
    # Let's replace it with a more obvious sparkling water image
    131: "https://images.unsplash.com/photo-1622484212850-eb596d769edc?w=400&q=80", 
}

files = [
    "qr-menu/assets/js/menu-data.js",
    "assets/js/menu-data.js"
]

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    updated = 0
    for item_id, image_url in DRINK_IMAGES.items():
        pattern = r'("id":\s*' + str(item_id) + r'\s*,.*?\})'

        def make_repl(url):
            def repl(match):
                block = match.group(1)
                if '"image":' in block:
                    return re.sub(r'"image":\s*"[^"]*"', '"image": "' + url + '"', block)
                else:
                    return re.sub(r'("price":)', '"image": "' + url + '",\n                \\1', block)
            return repl

        new_content = re.sub(pattern, make_repl(image_url), content, flags=re.DOTALL)
        if new_content != content:
            updated += 1
            content = new_content

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Updated {file_path}: {updated} items")
