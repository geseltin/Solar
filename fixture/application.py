from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.login_page import LoginPage
from pages.main_page import MainPage


class Application:
    def __init__(self, base_page_url):
        self.base_page_url = base_page_url
        self.driver = self.make_web_driver()
        self.loginPage = LoginPage(self)
        self.mainPage = MainPage(self)
        self.wait = WebDriverWait(self.driver, 15)

    def make_web_driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(self.base_page_url)
        return driver

    def close_browser(self):
        self.driver.quit()

