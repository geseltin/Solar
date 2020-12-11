from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import locators
import time


def test_valid_login(app):

    # Credentials
    login = "administrator"
    password = "5ecr3t"
    # Expected result
    expected_title = "Система управления полномочиями сотрудников | inRights"

    app.wait.until(EC.title_is("Вход в систему | inRights"))
    # app.wait.until(EC.presence_of_element_located((By.XPATH, locators.login_field))).clear()
    # app.wait.until(EC.presence_of_element_located((By.XPATH, locators.password_field))).clear()

    # enter login
    app.driver.find_element_by_xpath(locators.login_field).send_keys(login)

    # enter password
    for i in password:
        app.driver.find_element_by_xpath(locators.password_field).send_keys(i)
        time.sleep(0.5)
    # click login button
    app.driver.find_element_by_xpath(locators.login_button).click()

    app.wait.until(EC.presence_of_element_located((By.XPATH, locators.user_title_administrator)))
    actual_title = app.driver.title
    # check title
    assert expected_title.lower() == actual_title.lower()



def test_invalid_login(app):

    # Credentials
    login = "oknysh_idm"
    password = "5ecr3t"
    # Expected error message
    expected_error_message = "Извините, пользователя с таким логином и паролем найти не удалось. Попробуйте ещё раз."

    # Check if login page is presented
    actual_title = app.driver.title
    if actual_title.lower() != locators.login_page_title.lower():
        app.driver.find_element_by_xpath(locators.logout_button).click()
    else:
        return

    # Clearing fields
    app.driver.find_element_by_xpath(locators.login_field).clear()
    app.driver.find_element_by_xpath(locators.password_field).clear()

    # Entering wrong login
    app.driver.find_element_by_xpath(locators.login_field).send_keys(login)

    # enter password
    for i in password:
        app.driver.find_element_by_xpath(locators.password_field).send_keys(i)
        time.sleep(0.5)
    # click login button
    app.driver.find_element_by_xpath(locators.login_button).click()

    # Check result
    actual_result = app.driver.find_element_by_xpath(locators.error_field).text
    assert expected_error_message.lower() == actual_result.lower()
    time.sleep(3)


def test_invalid_password(app):
    # Credentials
    login = "Administrator"
    password = "Qwe12345"
    # Expected error message
    expected_error_message = "Извините, пользователя с таким логином и паролем найти не удалось. Попробуйте ещё раз."

    # Check if login page is presented
    actual_title = app.driver.title
    if actual_title.lower() != locators.login_page_title.lower():
        app.driver.find_element_by_xpath(locators.logout_button).click()

    # Clearing fields
    app.driver.find_element_by_xpath(locators.login_field).clear()
    app.driver.find_element_by_xpath(locators.password_field).clear()

    # Entering login
    app.driver.find_element_by_xpath(locators.login_field).send_keys(login)

    # Entering wrong password
    for i in password:
        app.driver.find_element_by_xpath(locators.password_field).send_keys(i)
        time.sleep(0.5)
    # click login button
    app.driver.find_element_by_xpath(locators.login_button).click()

    # Check result
    actual_result = app.driver.find_element_by_xpath(locators.error_field).text
    assert expected_error_message.lower() == actual_result.lower()
    time.sleep(3)


def test_empty_fields(app):
    # Wait for page load
    app.wait.until(EC.title_is("Вход в систему | inRights"))

    # Clearing fields
    app.driver.find_element_by_xpath(locators.login_field).clear()
    app.driver.find_element_by_xpath(locators.password_field).clear()

    # Check if login button is disabled
    login_button = app.driver.find_element_by_xpath(locators.login_button + '/..')
    print(str(login_button))
    attribute_value = login_button.get_attribute("aria-disabled")
    print(str(attribute_value))

    # Check attribute value
    if attribute_value == "false":
        button_state = False
    elif attribute_value == "true":
        button_state = True
    else:
        button_state = None

    assert button_state
