import allure
from allure_commons.types import Severity
from selene import browser, have


@allure.title('Открыть главную страницу "SberDevices"')
@allure.id("1001")
@allure.issue("issue")
@allure.testcase("testcase")
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "zmamedov")
@allure.feature("Issues в репозитории")
@allure.story("Просмотр Issues в репозитории")
@allure.link("https://sberdevices.ru", name="Testing")
def test_open_main_page():
    with allure.step('Открыть главную страницу магазина "SberDevices"'):
        browser.open('/')

    with allure.step('Проверить, что на главной странице есть кнопка "За покупками"'):
        browser.element('.sc-921013a8-4').should(have.text('За покупками'))


@allure.title('Проверить поле поиска')
@allure.id("1002")
@allure.issue("issue")
@allure.testcase("testcase")
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "zmamedov")
@allure.feature("Issues в репозитории")
@allure.story("Просмотр Issues в репозитории")
@allure.link("https://sberdevices.ru", name="Testing")
def test_search():
    with allure.step('Открыть главную страницу магазина "SberDevices"'):
        browser.open('/')

    with allure.step('Ввести в поле поиска "SberBoom"'):
        browser.element('.digi-instant-search').click().type('SberBoom').press_enter()

    with allure.step('В результатах поиска присутствует товар "Умная колонка SberBoom"'):
        browser.all('.sc-921013a8-4').element_by(have.exact_text('Умная колонка SberBoom'))


@allure.title('Открыть вкладку "Рассрочка"')
@allure.id("1001")
@allure.issue("issue")
@allure.testcase("testcase")
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "zmamedov")
@allure.feature("Issues в репозитории")
@allure.story("Просмотр Issues в репозитории")
@allure.link("https://sberdevices.ru", name="Testing")
def test_open_tab_installment():
    with allure.step('Открыть главную страницу магазина "SberDevices"'):
        browser.open('/')

    with allure.step('Нажать на вкладку "Рассрочка"'):
        browser.all('.sc-e64983b4-4').second.click()

    with allure.step('В открывшейся странице есть надпись "Рассрочка"'):
        browser.element('.sc-c0a896f4-4').should(have.exact_text('Рассрочка'))


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
