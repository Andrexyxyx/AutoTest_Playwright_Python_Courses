# Пример теста по проверке заголовка страницы


from playwright.sync_api import Page, expect

# Запуск теста - pytest tests/test_titles_litres.py::test_main_page_title --headed
def test_main_page_title(page: Page):
    """Проверка названия заголовка страницы"""
    page.goto("https://www.litres.ru/")
    assert page.title() == "Литрес – сервис электронных и аудиокниг, скачать в fb2 и mp3, читать и слушать онлайн на Litres"

# Запуск теста - pytest tests/test_titles_litres.py::test_audiobooks_title --headed
def test_audiobooks_title(page: Page):
    """Проверка перехода на страницу "Аудиокниги" и проверка заголовка страницы"""
    page.goto("https://www.litres.ru/")
    # page.get_by_test_id("lowerMenu__item--audiobooks").click() # Другой вариант поиска кнопки
    page.locator("xpath = //*[@id=\"lowerMenuWrap\"]/nav/div/a[7]").click()
    expect(page).to_have_title("Аудиокниги – слушать онлайн или скачать в mp3 на Литрес")