import asyncio
from playwright.async_api import async_playwright
import json
import re

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        url = "https://wolt.com/de/deu/berlin/restaurant/taka-fish-house-kottbusserdamm?srsltid=AfmBOoqoWGpnnHdU5af5wb_vn-gMckxOw7aefCNfYXOpL1dcydUu1cNO"
        print(f"Navigating to {url}")
        
        await page.goto(url, wait_until="networkidle")
        await page.wait_for_timeout(3000)
        
        # Scroll multiple times
        for _ in range(5):
            await page.evaluate("window.scrollBy(0, document.body.scrollHeight)")
            await page.wait_for_timeout(1000)
        
        # Extract all image URLs
        images = await page.evaluate('''() => {
            const imgs = Array.from(document.querySelectorAll('img'));
            return imgs.map(img => ({
                src: img.src,
                alt: img.alt
            })).filter(img => img.src && img.src.startsWith('http'));
        }''')
        
        # Also grab any div with background image
        bg_images = await page.evaluate('''() => {
            const divs = Array.from(document.querySelectorAll('div'));
            return divs.map(div => {
                const style = window.getComputedStyle(div);
                const bg = style.backgroundImage;
                if (bg && bg.includes('url(')) {
                    const url = bg.split('url("')[1]?.split('")')[0] || bg.split('url(')[1]?.split(')')[0];
                    return { url, text: div.innerText.substring(0, 50) };
                }
                return null;
            }).filter(item => item !== null);
        }''')
        
        with open("wolt_images.json", "w", encoding="utf-8") as f:
            json.dump({"imgs": images, "bgs": bg_images}, f, indent=2, ensure_ascii=False)
            
        print(f"Found {len(images)} images and {len(bg_images)} background images.")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
