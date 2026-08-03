import os

impressum_html = """<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Impressum | TAKA Fish House Kreuzberg</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/style.css">
    <style>
        .legal-content {
            padding: 120px 5% 60px;
            max-width: 800px;
            margin: 0 auto;
            color: #f8fafc;
        }
        .legal-content h1 {
            font-family: 'Playfair Display', serif;
            font-size: 2.5rem;
            margin-bottom: 2rem;
            color: #f1f5f9;
        }
        .legal-content h2 {
            font-size: 1.5rem;
            margin-top: 2rem;
            margin-bottom: 1rem;
            color: #94a3b8;
        }
        .legal-content p {
            line-height: 1.6;
            margin-bottom: 1rem;
            color: #cbd5e1;
        }
    </style>
</head>
<body>
    <!-- Header Navigation -->
    <header id="header" class="scrolled">
        <div class="header-container">
            <a href="index.html" class="brand-logo">
                <img src="assets/taka_logo.png" alt="TAKA Fish House Logo" class="brand-logo-img" style="height: 50px;">
            </a>
            <nav class="nav-links sm-hidden" aria-label="Main Navigation">
                <a href="index.html" data-i18n="nav-home">Anasayfa</a>
                <a href="index.html#about" data-i18n="nav-story">Hikayemiz</a>
                <a href="qr-menu/" data-i18n="nav-menu">Menü</a>
            </nav>
        </div>
    </header>

    <main class="legal-content">
        <h1>Impressum</h1>
        <p>Angaben gemäß § 5 TMG:</p>
        
        <h2>Taka Fish House GmbH</h2>
        <p>
            Kottbusser Damm 35<br>
            10967 Berlin<br>
            Deutschland
        </p>

        <h2>Kontakt</h2>
        <p>
            E-Mail: info@taka-fisch-haus.de<br>
            Website: www.ufuksenturk.com
        </p>

        <h2>Identifikationsdaten & Registereintrag</h2>
        <p>
            Taka Fish House GmbH mit Sitz in Berlin ist im Handelsregister mit der Rechtsform Gesellschaft mit beschränkter Haftung eingetragen.<br><br>
            <strong>Registernummer:</strong> HRB 280084 B<br>
            <strong>Amtsgericht:</strong> 14057 Berlin
        </p>
        
        <p>
            Das Unternehmen ist wirtschaftsaktiv. Die letzte Änderung im Handelsregister wurde am 12.10.2025 vorgenommen. Das Unternehmen wird derzeit von 2 Managern (2 x Geschäftsführer) geführt. Es sind 2 Gesellschafter an der Unternehmung beteiligt.
        </p>

        <h2>Umsatzsteuer-ID</h2>
        <p>Die Umsatzsteuer-ID des Unternehmens ist in den Firmendaten verfügbar.</p>

        <h2>Verbraucherstreitbeilegung/Universalschlichtungsstelle</h2>
        <p>Wir sind nicht bereit oder verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>

        <h2>Haftung für Inhalte</h2>
        <p>Als Diensteanbieter sind wir gemäß § 7 Abs.1 TMG für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich. Nach §§ 8 bis 10 TMG sind wir als Diensteanbieter jedoch nicht verpflichtet, übermittelte oder gespeicherte fremde Informationen zu überwachen oder nach Umständen zu forschen, die auf eine rechtswidrige Tätigkeit hinweisen.</p>
    </main>

    <!-- Footer -->
    <footer id="contact" style="background: #050A14; padding: 40px 0;">
        <div style="max-width: 1200px; margin: 0 auto; text-align: center; color: #8a9ab0;">
            <p>&copy; 2026 TAKA Fish House</p>
            <div style="margin-top: 10px;">
                <a href="index.html" style="color: #D4AF37; margin: 0 10px; text-decoration: none;">Anasayfa</a>
                <a href="impressum.html" style="color: #D4AF37; margin: 0 10px; text-decoration: none;">Impressum</a>
                <a href="datenschutz.html" style="color: #D4AF37; margin: 0 10px; text-decoration: none;">Datenschutz</a>
            </div>
        </div>
    </footer>
</body>
</html>
"""

