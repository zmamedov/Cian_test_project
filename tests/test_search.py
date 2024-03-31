import allure
from allure_commons.types import Severity

from sber_devices_test_project.pages.base_page import base_page
from sber_devices_test_project.pages.search_page import search_page


@allure.title('Find device by title')
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'zmamedov')
@allure.feature('Search')
@allure.story('Find device')
@allure.link('https://sberdevices.ru', name='SberDevices')
def test_search():
    device_name = 'SberBoom'

    base_page.open_main_page()

    search_page.click_on_search()
    search_page.type_device_name(device_name)

    search_page.check_search_result()
