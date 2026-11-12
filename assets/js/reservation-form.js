// Rezervasyon formu — kendi Vercel fonksiyonumuza (/api/reservation) JSON
// olarak gönderilir; fonksiyon maili Resend ile atar. Sadece 2xx cevapta
// danke.html açılır, aksi halde misafire telefon numarasıyla görünür bir
// hata gösterilir — başvuru hiçbir zaman sessizce kaybolmaz.
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('resForm');
    if (!form) return;

    const submitBtn = form.querySelector('.res-submit');
    const status = form.querySelector('.res-status');
    const thanksUrl = '/danke.html';

    function t(key, fallback) {
        const lang = (typeof i18n !== 'undefined' && i18n.currentLang) || 'de';
        return (typeof translations !== 'undefined' && translations[lang] && translations[lang][key]) || fallback;
    }

    function showError() {
        if (!status) return;
        status.textContent = t('res-error', 'Ihre Reservierung konnte nicht gesendet werden. Bitte rufen Sie uns an: +49 30 24644214');
        status.hidden = false;
    }

    let sending = false;

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        if (sending) return;
        if (!form.reportValidity()) return;

        sending = true;
        if (status) status.hidden = true;
        const originalLabel = submitBtn.textContent;
        submitBtn.disabled = true;
        submitBtn.textContent = t('res-sending', 'Wird gesendet…');

        try {
            const res = await fetch(form.getAttribute('action') || '/api/reservation', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
                body: JSON.stringify(Object.fromEntries(new FormData(form)))
            });
            if (res.ok) {
                window.location.href = thanksUrl;
                return;
            }
            console.error('Reservierung: Server hat abgelehnt', res.status);
            showError();
        } catch (err) {
            console.error('Reservierung: Netzwerkfehler', err);
            showError();
        }

        sending = false;
        submitBtn.disabled = false;
        submitBtn.textContent = originalLabel;
    });
});
