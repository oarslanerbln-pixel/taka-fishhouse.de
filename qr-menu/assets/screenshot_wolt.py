import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1280, "height": 1080})
        
        url = "https://wolt.com/de/deu/berlin/restaurant/taka-fish-house-kottbusserdamm?srsltid=AfmBOoqoWGpnnHdU5af5wb_vn-gMckxOw7aefCNfYXOpL1dcydUu1cNO"
        print(f"Navigating to {url}")
        
        await page.goto(url, wait_until="networkidle")
        await page.wait_for_timeout(3000)
        
        # Scroll to bottom
        for _ in range(10):
            await page.evaluate("window.scrollBy(0, 1000)")
            await page.wait_for_timeout(500)
            
        await page.evaluate("window.scrollTo(0, 0)")
        await page.wait_for_timeout(1000)
        
        items_to_screenshot = [
            "Dorade Sandwich",
            "Makrele Sandwich",
            "Lachs Sandwich",
            "Lachsuppe"
        ]
        
        for item in items_to_screenshot:
            try:
                # Find the element containing the text
                loc = page.locator(f"text='{item}'").first
                if await loc.count() > 0:
                    # The parent container that has the image
                    parent = loc.locator("xpath=ancestor::div[@data-test-id='MenuItem']").first
                    if await parent.count() > 0:
                        filename = f"{item.replace(' ', '_').lower()}.png"
                        await parent.screenshot(path=filename)
                        print(f"Saved {filename}")
                    else:
                        print(f"Parent for {item} not found")
                else:
                    print(f"Text {item} not found")
            except Exception as e:
                print(f"Error screenshotting {item}: {e}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
