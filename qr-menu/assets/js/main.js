(function() {
    const saved = localStorage.getItem('taka-theme');
    // Default to light theme
    if (saved !== 'dark') {
        document.documentElement.setAttribute('data-theme', 'light');
    } else {
        document.documentElement.setAttribute('data-theme', 'dark');
    }
})();

document.addEventListener('DOMContentLoaded', () => {

    // ── Theme Toggle ──────────────────────────────────────────
    const themeToggle = document.getElementById('themeToggle');

    // Remove preload class (just in case it still exists in HTML)
    document.documentElement.classList.remove('light-theme-preload');

    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('taka-theme', newTheme);

            // Small bounce animation on toggle
            themeToggle.style.transform = 'scale(0.85)';
            setTimeout(() => { themeToggle.style.transform = ''; }, 200);
        });
    }

    // ── Header Scroll Effect ──────────────────────────────────
    const header = document.getElementById('header');
    const heroBg = document.querySelector('.hero-bg');

    window.addEventListener('scroll', () => {
        const scrollPosition = window.scrollY;
        if (header) {
            if (scrollPosition > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        }
        
        // Parallax Effect
        if(heroBg && scrollPosition < window.innerHeight) {
            heroBg.style.transform = `translateY(${scrollPosition * 0.4}px)`;
        }
    }, { passive: true });

    // Smooth Scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            
            // Skip if it's just "#"
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                window.scrollTo({
                    top: targetElement.offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Reveal elements on scroll
    const revealElements = document.querySelectorAll('.feature-card, .menu-item, .reveal-up, .reveal-left, .reveal-right');
    
    const revealCallback = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = 1;
                entry.target.style.transform = 'translate(0, 0)';
                observer.unobserve(entry.target);
            }
        });
    };
    
    const revealOptions = {
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    };
    
    const revealObserver = new IntersectionObserver(revealCallback, revealOptions);
    
    revealElements.forEach(el => {
        el.style.opacity = 0;
        
        // Custom transforms based on class
        if (el.classList.contains('reveal-left')) {
            el.style.transform = 'translateX(-30px)';
        } else if (el.classList.contains('reveal-right')) {
            el.style.transform = 'translateX(30px)';
        } else {
            el.style.transform = 'translateY(30px)';
        }
        
        el.style.transition = 'all 0.8s cubic-bezier(0.25, 0.8, 0.25, 1)';
        revealObserver.observe(el);
    });

    // Force video play for mobile
    const video = document.getElementById('menuHeroVideo');
    if (video) {
        video.play().catch(() => {});
        document.body.addEventListener('touchstart', function() {
            if (video.paused) video.play();
        }, { once: true });
    }

});
