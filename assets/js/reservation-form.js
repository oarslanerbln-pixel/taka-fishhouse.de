// Rezervasyon formu — FormSubmit'e AJAX ile gönderim.
// Eskiden form düz HTML POST ile formsubmit.co'ya gidiyordu: FormSubmit
// tarafında bir sorun olduğunda (form aktive edilmemiş, alıcı adresi
// doğrulanmamış, kota/spam engeli) misafir ya FormSubmit'in kendi
// sayfasında kalıyor ya da hiçbir hata görmüyordu; mail hiç gelmese bile
// "gönderildi" sanılıyordu. Artık FormSubmit'in gerçek JSON yanıtı
// kontrol ediliyor — sadece success:"true" ise danke.html'e geçiliyor,
// aksi halde formun altında telefonla arama yönlendirmesi gösteriliyor.
// JS çalışmazsa form eskisi gibi normal POST ile gönderilmeye devam eder.
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('resForm');
    if (!form) return;

    const submitBtn = form.querySelector('.res-submit');
    const status = form.querySelector('.res-status');
    // Alıcı adresi tek yerde (form action) tutuluyor; AJAX ucu oradan türetiliyor.
    const ajaxUrl = form.action.replace('formsubmit.co/', 'formsubmit.co/ajax/');
    const thanksUrl = form.querySelector('input[name="_next"]')?.value || 'danke.html';

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

        const payload = {};
        new FormData(form).forEach((value, key) => {
            if (key !== '_next') payload[key] = value;
        });

        try {
            const res = await fetch(ajaxUrl, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
                body: JSON.stringify(payload)
            });
            const data = await res.json().catch(() => ({}));

            // FormSubmit başarıyı string olarak döndürüyor ("true"/"false").
            if (res.ok && String(data.success) === 'true') {
                window.location.href = thanksUrl;
                return;
            }
            console.error('Reservierung: FormSubmit hat abgelehnt', res.status, data.message || data);
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
