const fs = require('fs');

const dataPaths = ['qr-menu/assets/js/menu-data.js', 'assets/js/menu-data.js'];

dataPaths.forEach(dataPath => {
    let content = fs.readFileSync(dataPath, 'utf8');
    let dataStr = content.substring(content.indexOf('['), content.lastIndexOf(']') + 1);

    let menuData;
    try {
        menuData = eval(dataStr);
    } catch(e) {
        console.error("Failed to parse", dataPath, e);
        return;
    }

    menuData.forEach(category => {
        category.items.forEach(item => {
            if (item.nameTR === "Balık Çorbası") {
                item.image = "assets/balik_corbasi_1781536844068.png";
            } else if (item.nameTR === "Süzme Mercimek Çorbası") {
                item.image = "assets/mercimek_corbasi_1781536891043.png";
            } else if (item.nameTR === "Çoban Salatası") {
                item.image = "assets/coban_salatasi_1781536902968.png";
            } else if (item.nameTR === "Roka Salatası") {
                item.image = "assets/roka_salatasi_1781536915057.png";
            }
        });
    });

    let newContent = `const menuData = ${JSON.stringify(menuData, null, 4)};\n\nwindow.menuData = menuData;\n`;
    fs.writeFileSync(dataPath, newContent);
    console.log("Updated", dataPath);
});
