// Netlify yayını için sadece sitenin gerçek dosyalarını dist/ altına kopyalar.
// Repoda ham fotoğraflar, arşivler ve yardımcı scriptler var (yüzlerce MB);
// bunlar .vercelignore ile Vercel'e de gitmiyordu, aynı kuralları burada uyguluyoruz.
const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const out = path.join(root, 'dist');

const ROOT_FILES = [
    'index.html', 'danke.html', 'datenschutz.html', 'impressum.html', 'menu.html',
    'robots.txt', 'sitemap.xml', 'sw.js', 'service-worker.js'
];
const DIRS = ['assets', 'qr-menu'];

function keep(src) {
    const rel = path.relative(root, src).split(path.sep).join('/');
    const base = path.basename(src);
    if (/\.(py|log)$/i.test(base)) return false;
    if (/scratch/i.test(rel)) return false;
    if (/^_DSC.*\.JPG$/.test(base)) return false;
    if (base === 'vercel.json') return false;
    if (/^qr-menu\/[^/]+\.(json|png|jpg)$/i.test(rel)) return false; // scrape verisi / ekran görüntüleri
    return true;
}

fs.rmSync(out, { recursive: true, force: true });
fs.mkdirSync(out);
for (const f of ROOT_FILES) {
    const src = path.join(root, f);
    if (fs.existsSync(src)) fs.copyFileSync(src, path.join(out, f));
}
for (const d of DIRS) {
    fs.cpSync(path.join(root, d), path.join(out, d), { recursive: true, filter: keep });
}
console.log('dist hazır');
