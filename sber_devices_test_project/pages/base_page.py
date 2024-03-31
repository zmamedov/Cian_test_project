import allure
from selene import browser, have


class BasePage:

    def open_main_page(self):
        with allure.step('Открыть главную страницу магазина "SberDevices"'):
            browser.open('/')

    def button_for_shopping_is_visible(self):
        with allure.step('Кнопка "За покупками" отображается на главноей странице'):
            browser.element('.sc-921013a8-4').should(have.text('За покупками'))

    def switch_on_tab_installment(self):
        with allure.step('Нажать на вкладку "Рассрочка"'):
            browser.all('.sc-e64983b4-4').second.click()

    def check_installment_title(self):
        with allure.step('Проверить заголовок вкладки'):
            browser.element('.sc-c0a896f4-4').should(have.exact_text('Рассрочка'))


base_page = BasePage()
