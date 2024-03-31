import allure
from allure_commons.types import Severity

from sber_devices_test_project.pages.base_page import base_page
from sber_devices_test_project.pages.cart_page import cart_page
from sber_devices_test_project.pages.search_page import search_page


@allure.title('Add new device to the cart')
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'zmamedov')
@allure.feature('Cart')
@allure.story('Add product')
@allure.link('https://sberdevices.ru', name='SberDevices')
def test_add_product_to_cart():
    base_page.open_main_page()

    search_page.click_on_search()
    search_page.type_device_name('Sber')
    cart_page.add_device_to_cart()
    cart_page.open_cart()

    cart_page.check_count_devices_in_cart(count_devices=1)


@allure.title('Full clear of the cart')
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'zmamedov')
@allure.feature('Cart')
@allure.story('Clear cart')
@allure.link('https://sberdevices.ru', name='SberDevices')
def test_clear_cart():
    base_page.open_main_page()

    search_page.click_on_search()
    search_page.type_device_name('Sber')
    cart_page.add_device_to_cart()
    cart_page.open_cart()
    cart_page.clear_cart()

    cart_page.check_empty_cart()
