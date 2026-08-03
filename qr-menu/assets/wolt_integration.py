"""
Wolt Integration Script - Taka Fish House
==========================================
1. Wolt sayfasından ürün adı + görsel URL eşleştirmesi yapar (Playwright)
2. menu-data.js'te görseli olmayan ürünleri Wolt verileriyle günceller
3. Görselleri wolt_imgs/ klasörüne indirir ve yolları kaydeder

Kullanım:
    python wolt_integration.py
"""

import asyncio
import json
import os
import re
import sys
import codecs
import urllib.request
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

WOLT_URL = "https://wolt.com/de/deu/berlin/restaurant/taka-fish-house-kottbusserdamm"
MENU_DATA_PATH = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\js\menu-data.js'
WOLT_IMGS_DIR = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\wolt_imgs'
WOLT_MAPPING_FILE = r'c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus\qr-menu\assets\wolt_item_mapping.json'

# ──────────────────────────────────────────────
# ADIM 1: Wolt'tan ürün adı + görsel eşleştir
# ──────────────────────────────────────────────

async def scrape_wolt_items():
    """Wolt sayfasından her ürünün adı ve görsel URL'sini çeker."""
    print("\n🌐 Wolt sayfası açılıyor...")
    
    items = {}
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": 1440, "height": 900},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )
        page = await context.new_page()
        
        await page.goto(WOLT_URL, wait_until="networkidle", timeout=30000)
        print("✅ Sayfa yüklendi, scroll yapılıyor...")
        
        # Cookie/popup kapat
        try:
            await page.locator("button[data-localization-key='gdpr-consents.banner.accept-button']").click(timeout=3000)
        except:
            pass
        try:
            await page.get_by_role("button", name="Akzeptieren").click(timeout=3000)
        except:
            pass
        
        # Sayfayı yavaşça scroll et (lazy load için)
        for i in range(20):
            await page.evaluate("window.scrollBy(0, 600)")
            await page.wait_for_timeout(400)
        
        await page.wait_for_timeout(2000)
        
        # Yöntem 1: MenuItem data-test-id ile
        print("🔍 Ürünler taranıyor (data-test-id yöntemi)...")
        menu_items = await page.locator("[data-test-id='MenuItem']").all()
        print(f"   Bulunan ürün kartı: {len(menu_items)}")
        
        for item_el in menu_items:
            try:
                # Ürün adını bul
                name_el = item_el.locator("h3, [data-test-id='MenuItemName'], [class*='name'], [class*='title']").first
                name = (await name_el.inner_text()).strip() if await name_el.count() > 0 else None
                
                # Görsel URL bul
                img_el = item_el.locator("img").first
                img_src = await img_el.get_attribute("src") if await img_el.count() > 0 else None
                
                # Background image bul (eğer img yoksa)
                if not img_src:
                    div_with_bg = item_el.locator("div[style*='background']").first
                    if await div_with_bg.count() > 0:
                        style = await div_with_bg.get_attribute("style")
                        match = re.search(r'url\(["\']?(https?://[^"\')\s]+)["\']?\)', style or "")
                        if match:
                            img_src = match.group(1)
                
                if name and img_src and "imageproxy.wolt.com" in img_src:
                    # Yüksek kaliteli URL oluştur
                    base_url = img_src.split("?")[0]
                    # Wolt görsel proxy'ye boyut parametresi ekle
                    if "/assets/" in base_url:
                        img_url = f"{base_url}?w=600"
                    else:
                        img_url = img_src
                    
                    items[name] = img_url
                    print(f"   ✓ {name}")
            except Exception as e:
                pass
        
        # Yöntem 2: Eğer az ürün bulduysa, genel img taraması yap
        if len(items) < 5:
            print("\n🔍 Alternatif yöntem: Genel HTML taraması...")
            
            # Tüm ürün başlıklarını ve yanlarındaki görselleri bul
            result = await page.evaluate("""() => {
                const results = [];
                
                // MenuItem test id'si ile
                const menuItems = document.querySelectorAll('[data-test-id="MenuItem"]');
                menuItems.forEach(item => {
                    const nameEl = item.querySelector('h3') || 
                                   item.querySelector('[class*="name"]') ||
                                   item.querySelector('[class*="title"]') ||
                                   item.querySelector('p');
                    const imgEl = item.querySelector('img');
                    
                    if (nameEl && imgEl && imgEl.src && imgEl.src.includes('wolt')) {
                        results.push({
                            name: nameEl.innerText.trim(),
                            img: imgEl.src
                        });
                    }
                });
                
                // Eğer bulamadıysak, tüm içerikli img'leri dene
                if (results.length === 0) {
                    const allImgs = document.querySelectorAll('img[src*="imageproxy.wolt.com/assets"]');
                    allImgs.forEach(img => {
                        const parent = img.closest('[role="button"]') || img.parentElement?.parentElement?.parentElement;
                        if (parent) {
                            const textEl = parent.querySelector('h3') || parent.querySelector('p') || parent.querySelector('span');
                            if (textEl && textEl.innerText.trim().length > 2) {
                                results.push({
                                    name: textEl.innerText.trim().split('\\n')[0],
                                    img: img.src
                                });
                            }
                        }
                    });
                }
                
                return results;
            }""")
            
            for r in result:
                name = r['name']
                img = r['img']
                if name and img and name not in items:
                    items[name] = img
                    print(f"   ✓ {name}")
        
        # Sayfa kaynağını kaydet (debug için)
        page_content = await page.content()
        with open("wolt_page_debug.html", "w", encoding="utf-8") as f:
            f.write(page_content)
        print(f"\n💾 Debug HTML kaydedildi: wolt_page_debug.html")
        
        await browser.close()
    
    print(f"\n📋 Toplam {len(items)} ürün bulundu Wolt'ta")
    return items


