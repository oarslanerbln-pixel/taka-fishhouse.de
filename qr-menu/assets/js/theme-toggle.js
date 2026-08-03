document.addEventListener('DOMContentLoaded', () => {
    const themeBtn = document.getElementById('themeToggle');
    const savedTheme = localStorage.getItem('taka-theme');
    
    // Default to light (cream) theme if not set, since user specified it as the main theme
    if (savedTheme) {
        document.documentElement.setAttribute('data-theme', savedTheme);
    } else {
        document.documentElement.setAttribute('data-theme', 'light');
        localStorage.setItem('taka-theme', 'light');
    }

    if(themeBtn) {
        themeBtn.addEventListener('click', () => {
            const current = document.documentElement.getAttribute('data-theme');
            const next = current === 'light' ? 'dark' : 'light';
            document.documentElement.setAttribute('data-theme', next);
            localStorage.setItem('taka-theme', next);
        });
    }
});
