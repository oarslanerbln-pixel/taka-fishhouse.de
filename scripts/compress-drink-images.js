const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

const DIR = 'assets/img/products';

// [pngFile, jpgFile] — PNG kaldırılıp yerine sıkıştırılmış JPG kullanılacak,
// menu-data.js'teki image yolları da buna göre güncellenecek.
const jobs = [
  ['ayran_7gun.png', 'ayran_7gun.jpg'],
  ['buyuk_cay_v2.png', 'buyuk_cay_v2.jpg'],
  ['cappuccino.png', 'cappuccino.jpg'],
  ['capri_sonne.png', 'capri_sonne.jpg'],
  ['cay_cesitleri.png', 'cay_cesitleri.jpg'],
  ['fritz_cola_zero.png', 'fritz_cola_zero.jpg'],
  ['fuzetea.png', 'fuzetea.jpg'],
  ['kaffee_crema_v2.png', 'kaffee_crema_v2.jpg'],
  ['kucuk_cay_v2.png', 'kucuk_cay_v2.jpg'],
  ['lachs_dorade_durum.png', 'lachs_dorade_durum.jpg'],
  ['salgam_v2.png', 'salgam_v2.jpg'],
  ['turk_kahvesi_v2.png', 'turk_kahvesi_v2.jpg'],
  ['uludag_gazoz.png', 'uludag_gazoz.jpg'],
];

(async () => {
  const results = [];
  for (const [src, out] of jobs) {
    const srcPath = path.join(DIR, src);
    const outPath = path.join(DIR, out);
    const before = fs.statSync(srcPath).size;
    const buf = await sharp(srcPath)
      .resize({ width: 1024, withoutEnlargement: true })
      .flatten({ background: '#ffffff' })
      .jpeg({ quality: 82, mozjpeg: true, progressive: true })
      .toBuffer();
    fs.writeFileSync(outPath, buf);
    fs.unlinkSync(srcPath);
    results.push({ src, out, before, after: buf.length });
  }
  results.forEach(r => console.log(`${r.src} -> ${r.out}: ${(r.before/1024).toFixed(0)}KB -> ${(r.after/1024).toFixed(0)}KB`));
})();
