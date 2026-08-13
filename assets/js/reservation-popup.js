document.addEventListener('DOMContentLoaded', () => {
    const DISMISS_KEY = 'taka-res-popup-dismissed-at';
    const DISMISS_HOURS = 24;

    const dismissedAt = localStorage.getItem(DISMISS_KEY);
    if (dismissedAt && (Date.now() - Number(dismissedAt)) < DISMISS_HOURS * 60 * 60 * 1000) return;

    const reservationSection = document.getElementById('reservation');
    if (!reservationSection) return;

    function t(key, fallback) {
        const lang = (typeof i18n !== 'undefined' && i18n.currentLang) || 'de';
        return (typeof translations !== 'undefined' && translations[lang] && translations[lang][key]) || fallback;
    }

    function showPopup() {
        // Reservasyon bölümü zaten görünürdeyse (kullanıcı oraya kaymışsa)
        // rahatsız etmeye gerek yok.
        const rect = reservationSection.getBoundingClientRect();
        if (rect.top < window.innerHeight && rect.bottom > 0) return;

        const popup = document.createElement('div');
        popup.className = 'taka-res-popup';
        popup.innerHTML = `
            <button class="taka-res-popup-close" aria-label="Close">&times;</button>
            <div class="taka-res-popup-icon">🍽️</div>
            <div class="taka-res-popup-body">
                <strong>${t('res-popup-title', 'Reserve Your Table')}</strong>
                <p>${t('res-popup-text', 'Book now to avoid waiting during busy hours.')}</p>
                <a href="#reservation" class="taka-res-popup-cta"><span>${t('res-popup-cta', 'Make a Reservation')}</span></a>
            </div>
        `;

        const style = document.createElement('style');
        style.innerHTML = `
            .taka-res-popup {
                position: fixed;
                right: 20px;
                bottom: 20px;
                width: 320px;
                max-width: calc(100vw - 24px);
                background: linear-gradient(160deg, #000 0%, #0a0a0a 100%);
                border: none;
                border-radius: 4px;
                padding: 18px 18px 18px 16px;
                display: flex;
                gap: 12px;
                align-items: flex-start;
                z-index: 9998;
                box-shadow: 0 14px 40px rgba(0, 0, 0, 0.6);
                opacity: 0;
                transform: translateY(24px);
                animation: takaResPopupIn 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
                font-family: 'Inter', sans-serif;
            }
            /* Kart kenarında dönen koyu lacivert "neon" çizgi — sabit bir
               glow/halo yerine ince bir çerçeve şeklinde, sadece kenar
               boyunca akıp geçiyor (conic-gradient + mask ile kart
               içeriğinin üstüne taşmıyor, sadece kenar çizgisi görünüyor). */
            .taka-res-popup::before {
                content: '';
                position: absolute;
                inset: -1.5px;
                border-radius: inherit;
                padding: 1.5px;
                background: conic-gradient(from 0deg,
                    transparent 0%, transparent 55%,
                    #0a1a4a 63%, #2952d6 72%, #6fa8ff 76%, #2952d6 80%, #0a1a4a 88%,
                    transparent 100%);
                -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
                -webkit-mask-composite: xor;
                mask-composite: exclude;
                animation: takaResBorderSpin 3.5s linear infinite;
                pointer-events: none;
            }
            @keyframes takaResBorderSpin {
                to { transform: rotate(360deg); }
            }
            @keyframes takaResPopupIn {
                to { opacity: 1; transform: translateY(0); }
            }
            .taka-res-popup-icon { font-size: 1.6rem; line-height: 1; margin-top: 2px; }
            .taka-res-popup-body { flex: 1; }
            .taka-res-popup-body strong {
                display: block;
                color: #fff;
                font-size: 1rem;
                margin-bottom: 4px;
            }
            .taka-res-popup-body p {
                margin: 0 0 12px;
                color: #cbd5e1;
                font-size: 0.85rem;
                line-height: 1.4;
            }
            .taka-res-popup-cta {
                display: inline-block;
                background: var(--accent-color, #D4AF37);
                font-weight: 700;
                font-size: 0.85rem;
                padding: 8px 16px;
                border-radius: 4px;
                text-decoration: none;
                transition: background 0.2s ease;
            }
            .taka-res-popup-cta:hover { background: var(--accent-hover, #C29B27); }
            .taka-res-popup-cta span {
                background: linear-gradient(110deg, #fff 30%, #fff 42%, #fffbe6 48%, #ffe9a8 50%, #fffbe6 52%, #fff 58%, #fff 70%);
                background-size: 250% auto;
                background-position: 100% 0;
                -webkit-background-clip: text;
                background-clip: text;
                color: transparent;
                animation: takaResCtaShine 2.6s linear infinite;
            }
            @keyframes takaResCtaShine {
                to { background-position: -150% 0; }
            }
            .taka-res-popup-close {
                position: absolute;
                top: 8px;
                right: 10px;
                background: none;
                border: none;
                color: #94a3b8;
                font-size: 1.2rem;
                line-height: 1;
                cursor: pointer;
                padding: 4px;
            }
            .taka-res-popup-close:hover { color: #fff; }
            @media (max-width: 600px) {
                .taka-res-popup {
                    left: 12px;
                    right: 12px;
                    bottom: 12px;
                    width: auto;
                }
            }
        `;

        document.head.appendChild(style);
        document.body.appendChild(popup);

        function dismiss() {
            localStorage.setItem(DISMISS_KEY, String(Date.now()));
            popup.style.opacity = '0';
            popup.style.transform = 'translateY(24px)';
            popup.style.transition = 'all 0.4s ease';
            setTimeout(() => popup.remove(), 400);
        }

        popup.querySelector('.taka-res-popup-close').addEventListener('click', dismiss);
        popup.querySelector('.taka-res-popup-cta').addEventListener('click', dismiss);
    }

    function scheduleShow() {
        setTimeout(() => {
            const cookieBanner = document.querySelector('.taka-cookie-banner');
            if (!cookieBanner) { showPopup(); return; }
            // Çerez bandı hâlâ ekrandaysa üst üste binmesin, kapanmasını bekle.
            const observer = new MutationObserver(() => {
                if (!document.querySelector('.taka-cookie-banner')) {
                    observer.disconnect();
                    showPopup();
                }
            });
            observer.observe(document.body, { childList: true });
        }, 6000);
    }

    scheduleShow();
});
