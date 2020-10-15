from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait


def test_valid_login(webDriverInstance):
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

    driver = webDriverInstance.getWebDriverInstance()
    wait = WebDriverWait(driver, 10)

    # enter login
    login_field = wait.until(EC.presence_of_element_located((By.ID, _login_field)))
    login_field.send_keys(_login)
    # enter password
    for i in _password:
        driver.find_element_by_id(_password_field).send_keys(i)
        time.sleep(1)
    # click login button
    driver.find_element_by_id(_login_button).click()

    wait.until(EC.presence_of_element_located((By.XPATH, _user_title)))
    actualTitle = driver.title
    # check title
    assert _expected_title.lower() in actualTitle.lower()
    time.sleep(3)




