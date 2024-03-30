import allure
from allure_commons.types import Severity

from SberDevices_test_project.pages.base_page import open_main_page
from SberDevices_test_project.pages.cart import (add_device_to_cart, open_cart, check_count_devices_in_cart,
                                                 clear_cart, check_empty_cart)
from SberDevices_test_project.pages.search import click_on_search, type_device_name


@allure.title('Add new device to the cart')
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'zmamedov')
@allure.feature('Cart')
@allure.story('Add product')
@allure.link('https://sberdevices.ru', name='SberDevices')
def test_add_product_to_cart():
    open_main_page()

    click_on_search()
    type_device_name('Sber')
    add_device_to_cart()
    open_cart()

    check_count_devices_in_cart(count_devices=1)


@allure.title('Full clear of the cart')
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'zmamedov')
@allure.feature('Cart')
@allure.story('Clear cart')
@allure.link('https://sberdevices.ru', name='SberDevices')
def test_clear_cart():
    open_main_page()

    click_on_search()
    type_device_name('Sber')
    add_device_to_cart()
    open_cart()
    clear_cart()

    check_empty_cart()
