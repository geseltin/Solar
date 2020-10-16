import pytest
from fixture.webdriver import Application


@pytest.fixture(scope='session')
def app():
    application = Application(implicitly_wait_sec=10, base_page_url="http://10.201.48.146:8080/inrights/app/")
    return application


@pytest.fixture()
def print_info():
    print('Запускаю очередной тест')