# ──────────────────────────────────────────────
# ADIM 2: Eksik görselleri menüde bul
# ──────────────────────────────────────────────

def get_missing_items():
    """menu-data.js'te görseli olmayan ürünleri döndürür."""
    with open(MENU_DATA_PATH, encoding='utf-8') as f:
        content = f.read()
    
    item_blocks = re.findall(r'\{[^{}]+\}', content, re.DOTALL)
    
    missing = []
    for block in item_blocks:
        name_match = re.search(r'"nameDE":\s*"([^"]+)"', block)
        if name_match and '"image"' not in block:
            missing.append(name_match.group(1))
    
    return missing


# ──────────────────────────────────────────────
# ADIM 3: Fuzzy matching ile eşleştir
# ──────────────────────────────────────────────

def normalize(text):
    """Metni karşılaştırma için normalize eder."""
    import unicodedata
    text = text.lower().strip()
    # Yaygın Almanca özel karakterleri normalleştir
    text = text.replace('ü', 'u').replace('ö', 'o').replace('ä', 'a')
    text = text.replace('ß', 'ss').replace('é', 'e').replace('è', 'e')
    # Noktalama kaldır
    text = re.sub(r'[,\.\(\)\-–]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def find_best_match(menu_name, wolt_items):
    """
    Menu'deki ürün adını Wolt ürün listesiyle eşleştirir.
    Returns: (wolt_name, score) or None
    """
    menu_norm = normalize(menu_name)
    menu_words = set(menu_norm.split())
    
    best_match = None
    best_score = 0
    
    for wolt_name, img_url in wolt_items.items():
        wolt_norm = normalize(wolt_name)
        wolt_words = set(wolt_norm.split())
        
        # Tam eşleşme
        if menu_norm == wolt_norm:
            return (wolt_name, img_url, 1.0)
        
        # Kelime örtüşmesi
        if menu_words and wolt_words:
            intersection = menu_words & wolt_words
            union = menu_words | wolt_words
            jaccard = len(intersection) / len(union)
            
            # Önemli anahtar kelimeler bonus
            key_words = {'lachs', 'dorade', 'makrele', 'garnele', 'sardine', 
                        'sandwich', 'durum', 'dürüm', 'suppe', 'salat',
                        'burger', 'nudeln', 'wasser', 'cola', 'tee'}
            key_bonus = len(intersection & key_words) * 0.15
            
            score = jaccard + key_bonus
            
            if score > best_score:
                best_score = score
                best_match = (wolt_name, img_url, score)
    
    return best_match if best_score > 0.3 else None


# ──────────────────────────────────────────────
# ADIM 4: Görselleri indir ve menu-data.js güncelle
# ──────────────────────────────────────────────

def download_image(url, filename):
    """Wolt görselini indir, yüksek kalite parametresi ekle."""
    os.makedirs(WOLT_IMGS_DIR, exist_ok=True)
    filepath = os.path.join(WOLT_IMGS_DIR, filename)
    
    if os.path.exists(filepath):
        return filepath
    
    try:
        # Wolt imageproxy için yüksek kalite parametreleri
        if "imageproxy.wolt.com/assets/" in url and "?" not in url:
            url = f"{url}?w=600&q=85"
        
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://wolt.com/"
        })
        with urllib.request.urlopen(req, timeout=15) as response:
            with open(filepath, 'wb') as f:
                f.write(response.read())
        return filepath
    except Exception as e:
        print(f"   ⚠️  İndirme hatası ({filename}): {e}")
        return None

