/* Bağımlılıksız statik sunucu — yerel önizleme için. */
const http = require('http');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const PORT = Number(process.env.PORT) || 3000;

const TYPES = {
    '.html': 'text/html; charset=utf-8',
    '.css': 'text/css; charset=utf-8',
    '.js': 'text/javascript; charset=utf-8',
    '.json': 'application/json; charset=utf-8',
    '.svg': 'image/svg+xml',
    '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.JPG': 'image/jpeg',
    '.png': 'image/png', '.webp': 'image/webp', '.avif': 'image/avif',
    '.mp4': 'video/mp4', '.MP4': 'video/mp4',
    '.woff2': 'font/woff2', '.ico': 'image/x-icon'
};

http.createServer((req, res) => {
    const urlPath = decodeURIComponent(req.url.split('?')[0]);
    let filePath = path.join(ROOT, urlPath);

    if (!filePath.startsWith(ROOT)) {
        res.writeHead(403).end('Forbidden');
        return;
    }
    if (fs.existsSync(filePath) && fs.statSync(filePath).isDirectory()) {
        filePath = path.join(filePath, 'index.html');
    }
    if (!fs.existsSync(filePath)) {
        res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' }).end('404 — ' + urlPath);
        return;
    }

    const contentType = TYPES[path.extname(filePath)] || 'application/octet-stream';
    const { size } = fs.statSync(filePath);
    const range = req.headers.range;

    // Range desteği olmadan <video> seek/scrub çalışmaz (özellikle video
    // testinde gerçek kullanıcı deneyimini doğrulamak için gerekli —
    // Vercel'de zaten var, burada da olmalı ki yerel test güvenilir olsun.
    if (range) {
        const match = /bytes=(\d*)-(\d*)/.exec(range);
        const start = match[1] ? parseInt(match[1], 10) : 0;
        const end = match[2] ? parseInt(match[2], 10) : size - 1;
        res.writeHead(206, {
            'Content-Type': contentType,
            'Content-Range': `bytes ${start}-${end}/${size}`,
            'Accept-Ranges': 'bytes',
            'Content-Length': end - start + 1,
            'Cache-Control': 'no-store'
        });
        fs.createReadStream(filePath, { start, end }).pipe(res);
        return;
    }

    res.writeHead(200, {
        'Content-Type': contentType,
        'Accept-Ranges': 'bytes',
        'Content-Length': size,
        'Cache-Control': 'no-store'
    });
    fs.createReadStream(filePath).pipe(res);
}).listen(PORT, () => console.log('http://localhost:' + PORT));
