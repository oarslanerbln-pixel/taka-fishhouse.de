const fs = require('fs');

const updates = {
  14: 'assets/img/products/acili_ezme.jpg',
  65: 'assets/img/products/barbun.jpg',
  49: 'assets/img/products/bratkartoffel_taka_spezial.jpg',
  108: 'assets/img/products/fisch_burger.jpg',
  9991: 'assets/img/products/crispy_garnelen.jpg',
  35: 'assets/img/products/deniz_borulcesi.jpg',
  80: 'assets/img/products/dil_baligi.jpg',
  76: 'assets/img/products/garnelenpfanne_tomatensosse.jpg',
  61: 'assets/img/products/dorade.jpg',
  91: 'assets/img/products/dorade_sandwich.jpg',
  9701: 'assets/img/products/spesiyal_enginar.jpg',
  1: 'assets/img/products/lachssuppe.jpg',
  42: 'assets/img/products/fisch_auf_auberginenpuereebett.jpg',
  8: 'assets/img/products/garnelensalat.jpg',
  102: 'assets/img/products/garnele_duerum.jpg',
  43: 'assets/img/products/geschnetzelte_fischpfanne.jpg',
  9: 'assets/img/products/hamsisalat.jpg',
  93: 'assets/img/products/sardine_sandwich.jpg',
  63: 'assets/img/products/hamsi_gebraten.jpg',
  13: 'assets/img/products/havuc_tarator.jpg',
  15: 'assets/img/products/humus.jpg',
  81: 'assets/img/products/taka_spezial_2_personen.jpg',
  72: 'assets/img/products/istavrit.jpg',
  77: 'assets/img/products/garnelenpfanne_taka_spezial.jpg',
  10: 'assets/img/products/karisik_meze_tabagi.jpg',
  45: 'assets/img/products/kasarli_mantar.jpg',
  21: 'assets/img/products/kopoglu.jpg',
  90: 'assets/img/products/lachs_sandwich.jpg',
  99: 'assets/img/products/dorade_duerum.jpg',
  67: 'assets/img/products/lachsfilet.jpg',
  122: 'assets/img/products/erdbeer_magnolia.jpg',
  113: 'assets/img/products/penne_mit_garnelen.jpg',
  92: 'assets/img/products/makrele_sandwich.jpg',
  100: 'assets/img/products/makrele_duerum.jpg',
  17: 'assets/img/products/meeresfruechte_meze.jpg',
  71: 'assets/img/products/merlan.jpg',
  41: 'assets/img/products/oktopus_mit_pastirma.jpg',
  22: 'assets/img/products/oktopussalat.jpg',
  78: 'assets/img/products/izgara_ahtapot.jpg',
  32: 'assets/img/products/pembe_sultan.jpg',
  50: 'assets/img/products/pommes_frites.jpg',
  6: 'assets/img/products/rucolasalat.jpg',
  46: 'assets/img/products/ueberbackene_brokkoli.jpg',
  18: 'assets/img/products/saksuka.jpg',
  120: 'assets/img/products/hamsikoy_sutlac.jpg',
  9992: 'assets/img/products/taka_meeresfruechte_spezial.jpg',
  75: 'assets/img/products/garnelenpfanne_butter.jpg',
  27: 'assets/img/products/urla_meze.jpg',
  4: 'assets/img/products/gemischter_gruener_salat.jpg',
  30: 'assets/img/products/aubergine_mit_joghurt.jpg',
  38: 'assets/img/products/ueberbackener_garnelenauflauf.jpg',
  116: 'assets/img/products/warmer_griess_halva.jpg',
  101: 'assets/img/products/sardine_duerum.jpg',
  94: 'assets/img/products/garnele_sandwich.jpg',
  7: 'assets/img/products/lachssalat.jpg',
  5: 'assets/img/products/bauernsalat.jpg',
  73: 'assets/img/products/kalamaresringe.jpg',
  109: 'assets/img/products/balik_kofte_pilav.jpg',
};

let content = fs.readFileSync('assets/js/menu-data.js', 'utf8');
let notFound = [];
let updated = 0;

for (const [id, newImage] of Object.entries(updates)) {
  // Find "id": <id>, as a whole token (avoid matching 9 inside 91, etc.)
  const idRegex = new RegExp(`"id":\\s*${id}\\s*,`);
  const idMatch = idRegex.exec(content);
  if (!idMatch) {
    notFound.push({ id, reason: 'id not found' });
    continue;
  }
  const searchStart = idMatch.index + idMatch[0].length;
  // Find the next "id": to bound the search window (don't cross into next item)
  const nextIdRegex = /"id":\s*\d+\s*,/;
  const rest = content.slice(searchStart);
  const nextIdMatch = nextIdRegex.exec(rest);
  const windowEnd = nextIdMatch ? searchStart + nextIdMatch.index : content.length;
  const window = content.slice(searchStart, windowEnd);

  const imageFieldRegex = /"image":\s*"[^"]*"/;
  const imgMatch = imageFieldRegex.exec(window);
  if (!imgMatch) {
    notFound.push({ id, reason: 'no image field in window (item may have no image field at all)' });
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
if (notFound.length) {
  console.log('NOT FOUND:', JSON.stringify(notFound, null, 2));
}
