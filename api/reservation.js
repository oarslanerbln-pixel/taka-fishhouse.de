// Rezervasyon formu → Resend üzerinden mail.
// Vercel ortam değişkenleri:
//   RESEND_API_KEY   (zorunlu) Resend panelinden alınan API anahtarı
//   RESERVATION_TO   (opsiyonel) alıcı, varsayılan handeaydemr@gmail.com
//   RESERVATION_FROM (opsiyonel) gönderen; domain Resend'de doğrulanana kadar
//                    "onboarding@resend.dev" kullanılmalı (bu durumda Resend
//                    sadece hesabın kendi mail adresine gönderir).
const FIELDS = [
    ['Isim', 'İsim Soyisim'],
    ['Telefon', 'Telefon'],
    ['Tarih', 'Tarih'],
    ['Saat', 'Saat'],
    ['Kisi_Sayisi', 'Kişi Sayısı'],
    ['Not', 'Not']
];

function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}

module.exports = async (req, res) => {
    if (req.method !== 'POST') {
        res.setHeader('Allow', 'POST');
        return res.status(405).json({ ok: false });
    }

    const body = typeof req.body === 'object' && req.body ? req.body : {};

    // Spam tuzağı doluysa sessizce "başarılı" dön, mail gönderme.
    if (body._honey) return res.status(200).json({ ok: true });

    const data = {};
    for (const [key] of FIELDS) data[key] = String(body[key] || '').trim().slice(0, 500);
    if (!data.Isim || !data.Telefon || !data.Tarih || !data.Saat || !data.Kisi_Sayisi) {
        return res.status(400).json({ ok: false, error: 'missing_fields' });
    }

    const apiKey = process.env.RESEND_API_KEY;
    if (!apiKey) {
        console.error('Reservation: RESEND_API_KEY is not set');
        return res.status(500).json({ ok: false, error: 'not_configured' });
    }

    const rows = FIELDS
        .map(([key, label]) => `<tr><td style="padding:6px 12px;font-weight:bold">${label}</td><td style="padding:6px 12px">${escapeHtml(data[key] || '-')}</td></tr>`)
        .join('');
    const text = FIELDS.map(([key, label]) => `${label}: ${data[key] || '-'}`).join('\n');

    const r = await fetch('https://api.resend.com/emails', {
        method: 'POST',
        headers: { 'Authorization': `Bearer ${apiKey}`, 'Content-Type': 'application/json' },
        body: JSON.stringify({
            from: process.env.RESERVATION_FROM || 'TAKA Rezervasyon <onboarding@resend.dev>',
            to: (process.env.RESERVATION_TO || 'handeaydemr@gmail.com').split(',').map(s => s.trim()),
            subject: `Yeni Rezervasyon: ${data.Isim} – ${data.Tarih} ${data.Saat} (${data.Kisi_Sayisi} kişi)`,
            html: `<h2>Yeni Masa Rezervasyonu – Taka Fish House</h2><table style="border-collapse:collapse">${rows}</table>`,
            text
        })
    });

    if (!r.ok) {
        console.error('Reservation: Resend rejected', r.status, await r.text().catch(() => ''));
        return res.status(502).json({ ok: false, error: 'send_failed' });
    }
    // JS'siz normal form gönderimi: teşekkür sayfasına yönlendir.
    if (!String(req.headers.accept || '').includes('application/json')) {
        res.setHeader('Location', '/danke.html');
        return res.status(303).end();
    }
    return res.status(200).json({ ok: true });
};
