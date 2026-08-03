const fs = require('fs');

const keysToAdd = {
    tr: `
        "sig-chef": "Şef Seçimi",
        "sig-popular": "En Popüler",
        "sig-new": "Yeni",
        "sig-spicy": "Spesiyel",
        "sig-dish1": "Karışık Izgara Tabağı",
        "sig-dish1-desc": "Günlük taze balıklardan hazırlanan seçkin ızgara tabağı.",
        "sig-dish2": "Hamsi Salatası",
        "sig-dish2-desc": "Karadeniz'in klasiği, taze hamsi ile hazırlanan özel salata.",
        "sig-dish3": "Somon Sandviç",
        "sig-dish3-desc": "Taze somon, çıtır ekmek ve özel sos ile nefis bir sandviç.",
        "sig-dish4": "Karides Tava Spezial",
        "sig-dish4-desc": "Tereyağında sote karides, TAKA'nın efsane baharatıyla.",
`,
    de: `
        "sig-chef": "Empfehlung des Küchenchefs",
        "sig-popular": "Beliebteste",
        "sig-new": "Neu",
        "sig-spicy": "Spezial",
        "sig-dish1": "Gemischte Grillplatte",
        "sig-dish1-desc": "Ausgewählte Grillplatte mit täglich frischem Fisch.",
        "sig-dish2": "Sardellen-Salat (Hamsi)",
        "sig-dish2-desc": "Der Schwarzmeer-Klassiker, ein besonderer Salat mit frischen Sardellen.",
        "sig-dish3": "Lachs-Sandwich",
        "sig-dish3-desc": "Köstliches Sandwich mit frischem Lachs, knusprigem Brot und Spezialsauce.",
        "sig-dish4": "Garnelenpfanne Spezial",
        "sig-dish4-desc": "In Butter sautierte Garnelen mit der legendären TAKA-Gewürzmischung.",
`,
    en: `
        "sig-chef": "Chef's Choice",
        "sig-popular": "Most Popular",
        "sig-new": "New",
        "sig-spicy": "Special",
        "sig-dish1": "Mixed Grill Platter",
        "sig-dish1-desc": "Selected grill platter prepared with daily fresh fish.",
        "sig-dish2": "Anchovy Salad",
        "sig-dish2-desc": "The Black Sea classic, a special salad made with fresh anchovies.",
        "sig-dish3": "Salmon Sandwich",
        "sig-dish3-desc": "Delicious sandwich with fresh salmon, crispy bread and special sauce.",
        "sig-dish4": "Shrimp Pan Special",
        "sig-dish4-desc": "Butter-sautéed shrimp with TAKA's legendary spice blend.",
`,
    ru: `
        "sig-chef": "Выбор шеф-повара",
        "sig-popular": "Самые популярные",
        "sig-new": "Новое",
        "sig-spicy": "Специальный",
        "sig-dish1": "Ассорти на гриле",
        "sig-dish1-desc": "Отборное рыбное ассорти на гриле из свежего улова.",
        "sig-dish2": "Салат с хамсой",
        "sig-dish2-desc": "Черноморская классика, фирменный салат со свежей хамсой.",
        "sig-dish3": "Сэндвич с лососем",
        "sig-dish3-desc": "Вкуснейший сэндвич со свежим лососем, хрустящим хлебом и фирменным соусом.",
        "sig-dish4": "Креветки на сковороде",
        "sig-dish4-desc": "Креветки, обжаренные в сливочном масле с легендарными специями TAKA.",
`,
    es: `
        "sig-chef": "Recomendación del Chef",
        "sig-popular": "Más popular",
        "sig-new": "Nuevo",
        "sig-spicy": "Especial",
        "sig-dish1": "Parrillada Mixta",
        "sig-dish1-desc": "Parrillada selecta preparada con pescado fresco del día.",
        "sig-dish2": "Ensalada de Anchoas",
        "sig-dish2-desc": "El clásico del Mar Negro, una ensalada especial con anchoas frescas.",
        "sig-dish3": "Sándwich de Salmón",
        "sig-dish3-desc": "Delicioso sándwich con salmón fresco, pan crujiente y salsa especial.",
        "sig-dish4": "Sartén de Camarones Especial",
        "sig-dish4-desc": "Camarones salteados en mantequilla con la legendaria mezcla de especias TAKA.",
`,
    ar: `
        "sig-chef": "اختيار الشيف",
        "sig-popular": "الأكثر شهرة",
        "sig-new": "جديد",
        "sig-spicy": "خاص",
        "sig-dish1": "طبق مشاوي مشكل",
        "sig-dish1-desc": "طبق مشاوي مختار محضر من أسماك طازجة يومياً.",
        "sig-dish2": "سلطة الأنشوجة",
        "sig-dish2-desc": "كلاسيكية البحر الأسود، سلطة خاصة محضرة من الأنشوجة الطازجة.",
        "sig-dish3": "ساندويتش السلمون",
        "sig-dish3-desc": "ساندويتش لذيذ مع السلمون الطازج والخبز المقرمش والصلصة الخاصة.",
        "sig-dish4": "مقلاة الروبيان الخاصة",
        "sig-dish4-desc": "روبيان مقلي بالزبدة مع توابل تاكا الأسطورية.",
`
};

const files = [
    'assets/js/translations.js',
    'qr-menu/assets/js/translations.js'
];

files.forEach(file => {
    let content = fs.readFileSync(file, 'utf-8');
    
    for (const [lang, appendText] of Object.entries(keysToAdd)) {
        const langRegex = new RegExp('(' + lang + ':\\s*{[\\s\\S]*?)("sig-subtitle":\\s*"[^"]*",?)');
        content = content.replace(langRegex, (match, p1, p2) => {
            return p1 + p2 + appendText;
        });
    }
    
    fs.writeFileSync(file, content, 'utf-8');
    console.log('Updated ' + file);
});
