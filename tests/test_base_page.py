import allure
from allure_commons.types import Severity

from SberDevices_test_project.pages.base_page import open_main_page, button_for_shopping_is_visible, \
    switch_on_tab_installment, check_installment_title


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

    check_installment_title()
