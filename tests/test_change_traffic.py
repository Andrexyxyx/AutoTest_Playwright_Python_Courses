# ПОДМЕНА ТРАФФИКА
from time import sleep

from playwright.sync_api import Page, Route, expect
import re

# Запуск теста - pytest -v tests/test_change_traffic.py::test_change_request --headed
# ПОДМЕНА ТОГО, ЧТО МЫ ОТПРАВЛЯЕМ НА СЕРВЕР
def test_change_request(page: Page):

    """change_request - функция, которая будет обрабатывать перехваченный запрос"""
    def change_request(route_gym: Route):
        data = route_gym.request.post_data # Перехваченные данные
        if data:
            data = data.replace("User412", "Юзер")
        route_gym.continue_(post_data=data) # Команда, чтобы пробросить запрос дальше, иначе он зависнет

    """route ждет появления определенного запроса, останавливает его и отдает его нашему коду"""
    page.route(re.compile("profile/authenticate/"), change_request) # Ищем любой запрос, в URL которого есть "profile/authenticate/" и передает его в функцию change_request

    page.goto("https://gymlog.ru/profile/login/")
    page.locator("#email").fill("User412") # В devtools - id="email"
    page.locator("#password").fill("k9L-hL") # В devtools - id="password"
    page.get_by_role("button", name = "Войти").click() # (<button type = "submit" class ="...." > Войти < / button >)


# Запуск теста - pytest -v tests/test_change_traffic.py::test_change_response --headed
# ПОДМЕНА ТОГО, ЧТО НАМ ПРИСЫЛАЕТ СЕРВЕР
def test_change_response(page: Page):

    """change_response - функция, которая будет обрабатывать перехваченный ответ с сервера"""
    def change_response(route_gym: Route):
        response_gum = route_gym.fetch() # Перехватили, пробросили до сервера и полученный ответ записали в переменную response_gum
        data = (response_gum.text())
        data = data.replace("User412", "Андрей")
        route_gym.fulfill(response= response_gum, body = data) # Изменяем данные в body, и меняем их на то, что изменили в data


    """route ждет появления определенного запроса, останавливает его и отдает его нашему коду"""
    page.route(re.compile("profile/412/"), change_response) # Ищем любой запрос, в URL которого есть "profile/412/" и передает его в функцию change_response

    page.goto("https://gymlog.ru/profile/login/")
    page.locator("#email").fill("User412") # В devtools - id="email"
    page.locator("#password").fill("k9L-hL") # В devtools - id="password"
    page.get_by_role("button", name = "Войти").click() # (<button type = "submit" class ="...." > Войти < / button >)
    page.get_by_role("link", name="Мой профиль").click() # Решение, чтобы отработал перехват запроса - просто кликнуть на что угодно на странице
    sleep(5)
