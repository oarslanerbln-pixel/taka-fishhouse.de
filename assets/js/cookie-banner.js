document.addEventListener('DOMContentLoaded', () => {
    // Check if user already accepted cookies
    if (localStorage.getItem('taka-cookies-accepted')) return;

    // Create banner
    const banner = document.createElement('div');
    banner.className = 'taka-cookie-banner';
    banner.innerHTML = `
        <div class="cookie-content">
            <p><strong>Datenschutz & Cookies:</strong> Wir verwenden Cookies und ähnliche Technologien, um Ihnen das beste Erlebnis auf unserer Website zu bieten. Weitere Informationen finden Sie in unserer <a href="/datenschutz.html">Datenschutzerklärung</a>.</p>
            <div class="cookie-buttons">
                <button id="acceptCookies" class="btn btn-primary btn-sm">Akzeptieren</button>
            </div>
        </div>
    `;

    // Append styles directly to keep it self-contained
    const style = document.createElement('style');
    style.innerHTML = `
        .taka-cookie-banner {
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            width: 90%;
            max-width: 800px;
            background: rgba(15, 23, 42, 0.95);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: #fff;
            padding: 20px 25px;
            border-radius: 12px;
            z-index: 99999;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
            display: flex;
            align-items: center;
            justify-content: space-between;
            opacity: 0;
            transform: translate(-50%, 20px);
            animation: slideUpCookie 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards 1s;
        }
        .taka-cookie-banner .cookie-content {
            display: flex;
            align-items: center;
            justify-content: space-between;
            width: 100%;
            gap: 20px;
        }
        .taka-cookie-banner p {
            margin: 0;
            font-size: 0.9rem;
            line-height: 1.5;
            font-family: 'Inter', sans-serif;
            color: #cbd5e1;
        }
        .taka-cookie-banner p strong {
            color: #fff;
        }
        .taka-cookie-banner a {
            color: var(--primary);
            text-decoration: underline;
        }
        .taka-cookie-banner .cookie-buttons {
            flex-shrink: 0;
        }
        @keyframes slideUpCookie {
            to {
                opacity: 1;
                transform: translate(-50%, 0);
            }
        }
        @media (max-width: 768px) {
            .taka-cookie-banner .cookie-content {
                flex-direction: column;
                text-align: center;
            }
            .taka-cookie-banner .cookie-buttons {
                width: 100%;
            }
            .taka-cookie-banner .cookie-buttons button {
                width: 100%;
            }
        }
    `;

    document.head.appendChild(style);
    document.body.appendChild(banner);

    // Accept action
    document.getElementById('acceptCookies').addEventListener('click', () => {
        localStorage.setItem('taka-cookies-accepted', 'true');
        banner.style.opacity = '0';
        banner.style.transform = 'translate(-50%, 20px)';
        banner.style.transition = 'all 0.5s ease';
        setTimeout(() => banner.remove(), 500);
    });
});
