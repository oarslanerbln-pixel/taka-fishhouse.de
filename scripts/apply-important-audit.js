/*
 * scripts/audit-important.js tarafından üretilen
 * scripts/important-audit-report.json içindeki "removable" (güvenle
 * kaldırılabilir — çakışan hiçbir kural bulunamayan) bildirimlerden
 * SADECE "!important" ibaresini satır bazında kaldırır.
 *
 * Kasıtlı olarak css.stringify() KULLANMAZ — tüm dosyayı yeniden
 * biçimlendirmek, gözden geçirilemeyecek kadar büyük ve alakasız bir diff
 * üretir. Bunun yerine rapor edilen (dosya, satır, özellik) üçlüsünü
 * bulur, o TEK satırda " !important" metnini siler. Böylece git diff
 * sadece gerçekten değişen satırları gösterir.
 */
const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const report = JSON.parse(fs.readFileSync(path.join(__dirname, 'important-audit-report.json'), 'utf8'));

// Dosya bazında grupla
const byFile = new Map();
for (const r of report.removable) {
    if (!byFile.has(r.sheet)) byFile.set(r.sheet, []);
    byFile.get(r.sheet).push(r);
}

let totalApplied = 0;
let totalSkipped = 0;

for (const [relPath, entries] of byFile) {
    const filePath = path.join(ROOT, relPath);
    const lines = fs.readFileSync(filePath, 'utf8').split('\n');

    for (const entry of entries) {
        const idx = entry.line - 1;
        const line = lines[idx];
        if (line === undefined) {
            console.log(`  ATLANDI (satır bulunamadı): ${relPath}:${entry.line} ${entry.property}`);
            totalSkipped++;
            continue;
        }
        // Bu satır gerçekten bu özelliği ve !important'ı içeriyor mu? (güvenlik kontrolü)
        const propRe = new RegExp(`^\\s*${entry.property.replace(/[-]/g, '\\-')}\\s*:`);
        if (!propRe.test(line) || !/!important/i.test(line)) {
            console.log(`  ATLANDI (satır beklenenle eşleşmiyor): ${relPath}:${entry.line} ${entry.property} -> "${line.trim()}"`);
            totalSkipped++;
            continue;
        }
        const newLine = line.replace(/\s*!important/i, '');
        lines[idx] = newLine;
        totalApplied++;
    }

    fs.writeFileSync(filePath, lines.join('\n'), 'utf8');
    console.log(`Yazıldı: ${relPath} (${entries.length} aday)`);
}

console.log('');
console.log(`Uygulanan: ${totalApplied} | Atlanan: ${totalSkipped}`);
