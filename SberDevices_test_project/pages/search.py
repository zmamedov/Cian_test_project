import allure
from selene import browser, have, be


def click_on_search():
    browser.element('.digi-instant-search').should(be.visible).click()


def type_device_name(device_name):
    with allure.step(f'Ввести в поле поиска "{device_name}"'):
        browser.element('.digi-instant-search').type(device_name).press_enter()


def check_search_result():
    with allure.step('Название найденных товаров содержит "SberBoom"'):
        for device in browser.all('.digi-product__meta'):
            device.should(have.text('SberBoom'))

