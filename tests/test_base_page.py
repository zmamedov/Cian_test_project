import allure
from allure_commons.types import Severity
from selene import browser, have

from SberDevices_test_project.pages.base_page import open_main_page, button_for_shopping_is_visible, \
    switch_on_tab_installment


@allure.title('Open main page of "SberDevices"')
@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'zmamedov')
@allure.feature('Main Page')
@allure.story('Open main page')
@allure.link('https://sberdevices.ru', name='SberDevices')
def test_open_main_page():
    open_main_page()

    button_for_shopping_is_visible()


@allure.title('Go to the tab "Installment"')
@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'zmamedov')
@allure.feature('Main Page')
@allure.story('Open tab "Installment"')
@allure.link('https://sberdevices.ru', name='SberDevices')
def test_switch_on_tab_installment():
    open_main_page()

    switch_on_tab_installment()


@allure.title('Добавить товар в корзину')
@allure.id("1001")
@allure.issue("issue")
@allure.testcase("testcase")
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "zmamedov")
@allure.feature("Issues в репозитории")
@allure.story("Просмотр Issues в репозитории")
@allure.link("https://sberdevices.ru", name="Testing")
def test_add_product_to_cart():
    with allure.step('Открыть главную страницу магазина "SberDevices"'):
        browser.open('/')

    with allure.step('Добавить в корзину 1 товар'):
        browser.element('.digi-instant-search').click().type('Sber').press_enter()
        browser.all('.digi-product__button').first.click()
        browser.element('.sites-components__sc-1g65x4x-1').click()
        browser.element('.text-x32').should(have.exact_text('В корзине 1 товар'))


@allure.title('Очистка корзины')
@allure.id("1001")
@allure.issue("issue")
@allure.testcase("testcase")
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "zmamedov")
@allure.feature("Issues в репозитории")
@allure.story("Просмотр Issues в репозитории")
@allure.link("https://sberdevices.ru", name="Testing")
def test_clear_cart():
    with allure.step('Открыть главную страницу магазина "SberDevices"'):
        browser.open('/')

    with allure.step('Добавить в корзину 1 товар'):
        browser.element('.digi-instant-search').click().type('Sber').press_enter()
        browser.all('.digi-product__button').first.click()
        browser.element('.sites-components__sc-1g65x4x-1').click()

    with allure.step('Добавить в корзину 1 товар'):
        browser.element('[data-testid="buttonDelete"]').click()
        browser.element('.text-x32').should(have.exact_text('В корзине пока пусто'))
