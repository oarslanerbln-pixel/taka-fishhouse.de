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
    }
};

// Auto-init
document.addEventListener('DOMContentLoaded', () => {
    i18n.init();
    
    // Setup event listeners for switcher buttons
    document.addEventListener('click', (e) => {
        if (e.target.classList.contains('lang-btn')) {
            const lang = e.target.dataset.lang;
            i18n.setLanguage(lang);
        }
    });
});
