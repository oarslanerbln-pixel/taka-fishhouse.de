from playwright.sync_api import sync_playwright
import json
import time

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    page.goto('https://www.lieferando.de/speisekarte/taka-fish-house-kreuzberg', wait_until='networkidle')
    time.sleep(5) # wait for lazy loading
    # scroll a bit to load images
    page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)
    
    items = page.locator('div[data-qa="item-card"]')
    result = []
    
    count = items.count()
    for i in range(count):
        item = items.nth(i)
        name_el = item.locator('h3[data-qa="item-name"]')
        if name_el.count() > 0:
            name = name_el.inner_text().strip()
            # Try to get image
            img_el = item.locator('img[data-qa="item-image"]')
            img_url = None
            if img_el.count() > 0:
                img_url = img_el.get_attribute('src')
            
            # also extract price to make matching easier
            price_el = item.locator('span[data-qa="item-price"]')
            price = None
            if price_el.count() > 0:
                price = price_el.inner_text().strip()
                
            result.append({'name': name, 'image': img_url, 'price': price})
            
    with open('lieferando_data.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
