# Установка Playwright - pip install pytest-playwright
# Установка браузеров - playwright install

# Запуск всех тестов проекта - pytest
# Запуск всех тестов файла - pytest test_file.py
# Запуск определенного теста в файле - pytest test_file.py::test_function_name

# Запуск всех тестов проекта c красивым выводом результата в консоль - pytest -v
# Запуск всех тестов проекта c печатью в консоль - pytest -s

# Запуск в режиме с браузером - pytest --headed
# Запуск определенного браузера - pytest --browser chromium firefox webkit (chromium - по умолчанию)


from playwright.sync_api import Page, expect

def test_wiki(page: Page):
    page.goto("https://ru.wikipedia.org/")
    expect(page.get_by_text("Добро пожаловать в Википедию")).to_be_visible()