def update_menu_data(mapping):
    """
    mapping: {menu_de_name: relative_image_path}
    menu-data.js'te bu isimlere image ekler.
    """
    with codecs.open(MENU_DATA_PATH, 'r', 'utf-8') as f:
        content = f.read()
    
    updated = 0
    for de_name, img_path in mapping.items():
        # nameDE içeren bloğu bul ve image ekle
        pattern = r'("nameDE":\s*"' + re.escape(de_name) + r'")'
        
        def add_image(m):
            return m.group(1)
        
        # Daha güvenli: blok içinde image yoksa ekle
        # Regex: nameDE'den sonraki satırları bul, image yoksa ekle
        block_pattern = r'(\{\s*(?:[^{}]|\n)*?"nameDE":\s*"' + re.escape(de_name) + r'"(?:[^{}]|\n)*?\})'
        
        def replacer(m):
            block = m.group(1)
            if '"image"' in block:
                return block  # zaten var, dokunma
            # image ekle (price'tan sonra veya nameDE'den sonra)
            if '"price"' in block:
                return re.sub(
                    r'("price":\s*"[^"]+"),?',
                    lambda x: x.group(0).rstrip(',') + f',\n                "image": "{img_path}"',
                    block, count=1
                )
            else:
                return re.sub(
                    r'("nameDE":\s*"' + re.escape(de_name) + r'"),?',
                    lambda x: x.group(0).rstrip(',') + f',\n                "image": "{img_path}"',
                    block, count=1
                )
        
        new_content = re.sub(block_pattern, replacer, content, flags=re.DOTALL)
        if new_content != content:
            content = new_content
            updated += 1
    
    with codecs.open(MENU_DATA_PATH, 'w', 'utf-8') as f:
        f.write(content)
    
    return updated


# ──────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────

async def main():
    print("=" * 60)
    print("🐟 TAKA FISH HOUSE — Wolt Görsel Entegrasyonu")
    print("=" * 60)
    
    # Eksik ürünleri bul
    missing_items = get_missing_items()
    print(f"\n📋 Görseli eksik {len(missing_items)} ürün bulundu:")
    for m in missing_items:
        print(f"   - {m}")
    
    # Wolt'tan veri çek
    wolt_items = await scrape_wolt_items()
    
    # Eşleştirme yap
    print("\n🔗 Eşleştirme yapılıyor...")
    
    mapping = {}      # {de_name: relative_path} — menu-data.js için
    to_download = {}  # {filename: wolt_url} — indirilecekler
    unmatched = []    # Eşleşemeyen ürünler
    
    for menu_name in missing_items:
        match = find_best_match(menu_name, wolt_items)
        if match:
            wolt_name, img_url, score = match
            
            # Dosya adı oluştur
            safe_name = re.sub(r'[^\w\s-]', '', menu_name.lower())
            safe_name = re.sub(r'\s+', '_', safe_name.strip())[:50]
            filename = f"{safe_name}.jpg"
            
            rel_path = f"assets/wolt_imgs/{filename}"
            
            mapping[menu_name] = rel_path
            to_download[filename] = img_url
            print(f"   ✅ '{menu_name}' → '{wolt_name}' (skor: {score:.2f})")
        else:
            unmatched.append(menu_name)
            print(f"   ❌ '{menu_name}' → eşleşme bulunamadı")
    
    # Eşleşme raporu kaydet
    report = {
        "matched": {k: {"path": v, "wolt_url": to_download.get(os.path.basename(v), "")} 
                    for k, v in mapping.items()},
        "unmatched": unmatched,
        "wolt_items": wolt_items
    }
    with open(WOLT_MAPPING_FILE, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\n💾 Eşleştirme raporu kaydedildi: wolt_item_mapping.json")
    
    if not mapping:
        print("\n⚠️  Hiç eşleştirme yapılamadı. wolt_page_debug.html dosyasını kontrol edin.")
        print("   Wolt sayfası robot koruması nedeniyle yüklenememiş olabilir.")
        return
    
    # Görselleri indir
    print(f"\n📥 {len(to_download)} görsel indiriliyor...")
    downloaded = 0
    for filename, url in to_download.items():
        result = download_image(url, filename)
        if result:
            downloaded += 1
            print(f"   ✓ {filename}")
    
    print(f"\n✅ {downloaded}/{len(to_download)} görsel indirildi")
    
    # menu-data.js'i güncelle
    print(f"\n📝 menu-data.js güncelleniyor...")
    updated = update_menu_data(mapping)
    print(f"✅ {updated} ürün güncellendi")
    
    # Özet
    print("\n" + "=" * 60)
    print("📊 ÖZET")
    print("=" * 60)
    print(f"   Eksik görsel: {len(missing_items)}")
    print(f"   Wolt'ta bulunan: {len(wolt_items)}")
    print(f"   Eşleştirilen: {len(mapping)}")
    print(f"   İndirilen: {downloaded}")
    print(f"   Eşleşemeyen: {len(unmatched)}")
    if unmatched:
        print(f"\n   ⚠️  Eşleşemeyen ürünler (manuel eklenebilir):")
        for u in unmatched:
            print(f"      - {u}")

if __name__ == "__main__":
    asyncio.run(main())
