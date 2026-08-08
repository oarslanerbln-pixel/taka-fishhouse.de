const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

const SRC_DIR = 'YENI ÜRÜN RESIMLERI';
const OUT_DIR = 'assets/img/products';

// [sourceFile, itemId, outputFileName]
const jobs = [
  ['acili ezme.png', 14, 'acili_ezme.jpg'],
  ['barbun.png', 65, 'barbun.jpg'],
  ['bratkartoffel.png', 49, 'bratkartoffel_taka_spezial.jpg'],
  ['burger menü cocuk.png', 108, 'fisch_burger.jpg'],
  ['crispy garnelen.png', 9991, 'crispy_garnelen.jpg'],
  ['deniz börülcesi.png', 35, 'deniz_borulcesi.jpg'],
  ['dil baligi.png', 80, 'dil_baligi.jpg'],
  ['domatesli karides.png', 76, 'garnelenpfanne_tomatensosse.jpg'],
  ['doraade.png', 61, 'dorade.jpg'],
  ['dorade sandvic.png', 91, 'dorade_sandwich.jpg'],
  ['enginar.png', 9701, 'spesiyal_enginar.jpg'],
  ['fisch suppe.png', 1, 'lachssuppe.jpg'],
  ['fisch-auf-auberginenpürreebett.png', 42, 'fisch_auf_auberginenpuereebett.jpg'],
  ['garnele salata.png', 8, 'garnelensalat.jpg'],
  ['garnele-dürüm.png', 102, 'garnele_duerum.jpg'],
  ['geschnitzelte fischpfanne.png', 43, 'geschnetzelte_fischpfanne.jpg'],
  ['hamsi -salatasi.png', 9, 'hamsisalat.jpg'],
  ['hamsi-sadnvic.png', 93, 'sardine_sandwich.jpg'],
  ['hamsi.png', 63, 'hamsi_gebraten.jpg'],
  ['havuc-tarator.png', 13, 'havuc_tarator.jpg'],
  ['humus.png', 15, 'humus.jpg'],
  ['iki kisilik taka spesiyal 75€ olan.png', 81, 'taka_spezial_2_personen.jpg'],
  ['istavrit.png', 72, 'istavrit.jpg'],
  ['karides taka spezial.png', 77, 'garnelenpfanne_taka_spezial.jpg'],
  ['karisik meze tabagi.png', 10, 'karisik_meze_tabagi.jpg'],
  ['kasarli-mantar.png', 45, 'kasarli_mantar.jpg'],
  ['köpoglu.png', 21, 'kopoglu.jpg'],
  ['lachs-sandvich.png', 90, 'lachs_sandwich.jpg'],
  ['lachs-ve - doraade -dürüm.png', 99, 'dorade_duerum.jpg'],
  ['lachsfilet.png', 67, 'lachsfilet.jpg'],
  ['magnolia.png', 122, 'erdbeer_magnolia.jpg'],
  ['makarna -garnele.png', 113, 'penne_mit_garnelen.jpg'],
  ['makrele sandvic.png', 92, 'makrele_sandwich.jpg'],
  ['makrele-durum.png', 100, 'makrele_duerum.jpg'],
  ['meeresfrüchte.png', 17, 'meeresfruechte_meze.jpg'],
  ['merlan mezgit.png', 71, 'merlan.jpg'],
  ['octopus pastirma.png', 41, 'oktopus_mit_pastirma.jpg'],
  ['octopus salat.png', 22, 'oktopussalat.jpg'],
  ['octopus.png', 78, 'izgara_ahtapot.jpg'],
  ['pembe sultan.png', 32, 'pembe_sultan.jpg'],
  ['pommes.png', 50, 'pommes_frites.jpg'],
  ['roka salatasi.png', 6, 'rucolasalat.jpg'],
  ['rokoli.png', 46, 'ueberbackene_brokkoli.jpg'],
  ['saksuka.png', 18, 'saksuka.jpg'],
  ['sütlac.png', 120, 'hamsikoy_sutlac.jpg'],
  ['taka-meeresfrüchte-speazial.png', 9992, 'taka_meeresfruechte_spezial.jpg'],
  ['tereyagda karides.png', 75, 'garnelenpfanne_butter.jpg'],
  ['urla-meze.png', 27, 'urla_meze.jpg'],
  ['yesil salata.png', 4, 'gemischter_gruener_salat.jpg'],
  ['yogrutlu-patlican.png', 30, 'aubergine_mit_joghurt.jpg'],
  ['überbackener-garnelenauflauf.png', 38, 'ueberbackener_garnelenauflauf.jpg'],
  ['ChatGPT Image 7. Aug. 2026, 14_26_15.png', 116, 'warmer_griess_halva.jpg'],
  ['ChatGPT Image 7. Aug. 2026, 14_30_59.png', 101, 'sardine_duerum.jpg'],
  ['ChatGPT Image 7. Aug. 2026, 14_31_28.png', 94, 'garnele_sandwich.jpg'],
  ['ChatGPT Image 7. Aug. 2026, 14_40_09.png', 7, 'lachssalat.jpg'],
  ['ChatGPT Image 7. Aug. 2026, 14_40_33.png', 5, 'bauernsalat.jpg'],
  ['ChatGPT Image 7. Aug. 2026, 14_41_36.png', 73, 'kalamaresringe.jpg'],
  ['ChatGPT Image 7. Aug. 2026, 14_42_23.png', 109, 'balik_kofte_pilav.jpg'],
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
  fs.writeFileSync(
    'C:/Users/oarsl/AppData/Local/Temp/claude/C--Users-oarsl-Desktop-Is-Dosyasi-Taka-Fisch-Haus/40303d25-ca78-4317-9569-e776d8239beb/scratchpad/process_results.json',
    JSON.stringify(results, null, 2)
  );
  const ok = results.filter(r => r.status === 'OK').length;
  console.log(`Done: ${ok}/${results.length} processed successfully`);
  results.filter(r => r.status !== 'OK').forEach(r => console.log('FAILED:', r.outName, r.status));
})();
