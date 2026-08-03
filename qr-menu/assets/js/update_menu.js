const fs = require('fs');

const dataPath = './menu-data.js';
let content = fs.readFileSync(dataPath, 'utf-8');

// Temporarily convert to CommonJS to require it
const tempPath = './temp-menu.js';
fs.writeFileSync(tempPath, content.replace('const menuData =', 'module.exports =').replace('window.menuData = menuData;', ''));

const menuData = require('./temp-menu.js');

// Prices and removals mapping
const updates = {
    // Ana Yemekler -> Hauptgerichte
    61: { price: "24,50" }, // Çipura
    62: { price: "24,50" }, // Levrek
    63: { price: "20,00" }, // Hamsi Tava
    65: { price: "25,00" }, // Barbun
    66: { price: "22,00" }, // Uskumru
    67: { price: "26,00" }, // Somon File
    68: { price: "23,00" }, // Alabalık
    71: { price: "22,00" }, // Mezgit
    72: { price: "22,00" }, // İstavrit
    73: { price: "22,00" }, // Kalamar Halka
    74: { price: "29,50" }, // Karışık Izgara
    75: { price: "25,00" }, // Tereyağlı Karides
    76: { price: "25,00" }, // Domatesli Karides
    77: { price: "28,00" }, // Taka Spesiyal Karides
    78: { price: "32,00" }, // Izgara Ahtapot
    80: { price: "32,00" }, // Dil Balığı
    
    // Ara Sıcaklar -> Warme Zwischengerichte
    38: { price: "19,50" }, // Kaşarlı Karides Güveç
    39: { price: "21,50" }, // Izgara Karides
    41: { price: "18,50" }, // Pastırmalı Ahtapot
    42: { price: "16,50" }, // Patlıcanlı Balık
    43: { price: "15,50" }, // Balık Kokoreç
    44: { price: "18,50" }, // Deniz Mahsülleri Taka
    45: { price: "10,50" }, // Kaşarlı Mantar
    46: { price: "10,50" }, // Kaşarlı Brokoli
    47: { price: "9,50" }, // Pastırmalı Humus
    48: { price: "8,50" }, // Soğan Sarımsak Güveç (Wait, is this in the new menu? New menu doesn't have Soğan Sarımsak Güveç! Wait, let's keep it if not sure, but user said "bazıları yok". Let's check.)
    49: { price: "7,50" }, // Tavada Kızarmış Patates
    50: { price: "4,50" }, // Patates Kızartması
    
    // Soğuk Mezeler -> Kalte Vorspeisen
    10: { price: "13,50 / 22,50" }, // Karışık Meze (Gemischter Vorspeisenteller)
    13: { price: "4,50 / 7,50" }, // Havuç Tarator
    14: { price: "4,50 / 7,50" }, // Acı Antep Ezmesi
    15: { price: "4,50 / 7,50" }, // Humus
    16: { price: "8,50 / 12,50" }, // Levrek Marin
    17: { price: "8,50 / 12,50" }, // Deniz Mahsülleri
    18: { price: "4,50 / 7,50" }, // Şakşuka
    19: { price: "4,50 / 7,50" }, // Girit Ezmesi
    20: { price: "4,50 / 7,50" }, // Fava (Wait, Fava is not in the new menu! It goes up to 23 in new menu)
    21: { price: "4,50 / 7,50" }, // Köpoğlu
    22: { price: "9,50 / 14,50" }, // Ahtapot Salatası
    23: { price: "4,50 / 7,50" }, // Narlı Dibariye
    27: { price: "4,50 / 7,50" }, // Urla Meze
    30: { price: "4,50 / 7,50" }, // Yoğurtlu Patlıcan
    31: { price: "4,50 / 7,50" }, // Kuru Cacık
    32: { price: "4,50 / 7,50" }, // Pembe Sultan
    35: { price: "9,50 / 12,50" }, // Deniz Börülcesi
    
    // Çorba ve Salata -> Suppen / Salate
    1: { price: "8,50" }, // Balık Çorbası
    4: { price: "6,00 / 8,00" }, // Karışık Yeşil Salata
    5: { price: "6,50 / 8,50" }, // Çoban Salatası
    6: { price: "6,00 / 8,00" }, // Roka Salatası
    7: { price: "17,50" }, // Somon Salatası
    8: { price: "17,50" }, // Karides Salatası
    9: { price: "15,50" }, // Hamsi Salatası
    
    // Çocuk Menüsü & Makarna -> Kindermenü & Nudeln
    108: { price: "16,00" }, // Balık Burger Menü
    109: { price: "16,00" }, // Balık Köfte Menü
    112: { price: "20,00" }, // Somonlu Makarna
    113: { price: "20,00" }, // Karidesli Makarna
    
    // Tatlılar -> Desserts
    116: { price: "9,00" }, // Dondurmalı İrmik Helvası
    118: { price: "7,90" }, // Fırında Meyhane Helvası
    119: { price: "5,90" }, // Kazandibi -> Wait, Kazandibi is not in new menu! New menu has Erdbeer Magnolia 5,90.
    120: { price: "5,90" }, // Hamsiköy Sütlacı
    
    // İçecekler -> Getränke
    130: { price: "2,50 / 6,50" }, // Su
    131: { price: "2,90 / 6,90" }, // Maden Suyu
    // the rest of 0,2l drinks are 2,90 which is correct
};

// IDs to remove explicitly as per user instruction and missing from physical menu
const toRemove = [
    56, 57, 84, 85, 86, // Spesiyaller & Karadeniz (Hamsili Pilav, Turşu, Tuzda Balık, Buğulama)
    81, // Kılıç Balığı
    79, // Balık Güveç
    64, // Hamsi Buğulama
    20, 28, 29, 33, 34, // Fava, Avokadolu Karides, Peynirli Fesleğen, Elmalı Semizotu, Sağlık İksiri
    48, // Soğan Sarımsak Güveç
    117, 119, 121, // Un Helvası, Kazandibi, Kabak Tatlısı
    2 // Günün Çorbası
];

// Process menuData
const newData = [];

for (const category of menuData) {
    if (category.categoryId === 'spezialitaten') continue; // Category entirely removed in new menu
    
    const newItems = [];
    for (const item of category.items) {
        if (toRemove.includes(item.id)) continue;
        
        if (updates[item.id]) {
            item.price = updates[item.id].price;
        }
        newItems.push(item);
    }
    
    category.items = newItems;
    newData.push(category);
}

// Ensure "Zinnur" and "Çıtır Enginar" are added maybe?
// User said "görsel açıdan bizim tasarladığımız görseller kalsın, fiyatlar önemli, olmayanları çıkar".
// So I will just update the current ones and remove the missing ones. I won't add the new ones because we don't have images for them, unless required. Let's just do what's safe.

let finalContent = `const menuData = ${JSON.stringify(newData, null, 4)};\n\nwindow.menuData = menuData;\n`;

fs.writeFileSync(dataPath, finalContent);
fs.unlinkSync(tempPath);
console.log('Update complete.');
