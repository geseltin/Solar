from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def test_valid_login(app):
    # Locators
    _login_field = "//input[@name='login']"
    _password_field = "//input[@name='password']"
    _login_button = "//a[1]/span[1]"
    _user_title = "//span[contains(text(), 'administrator')]"
    # Credentials
    _login = "administrator"
    _password = "5ecr3t"
    # Expected result
    _expected_title = "Система управления полномочиями сотрудников | inRights"

    # enter login
    app.wait.until(EC.presence_of_element_located((By.XPATH, _login_field))).send_keys(_login)

    # enter password
    for i in _password:
        app.driver.find_element_by_xpath(_password_field).send_keys(i)
        time.sleep(0.5)
    # click login button
    app.driver.find_element_by_xpath(_login_button).click()

    app.wait.until(EC.presence_of_element_located((By.XPATH, _user_title)))
    actual_title = app.driver.title
    # check title
    assert _expected_title.lower() in actual_title.lower()
    time.sleep(3)




