const i18n = {
    currentLang: 'de', // Default language
    supportedLangs: ['tr', 'de', 'en', 'ru', 'es', 'ar'],

    init() {
        // 1. Determine language
        const savedLang = localStorage.getItem('taka_lang');
        const browserLang = navigator.language.split('-')[0];
        
        if (savedLang && this.supportedLangs.includes(savedLang)) {
            this.currentLang = savedLang;
        } else if (this.supportedLangs.includes(browserLang)) {
            this.currentLang = browserLang;
        } else {
            this.currentLang = 'de'; // Fallback
        }

        // 2. Set initial state
        this.updateUI();
        this.updateLanguageSwitcher();
    },

    setLanguage(lang) {
        if (!this.supportedLangs.includes(lang)) return;
        
        this.currentLang = lang;
        localStorage.setItem('taka_lang', lang);
        
        this.updateUI();
        this.updateLanguageSwitcher();
        
        // Dispatch event for other scripts (like the menu renderer)
        document.dispatchEvent(new CustomEvent('languageChanged', { detail: { lang } }));
    },

    updateUI() {
        document.documentElement.lang = this.currentLang;
        document.documentElement.dir = this.currentLang === 'ar' ? 'rtl' : 'ltr';
        
        const elements = document.querySelectorAll('[data-i18n]');
        elements.forEach(el => {
            const key = el.getAttribute('data-i18n');
            if (translations[this.currentLang] && translations[this.currentLang][key]) {
                el.innerHTML = translations[this.currentLang][key];
            }
        });

        // [data-i18n] sadece innerHTML'i güncelliyordu — arama kutusunun
        // placeholder'ı hiç işlenmiyordu, dil değişse de hep sabit kalıyordu
        // (Türkçe yazılmıştı, Almanca'da bile "Yemek ara..." görünüyordu).
        const placeholderElements = document.querySelectorAll('[data-i18n-placeholder]');
        placeholderElements.forEach(el => {
            const key = el.getAttribute('data-i18n-placeholder');
            if (translations[this.currentLang] && translations[this.currentLang][key]) {
                el.setAttribute('placeholder', translations[this.currentLang][key]);
            }
        });
    },

    updateLanguageSwitcher() {
        const switcher = document.getElementById('langSwitcher');
        if (!switcher) return;

        // Update the visual state of the switcher if needed.
        // For a simple button toggle, we can just highlight the active one.
        const btns = switcher.querySelectorAll('.lang-btn');
        btns.forEach(btn => {
            if (btn.dataset.lang === this.currentLang) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });

        // Trigger butonundaki kod (ör. "DE") her zaman aktif dili göstersin.
        const triggerCode = switcher.querySelector('.lang-trigger-code');
        if (triggerCode) triggerCode.textContent = this.currentLang.toUpperCase();
    }
};

// Auto-init
document.addEventListener('DOMContentLoaded', () => {
    i18n.init();

    // Setup event listeners for switcher buttons
    // (closest() kullanılıyor çünkü buton artık kod+isim span'ları
    // içeriyor — tıklama span'a denk gelirse e.target .lang-btn'in
    // kendisi olmuyordu ve dil hiç değişmiyordu.)
    document.addEventListener('click', (e) => {
        const langBtn = e.target.closest('.lang-btn');
        if (langBtn) {
            i18n.setLanguage(langBtn.dataset.lang);
            closeLangDropdown();
        }
    });

    // Dil seçici artık açılır bir menü: masaüstünde hover ile, dokunmatik
    // ekranlarda (hover'ın çalışmadığı yerlerde) dokunarak açılıp kapanıyor.
    const langSwitcher = document.getElementById('langSwitcher');
    const langTrigger = document.getElementById('langTrigger');
    function closeLangDropdown() {
        if (!langSwitcher) return;
        langSwitcher.classList.remove('open');
        if (langTrigger) langTrigger.setAttribute('aria-expanded', 'false');
    }
    if (langSwitcher && langTrigger) {
        langTrigger.addEventListener('click', (e) => {
            e.stopPropagation();
            const isOpen = langSwitcher.classList.toggle('open');
            langTrigger.setAttribute('aria-expanded', String(isOpen));
        });
        document.addEventListener('click', (e) => {
            if (!langSwitcher.contains(e.target)) closeLangDropdown();
        });
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') closeLangDropdown();
        });
    }

    // Mobil dokunsal geri bildirim (haptic) — dil butonları, kategori
    // sekmeleri ve diğer basılabilir butonlarda hafif titreşim.
    // iOS Safari navigator.vibrate desteklemiyor, feature-detect şart.
    document.addEventListener('click', (e) => {
        const btn = e.target.closest('button, .btn, .lang-btn, .cat-btn, .fav-btn, .clear-search-btn');
        if (btn && navigator.vibrate) navigator.vibrate(10);
    });
});
