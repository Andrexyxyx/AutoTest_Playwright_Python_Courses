# Пример тестов с поиском разного вида локаторов


from playwright.sync_api import Page, expect

# Запуск теста - pytest tests/test_locators_litres.py::test_locator_role --headed
def test_locator_role(page: Page):
    """Поиск и ОЖИДАНИЕ кнопки 'Найти', нажатие и поиск текста в плэйхолдере"""
    page.goto("https://www.litres.ru/")
    page.get_by_role("link", name = "Популярное").click()
    expect(page).to_have_title("Лучшие книги 2026 – читать онлайн бесплатно или скачать в fb2")
    page.get_by_role("button", name = "Найти").wait_for(timeout=7000).click() #Будет явно ждать кнопку 7 секунд, а не 5 как по умолчанию
    expect(page.get_by_placeholder("Искать на Литрес")).to_be_visible()


# Запуск теста - pytest tests/test_locators_litres.py::test_locator_placeholder --headed
def test_locator_placeholder(page: Page):
    """Поиск и заполнение элемента по плэйсхолдеру, просмотр результатов поиска, ВЫДАЧА ОПРЕДЕЛЕННОГО СООБЕЩЕНИЯ В ОШИБКЕ"""
    page.goto("https://www.litres.ru/")
    page.get_by_placeholder("Искать на Литрес").fill("Игра престолов")
    page.keyboard.press("Enter")
    expect(page.get_by_text("Результаты поиска «Игра престолов1»"), "Покажи мне логи!!!").to_be_visible()


# Запуск теста - pytest tests/test_locators_litres.py::test_locator_datatestid --headed
def test_locator_datatestid(page: Page):
    """Поиск элемента по testid и проверка наличия текста"""
    page.goto("https://www.litres.ru/")
    page.get_by_test_id("tab-login").click()
    expect(page.get_by_text("Вход или регистрация")).to_be_visible()


# Запуск теста - pytest -v tests/test_locators_litres.py::test_locator_xpath --headed
def test_locator_xpath(page: Page):
    """Поиск элемента по xpath"""
    page.goto("https://www.litres.ru/")
    expect(page.locator("xpath=//a[@title='YouTube']")).to_be_visible() # a - ссылочный тип, title - атрибут (<a href="https://www.youtube.com..." ... title="YouTube"><img src="...."....</a>)


# Запуск теста - pytest -v tests/test_locators_litres.py::test_count_elements --headed
def test_count_elements(page: Page):
    """Поиск и подсчет нескольких элементов по количеству"""
    page.goto("https://www.litres.ru/")
    page.get_by_placeholder("Искать на Литрес").fill("Игра престолов")
    page.get_by_test_id("search__button").click()

    books = page.get_by_test_id("art__wrapper")
    expect(books).to_have_count(24, timeout = 10000) # Ожидаем, что будет 24 элемента и указываем задержку в 10 сек
    page.pause()