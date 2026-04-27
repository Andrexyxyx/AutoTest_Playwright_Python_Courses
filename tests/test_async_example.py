# Пример теста в асинхронном режиме (Python)

from playwright.async_api import async_playwright
import asyncio

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False) # Запуск теста в режиме, когда видно браузер
        page = await browser.new_page()
        await page.goto("https://www.google.com/")
        await page.screenshot(path = "screenshots/google.png")
        await browser.close()

asyncio.run(main())