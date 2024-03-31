import allure
from selene import browser, have, be


class SearchPage:
    def click_on_search(self):
        with allure.step(f'Кликнуть на поле поиска'):
            browser.element('.digi-instant-search').should(be.visible).click()

    def type_device_name(self, device_name):
        with allure.step(f'Ввести в поле поиска "{device_name}"'):
            browser.element('.digi-instant-search').set_value(device_name).press_enter()

    def check_search_result(self):
        with allure.step('Название первого товара содержит "SberBoom" в списке результатов'):
            browser.all('.digi-product__meta').first.should(have.text('SberBoom'))


search_page = SearchPage()
