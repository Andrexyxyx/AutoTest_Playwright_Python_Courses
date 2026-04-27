# НАЖАТИЕ НА КОНКРЕТНЫЙ ВАРИАНТ В ДРОПДАУНЕ (СЕЛЕКТ-БОКСЕ)
from time import sleep
from playwright.sync_api import Page, expect, Dialog


# Запуск теста - pytest tests/test_dropdown.py::test_select --headed
def test_select(page: Page):
    page.goto("https://qa-practice.com/elements/iframe/iframe_page")
    page.locator("#sorter").first.select_option("Price") # Поиск ПЕРВОГО элемента по id = sorter и выбор варианта "Price"
