import os

def fix_qr_menu():
    filepath = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\index.html"
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Eger Vercel SSO varsa diye bir check
    if "SAML SSO" in content:
        print("DIKKAT: VERCEL SSO VAR, GIT CHECKOUT YAPILMADI!")
        return

    # UTF-8 Bozukluklarini duzelt
    replacements = {
        'Ã¼': 'ü', 'Ä±': 'ı', 'ÄŸ': 'ğ', 'ÅŸ': 'ş', 'Ã¶': 'ö', 'Ã§': 'ç',
        'Ã‡': 'Ç', 'Åž': 'Ş', 'Ä°': 'İ', 'Ã–': 'Ö', 'Ãœ': 'Ü', 'â‚¬': '€',
        'ðŸ ƒ': '🌿', 'ðŸ Ÿ': '🍤'
    }
    for bad, good in replacements.items():
        content = content.replace(bad, good)
        
    # Yollari duzelt (assets/ -> ../assets/)
    # Regex yerine basit replace yapiyoruz, dikkatlice.
    # Oncelikle double slash olmamasi icin ../assets/ olanlari assets/ yapalim ki guvenli olsun
    content = content.replace('../assets/', 'assets/')
    
    # Simdi tum assets/ yazanlari ../assets/ yapalim (cunku bu dosya qr-menu/ icinde!)
    content = content.replace('"assets/', '"../assets/')
    content = content.replace("'assets/", "'../assets/")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("qr-menu/index.html FIXLENDI!")

def fix_menu_html():
    filepath = r"c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\menu.html"
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # UTF-8 Bozukluklarini duzelt
    replacements = {
        'Ã¼': 'ü', 'Ä±': 'ı', 'ÄŸ': 'ğ', 'ÅŸ': 'ş', 'Ã¶': 'ö', 'Ã§': 'ç',
        'Ã‡': 'Ç', 'Åž': 'Ş', 'Ä°': 'İ', 'Ã–': 'Ö', 'Ãœ': 'Ü', 'â‚¬': '€',
        'ðŸ ƒ': '🌿', 'ðŸ Ÿ': '🍤'
    }
    for bad, good in replacements.items():
        content = content.replace(bad, good)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("menu.html FIXLENDI!")

fix_qr_menu()
fix_menu_html()
