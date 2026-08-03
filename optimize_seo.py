import os
import re

seo_meta_tags = """
    <!-- SEO & Performance Optimization -->
    <meta name="description" content="TAKA Fish House Kreuzberg. 100% frischer Fisch, ohne Zusatzstoffe. Bosphorus-Brise im Herzen von Berlin. / Karadeniz'in taze lezzetleri.">
    <meta name="keywords" content="Fischrestaurant Berlin, Kreuzberg Fisch, Taka Fish House, frischer Fisch, ohne Zusatzstoffe, Balik Restorani Berlin, Karadeniz yemekleri, seafood Berlin">
    <meta name="author" content="TAKA Fish House">
    
    <!-- Open Graph / Social Media -->
    <meta property="og:title" content="TAKA Fish House | Kreuzberg">
    <meta property="og:description" content="100% Fisch. Purer Geschmack. Authentische Schwarzmeer-Spezialitäten in Berlin Kreuzberg.">
    <meta property="og:image" content="https://taka-fisch-haus.vercel.app/assets/taka-logo-gold.svg">
    <meta property="og:url" content="https://taka-fisch-haus.vercel.app/">
    <meta property="og:type" content="restaurant">
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="TAKA Fish House | Kreuzberg">
    <meta name="twitter:description" content="100% Fisch. Purer Geschmack. Authentische Schwarzmeer-Spezialitäten in Berlin Kreuzberg.">
    
    <!-- Preconnect & Preload for Performance -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preload" href="assets/css/style.css" as="style">
    <link rel="preload" as="image" href="assets/taka-logo-gold.svg">
"""

qr_seo_meta_tags = seo_meta_tags.replace('assets/', '../assets/')

def optimize_file(filepath, meta_tags):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add lang="de" if missing
    if '<html' in content and 'lang=' not in content:
        content = content.replace('<html', '<html lang="de"')

    # Insert meta tags before closing head
    if '<!-- SEO & Performance Optimization -->' not in content:
        content = content.replace('</head>', meta_tags + '\n</head>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

optimize_file('index.html', seo_meta_tags)
optimize_file('qr-menu/index.html', qr_seo_meta_tags)

print("SEO tags and preloads added to HTML files.")
