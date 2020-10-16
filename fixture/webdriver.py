from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Application:
    def __init__(self, implicitly_wait_sec, base_page_url):
        self.implicitly_wait_sec = implicitly_wait_sec
        self.base_page_url = base_page_url
        self.driver = self.make_web_driver()
        self.wait = WebDriverWait(self.driver, 10)

    def make_web_driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(self.implicitly_wait_sec)
        driver.get(self.base_page_url)
        return driver
