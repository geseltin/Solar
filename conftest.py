import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    application = Application(base_page_url="http://10.201.48.88:8080/inrights/app/")
    request.addfinalizer(application.close_browser)
    return application
