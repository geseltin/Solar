import pytest
from fixture.webdriver import WebDriverInstance


@pytest.fixture()
def webDriverInstance():
    fixture = WebDriverInstance()
    return fixture






