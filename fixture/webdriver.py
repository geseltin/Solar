from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

class WebDriverInstance():

    # Locators
    _login_field = "textfield-1017-inputEl"
    _password_field = "textfield-1018-inputEl"
    _login_button = "button-1022-btnInnerEl"
    _user_title = "//a[1]/span[@role='presentation']/span[@role='presentation']/span[contains(text(), 'administrator')]"
    # Credentials
    _login = "administrator"
    _password = "5ecr3t"
    # Expected result
    _expected_title = "Система управления полномочиями сотрудников | inRights"

    def test_login(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        wait = WebDriverWait(driver, 10)
        driver.get("http://10.201.48.146:8080/inrights/app/")
        login_field = wait.until(EC.presence_of_element_located((By.ID, self._login_field)))
        login_field.send_keys(self._login)

        for i in self._password:
            driver.find_element_by_id(self._password_field).send_keys(i)
            time.sleep(1)
        driver.find_element_by_id(self._login_button).click()

        wait.until(EC.presence_of_element_located((By.XPATH, self._user_title)))
        actualTitle = driver.title

        assert self._expected_title.lower() in actualTitle.lower()
        time.sleep(3)


cc = WebDriverFactory()
cc.test_login()