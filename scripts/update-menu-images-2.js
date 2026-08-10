const fs = require('fs');

const updates = {
  68: 'assets/img/products/forelle_ai.jpg',
  65: 'assets/img/products/rotbarbe_ai2.jpg',
  31: 'assets/img/products/kuru_cacik_ai.jpg',
  16: 'assets/img/products/wolfsbarsch_marin_ai.jpg',
  109: 'assets/img/products/balik_kofte_pilav_01.jpg',
  39: 'assets/img/products/jumbo_garnelen_ai.jpg',
  74: 'assets/img/products/gemischter_taka_spezial_teller_ai.jpg',
  47: 'assets/img/products/humus_mit_pastirma_ai.jpg',
  19: 'assets/img/products/girit_ezmesi_ai.jpg',
};

let content = fs.readFileSync('assets/js/menu-data.js', 'utf8');
let notFound = [];
let updated = 0;

for (const [id, newImage] of Object.entries(updates)) {
  const idRegex = new RegExp(`"id":\\s*${id}\\s*,`);
  const idMatch = idRegex.exec(content);
  if (!idMatch) {
    notFound.push({ id, reason: 'id not found' });
    continue;
  }
  const searchStart = idMatch.index + idMatch[0].length;
  const nextIdRegex = /"id":\s*\d+\s*,/;
  const rest = content.slice(searchStart);
  const nextIdMatch = nextIdRegex.exec(rest);
  const windowEnd = nextIdMatch ? searchStart + nextIdMatch.index : content.length;
  const window = content.slice(searchStart, windowEnd);

  const imageFieldRegex = /"image":\s*"[^"]*"/;
  const imgMatch = imageFieldRegex.exec(window);
  if (!imgMatch) {
    notFound.push({ id, reason: 'no image field in window' });
    continue;
  }
  const absoluteStart = searchStart + imgMatch.index;
  const absoluteEnd = absoluteStart + imgMatch[0].length;
  const replacement = `"image": "${newImage}"`;
  content = content.slice(0, absoluteStart) + replacement + content.slice(absoluteEnd);
  updated++;
}

fs.writeFileSync('assets/js/menu-data.js', content);
console.log(`Updated ${updated}/${Object.keys(updates).length} items`);
if (notFound.length) console.log('NOT FOUND:', JSON.stringify(notFound, null, 2));
