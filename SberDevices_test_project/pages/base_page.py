import allure
from selene import browser, have, be


def open_main_page():
    with allure.step('Открыть главную страницу магазина "SberDevices"'):
        browser.open('/')


def button_for_shopping_is_visible():
    with allure.step('Кнопка "За покупками" отображается на главноей странице'):
        browser.element('.sc-921013a8-4').should(have.text('За покупками'))


def switch_on_tab_installment():
    with allure.step('Нажать на вкладку "Рассрочка"'):
        browser.all('.sc-e64983b4-4').second.click()


def check_installment_title():
    with allure.step('Проверить заголовок вкладки'):
        browser.element('.sc-c0a896f4-4').should(have.exact_text('Рассрочка'))


def click_on_search():
    browser.element('.digi-instant-search').should(be.visible).click()


def type_device_name(device_name):
    with allure.step(f'Ввести в поле поиска {device_name}'):
        browser.element('.digi-instant-search').type(device_name).press_enter()


def check_search_result():
    with allure.step('В результатах поиска присутствует товар "Умная колонка SberBoom"'):
        browser.all('.sc-921013a8-4').element_by(have.exact_text('Умная колонка SberBoom'))
