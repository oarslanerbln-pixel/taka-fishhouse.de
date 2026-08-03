const fs = require('fs');
const path = require('path');

// Proje ana dizini
const rootDir = __dirname;

// Taranacak medya uzantıları
const mediaExtensions = ['.jpg', '.jpeg', '.png', '.webp', '.mp4', '.avif', '.svg', '.gif', '.pdf'];

// Kodların okunacağı hedef dosyalar ve klasörler
const sourcePaths = [
    'assets/js/menu-data.js',
    'qr-menu/assets/js/menu-page.js',
    'assets/js/menu-page.js',
    'index.html',
    'qr-menu/index.html',
    'assets/css',
    'qr-menu/assets/css'
];

// Medyaların aranacağı klasörler
const assetFolders = [
    'assets',
    'qr-menu/assets'
];

// Kesinlikle silinmesini istediğimiz gereksiz dosyalar
const explicitDeletions = [
    'qr-menu/assets/wolt_page_debug.html'
];

function getAllFiles(dirPath, arrayOfFiles) {
    if (!fs.existsSync(dirPath)) return arrayOfFiles;
    
    const files = fs.readdirSync(dirPath);
    arrayOfFiles = arrayOfFiles || [];

    files.forEach(function (file) {
        if (fs.statSync(dirPath + "/" + file).isDirectory()) {
            arrayOfFiles = getAllFiles(dirPath + "/" + file, arrayOfFiles);
        } else {
            arrayOfFiles.push(path.join(dirPath, "/", file));
        }
    });

    return arrayOfFiles;
}

function runCleanup() {
    console.log("🔍 Taka Fisch Haus Akıllı Temizlik Aracı Başladı...\n");
    
    const isDeleteMode = process.argv.includes('--delete');

    // 1. Tüm text kod içeriğini birleştir
    let allSourceCode = "";
    
    sourcePaths.forEach(srcPath => {
        const fullPath = path.join(rootDir, srcPath);
        if (fs.existsSync(fullPath)) {
            if (fs.statSync(fullPath).isDirectory()) {
                const files = getAllFiles(fullPath);
                files.forEach(f => {
                    if (f.endsWith('.css') || f.endsWith('.js') || f.endsWith('.html')) {
                        allSourceCode += fs.readFileSync(f, 'utf8') + "\n";
                    }
                });
            } else {
                allSourceCode += fs.readFileSync(fullPath, 'utf8') + "\n";
            }
        }
    });

    // 2. Asset dosyalarını bul
    let allAssetFiles = [];
    assetFolders.forEach(folder => {
        const fullPath = path.join(rootDir, folder);
        if (fs.existsSync(fullPath)) {
            allAssetFiles = getAllFiles(fullPath, allAssetFiles);
        }
    });

    // Filtreleme (sadece resim/video)
    allAssetFiles = allAssetFiles.filter(file => {
        return mediaExtensions.includes(path.extname(file).toLowerCase());
    });

    let unusedFiles = [];
    let usedCount = 0;

    // 3. Dosya isimlerinin source kodda geçip geçmediğini kontrol et
    allAssetFiles.forEach(file => {
        const baseName = path.basename(file);
        
        // Çok katı bir güvenlik: isim string olarak hiç geçmiyorsa kullanılmıyor demektir.
        // Hatalı URL eşleşmeleri veya URL decode gerektiren boşluklu isimler için baseName'i encode ederek de bakalım.
        const encodedBaseName = encodeURIComponent(baseName);
        
        if (allSourceCode.includes(baseName) || allSourceCode.includes(encodedBaseName)) {
            usedCount++;
        } else {
            unusedFiles.push(file);
        }
    });

    // Kesin silinecekleri ekle
    explicitDeletions.forEach(delPath => {
        const fullPath = path.join(rootDir, delPath);
        if (fs.existsSync(fullPath)) {
            unusedFiles.push(fullPath);
        }
    });

    console.log(`✅ Toplam Kod Dosyası Tarandı.`);
    console.log(`📷 Toplam Medya Dosyası: ${allAssetFiles.length}`);
    console.log(`🔗 Aktif Kullanılan: ${usedCount}`);
    console.log(`🗑️ KULLANILMAYAN (ÇÖP) DOSYA SAYISI: ${unusedFiles.length}\n`);

    if (unusedFiles.length > 0) {
        if (!isDeleteMode) {
            console.log("🚨 KULLANILMAYAN DOSYALARIN LİSTESİ (SİLİNMEDİ! Sadece Analiz):");
            unusedFiles.forEach(f => {
                console.log(" - " + path.relative(rootDir, f));
            });
            console.log("\n⚠️ DİKKAT: Bu dosyaları KALICI olarak silmek için komutu şu şekilde çalıştırın:");
            console.log("   node cleanup-unused-assets.js --delete");
        } else {
            console.log("💥 DOSYALAR SİLİNİYOR...");
            let deletedCount = 0;
            unusedFiles.forEach(f => {
                try {
                    fs.unlinkSync(f);
                    console.log("Silindi: " + path.relative(rootDir, f));
                    deletedCount++;
                } catch (e) {
                    console.error("Hata! Silinemedi: " + path.relative(rootDir, f));
                }
            });
            console.log(`\n🎉 BAŞARILI: Toplam ${deletedCount} gereksiz dosya temizlendi.`);
            console.log("Şimdi 'vercel --prod' komutuyla çok daha hızlı deploy edebilirsiniz!");
        }
    } else {
        console.log("🌟 Harika! Projenizde hiç gereksiz dosya kalmamış.");
    }
}

runCleanup();
