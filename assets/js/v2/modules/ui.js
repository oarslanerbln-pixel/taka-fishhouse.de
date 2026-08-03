export function initUI() {
    // Splash Intro Hide Logic (Load based)
    const premiumSplash = document.getElementById('premium-splash');
    if (premiumSplash) {
        const hideSplash = () => {
            premiumSplash.classList.add('hide-splash');
            setTimeout(() => {
                premiumSplash.style.display = 'none';
            }, 500);
        };
        if (document.readyState === 'complete') {
            hideSplash();
        } else {
            window.addEventListener('load', hideSplash);
        }
    }

    // Audio Toggle
    const heroVideo = document.getElementById('heroVideo');
    const audioToggle = document.getElementById('audioToggle');
    if (audioToggle && heroVideo) {
        audioToggle.addEventListener('click', (e) => {
            e.preventDefault();
            if (heroVideo.muted) {
                heroVideo.muted = false;
                audioToggle.classList.add('playing');
            } else {
                heroVideo.muted = true;
                audioToggle.classList.remove('playing');
            }
        });
    }

    // Scroll Progress Bar
    const scrollProgress = document.getElementById('scrollProgress');
    if (scrollProgress) {
        window.addEventListener('scroll', () => {
            const scrollTop = window.scrollY;
            const docHeight = document.documentElement.scrollHeight - window.innerHeight;
            const progress = docHeight > 0 ? scrollTop / docHeight : 0;
            scrollProgress.style.transform = `scaleX(${progress})`;
        }, { passive: true });
    }

    // Back to top button
    const scrollTopBtn = document.querySelector('.scroll-top');
    if (scrollTopBtn) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 500) {
                scrollTopBtn.classList.add('visible');
            } else {
                scrollTopBtn.classList.remove('visible');
            }
        }, { passive: true });

        scrollTopBtn.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // Update Instagram Reel links
    const instaLinks = document.querySelectorAll('a[href*="instagram.com/reel/"]');
    instaLinks.forEach(link => {
        link.href = "https://www.instagram.com/reel/DXZVkcmgpGm/?igsh=MWJ6ZHBydjVha3lnMQ==";
    });

    // Our Story Video Seamless Loop Fade
    const storyVideo = document.getElementById('ourStoryVideo');
    if (storyVideo) {
        const FADE_DURATION = 0.8; // Match CSS transition duration
        storyVideo.addEventListener('timeupdate', () => {
            // Fade out slightly before the end of the video
            if (storyVideo.duration && storyVideo.currentTime >= storyVideo.duration - FADE_DURATION) {
                storyVideo.style.opacity = '0';
            } else {
                storyVideo.style.opacity = '1';
            }
        });
    }

    // Reservation form - Handle Validation
    const resForm = document.querySelector('.res-form');
    if (resForm) {
        resForm.noValidate = true;

        resForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const name = resForm.querySelector('input[name="İsim"]').value.trim();
            const email = resForm.querySelector('input[name="Email"]').value.trim();
            const phone = resForm.querySelector('input[name="Telefon"]').value.trim();
            const date = resForm.querySelector('input[name="Tarih"]').value.trim();

            if (!name) return window.showToast("Lütfen İsim Soyisim alanını doldurun.");
            if (!email || !/^\S+@\S+\.\S+$/.test(email)) return window.showToast("Geçerli bir E-posta adresi girin.");
            if (!phone) return window.showToast("Lütfen Telefon Numarası girin.");
            if (!date) return window.showToast("Lütfen Rezervasyon Tarihi seçin.");

            const submitBtn = resForm.querySelector('button[type="submit"]');
            const originalText = submitBtn.textContent;
            submitBtn.textContent = "Gönderiliyor...";
            submitBtn.disabled = true;

            try {
                await fetch("https://formsubmit.co/ajax/handeaydemr@gmail.com", {
                    method: "POST",
                    headers: { 
                        'Content-Type': 'application/json',
                        'Accept': 'application/json'
                    },
                    body: JSON.stringify({
                        İsim: name,
                        Email: email,
                        Telefon: phone,
                        Tarih: date,
                        _subject: "Yeni Masa Rezervasyonu - Taka Fish House",
                        _template: "table"
                    })
                });

                window.showToast("Rezervasyon talebiniz başarıyla alındı. Teşekkür ederiz!", "success");
                resForm.reset();
            } catch (err) {
                window.showToast("Bir hata oluştu. Lütfen telefonla iletişime geçin.");
            } finally {
                submitBtn.textContent = originalText;
                submitBtn.disabled = false;
            }
        });
    }

    // Match Footer to Creamy Theme
    const siteFooter = document.querySelector('.site-footer.force-dark');
    if (siteFooter) {
        siteFooter.classList.remove('force-dark');
    }

    // Cleanup: remove broken HTML text nodes between sections
    const heroSection = document.getElementById('hero');
    if (heroSection) {
        let node = heroSection.nextSibling;
        while (node && node !== document.getElementById('about')) {
            const next = node.nextSibling;
            if (node.nodeType === Node.TEXT_NODE || (node.nodeType === Node.ELEMENT_NODE && !node.id && node.tagName === 'DIV' && !node.className)) {
                node.remove();
            }
            node = next;
        }
    }
}

// ============================
// SPLASH SCREEN (PRE-LOADER)
// ============================
const splashHTML = `
<div id="takaSplashScreen" class="taka-splash-screen">
    <img src="assets/images/logo.png" alt="Taka Fisch Haus" class="taka-splash-logo">
</div>`;
document.body.insertAdjacentHTML('afterbegin', splashHTML);

window.addEventListener('load', () => {
    const splash = document.getElementById('takaSplashScreen');
    if (splash) {
        splash.classList.add('is-hidden');
        setTimeout(() => splash.remove(), 1500);
    }
});

// ============================
// TOAST NOTIFICATION SYSTEM
// ============================
const toastContainerHTML = `<div id="taka-toast-container"></div>`;
document.body.insertAdjacentHTML('beforeend', toastContainerHTML);

window.showToast = function(message, type = 'error') {
    const container = document.getElementById('taka-toast-container');
    if (!container) return;

    const toast = document.createElement('div');
    toast.className = `taka-toast ${type === 'success' ? 'taka-toast--success' : ''}`;
    toast.textContent = message;
    container.appendChild(toast);

    void toast.offsetWidth;
    toast.classList.add('is-visible');

    setTimeout(() => {
        toast.classList.remove('is-visible');
        setTimeout(() => toast.remove(), 400); 
    }, 3500);
}
