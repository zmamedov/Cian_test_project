import allure
from selene import browser, have


class CartPage:

    def add_device_to_cart(self):
        with allure.step('Добавить в корзину первый товар'):
            browser.all('.digi-product__button').first.click()

    def open_cart(self):
        with allure.step('Открыть корзину'):
            browser.element('.sites-components__sc-1g65x4x-1').click()

    def check_count_devices_in_cart(self, count_devices):
        with allure.step(f'В корзине ровно {count_devices} товар'):
            browser.element('.text-x32').should(have.exact_text(f'В корзине {count_devices} товар'))

    def clear_cart(self):
        with allure.step(f'Нажать на иконку очистки корзины'):
            browser.element('[data-testid="buttonDelete"]').click()

    def check_empty_cart(self):
        with allure.step('Корзина пустая'):
            browser.element('.text-x32').should(have.exact_text('В корзине пока пусто'))


cart_page = CartPage()
