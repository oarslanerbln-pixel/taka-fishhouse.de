import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        url = "https://share.google/TIgoVdZtLqoGLiBE0"
        print(f"Fetching {url}")
        await page.goto(url, timeout=15000)
        await page.wait_for_timeout(5000)
        
        # Get all image sources
        imgs = await page.evaluate('''() => {
            return Array.from(document.querySelectorAll('img')).map(img => img.src);
        }''')
        
        print("Images found:")
        for img in set(imgs):
            print(f"  {img}")
            
        await browser.close()

asyncio.run(main())
