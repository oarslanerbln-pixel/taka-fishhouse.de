/*
 * Bir kerelik göç scripti: assets/js/menu-data.js içindeki her ürüne
 * kalıcı bir "diet" alanı ekler ({ vegetarian, glutenFree }).
 *
 * Eskiden qr-menu/assets/js/menu-page.js şunu yapıyordu:
 *   isVeg = vegetarianIds.includes(id) || id >= 130 || category === 'desserts' | 'getranke' | 'alkohol'
 * "id >= 130" rastgele bir sayısal eşikti — ürünün ne olduğuyla ilgisi yoktu.
 * "desserts"/"getranke"/"alkohol" kategori ID'leri de veride hiç yoktu
 * (gerçek ID'ler: tatlilar, soguk-icecekler, sicak-icecekler).
 *
 * Bu script onun yerine, ürünün KENDİ verisinden türetilen kurallar kullanır:
 *   - vegetarian: EU alerjen kodları 2 (kabuklu deniz ürünü), 4 (balık),
 *     14 (yumuşakça) varsa YA DA isimde et/balık anahtar kelimesi geçiyorsa false.
 *   - glutenFree: alerjen kodu "1" (gluten) varsa false; kırılgan/ekmekli/
 *     unlu/kaplamalı isim kalıpları (sandviç, dürüm, makarna, helva, kızarmış
 *     dondurma, pommes/patates kızartması...) varsa mutfak beyan etmemiş olsa
 *     bile temkinli davranıp false yapılır; bunların dışında mutfağın kendi
 *     alerjen beyanına güvenilir.
 *
 * Sonuç kesin bir gıda güvenliği sertifikası DEĞİLDİR — mutfağın gerçek
 * uygulamalarını (ortak kızartma yağı, çapraz bulaşma) bilmiyorum. Script
 * çıktısını incelemeniz için "İNCELEME GEREKİYOR" etiketli satırlar ayrıca
 * konsola basılır.
 */
const fs = require('fs');
const path = require('path');

const FILE = path.join(__dirname, '..', 'assets', 'js', 'menu-data.js');

const src = fs.readFileSync(FILE, 'utf8');
const sandbox = { window: {} };
new Function('window', src + '\nwindow.menuData = menuData;')(sandbox.window);
const menuData = sandbox.window.menuData;

const MEAT_FISH_KEYWORDS = [
    // Balık / fish
    'fisch', 'fish', 'balık', 'balik',
    'lachs', 'salmon', 'somon',
    'dorade', 'sea bream', 'çipura', 'cipura',
    'wolfsbarsch', 'sea bass', 'levrek',
    'hamsi', 'anchov',
    'barbun', 'mullet',
    'uskumru', 'makrele', 'mackerel',
    'alabalık', 'alabalik', 'forelle', 'trout',
    'mezgit', 'whiting', 'merlan',
    'istavrit', 'stöcker', 'horse mackerel',
    'dil balığı', 'dil baligi', 'seezunge', 'sole fish',
    'sardalya', 'sardine',
    // Kabuklu / kısımlar / yumuşakça
    'kalamar', 'calamari', 'karides', 'garnele', 'shrimp',
    'ahtapot', 'oktopus', 'octopus', 'midye', 'mussel',
    'meeresfrücht', 'meeresfruecht', 'seafood', 'deniz mahsül', 'deniz mahsul',
    // Kırmızı et / işlenmiş et (bu menüde sadece pastırma garnitür olarak geçiyor)
    'pastırma', 'pastirma', 'speck'
];

const GLUTEN_RISK_KEYWORDS = [
    'sandwich', 'sandviç', 'sandvic',
    'dürüm', 'durum', 'wrap', 'burger',
    'nudeln', 'makarna', 'pasta',
    'helva', 'halva', 'grieß', 'greiss', 'irmik',
    'paniert', 'kalamar halka', 'crispy',
    'kızarmış dondurma', 'kizarmis dondurma', 'fried ice cream',
    'pommes', 'patates kızart', 'patates kizart', 'french fries',
    'kokoreç', 'kokorec'
];

