import asyncio
from playwright.async_api import async_playwright

links = {
    "buyuk_cay": "https://share.google/1Fzr2ZLYNFIg5WgQZ",
    "kucuk_cay": "https://share.google/vHPLEFKeMLn1aIdbk",
    "ayran_7gun": "https://share.google/iGyx73OdnyOMmKKhI",
    "kaffee_crema": "https://share.google/dtEUiBIgtWj5RCqLn",
    "kaffee_latte": "https://share.google/lbNdpibrFFxfYGe1e",
    "turk_mokka": "https://share.google/vMswTF9rHtC9IDd9J",
}

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        for name, url in links.items():
            try:
                await page.goto(url, timeout=15000)
                await page.wait_for_selector('img', timeout=5000)
                
                # In Google Photos share links, the main image usually has a class or is the largest image.
                # Let's get all image sources and find the most likely one
                imgs = await page.evaluate('''() => {
                    return Array.from(document.querySelectorAll('img')).map(img => img.src).filter(src => src.startsWith('http') && !src.includes('avatar') && !src.includes('logo'));
                }''')
                
                print(f"{name}:")
                for img in set(imgs):
                    print(f"  {img}")
                    
            except Exception as e:
                print(f"Error fetching {name}: {e}")
        await browser.close()

asyncio.run(main())
