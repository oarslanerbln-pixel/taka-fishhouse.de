/*
 * !important denetimi.
 *
 * Soru her !important bildirimi için aynı: "Bu !important'ı kaldırırsam,
 * kademelemede (cascade) bu özelliği başka bir kural ele geçirebilir mi?"
 *
 * Yöntem (temkinli / güvenli tarafta hata yapacak şekilde tasarlandı):
 *   1. style.css + menu-page.css + (varsa) theme.css tek bir kademe sırasına
 *      göre ayrıştırılır (gerçek <link> yükleme sırasıyla aynı).
 *   2. Her !important bildirimi için AYNI ÖZELLİĞİ ayarlayan TÜM diğer
 *      kurallar taranır.
 *   3. İki kuralın "çakışabilir" sayılması için anahtar seçicilerinin
 *      (rightmost compound selector) en az bir ortak token'ı (class/id/tag)
 *      paylaşması yeterli görülür — bu kasıtlı olarak gevşek bir eşleşme;
 *      gerçekte çakışmayan bazı çiftleri de "çakışıyor" sayabilir ama asla
 *      gerçekten gerekli bir !important'ı "gereksiz" diye işaretlemez.
 *   4. Çakışan HİÇBİR kural yoksa → !important kanıtlanmış şekilde ölü
 *      ağırlıktır, kaldırılması güvenlidir.
 *   5. Çakışan bir kural varsa → !important olduğu gibi bırakılır.
 *
 * Bu script SADECE rapor üretir, dosya değiştirmez.
 */
const fs = require('fs');
const path = require('path');
const css = require('css');

const ROOT = path.join(__dirname, '..');

function load(relPath) {
    const full = path.join(ROOT, relPath);
    return { relPath, ast: css.parse(fs.readFileSync(full, 'utf8'), { source: relPath }) };
}

// Gerçek <link> sırasıyla aynı: style.css önce, sonra menu-page.css, sonra (varsa) theme.css.
const sheets = [
    load('assets/css/style.css'),
    load('qr-menu/assets/css/menu-page.css'),
    load('qr-menu/assets/css/theme.css'),
];

// Kademedeki tüm kuralları düz bir listeye çıkar (media query içindekiler dahil, media koşulu etiketlenerek).
function flatten(ast, sheetName, mediaCtx) {
    const out = [];
    for (const node of ast.stylesheet.rules) {
        if (node.type === 'rule') {
            out.push({ sheet: sheetName, media: mediaCtx || null, selectors: node.selectors, declarations: node.declarations, position: node.position });
        } else if (node.type === 'media') {
            out.push(...flatten({ stylesheet: { rules: node.rules } }, sheetName, node.media));
        }
    }
    return out;
}

let allRules = [];
sheets.forEach((s, i) => {
    allRules.push(...flatten(s.ast, s.relPath, null).map(r => ({ ...r, sheetOrder: i })));
});