datenschutz_html = impressum_html.replace("Impressum | TAKA Fish House Kreuzberg", "Datenschutz | TAKA Fish House Kreuzberg")
datenschutz_html = datenschutz_html.replace("<h1>Impressum</h1>", "<h1>Datenschutzerklärung (DSGVO)</h1>")
datenschutz_html = datenschutz_html.replace("""<p>Angaben gemäß § 5 TMG:</p>
        
        <h2>Taka Fish House GmbH</h2>
        <p>
            Kottbusser Damm 35<br>
            10967 Berlin<br>
            Deutschland
        </p>

        <h2>Kontakt</h2>
        <p>
            E-Mail: info@taka-fisch-haus.de<br>
            Website: www.ufuksenturk.com
        </p>

        <h2>Identifikationsdaten & Registereintrag</h2>
        <p>
            Taka Fish House GmbH mit Sitz in Berlin ist im Handelsregister mit der Rechtsform Gesellschaft mit beschränkter Haftung eingetragen.<br><br>
            <strong>Registernummer:</strong> HRB 280084 B<br>
            <strong>Amtsgericht:</strong> 14057 Berlin
        </p>
        
        <p>
            Das Unternehmen ist wirtschaftsaktiv. Die letzte Änderung im Handelsregister wurde am 12.10.2025 vorgenommen. Das Unternehmen wird derzeit von 2 Managern (2 x Geschäftsführer) geführt. Es sind 2 Gesellschafter an der Unternehmung beteiligt.
        </p>

        <h2>Umsatzsteuer-ID</h2>
        <p>Die Umsatzsteuer-ID des Unternehmens ist in den Firmendaten verfügbar.</p>

        <h2>Verbraucherstreitbeilegung/Universalschlichtungsstelle</h2>
        <p>Wir sind nicht bereit oder verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>

        <h2>Haftung für Inhalte</h2>
        <p>Als Diensteanbieter sind wir gemäß § 7 Abs.1 TMG für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich. Nach §§ 8 bis 10 TMG sind wir als Diensteanbieter jedoch nicht verpflichtet, übermittelte oder gespeicherte fremde Informationen zu überwachen oder nach Umständen zu forschen, die auf eine rechtswidrige Tätigkeit hinweisen.</p>""", """
        <h2>1. Datenschutz auf einen Blick</h2>
        <p><strong>Allgemeine Hinweise</strong><br>
        Die folgenden Hinweise geben einen einfachen Überblick darüber, was mit Ihren personenbezogenen Daten passiert, wenn Sie diese Website besuchen. Personenbezogene Daten sind alle Daten, mit denen Sie persönlich identifiziert werden können.</p>

        <h2>2. Datenerfassung auf dieser Website</h2>
        <p><strong>Wer ist verantwortlich für die Datenerfassung auf dieser Website?</strong><br>
        Die Datenverarbeitung auf dieser Website erfolgt durch den Websitebetreiber:<br>
        Taka Fish House GmbH<br>
        Kottbusser Damm 35, 10967 Berlin<br>
        HRB 280084 B (Amtsgericht 14057 Berlin)</p>

        <h2>3. Hosting und Content Delivery Networks (CDN)</h2>
        <p><strong>Externes Hosting</strong><br>
        Diese Website wird bei einem externen Dienstleister gehostet (Hoster). Die personenbezogenen Daten, die auf dieser Website erfasst werden, werden auf den Servern des Hosters gespeichert. Hierbei kann es sich v. a. um IP-Adressen, Kontaktanfragen, Meta- und Kommunikationsdaten, Vertragsdaten, Kontaktdaten, Namen, Websitezugriffe und sonstige Daten, die über eine Website generiert werden, handeln.</p>

        <h2>4. Allgemeine Hinweise und Pflichtinformationen</h2>
        <p><strong>Datenschutz</strong><br>
        Die Betreiber dieser Seiten nehmen den Schutz Ihrer persönlichen Daten sehr ernst. Wir behandeln Ihre personenbezogenen Daten vertraulich und entsprechend der gesetzlichen Datenschutzvorschriften (DSGVO) sowie dieser Datenschutzerklärung.</p>
        """)

with open('impressum.html', 'w', encoding='utf-8') as f:
    f.write(impressum_html)

with open('datenschutz.html', 'w', encoding='utf-8') as f:
    f.write(datenschutz_html)

print("Created impressum.html and datenschutz.html")
