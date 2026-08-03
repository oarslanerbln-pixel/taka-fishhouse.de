import asyncio
import json
import sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

QUERIES = {
    "water": "water bottle",
    "cola": "cola bottle",
    "fanta": "orange soda glass",
    "sprite": "sprite bottle",
    "apple_juice": "apple juice glass",
    "ayran": "kefir glass",
    "tea": "turkish tea glass",
    "coffee": "cappuccino cup",
    "espresso": "espresso cup",
    "latte": "latte macchiato"
}

async def fetch_unsplash_images():
    print("Unsplash'tan görseller çekiliyor...")
    results = {}
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        for key, query in QUERIES.items():
            print(f"Aranıyor: {query}")
            await page.goto(f"https://unsplash.com/s/photos/{query.replace(' ', '-')}")
            await page.wait_for_timeout(2000)
            
            img_src = await page.evaluate('''() => {
                const imgs = document.querySelectorAll('img[srcset]');
                for (let img of imgs) {
                    if (img.src && img.src.includes('images.unsplash.com/photo-')) {
                        // Return the base URL without query params for highest quality or keep a small width
                        return img.src.split('?')[0] + "?w=600&h=600&fit=crop";
                    }
                }
                return null;
            }''')
            
            if img_src:
                print(f" Bulundu: {img_src}")
                results[key] = img_src
            else:
                print(" Bulunamadı.")
                
        await browser.close()
        
        with open("unsplash_images.json", "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2)
            
if __name__ == "__main__":
    asyncio.run(fetch_unsplash_images())
