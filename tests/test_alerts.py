# ПРОВЕРКА ВСПЛЫВАЮЩИХ АЛЕРТОВ
from time import sleep

from playwright.sync_api import Page, expect, Dialog


# Запуск теста - pytest tests/test_alerts.py::test_alert --headed
def test_alert(page: Page):
    """Принудительное ожидание алерта и нажатие на него"""
    page.goto("https://demoblaze.com/")

    """Функция по принятию алерта"""
    def accept_alert(alert: Dialog): # Говорим, что alert является представителем класса Dialog
        print(alert.message) # Печатаем текст из алерта
        alert.accept() # Принимаем алерт

    page.on("dialog", accept_alert)  # Когда будет диалог, т.е. алерт, то выполним функцию accept_alert по его принятию
    page.get_by_role("link", name="Samsung galaxy s6").click()  # В devtools - <a href="....">Samsung galaxy s6</a>
    page.get_by_role("link", name="Add to cart").click()  # В devtools - <a href="..." class="btn btn-success btn-lg">Add to cart</a>
    page.wait_for_event("dialog") # Принудительное ожидание появления диалога - т.е. алерта
    page.locator("#cartur").click()  # В devtools - <a class="nav-link" href="cart.html" id="cartur">Cart</a>


