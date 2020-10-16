import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_valid_login(app):
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

    # enter login
    login_field = app.wait.until(EC.presence_of_element_located((By.ID, _login_field)))
    login_field.send_keys(_login)
    # enter password
    for i in _password:
        app.driver.find_element_by_id(_password_field).send_keys(i)
        time.sleep(1)
    # click login button
        app.driver.find_element_by_id(_login_button).click()

    app.wait.until(EC.presence_of_element_located((By.XPATH, _user_title)))
    actual_title = app.driver.title
    # check title
    assert _expected_title.lower() in actual_title.lower()
    time.sleep(3)




