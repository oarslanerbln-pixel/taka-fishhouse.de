const fs = require('fs');
const path = 'c:\\Users\\oarsl\\Desktop\\Is Dosyasi\\Taka Fisch Haus\\qr-menu\\assets\\js\\menu-data.js';

let content = fs.readFileSync(path, 'utf8');

const imageMap = {
    "Hamsili Pilav": "https://images.unsplash.com/photo-1534080564583-6be75777b70a?w=600&q=80",
    "Turşu Kavurması": "https://images.unsplash.com/photo-1588195538326-c5b1e9f80a1b?w=600&q=80",
    "Tuzda Balık (4 Kişiye uygun)": "https://images.unsplash.com/photo-1511259063236-8a719c23eaac?w=600&q=80",
    "2 Kişilik Balık Buğulama": "https://images.unsplash.com/photo-1544148103-0773bf10d330?w=600&q=80",
    "4 Kişilik Balık Buğulama": "https://images.unsplash.com/photo-1544148103-0773bf10d330?w=600&q=80",
    "Havuç Tarator": "https://images.unsplash.com/photo-1541529086526-db283c563270?w=600&q=80",
    "Acı Antep Ezmesi": "https://images.unsplash.com/photo-1577906096429-f73c2c312435?w=600&q=80",
    "Levrek Marin": "https://images.unsplash.com/photo-1498654896293-37aacf113fd9?w=600&q=80",
    "Girit Ezmezi": "https://images.unsplash.com/photo-1541529086526-db283c563270?w=600&q=80",
    "Fava": "https://images.unsplash.com/photo-1541529086526-db283c563270?w=600&q=80",
    "Köpoğlu": "https://images.unsplash.com/photo-1577906096429-f73c2c312435?w=600&q=80",
    "Ahtapot Salatası": "https://images.unsplash.com/photo-1599084993091-1cb5c0721cc6?w=600&q=80",
    "Narlı Dibariye": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=600&q=80",
    "Tavada Kızarmış Patates, Taka Spesiyal": "https://images.unsplash.com/photo-1576107232684-1279f3908594?w=600&q=80",
    "Günün Çorbası": "https://images.unsplash.com/photo-1547592166-23ac45d44ad4?w=600&q=80",
    "Karışık Yeşil Salata": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=600&q=80",
    "Roka Salatası": "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?w=600&q=80",
    "Karides Salatası": "https://images.unsplash.com/photo-1551248429-40975aa4de74?w=600&q=80",
    "Hamsi Salatası": "https://images.unsplash.com/photo-1534080564583-6be75777b70a?w=600&q=80",
    "Balık Burger Menü": "https://images.unsplash.com/photo-1550547660-d9450f859349?w=600&q=80",
    "Balık Köfte Menü": "https://images.unsplash.com/photo-1529042410759-befb1204b468?w=600&q=80",
    "Somonlu Makarna (Özel Sos)": "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=600&q=80",
    "Karidesli Makarna (Özel Sos)": "https://images.unsplash.com/photo-1563379926898-05f4575a45d8?w=600&q=80",
    "Dondurmalı İrmik Helvası": "https://images.unsplash.com/photo-1551024601-bec78aea704b?w=600&q=80",
    "Un Helvası": "https://images.unsplash.com/photo-1551024601-bec78aea704b?w=600&q=80",
    "Fırında Meyhane Helvası": "https://images.unsplash.com/photo-1551024601-bec78aea704b?w=600&q=80",
    "Kazandibi": "https://images.unsplash.com/photo-1517244683847-7456b63c5969?w=600&q=80",
    "Hamsiköy Sütlacı (Fırında)": "https://images.unsplash.com/photo-1517244683847-7456b63c5969?w=600&q=80",
    "Kabak Tatlısı": "https://images.unsplash.com/photo-1605335645391-9e7b23bc01b5?w=600&q=80",
    "Su (0,25l)": "https://images.unsplash.com/photo-1548839140-29a749e1bc4e?w=600&q=80",
    "Maden Suyu (0,25l)": "https://images.unsplash.com/photo-1560416313-414b33c856a9?w=600&q=80",
    "Coca Cola (0,2l)": "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=600&q=80",
    "Ayran (0,25l)": "https://images.unsplash.com/photo-1556881286-fc6915169721?w=600&q=80",
    "Şalgam Suyu": "https://images.unsplash.com/photo-1589182373726-e4f658ab50f0?w=600&q=80",
    "Çay": "https://images.unsplash.com/photo-1576092762791-dd9e2220afa1?w=600&q=80",
    "Türk Kahvesi": "https://images.unsplash.com/photo-1542382151-0a649392e2eb?w=600&q=80"
};

let lines = content.split('\n');
let modified = lines.map(line => {
    for (const [name, url] of Object.entries(imageMap)) {
        if (line.includes(`nameTR: "${name}"`)) {
            if (!line.includes('image:')) {
                return line.replace(' }', `, image: "${url}" }`);
            }
        }
    }
    return line;
});

fs.writeFileSync(path, modified.join('\n'), 'utf8');
console.log('Images updated successfully');
