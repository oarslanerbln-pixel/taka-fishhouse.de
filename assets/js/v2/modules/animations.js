export function initAnimations() {
    // Magnetic Buttons (Premium Micro-interaction)
    const magneticElements = document.querySelectorAll('.btn, .brand-logo, .feature-icon-wrap, .gallery-overlay-icon');
    if (window.matchMedia('(pointer: fine)').matches && typeof gsap !== 'undefined') {
        magneticElements.forEach(el => {
            el.addEventListener('mousemove', (e) => {
                const rect = el.getBoundingClientRect();
                const x = e.clientX - rect.left - rect.width / 2;
                const y = e.clientY - rect.top - rect.height / 2;
                gsap.to(el, { x: x * 0.3, y: y * 0.3, duration: 0.6, ease: 'power3.out' });
            });
            el.addEventListener('mouseleave', () => {
                gsap.to(el, { x: 0, y: 0, duration: 0.8, ease: 'elastic.out(1, 0.3)' });
            });
        });
    }

    // Hero Dynamic Flashlight
    const heroSection = document.getElementById('home');
    const heroLight = document.getElementById('heroLightOverlay');
    if (heroSection && heroLight && window.matchMedia('(pointer: fine)').matches) {
        heroSection.addEventListener('mousemove', (e) => {
            const rect = heroSection.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            heroLight.style.setProperty('--mouse-x', `${x}px`);
            heroLight.style.setProperty('--mouse-y', `${y}px`);
        });
    }

    if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') {
        // Fallback for animations
        initFallbackAnimations();
        initMobileHoverObserver();
        return;
    }

    gsap.config({ nullTargetWarn: false });
    gsap.registerPlugin(ScrollTrigger);

    initHeroGSAP();
    initScrollGSAP();
    initMobileHoverObserver();
    initLenisScroll();
}

function initLenisScroll() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    if (typeof Lenis !== 'undefined') {
        const lenis = new Lenis({
            duration: 1.4,
            easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
            direction: 'vertical',
            gestureDirection: 'vertical',
            smooth: true,
            mouseMultiplier: 1,
            smoothTouch: false,
            touchMultiplier: 2,
        });

        // Sync GSAP ScrollTrigger with Lenis
        if (typeof ScrollTrigger !== 'undefined') {
            lenis.on('scroll', ScrollTrigger.update);
            gsap.ticker.add((time) => {
                lenis.raf(time * 1000);
            });
            gsap.ticker.lagSmoothing(0);
        } else {
            function raf(time) {
                lenis.raf(time);
                requestAnimationFrame(raf);
            }
            requestAnimationFrame(raf);
        }
    } else {
        console.warn("Lenis library not loaded. Ensure it is added in index.html");
    }
}

function initMobileHoverObserver() {
    // Only apply on touch devices or small screens
    if (window.matchMedia('(hover: none) or (max-width: 900px)').matches) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                } else {
                    entry.target.classList.remove('is-visible');
                }
            });
        }, { threshold: 0.6 });

        const hoverElements = document.querySelectorAll('.sig-card, .hero-social-icons a');
        hoverElements.forEach(el => observer.observe(el));
    }
}

function initHeroGSAP() {
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

    gsap.from('.hero-video-container video', { scale: 1.15, duration: 2.5, ease: 'power3.out' });
    gsap.to('.hero-video-container video', {
        scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true },
        y: '20%', ease: 'none'
    });

    gsap.from('.circular-badge', { opacity: 0, scale: 0.5, rotation: -90, duration: 1.5, ease: 'power3.out', delay: 1.2 });
    gsap.from('.audio-toggle', { opacity: 0, y: 20, duration: 1, ease: 'power3.out', delay: 1.4 });
}

