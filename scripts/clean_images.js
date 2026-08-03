const fs = require('fs');

const dataPath = 'qr-menu/assets/js/menu-data.js';
let content = fs.readFileSync(dataPath, 'utf8');

// Extract the array
let dataStr = content.substring(content.indexOf('['), content.lastIndexOf(']') + 1);

let menuData;
try {
    menuData = eval(dataStr);
} catch(e) {
    console.error("Failed to parse menu-data.js", e);
    process.exit(1);
}

// Modify
menuData.forEach(category => {
    category.items.forEach(item => {
        if (item.nameTR === "Havuç Tarator") {
            item.image = "assets/havuc_tarator_ai.png";
        } else if (item.nameTR === "Acı Antep Ezmesi") {
            item.image = "assets/antepe_ezmesi_ai.png";
        } else if (item.nameTR === "Levrek Marin") {
            item.image = "assets/levrek_marin_ai.png";
        } else if (item.image && item.image.includes('unsplash.com')) {
            delete item.image; // Remove generic Unsplash images
        }
    });
});

let newContent = `const menuData = ${JSON.stringify(menuData, null, 4)};\n\nwindow.menuData = menuData;\n`;
fs.writeFileSync(dataPath, newContent);
console.log("Updated menu-data.js successfully.");
