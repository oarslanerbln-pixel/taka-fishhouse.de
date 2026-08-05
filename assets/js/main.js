document.addEventListener('DOMContentLoaded', () => {

    // ===== ŞU AN AÇIK / KAPALI GÖSTERGESİ =====
    // Ziyaretçinin kendi tarayıcı saati DEĞİL, Berlin yerel saati kullanılır —
    // aksi halde yurt dışından (farklı saat diliminden) bakan biri yanlış
    // açık/kapalı durumu görür. Saatler sayfada her yerde görünen "Her Gün:
    // 11:00-22:00" ile birebir aynı (qr-menu/index.html'deki eski JSON-LD'de
    // Cuma-Pazar 23:00'e kadar yazıyordu — bu sayfadaki metinle çelişiyordu,
    // burada gerçek/görünen saat esas alındı).
    (function updateOpenStatus() {
        const el = document.getElementById('openStatus');
        if (!el) return;

        const OPEN_MIN = 11 * 60;
        const CLOSE_MIN = 22 * 60;

        function berlinMinutesNow() {
            const parts = new Intl.DateTimeFormat('en-GB', {
                timeZone: 'Europe/Berlin', hour: '2-digit', minute: '2-digit', hour12: false
            }).formatToParts(new Date());
            const h = parseInt(parts.find(p => p.type === 'hour').value, 10);
            const m = parseInt(parts.find(p => p.type === 'minute').value, 10);
            return h * 60 + m;
        }

        function render() {
            const lang = (window.i18n && window.i18n.currentLang) || document.documentElement.lang || 'de';
            const t = (typeof translations !== 'undefined' && translations[lang]) || {};
            const now = berlinMinutesNow();
            const isOpen = now >= OPEN_MIN && now < CLOSE_MIN;
            const timeStr = isOpen ? '22:00' : '11:00';
            const template = isOpen
                ? (t['status-open'] || 'Şu an açık · {time}\'e kadar')
                : (t['status-closed'] || 'Şu an kapalı · {time}\'de açılıyor');
            el.textContent = template.replace('{time}', timeStr);
            el.classList.toggle('is-open', isOpen);
            el.classList.toggle('is-closed', !isOpen);
        }

        render();
        setInterval(render, 60000); // dakika sınırını geçince (11:00/22:00) durum otomatik güncellensin
        document.addEventListener('languageChanged', render);
    })();

    // ===== GOOGLE MAPS RIZA KAPISI =====
    // iframe artık sayfayla birlikte otomatik yüklenmiyor (DSGVO — ziyaretçinin
    // IP'sini onaysız Google'a gönderiyordu). Kullanıcı ya tıklar ya da daha
    // önce çerez bannerından genel onay vermişse otomatik yüklenir.
    (function initMapConsentGate() {
        const gate = document.getElementById('mapConsentGate');
        const btn = document.getElementById('mapConsentBtn');
        if (!gate) return;

        function loadMap() {
            const src = gate.dataset.mapSrc;
            if (!src) return;
            const iframe = document.createElement('iframe');
            iframe.src = src;
            iframe.width = '100%';
            iframe.height = '100%';
            iframe.style.border = '0';
            iframe.loading = 'lazy';
            iframe.setAttribute('allowfullscreen', '');
            gate.replaceWith(iframe);
        }

        if (localStorage.getItem('taka-cookies-accepted')) {
            loadMap();
        } else if (btn) {
            btn.addEventListener('click', loadMap);
        }
    })();

    // Splash Intro Hide Logic
    const premiumSplash = document.getElementById('premium-splash');
    if (premiumSplash) {
        setTimeout(() => {
            premiumSplash.classList.add('hide-splash');
            setTimeout(() => {
                premiumSplash.style.display = 'none';
            }, 500); // Wait for CSS transition
        }, 2000); // Splash duration before fading out
    }

    // Custom cursor removed as per request.

    // =====================================================
    // HERO PREMIUM INTERACTIONS (Lighting & Audio & Lens)
    // =====================================================

    const heroSection = document.getElementById('home');
    const heroLight = document.getElementById('heroLightOverlay');
    const heroVideo = document.getElementById('heroVideo');
    const audioToggle = document.getElementById('audioToggle');

    if (heroSection && heroLight && window.matchMedia('(pointer: fine)').matches) {
        // 1. Dynamic Flashlight
        heroSection.addEventListener('mousemove', (e) => {
            const rect = heroSection.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            heroLight.style.setProperty('--mouse-x', `${x}px`);
            heroLight.style.setProperty('--mouse-y', `${y}px`);
        });

    }

    // 3. Audio Toggle
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
        
        // Setup initial badge GSAP entrance
        if (typeof gsap !== 'undefined') {
            gsap.from('.audio-toggle', {
                opacity: 0,
                y: 20,
                duration: 1,
                ease: 'power3.out',
                delay: 1.4
            });
        }
    }

    // =====================================================
    // MAGNETIC BUTTONS (Premium Micro-interaction)
    // =====================================================
    const magneticElements = document.querySelectorAll('.btn, .brand-logo, .feature-icon-wrap, .gallery-overlay-icon');
    
    if (window.matchMedia('(pointer: fine)').matches) {
        magneticElements.forEach(el => {
            el.addEventListener('mousemove', (e) => {
                const rect = el.getBoundingClientRect();
                const x = e.clientX - rect.left - rect.width / 2;
                const y = e.clientY - rect.top - rect.height / 2;
                
                gsap.to(el, {
                    x: x * 0.3,
                    y: y * 0.3,
                    duration: 0.6,
                    ease: 'power3.out'
                });
            });

            el.addEventListener('mouseleave', () => {
                gsap.to(el, {
                    x: 0,
                    y: 0,
                    duration: 0.8,
                    ease: 'elastic.out(1, 0.3)'
                });
            });
        });
    }

    // =====================================================
    // SCROLL PROGRESS BAR
    // =====================================================
    const scrollProgress = document.getElementById('scrollProgress');
    if (scrollProgress) {
        window.addEventListener('scroll', () => {
            const scrollTop = window.scrollY;
            const docHeight = document.documentElement.scrollHeight - window.innerHeight;
            const progress = docHeight > 0 ? scrollTop / docHeight : 0;
            scrollProgress.style.transform = `scaleX(${progress})`;
        }, { passive: true });
    }

    // =====================================================
    // HEADER SCROLL EFFECT
    // =====================================================
    const header = document.getElementById('header');
    window.addEventListener('scroll', () => {
        if (header) {
            header.classList.toggle('scrolled', window.scrollY > 60);
        }
    }, { passive: true });

    // =====================================================
    // MOBILE NAV TOGGLE (hamburger)
    // =====================================================
    const navToggle = document.getElementById('navToggle');
    const navBackdrop = document.getElementById('navBackdrop');
    const navLinks = document.getElementById('navLinks');

    function closeMobileNav() {
        if (header) header.classList.remove('nav-open');
        if (navToggle) navToggle.setAttribute('aria-expanded', 'false');
        document.body.classList.remove('nav-lock-scroll');
    }

    function toggleMobileNav() {
        if (!header) return;
        const isOpen = header.classList.toggle('nav-open');
        if (navToggle) navToggle.setAttribute('aria-expanded', String(isOpen));
        document.body.classList.toggle('nav-lock-scroll', isOpen);
    }

    if (navToggle) navToggle.addEventListener('click', toggleMobileNav);
    if (navBackdrop) navBackdrop.addEventListener('click', closeMobileNav);
    if (navLinks) navLinks.querySelectorAll('a').forEach(a => a.addEventListener('click', closeMobileNav));
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeMobileNav(); });
    window.addEventListener('resize', () => { if (window.innerWidth > 991) closeMobileNav(); }, { passive: true });

    // =====================================================
    // SMOOTH SCROLL for anchor links
    // =====================================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            const target = document.querySelector(targetId);
            if (target) {
                e.preventDefault();
                const offset = 80;
                window.scrollTo({ top: target.offsetTop - offset, behavior: 'smooth' });
            }
        });
    });

    // =====================================================
    // GSAP ANIMATIONS
    // =====================================================
    if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
        gsap.config({ nullTargetWarn: false });
        gsap.registerPlugin(ScrollTrigger);

        // ----- HERO ENTRANCE -----
        const heroTl = gsap.timeline({ delay: 0.3 });

        try {
            heroTl
                .from('.hero-badge', { opacity: 0, y: 30, duration: 0.9, ease: 'power3.out' })
                .from('.hero-title', { opacity: 0, y: 50, duration: 1, ease: 'power3.out' }, '-=0.5')
                .from('.hero-subtitle', { opacity: 0, y: 30, duration: 0.9, ease: 'power3.out' }, '-=0.6')
                .fromTo('.hero-actions', { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.9, ease: 'power3.out' }, '-=0.5')
                .fromTo('.scroll-indicator', { opacity: 0 }, { opacity: 1, duration: 0.8, ease: 'power3.out' }, '-=0.3');
        } catch(e) {
            console.warn("GSAP Hero Anim Error:", e);
        }

        // Hero Video Parallax & Entrance
        gsap.from('.hero-video-container video', {
            scale: 1.15,
            duration: 2.5,
            ease: 'power3.out'
        });

        gsap.to('.hero-video-container video', {
            scrollTrigger: {
                trigger: '.hero',
                start: 'top top',
                end: 'bottom top',
                scrub: true
            },
            y: '20%',
            ease: 'none'
        });

        // ----- FADE UP ELEMENTS (RESERVATION, REVIEWS, CONTACT) -----
        gsap.utils.toArray('.gsap-fade-up').forEach(elem => {
            gsap.fromTo(elem, 
                { opacity: 0, y: 40 },
                {
                    scrollTrigger: {
                        trigger: elem,
                        start: 'top 85%'
                    },
                    opacity: 1,
                    y: 0,
                    duration: 0.8,
                    ease: 'power3.out'
                }
            );
        });

        // ----- STATS STRIP -----
        gsap.from('.stat-block', {
            scrollTrigger: {
                trigger: '.stats-strip',
                start: 'top 85%',
            },
            opacity: 0,
            y: 40,
            stagger: 0.15,
            duration: 0.9,
            ease: 'power3.out'
        });

        // CountUp animation for numbers
        document.querySelectorAll('[data-count]').forEach(el => {
            const target = parseInt(el.getAttribute('data-count'));
            ScrollTrigger.create({
                trigger: el,
                start: 'top 85%',
                onEnter: () => {
                    gsap.fromTo(el, { innerText: 0 }, {
                        innerText: target,
                        duration: 1.5,
                        ease: 'power2.out',
                        snap: { innerText: 1 },
                        onUpdate: function() {
                            el.textContent = Math.round(this.targets()[0].innerText);
                        }
                    });
                },
                once: true
            });
        });

        // ----- FEATURE CARDS -----
        gsap.from('.feature-card', {
            scrollTrigger: {
                trigger: '.features-grid',
                start: 'top 80%',
            },
            opacity: 0,
            y: 60,
            stagger: 0.15,
            duration: 1,
            ease: 'power3.out'
        });

        // ----- MENU SECTION HEADER -----
        gsap.from('.digital-menu-section .section-header', {
            scrollTrigger: {
                trigger: '.digital-menu-section',
                start: 'top 80%',
            },
            opacity: 0,
            y: 40,
            duration: 0.9,
            ease: 'power3.out'
        });

        gsap.from('.menu-action', {
            scrollTrigger: {
                trigger: '.menu-action',
                start: 'top 90%',
            },
            opacity: 0,
            y: 30,
            duration: 0.9,
            ease: 'power3.out'
        });

        // ----- STORY SECTION -----
        gsap.from('.story-content', {
            scrollTrigger: {
                trigger: '.story-section',
                start: 'top 75%',
            },
            opacity: 0,
            x: -60,
            duration: 1.1,
            ease: 'power3.out'
        });

        gsap.from('.story-image-wrap', {
            scrollTrigger: {
                trigger: '.story-section',
                start: 'top 75%',
            },
            opacity: 0,
            x: 60,
            duration: 1.1,
            ease: 'power3.out',
            delay: 0.15
        });

        // ----- ATMOSPHERE BANNER -----
        gsap.from('.atmosphere-content h2', {
            scrollTrigger: {
                trigger: '.atmosphere-section',
                start: 'top 70%',
            },
            opacity: 0,
            y: 50,
            duration: 1,
            ease: 'power3.out'
        });

        gsap.from('.atmosphere-content p', {
            scrollTrigger: {
                trigger: '.atmosphere-section',
                start: 'top 70%',
            },
            opacity: 0,
            y: 30,
            duration: 1,
            ease: 'power3.out',
            delay: 0.2
        });

        // ----- GALLERY -----
        gsap.from('.gallery-header', {
            scrollTrigger: {
                trigger: '.instagram-gallery',
                start: 'top 80%',
            },
            opacity: 0,
            y: 40,
            duration: 0.9,
            ease: 'power3.out'
        });

        gsap.from('.gallery-item', {
            scrollTrigger: {
                trigger: '.gallery-grid',
                start: 'top 80%',
            },
            opacity: 0,
            y: 50,
            scale: 0.95,
            stagger: 0.1,
            duration: 0.9,
            ease: 'power3.out'
        });

        // ----- RESERVATION -----
        gsap.from('.reservation-container', {
            scrollTrigger: {
                trigger: '.reservation-section',
                start: 'top 80%',
            },
            opacity: 0,
            y: 60,
            duration: 1.1,
            ease: 'power3.out'
        });

        // ----- GENERAL GSAP CLASS TARGETS -----
        gsap.utils.toArray('.gsap-fade-up').forEach(el => {
            gsap.from(el, {
                scrollTrigger: {
                    trigger: el,
                    start: 'top 90%',
                },
                opacity: 0,
                y: 40,
                duration: 0.9,
                ease: 'power3.out'
            });
        });

        // ----- EDITORIAL FEATURES BLOCKS -----
        gsap.utils.toArray('.editorial-block').forEach((block, i) => {
            const isRight = block.classList.contains('block-right');
            gsap.from(block, {
                scrollTrigger: {
                    trigger: block,
                    start: 'top 85%',
                },
                opacity: 0,
                x: isRight ? 60 : -60,
                y: 30,
                duration: 1.1,
                ease: 'power3.out',
                delay: i * 0.08
            });

            const line = block.querySelector('.editorial-line');
            if (line) {
                gsap.to(line, {
                    scrollTrigger: {
                        trigger: block,
                        start: 'top 80%',
                    },
                    width: '80px',
                    opacity: 0.5,
                    duration: 1,
                    ease: 'power3.out',
                    delay: 0.4
                });
            }
        });

        // ----- STORY EDITORIAL REVEAL -----
        const storyEditorial = document.querySelector('.story-editorial');
        if (storyEditorial) {
            // Image mask reveal (slide mask away to reveal image)
            const mask = storyEditorial.querySelector('.image-reveal-mask');
            if (mask) {
                gsap.to(mask, {
                    scrollTrigger: {
                        trigger: storyEditorial,
                        start: 'top 70%',
                    },
                    scaleX: 0,
                    transformOrigin: 'right center',
                    duration: 1.4,
                    ease: 'power4.inOut'
                });
            }

            // Oversized title
            gsap.from(storyEditorial.querySelector('.oversized-title'), {
                scrollTrigger: {
                    trigger: storyEditorial,
                    start: 'top 75%',
                },
                opacity: 0,
                y: 60,
                duration: 1.2,
                ease: 'power3.out',
                delay: 0.3
            });

            // Text wrapper slide in
            gsap.from(storyEditorial.querySelector('.story-text-wrapper'), {
                scrollTrigger: {
                    trigger: storyEditorial,
                    start: 'top 70%',
                },
                opacity: 0,
                x: 40,
                duration: 1,
                ease: 'power3.out',
                delay: 0.6
            });

            // Story editorial image parallax
            gsap.to(storyEditorial.querySelector('.story-editorial-image img'), {
                scrollTrigger: {
                    trigger: storyEditorial,
                    start: 'top bottom',
                    end: 'bottom top',
                    scrub: true
                },
                y: '8%',
                ease: 'none'
            });
        }

    } else {
        // Fallback: simple IntersectionObserver if GSAP fails to load
        const fallbackObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'none';
                    fallbackObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });

        document.querySelectorAll('.feature-card, .stat-block, .gallery-item, .gsap-fade-up, .gsap-fade-left, .gsap-fade-right, .story-content, .story-image-wrap').forEach(el => {
            el.style.transition = 'opacity 0.8s ease, transform 0.8s ease';
            fallbackObserver.observe(el);
        });
    }

    // =====================================================
    // DIGITAL MENU & SWIPER LOGIC
    // =====================================================
    if (typeof menuData !== 'undefined' && document.getElementById('menuTabsWrapper')) {
        const tabsWrapper = document.getElementById('menuTabsWrapper');
        const contentContainer = document.getElementById('menuContentContainer');

        menuData.forEach((category, index) => {
            const isActive = index === 0 ? 'active' : '';

            // Tab
            const tabHTML = `<div class="swiper-slide tab-btn ${isActive}" data-target="${category.categoryId}">${category.categoryNameTR}</div>`;
            tabsWrapper.insertAdjacentHTML('beforeend', tabHTML);

            // Content Panel
            let itemsHTML = '';
            category.items.forEach(item => {
                const imageSrc = item.image || '';
                const imageHtml = imageSrc
                    ? `<img src="${imageSrc}" alt="${item.nameTR}" loading="lazy" style="width:100%;height:100%;object-fit:cover;">`
                    : `<span style="font-size:0.8rem;letter-spacing:1px;opacity:0.4;">✦</span>`;

                itemsHTML += `
                    <div class="swiper-slide menu-card glass-card">
                        <div class="img-placeholder" style="${imageSrc ? 'background:none;border-bottom:none;padding:0;' : ''}">
                            ${imageHtml}
                        </div>
                        <div class="menu-info">
                            <div class="menu-header">
                                <h3 class="tr-name">${item.nameTR}</h3>
                                <span class="price">${item.price} €</span>
                            </div>
                            <p class="de-name">${item.nameDE}</p>
                        </div>
                    </div>
                `;
            });

            const panelHTML = `
                <div class="menu-category-panel ${isActive}" id="${category.categoryId}" style="display:${isActive ? 'block' : 'none'};opacity:${isActive ? '1' : '0'};transition:opacity 0.4s ease;">
                    <div class="swiper category-swiper">
                        <div class="swiper-wrapper">${itemsHTML}</div>
                        <div class="swiper-pagination"></div>
                    </div>
                </div>
            `;
            contentContainer.insertAdjacentHTML('beforeend', panelHTML);
        });

        // Init Swipers
        const tabsSwiper = new Swiper('.menu-tabs-swiper', {
            slidesPerView: 'auto',
            spaceBetween: 10,
            freeMode: true,
            watchSlidesProgress: true,
        });

        const categorySwipers = {};
        document.querySelectorAll('.category-swiper').forEach(swiperEl => {
            const categoryId = swiperEl.closest('.menu-category-panel').id;
            categorySwipers[categoryId] = new Swiper(swiperEl, {
                slidesPerView: 1.15,
                spaceBetween: 20,
                grabCursor: true,
                pagination: {
                    el: swiperEl.querySelector('.swiper-pagination'),
                    clickable: true,
                    dynamicBullets: true,
                },
                breakpoints: {
                    640: { slidesPerView: 2.2, spaceBetween: 20 },
                    1024: { slidesPerView: 3.2, spaceBetween: 30 }
                }
            });
        });

        // Tab click logic
        const tabBtns = document.querySelectorAll('.tab-btn');
        const panels = document.querySelectorAll('.menu-category-panel');

        tabBtns.forEach((btn, index) => {
            btn.addEventListener('click', () => {

                tabBtns.forEach(t => t.classList.remove('active'));
                btn.classList.add('active');

                const targetId = btn.getAttribute('data-target');
                panels.forEach(p => {
                    p.classList.remove('active');
                    p.style.display = 'none';
                    p.style.opacity = '0';
                });

                const targetPanel = document.getElementById(targetId);
                targetPanel.style.display = 'block';
                void targetPanel.offsetWidth;
                targetPanel.classList.add('active');
                targetPanel.style.opacity = '1';

                if (categorySwipers[targetId]) {
                    categorySwipers[targetId].update();
                }

                tabsSwiper.slideTo(index > 0 ? index - 1 : 0);
            });
        });
    }

    // =====================================================
    // VIDEO TRIM LOGIC (Our Story Video)
    // Cut the last 1 second due to corruption
    // =====================================================
    const ourStoryVideo = document.getElementById('ourStoryVideo');
    if (ourStoryVideo) {
        ourStoryVideo.addEventListener('timeupdate', function() {
            if (!isNaN(ourStoryVideo.duration) && ourStoryVideo.duration > 1) {
                const endTime = ourStoryVideo.duration - 1.0;
                if (ourStoryVideo.currentTime >= endTime) {
                    ourStoryVideo.currentTime = 0;
                    ourStoryVideo.play();
                }
            }
        });
    }

    // =====================================================
    // SIGNATURE DISHES MARQUEE (kendiliğinden kayan + elle kaydırılabilir)
    //
    // Eskiden salt CSS transform animasyonuydu — elle tutulup
    // kaydırılamıyordu (ne masaüstünde ne mobilde), çünkü transform
    // native scroll/drag ile aynı anda çalışmaz. Sonra ayrı bir "paused"
    // flag + setTimeout ile duraklat/devam-et yapıldı, ama bu dağınık
    // durum (her event kendi timer'ını kurup iptal ediyordu) hover'dan
    // çıkınca bazen hiç devam etmeme hatasına yol açtı — flag bir yerde
    // "true" kalıp bir daha false olmuyordu.
    //
    // Artık TEK bir kaynak var: lastInteraction (son etkileşim zamanı).
    // Her kare "üstünden ne kadar süre geçti" diye SORUYOR, hiçbir yerde
    // kalıcı bir "duraklatıldı" durumu tutulmuyor — bu yüzden yarışa
    // (race condition) hiç açık değil, kendiliğinden her zaman doğru
    // duruma dönüyor.
    //
    // Ayrıca: native overflow-x:auto sadece dokunmatik/trackpad'de elle
    // kaydırmayı destekler — normal FARE ile "tutup çekmek" tarayıcının
    // kendiliğinden yapmadığı bir şey, bu yüzden gerçek mousedown/
    // mousemove/mouseup tabanlı sürükleme burada elle eklendi.
    // =====================================================
    (function signatureMarquee() {
        const wrapper = document.querySelector('.signature-marquee-wrapper');
        const track = document.querySelector('.signature-marquee-track');
        if (!wrapper || !track) return;
        if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

        const SPEED = 0.55;       // px / kare (~60fps ≈ 33px/sn)
        const RESUME_DELAY = 2000; // son etkileşimden bu kadar ms sonra otomatik kayma geri başlar

        let lastInteraction = 0; // 0 = henüz hiç etkileşim yok -> hep kayar
        let isDragging = false;
        let dragStartX = 0;
        let dragStartScroll = 0;
        let dragDistance = 0; // sürüklerken alınan toplam yatay yol (px)

        function markInteraction() {
            lastInteraction = performance.now();
        }

        function loopWidth() {
            // SET 1 + SET 2 birebir aynı olduğu için tam yarısı bir döngü.
            return track.scrollWidth / 2;
        }

        function tick() {
            const idleFor = performance.now() - lastInteraction;
            if (!isDragging && idleFor > RESUME_DELAY) {
                const half = loopWidth();
                let next = wrapper.scrollLeft + SPEED;
                if (half > 0 && next >= half) next -= half;
                wrapper.scrollLeft = next;
            }
            requestAnimationFrame(tick);
        }

        // --- Fare ile tut-sürükle (native değil, elle yazıldı) ---
        wrapper.addEventListener('mousedown', function (e) {
            isDragging = true;
            dragDistance = 0;
            markInteraction();
            dragStartX = e.pageX;
            dragStartScroll = wrapper.scrollLeft;
            wrapper.classList.add('is-dragging');
            e.preventDefault(); // metin/kart seçimini engelle
        });
        window.addEventListener('mousemove', function (e) {
            if (!isDragging) return;
            markInteraction();
            const dx = e.pageX - dragStartX;
            dragDistance = Math.abs(dx);
            wrapper.scrollLeft = dragStartScroll - dx;
        });
        window.addEventListener('mouseup', function () {
            if (!isDragging) return;
            isDragging = false;
            wrapper.classList.remove('is-dragging');
            markInteraction();
        });
        // Kullanıcı bir kartı gerçekten SÜRÜKLEDİYSE (5px'ten fazla), aynı
        // el bırakmadan doğan click'in linke gitmesini engelle — yoksa her
        // sürükleme yanlışlıkla qr-menu/ sayfasına atlıyordu. Az hareket
        // (gerçek bir tıklama) etkilenmiyor.
        wrapper.addEventListener('click', function (e) {
            if (dragDistance > 5) {
                e.preventDefault();
                e.stopPropagation();
            }
        }, true);

        // --- Dokunmatik/trackpad: native scroll zaten çalışıyor, sadece
        //     "az önce etkileşim oldu" diye işaretlememiz yeterli ---
        ['touchstart', 'touchmove', 'wheel'].forEach(function (evt) {
            wrapper.addEventListener(evt, markInteraction, { passive: true });
        });
        wrapper.addEventListener('scroll', markInteraction, { passive: true });
        // Üstüne gelince dursun (okumak isteyen okuyabilsin) — el çekilince
        // hiçbir ek işlem gerekmiyor, tick() zaten RESUME_DELAY sonra
        // kendiliğinden devam ediyor.
        wrapper.addEventListener('mouseenter', markInteraction);

        requestAnimationFrame(tick);
    })();

});
