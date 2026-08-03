/*
 * Google Fonts'u yerel barındırmaya taşır (DSGVO / LG München I kararı
 * riskini kapatmak için — dış CDN'den font çekmek ziyaretçinin IP'sini
 * onaysız Google'a gönderiyor).
 *
 * Siteye şu ana kadar dağılmış 4 aile/6 <link>/@import isteğini tek bir
 * yerel css2.css + assets/fonts/*.woff2 setine indirger.
 *
 * 1. Her aile için Google'ın css2 endpoint'ini MODERN bir User-Agent ile
 *    çeker (woff2 URL'leri almak için — eski UA ttf/eot döner).
 * 2. Dönen CSS'teki her @font-face bloğundaki woff2 dosyasını indirir.
 * 3. Yerel dosya adlarıyla yeni bir @font-face CSS'i üretir
 *    (assets/fonts/fonts.css).
 */
const fs = require('fs');
const path = require('path');
const https = require('https');

const ROOT = path.join(__dirname, '..');
const FONTS_DIR = path.join(ROOT, 'assets', 'fonts');
fs.mkdirSync(FONTS_DIR, { recursive: true });

const MODERN_UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36';

// Sitede gerçekten kullanılan tüm aile+kesim kombinasyonlarının birleşimi
// (index.html/_typography.css + menu.html/impressum/datenschutz +
// qr-menu/index.html + style.css @import taranarak çıkarıldı).
const FAMILIES = [
    'Inter:wght@300;400;500;600;700',
    'Oswald:wght@300;400;500;600;700',
    'Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500',
    'Cormorant+Garamond:wght@300;400;600',
];

function fetchText(url, headers = {}) {
    return new Promise((resolve, reject) => {
        https.get(url, { headers: { 'User-Agent': MODERN_UA, ...headers } }, (res) => {
            if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
                fetchText(res.headers.location, headers).then(resolve, reject);
                return;
            }
            let data = '';
            res.on('data', (c) => (data += c));
            res.on('end', () => resolve(data));
        }).on('error', reject);
    });
}

function fetchBinary(url) {
    return new Promise((resolve, reject) => {
        https.get(url, { headers: { 'User-Agent': MODERN_UA } }, (res) => {
            if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
                fetchBinary(res.headers.location).then(resolve, reject);
                return;
            }
            const chunks = [];
            res.on('data', (c) => chunks.push(c));
            res.on('end', () => resolve(Buffer.concat(chunks)));
        }).on('error', reject);
    });
}

function slugFamily(name) {
    return name.toLowerCase().replace(/[^a-z0-9]+/g, '-');
}

async function run() {
    let outCss = '/* Yerel barındırılan Google Fonts — scripts/localize-fonts.js ile üretildi.\n   DSGVO: font dosyaları artık Google sunucularından değil, bu domainden servis ediliyor. */\n\n';
    let fileCount = 0;
    // (aile|ağırlık|stil) başına sıra numarası — Google'ın alt küme (latin/
    // cyrillic/greek/vietnamese) adlarını GÜVENİLİR şekilde tahmin etmeye
    // çalışmak yerine (önceki iki deneme de yanlış eşleşip dosyaların
    // sessizce üzerine yazılmasına yol açtı) her bloğa çakışması imkansız
    // bir sıra numarası veriliyor. Gerçek unicode-range CSS yorumunda duruyor.
    const seq = new Map();

    for (const familyParam of FAMILIES) {
        const url = `https://fonts.googleapis.com/css2?family=${familyParam}&display=swap`;
        console.log('Çekiliyor:', url);
        const css = await fetchText(url);

        const blocks = css.split('@font-face').slice(1).map((b) => '@font-face' + b.split('}')[0] + '}');
        for (const block of blocks) {
            const family = (block.match(/font-family:\s*'([^']+)'/) || [])[1];
            const style = (block.match(/font-style:\s*(\w+)/) || [])[1] || 'normal';
            const weight = (block.match(/font-weight:\s*(\d+)/) || [])[1] || '400';
            const unicodeRange = (block.match(/unicode-range:\s*([^;]+);/) || [])[1] || '';
            const srcUrl = (block.match(/url\(([^)]+)\)/) || [])[1];
            if (!family || !srcUrl) continue;

            const key = `${family}|${weight}|${style}`;
            const n = (seq.get(key) || 0) + 1;
            seq.set(key, n);

            const fileName = `${slugFamily(family)}-${weight}-${style}-${n}.woff2`;
            const filePath = path.join(FONTS_DIR, fileName);

            const buf = await fetchBinary(srcUrl);
            fs.writeFileSync(filePath, buf);
            fileCount++;
            console.log('  indirildi:', fileName, (buf.length / 1024).toFixed(0) + 'KB', '| range:', unicodeRange.slice(0, 50));

            outCss += `/* unicode-range: ${unicodeRange} */\n@font-face {\n  font-family: '${family}';\n  font-style: ${style};\n  font-weight: ${weight};\n  font-display: swap;\n  src: url('../fonts/${fileName}') format('woff2');\n  unicode-range: ${unicodeRange};\n}\n\n`;
        }
    }

    fs.writeFileSync(path.join(ROOT, 'assets', 'css', 'google-fonts-local.css'), outCss, 'utf8');
    console.log('');
    console.log(`Tamamlandı: ${fileCount} font dosyası indirildi.`);
    console.log('Yazıldı: assets/css/google-fonts-local.css');
}

run().catch((e) => { console.error('HATA:', e); process.exit(1); });
