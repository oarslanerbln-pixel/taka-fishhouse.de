from playwright.sync_api import sync_playwright
import time

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    page.goto('https://www.lieferando.de/speisekarte/taka-fish-house-kreuzberg', wait_until='networkidle')
    time.sleep(5)
    page.screenshot(path='screenshot.png')
    with open('page.html', 'w', encoding='utf-8') as f:
        f.write(page.content())
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