function initScrollGSAP() {
    // Fade Up Elements
    gsap.utils.toArray('.gsap-fade-up, .contact-details h2, .contact-desc, .contact-info-item, .reviews-main-title, .google-rating-summary').forEach(elem => {
        gsap.fromTo(elem, { opacity: 0, y: 40 }, {
            scrollTrigger: { trigger: elem, start: 'top 85%' },
            opacity: 1, y: 0, duration: 0.8, ease: 'power3.out'
        });
    });

    // Contact Map Reveal
    gsap.to('.contact-map', {
        scrollTrigger: { trigger: '.contact-section', start: 'top 75%' },
        opacity: 1, duration: 1, ease: 'power3.out'
    });

    // Stats Strip
    gsap.from('.stat-block', {
        scrollTrigger: { trigger: '.stats-strip', start: 'top 85%' },
        opacity: 0, y: 40, stagger: 0.15, duration: 0.9, ease: 'power3.out'
    });

    // CountUp
    document.querySelectorAll('[data-count]').forEach(el => {
        const target = parseInt(el.getAttribute('data-count'));
        ScrollTrigger.create({
            trigger: el, start: 'top 85%', once: true,
            onEnter: () => {
                gsap.fromTo(el, { innerText: 0 }, {
                    innerText: target, duration: 1.5, ease: 'power2.out', snap: { innerText: 1 },
                    onUpdate: function() { el.textContent = Math.round(this.targets()[0].innerText); }
                });
            }
        });
    });

    // Editorial Blocks
    gsap.utils.toArray('.editorial-block').forEach((block, i) => {
        gsap.to(block, {
            scrollTrigger: { trigger: block, start: 'top 85%' },
            opacity: 1, duration: 1.1, ease: 'power3.out', delay: i * 0.08
        });
        const line = block.querySelector('.editorial-line');
        if (line) {
            gsap.to(line, {
                scrollTrigger: { trigger: block, start: 'top 80%' },
                width: '80px', opacity: 0.5, duration: 1, ease: 'power3.out', delay: 0.4
            });
        }
    });

    // Story Editorial Reveal
    const storyEditorial = document.querySelector('.story-editorial');
    if (storyEditorial) {
        const mask = storyEditorial.querySelector('.image-reveal-mask');
        if (mask) {
            gsap.to(mask, { scrollTrigger: { trigger: storyEditorial, start: 'top 70%' }, scaleX: 0, transformOrigin: 'right center', duration: 1.4, ease: 'power4.inOut' });
        }
        gsap.to(storyEditorial.querySelector('.story-editorial-image img'), {
            scrollTrigger: { trigger: storyEditorial, start: 'top bottom', end: 'bottom top', scrub: true },
            y: '8%', ease: 'none'
        });
    }

    // Atmosphere
    gsap.to('.atmosphere-content h2', { scrollTrigger: { trigger: '.atmosphere-section', start: 'top 70%' }, opacity: 1, y: 0, duration: 1, ease: 'power3.out' });
    gsap.to('.atmosphere-content p', { scrollTrigger: { trigger: '.atmosphere-section', start: 'top 70%' }, opacity: 1, y: 0, duration: 1, ease: 'power3.out', delay: 0.2 });

    // Gallery
    gsap.to('.gallery-header', { scrollTrigger: { trigger: '.instagram-gallery', start: 'top 80%' }, opacity: 1, y: 0, duration: 0.9, ease: 'power3.out' });
    gsap.to('.gallery-item', { scrollTrigger: { trigger: '.gallery-grid', start: 'top 80%' }, opacity: 1, y: 0, scale: 1, stagger: 0.1, duration: 0.9, ease: 'power3.out' });

    // Reservation
    gsap.to('.reservation-container', { scrollTrigger: { trigger: '.reservation-section', start: 'top 80%' }, opacity: 1, y: 0, duration: 1.1, ease: 'power3.out' });

    // Reviews Grid
    gsap.to('.review-card', { scrollTrigger: { trigger: '.reviews-grid', start: 'top 80%' }, opacity: 1, y: 0, stagger: 0.1, duration: 0.9, ease: 'power3.out' });
}

function initFallbackAnimations() {
    const fallbackObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'none';
                fallbackObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.editorial-block, .stat-block, .gallery-item, .gsap-fade-up, .review-card, .contact-details h2, .contact-desc, .contact-info-item, .reviews-main-title, .google-rating-summary').forEach(el => {
        el.style.transition = 'opacity 0.8s ease, transform 0.8s ease';
        fallbackObserver.observe(el);
    });
}
