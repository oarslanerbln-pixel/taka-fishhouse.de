import asyncio
import json
import re
import sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

UBEREATS_URL = "https://www.ubereats.com/de-en/store/taka-restaurant/LFSSR2wyU9ylHG_P4cVDaQ?srsltid=AfmBOopedU1oda6_56eWqAL1TKhTVU66xvg4sf-w_rB1IRporh9Wr9q7"

async def scrape_ubereats():
    print("UberEats sayfası açılıyor...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        await page.goto(UBEREATS_URL, wait_until="domcontentloaded")
        await page.wait_for_timeout(3000)
        
        # Scroll to load lazy images
        for _ in range(15):
            await page.evaluate("window.scrollBy(0, 800)")
            await page.wait_for_timeout(500)
            
        print("Taranıyor...")
        
        items = await page.evaluate('''() => {
            const results = [];
            // UberEats menu items are usually in li elements
            const lis = document.querySelectorAll('li');
            lis.forEach(li => {
                const textNode = li.querySelector('span') || li.querySelector('div[data-testid="rich-text"]');
                const imgNode = li.querySelector('img');
                
                if (textNode && textNode.innerText.trim().length > 2) {
                    const name = textNode.innerText.trim();
                    const img = imgNode ? imgNode.src : null;
                    if (name) {
                        results.push({name, img});
                    }
                }
            });
            return results;
        }''')
        
        # Find next data if present to get high-res images
        next_data_json = await page.evaluate('''() => {
            const script = document.getElementById('__NEXT_DATA__');
            return script ? script.innerHTML : null;
        }''')
        
        await browser.close()
        
        with open("ubereats_scraped.json", "w", encoding="utf-8") as f:
            json.dump({"items": items, "next_data": bool(next_data_json)}, f, indent=2, ensure_ascii=False)
            
        print(f"Toplam {len(items)} liste elemanı bulundu.")
        valid_items = [i for i in items if i['img'] and "http" in i['img']]
        print(f"Görseli olan: {len(valid_items)}")
        
if __name__ == "__main__":
    asyncio.run(scrape_ubereats())
