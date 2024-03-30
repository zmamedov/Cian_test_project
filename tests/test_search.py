import allure
from allure_commons.types import Severity

from SberDevices_test_project.pages.base_page import open_main_page
from SberDevices_test_project.pages.search import click_on_search, type_device_name, check_search_result


@allure.title('Find device by title')
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'zmamedov')
@allure.feature('Search')
@allure.story('Find device')
@allure.link('https://sberdevices.ru', name='SberDevices')
def test_search():
    device_name = 'SberBoom'

    open_main_page()

    click_on_search()
    type_device_name(device_name)

    check_search_result()
