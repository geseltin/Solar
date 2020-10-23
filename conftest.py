import pytest
from fixture.webdriver import Application


@pytest.fixture(scope="session")
def app():
    application = Application(base_page_url="http://10.201.48.146:8080/inrights/app/")
    return application


