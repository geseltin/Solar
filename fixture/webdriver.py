from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class Application:
    def __init__(self, base_page_url):
        self.base_page_url = base_page_url
        self.driver = self.make_web_driver()
        self.wait = WebDriverWait(self.driver, 10)

    def make_web_driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(self.base_page_url)
        return driver

