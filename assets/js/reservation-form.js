// Rezervasyon formu — Netlify Forms'a AJAX ile gönderim.
// Başvurular Netlify panelinde (Forms) saklanır, bildirim maili oradan gider;
// mail gelmese bile başvuru kaybolmaz. Cevap 2xx değilse misafire telefon
// numarasıyla birlikte görünür bir hata gösterilir. JS çalışmazsa form normal
// POST ile Netlify'a gider ve danke.html açılır.
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('resForm');
    if (!form) return;

    const submitBtn = form.querySelector('.res-submit');
    const status = form.querySelector('.res-status');
    const thanksUrl = form.getAttribute('action') || '/danke.html';

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
            const res = await fetch('/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: new URLSearchParams(new FormData(form)).toString()
            });
            if (res.ok) {
                window.location.href = thanksUrl;
                return;
            }
            console.error('Reservierung: Netlify Forms hat abgelehnt', res.status);
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