// Alerjen alanı hiç dolu olmayan, gerçekten "sade" ürünler için
// (su, çay, kahve, çıplak salata) — pişmiş/işlenmiş yemekler için GEÇERLİ DEĞİL.
const RAW_SAFE_CATEGORIES = new Set(['soguk-icecekler', 'sicak-icecekler']);
const RAW_SAFE_SALAD_IDS = new Set([4, 5, 6]); // sade yeşil/çoban/roka salatası — sos/alerjen beyanı yok ama çiğ sebze

function hasKeyword(name, list) {
    const n = name.toLowerCase();
    return list.some(k => n.includes(k));
}

function classify(item, categoryId) {
    const codes = String(item.allergens || '').split(',').map(s => s.trim()).filter(Boolean);
    const hasCode = c => codes.includes(c);
    const name = [item.nameTR, item.nameDE, item.nameEN].filter(Boolean).join(' | ');

    const seafoodAllergen = hasCode('2') || hasCode('4') || hasCode('14');
    const nameSuggestsMeatFish = hasKeyword(name, MEAT_FISH_KEYWORDS);
    const vegetarian = !seafoodAllergen && !nameSuggestsMeatFish;

    const glutenAllergen = hasCode('1');
    const nameSuggestsGlutenRisk = hasKeyword(name, GLUTEN_RISK_KEYWORDS);

    let glutenFree;
    let flag = null;

    if (glutenAllergen) {
        glutenFree = false;
    } else if (nameSuggestsGlutenRisk) {
        glutenFree = false;
        if (codes.length && !hasCode('1')) {
            flag = `Alerjen listesi "1" (gluten) içermiyor ama isim gluten riski taşıyor — mutfağın "${item.allergens}" beyanını kontrol edin.`;
        }
    } else if (codes.length) {
        glutenFree = true; // mutfağın kendi beyanına güveniliyor
    } else if (RAW_SAFE_CATEGORIES.has(categoryId) || RAW_SAFE_SALAD_IDS.has(item.id)) {
        glutenFree = true;
    } else {
        glutenFree = false; // veri yok — iddia yok
        flag = 'Alerjen alanı hiç dolu değil; glutensiz varsayılmadı, mutfağın doldurması gerekiyor.';
    }

    // Girit Ezmesi (peynir ezmesi) gibi, isimle alerjen kodu çelişen durumları ayrıca işaretle.
    if (seafoodAllergen && !hasKeyword(name, MEAT_FISH_KEYWORDS) && !/deniz|meeres|seafood/i.test(name)) {
        flag = (flag ? flag + ' ' : '') + `İsimde balık/deniz ürünü ipucu yok ama alerjen kodu "${item.allergens}" balık/kabuklu/yumuşakça içeriyor — veri girişi hatası olabilir, mutfakla teyit edin.`;
    }

    return { vegetarian, glutenFree, flag };
}

const flags = [];
const idCounts = new Map();

for (const category of menuData) {
    for (const item of category.items) {
        const { vegetarian, glutenFree, flag } = classify(item, category.categoryId);
        item.diet = { vegetarian, glutenFree };
        if (flag) flags.push(`  [#${item.id} ${item.nameDE || item.nameTR}] ${flag}`);

        const key = item.id;
        idCounts.set(key, (idCounts.get(key) || 0) + 1);
    }
}

const dupIds = [...idCounts.entries()].filter(([, n]) => n > 1).map(([id]) => id);

// ---- Dosyayı yeniden yaz ----
function serialize(data) {
    return JSON.stringify(data, null, 4)
        // JSON.stringify tek tırnak kullanmaz; orijinal dosya çift tırnaklıydı, aynı kalsın.
        .replace(/^(\s*)"([a-zA-Z0-9_]+)":/gm, '$1"$2":');
}

const out = `const menuData = ${serialize(menuData)};\n\nwindow.menuData = menuData;\n`;
fs.writeFileSync(FILE, out, 'utf8');

console.log(`Yazıldı: ${FILE}`);
console.log(`Toplam ürün: ${[...idCounts.values()].reduce((a, b) => a + b, 0)}`);
console.log('');
console.log(`=== İNCELEME GEREKEN ${flags.length} SATIR ===`);
flags.forEach(f => console.log(f));
console.log('');
console.log(`=== TEKRARLANAN ID'LER (${dupIds.length}) — ayrı bir veri bütünlüğü sorunu, bu göçle ilgisi yok ===`);
console.log('  ' + dupIds.join(', '));
