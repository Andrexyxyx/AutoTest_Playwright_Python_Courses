# ПРОВЕРКА ПЕРЕХОДОВ И НАЖАТИЙ НА ДРУГИХ ВКЛАДКАХ
from time import sleep

from playwright.sync_api import Page, BrowserContext


# Запуск теста - pytest tests/test_tabs.py::test_tabs --headed
def test_tabs(page: Page, context: BrowserContext):  # context - специальная фикстура для работы именно с браузером, а не с вкладкой, как Page
    page.goto("https://blog.promopult.ru/content/35-primerov-prekrasnyx-posadochnyx-stranic-dizajnu-kotoryx-mozhno-tolko-pozavidovat-i-kriticheskij-razbor.html")

    with context.expect_page() as new_tab_event: # Ожидание появления события открытия новой вкладки
        page.get_by_role("link", name="growfood.pro").click()  # В devtools - <a href="....">growfood.pro</a>
        new_tab = new_tab_event.value # new_tab - сессия работы с новой вкладкой

    # Уже после перехода на другую страницу
    new_tab.locator("xpath=//*[@id=\"navbar\"]/div/div[5]/div/div[2]").click()