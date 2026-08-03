const fs = require('fs');

const dataPath = 'qr-menu/assets/js/menu-data.js';
let content = fs.readFileSync(dataPath, 'utf8');

let dataStr = content.substring(content.indexOf('['), content.lastIndexOf(']') + 1);

let menuData;
try {
    menuData = eval(dataStr);
} catch(e) {
    console.error("Failed to parse menu-data.js", e);
    process.exit(1);
}

menuData.forEach(category => {
    category.items.forEach(item => {
        if (item.nameTR === "Hamsili Pilav") {
            item.image = "assets/hamsili_pilav_ai.png";
        } else if (item.nameTR === "Turşu Kavurması") {
            item.image = "assets/tursu_kavurmasi_ai.png";
        } else if (item.nameTR === "Tuzda Balık (4 Kişiye uygun)") {
            item.image = "assets/tuzda_balik_ai.png";
        } else if (item.nameTR === "2 Kişilik Balık Buğulama" || item.nameTR === "4 Kişilik Balık Buğulama") {
            item.image = "assets/balik_bugulama_ai.png";
        }
    });
});

let newContent = `const menuData = ${JSON.stringify(menuData, null, 4)};\n\nwindow.menuData = menuData;\n`;
fs.writeFileSync(dataPath, newContent);
console.log("Updated menu-data.js successfully with specials.");