// Anahtar seçici: virgülle ayrılmış grup içindeki her bir seçicinin EN SAĞDAKİ
// basit seçicisi (kombinatörden sonraki kısım) — matchleme burada olur.
function keyTokens(selector) {
    const rightmost = selector.trim().split(/\s+/).pop();
    // pseudo-class/element'leri at, class/id/tag token'larını çıkar
    const cleaned = rightmost.replace(/::?[a-zA-Z-]+(\([^)]*\))?/g, '');
    const tokens = cleaned.match(/[.#]?[a-zA-Z_][a-zA-Z0-9_-]*/g) || [];
    return new Set(tokens.map(t => t.toLowerCase()));
}

// Shorthand/longhand aileleri: bir ailedeki HERHANGİ bir özellik, aynı
// ailedeki başka bir özellikle "çakışabilir" sayılır (örn. background
// shorthand'ı background-color longhand'ını ezebilir). Kenar-spesifik
// (border-top vs border-bottom-color) ayrımı YAPILMAZ — kasıtlı olarak
// kaba/temkinli: bazı gerçekte çakışmayan çiftleri de "çakışıyor" sayar,
// ama gerçek bir çakışmayı ASLA "yok" saymaz. Bu script'in daha önceki
// sürümü tam bu yüzden bir gerçek bug'ı kaçırmıştı (background vs
// background-color ayrı özellik sayılıyordu).
const SHORTHAND_FAMILIES = [
    ['background', 'background-color', 'background-image', 'background-position', 'background-size', 'background-attachment', 'background-clip', 'background-repeat', 'background-origin', '-webkit-background-clip'],
    ['border', 'border-color', 'border-width', 'border-style', 'border-top', 'border-right', 'border-bottom', 'border-left', 'border-top-color', 'border-right-color', 'border-bottom-color', 'border-left-color', 'border-radius', 'border-top-left-radius', 'border-top-right-radius', 'border-bottom-left-radius', 'border-bottom-right-radius'],
    ['margin', 'margin-top', 'margin-right', 'margin-bottom', 'margin-left'],
    ['padding', 'padding-top', 'padding-right', 'padding-bottom', 'padding-left'],
    ['font', 'font-family', 'font-size', 'font-style', 'font-weight', 'font-variant', 'line-height'],
    ['flex', 'flex-grow', 'flex-shrink', 'flex-basis', 'flex-direction', 'flex-wrap'],
    ['animation', 'animation-delay', 'animation-duration', 'animation-name', 'animation-timing-function', 'animation-iteration-count', 'animation-fill-mode', 'animation-play-state'],
    ['overflow', 'overflow-x', 'overflow-y'],
    ['inset', 'top', 'right', 'bottom', 'left'],
    ['outline', 'outline-color', 'outline-width', 'outline-style'],
    ['text-decoration', 'text-decoration-line', 'text-decoration-color', 'text-decoration-style'],
    ['list-style', 'list-style-type', 'list-style-position', 'list-style-image'],
    ['mask-image', '-webkit-mask-image'],
    ['backdrop-filter', '-webkit-backdrop-filter'],
    ['transition', 'transition-property', 'transition-duration', 'transition-timing-function', 'transition-delay'],
    ['grid-template-columns', 'grid-template-rows', 'grid-template', 'grid'],
    ['transform', 'transform-origin'],
];
const familyKeyByProp = new Map();
SHORTHAND_FAMILIES.forEach((fam, i) => fam.forEach(p => familyKeyByProp.set(p, i)));
function propertiesCompete(a, b) {
    if (a === b) return true;
    const fa = familyKeyByProp.get(a);
    const fb = familyKeyByProp.get(b);
    return fa !== undefined && fa === fb;
}

function specificity(selector) {
    // Kabaca: (id, class/attr/pseudo-class, tag) — !important karşılaştırmasında
    // sadece "var mı yok mu" olarak kullanılacak, tam sıralama gerekmiyor.
    const ids = (selector.match(/#[a-zA-Z_-][\w-]*/g) || []).length;
    const classes = (selector.match(/\.[a-zA-Z_-][\w-]*/g) || []).length
        + (selector.match(/\[[^\]]+\]/g) || []).length
        + (selector.match(/:[a-zA-Z-]+(\([^)]*\))?/g) || []).length;
    const tags = (selector.replace(/\.[\w-]+|#[\w-]+|\[[^\]]+\]|:[a-zA-Z-]+(\([^)]*\))?/g, '').match(/[a-zA-Z][a-zA-Z0-9]*/g) || []).length;
    return ids * 100 + classes * 10 + tags;
}

// Tüm (seçici, özellik) çiftlerini TEK düz listede topla — artık property
// adına göre ayrı kovalara BÖLÜNMÜYOR, çünkü shorthand/longhand çiftleri
// (background / background-color gibi) farklı kovalara düşüp birbirini
// hiç görmüyordu. Bu, ilk sürümün gözden kaçırdığı gerçek regresyonun
// kök nedeniydi.
const allDecls = [];
for (const rule of allRules) {
    for (const sel of rule.selectors) {
        const tokens = keyTokens(sel);
        const spec = specificity(sel);
        for (const decl of rule.declarations) {
            if (decl.type !== 'declaration') continue;
            allDecls.push({
                selector: sel,
                property: decl.property,
                tokens,
                spec,
                sheetOrder: rule.sheetOrder,
                sheet: rule.sheet,
                media: rule.media,
                // ÖNEMLİ: kuralın değil, DEYİMİN (declaration) kendi konumu —
                // aksi halde çok satırlı kurallarda yanlış satır işaretlenir.
                position: decl.position || rule.position,
                important: !!decl.value && /!important/i.test(decl.value),
                value: decl.value,
            });
        }
    }
}

const results = { removable: [], keep: [] };

for (const entry of allDecls) {
    if (!entry.important) continue;
    // Aynı AİLEDEN bir özelliği ayarlayan, seçici token'ı çakışan,
    // KENDİSİ OLMAYAN başka bir bildirim var mı?
    const competitor = allDecls.find(other =>
        other !== entry &&
        propertiesCompete(entry.property, other.property) &&
        [...other.tokens].some(t => entry.tokens.has(t))
    );
    const record = {
        sheet: entry.sheet,
        line: entry.position ? entry.position.start.line : '?',
        selector: entry.selector,
        property: entry.property,
        media: entry.media,
    };
    if (competitor) {
        results.keep.push({ ...record, competitorSelector: competitor.selector, competitorProperty: competitor.property, competitorImportant: competitor.important, competitorSheet: competitor.sheet, competitorLine: competitor.position ? competitor.position.start.line : '?' });
    } else {
        results.removable.push(record);
    }
}

console.log(`Toplam !important bildirimi: ${results.removable.length + results.keep.length}`);
console.log(`  Güvenle kaldırılabilir (çakışan kural yok): ${results.removable.length}`);
console.log(`  Korunmalı (en az bir çakışan kural var): ${results.keep.length}`);
console.log('');
console.log('=== GÜVENLE KALDIRILABİLİR ===');
results.removable.forEach(r => console.log(`  ${r.sheet}:${r.line}  ${r.selector} { ${r.property} }${r.media ? '  @media ' + r.media : ''}`));

fs.writeFileSync(
    path.join(__dirname, 'important-audit-report.json'),
    JSON.stringify(results, null, 2),
    'utf8'
);
console.log('');
console.log('Tam rapor: scripts/important-audit-report.json');
