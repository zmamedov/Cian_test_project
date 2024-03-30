import allure
from selene import browser, have, be


def click_on_search():
    with allure.step(f'Кликнуть на поле поиска'):
        browser.element('.digi-instant-search').should(be.visible).click()


def type_device_name(device_name):
    with allure.step(f'Ввести в поле поиска "{device_name}"'):
        browser.element('.digi-instant-search').set_value(device_name).press_enter()


def check_search_result():
    with allure.step('Название первого товара содержит "SberBoom" в списке результатов'):
        browser.all('.digi-product__meta').first.should(have.text('SberBoom'))
