# Пример теста в синхронном режиме (Python)

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False) # Запуск теста в режиме, когда видно браузер
    page = browser.new_page()
    page.goto("https://bigtesty.ru/")
    page.screenshot(path = "screenshots/homepage.png")
    browser.close()