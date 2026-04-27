# Пример теста с проверкой и поиском элемента в Iframe
from time import sleep
from playwright.sync_api import Page, expect, Dialog


# Запуск теста - pytest tests/test_iframes.py::test_iframe --headed
def test_iframe(page: Page):
    page.goto("https://qa-practice.com/elements/iframe/iframe_page")
    page.frame_locator("iframe").locator(".navbar-toggler-icon").click() # Поиск элемента внутри iframe по классу navbar-toggler-icon
