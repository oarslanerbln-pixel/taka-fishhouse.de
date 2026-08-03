const fs = require('fs');
const path = 'c:\\Users\\oarsl\\Desktop\\Is Dosyasi\\Taka Fisch Haus\\qr-menu\\assets\\js\\menu-data.js';

let content = fs.readFileSync(path, 'utf8');

// Replace all occurrences of ?w=600&q=80 with ?w=200&q=50&fm=webp
let optimizedContent = content.replace(/\?w=600&q=80/g, '?w=200&q=50&fm=webp');

fs.writeFileSync(path, optimizedContent, 'utf8');
console.log('Images optimized successfully!');
