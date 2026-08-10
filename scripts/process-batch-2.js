const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

const SRC_DIR = 'YENI ÜRÜN RESIMLERI';
const OUT_DIR = 'assets/img/products';

// [sourceFile, itemId, outputFileName]
const jobs = [
  ['alabalik.png', 68, 'forelle_ai.jpg'],
  ['barbun.png', 65, 'rotbarbe_ai2.jpg'],
  ['kuru cacik.png', 31, 'kuru_cacik_ai.jpg'],
  ['wolfsbarsch marin.png', 16, 'wolfsbarsch_marin_ai.jpg'],
  ['köfte pilav - 01.png', 109, 'balik_kofte_pilav_01.jpg'],
  ['jumbo garnelen.png', 39, 'jumbo_garnelen_ai.jpg'],
  ['karisik izgara.png', 74, 'gemischter_taka_spezial_teller_ai.jpg'],
  ['humus mit pastirma.png', 47, 'humus_mit_pastirma_ai.jpg'],
  ['girit ezmesi.png', 19, 'girit_ezmesi_ai.jpg'],
];

(async () => {
  const results = [];
  for (const [src, itemId, outName] of jobs) {
    const srcPath = path.join(SRC_DIR, src);
    const outPath = path.join(OUT_DIR, outName);
    if (!fs.existsSync(srcPath)) {
      results.push({ itemId, outName, status: 'MISSING_SOURCE' });
      continue;
    }
    try {
      const buf = await sharp(srcPath)
        .resize({ width: 1024, withoutEnlargement: true })
        .flatten({ background: '#ffffff' })
        .jpeg({ quality: 85, mozjpeg: true, progressive: true })
        .toBuffer();
      fs.writeFileSync(outPath, buf);
      results.push({ itemId, outName, status: 'OK', bytes: buf.length });
    } catch (e) {
      results.push({ itemId, outName, status: 'ERROR: ' + e.message });
    }
  }
  const ok = results.filter(r => r.status === 'OK').length;
  console.log(`Done: ${ok}/${results.length}`);
  results.forEach(r => console.log(' -', r.outName, r.status, r.bytes || ''));
})();
