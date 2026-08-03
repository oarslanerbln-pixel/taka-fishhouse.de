/*
 * scripts/apply-important-audit.js'in tersi: important-audit-report.json'daki
 * "removable" listesindeki her satıra " !important" ibaresini GERİ EKLER.
 * Aracın shorthand/longhand kör noktası (background vs background-color)
 * nedeniyle bir regresyona yol açtığı görüldüğü için temiz bir başlangıç
 * noktasına dönmek amacıyla kullanıldı.
 */
const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const report = JSON.parse(fs.readFileSync(path.join(__dirname, 'important-audit-report.json'), 'utf8'));

const byFile = new Map();
for (const r of report.removable) {
    if (!byFile.has(r.sheet)) byFile.set(r.sheet, []);
    byFile.get(r.sheet).push(r);
}

let restored = 0, skipped = 0;
for (const [relPath, entries] of byFile) {
    const filePath = path.join(ROOT, relPath);
    const lines = fs.readFileSync(filePath, 'utf8').split('\n');
    for (const entry of entries) {
        const idx = entry.line - 1;
        const line = lines[idx];
        if (line === undefined) { skipped++; continue; }
        const propRe = new RegExp(`^\\s*${entry.property.replace(/[-]/g, '\\-')}\\s*:`);
        if (!propRe.test(line)) { skipped++; continue; }
        if (/!important/i.test(line)) { skipped++; continue; } // zaten var (manuel düzeltilmiş sm-hidden gibi haric)
        // Noktalı virgülden hemen önce ekle.
        lines[idx] = line.replace(/;(\s*)$/, ' !important;$1');
        restored++;
    }
    fs.writeFileSync(filePath, lines.join('\n'), 'utf8');
}
console.log(`Geri eklendi: ${restored} | Atlandı: ${skipped}`);
