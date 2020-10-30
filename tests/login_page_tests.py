from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import locators
import time


def test_valid_login(app):

    # Credentials
    _login = "administrator"
    _password = "5ecr3t"
    # Expected result
    _expected_title = "Система управления полномочиями сотрудников | inRights"

    # Clearing fields
    app.wait.until(EC.presence_of_element_located((By.XPATH, locators._login_field))).clear()
    app.wait.until(EC.presence_of_element_located((By.XPATH, locators._password_field))).clear()

    # enter login
    app.wait.until(EC.presence_of_element_located((By.XPATH, locators._login_field))).send_keys(_login)

    # enter password
    for i in _password:
        app.driver.find_element_by_xpath(locators._password_field).send_keys(i)
        time.sleep(0.5)
    # click login button
    app.driver.find_element_by_xpath(locators._login_button).click()

    app.wait.until(EC.presence_of_element_located((By.XPATH, locators._user_title_administrator)))
    actual_title = app.driver.title
    # check title
    assert _expected_title.lower() in actual_title.lower()
    time.sleep(3)


def test_invalid_login(app):

    # Credentials
    _login = "oknysh_idm"
    _password = "5ecr3t"
    # Expected error message
    _expected_error_message = "Извините, пользователя с таким логином и паролем найти не удалось. Попробуйте ещё раз."

    # Check if login page is presented
    actual_title = app.driver.title
    if actual_title.lower() != locators._login_page_title.lower():
        app.driver.find_element_by_xpath(locators._logout_button).click()

    # Clearing fields
    app.wait.until(EC.presence_of_element_located((By.XPATH, locators._login_field))).clear()
    app.wait.until(EC.presence_of_element_located((By.XPATH, locators._password_field))).clear()

    # Entering wrong login
    app.wait.until(EC.presence_of_element_located((By.XPATH, locators._login_field))).send_keys(_login)

    # enter password
    for i in _password:
        app.driver.find_element_by_xpath(locators._password_field).send_keys(i)
        time.sleep(0.5)
    # click login button
    app.driver.find_element_by_xpath(locators._login_button).click()

    # Check result
    actual_result = app.driver.find_element_by_xpath(locators._error_field).text
    assert _expected_error_message.lower() in actual_result.lower()
    time.sleep(3)


def test_invalid_password(app):
    # Credentials
    _login = "Administrator"
    _password = "Qwe12345"
    # Expected error message
    _expected_error_message = "Извините, пользователя с таким логином и паролем найти не удалось. Попробуйте ещё раз."

    # Check if login page is presented
    actual_title = app.driver.title
    if actual_title.lower() != locators._login_page_title.lower():
        app.driver.find_element_by_xpath(locators._logout_button).click()

    # Clearing fields
    app.wait.until(EC.presence_of_element_located((By.XPATH, locators._login_field))).clear()
    app.wait.until(EC.presence_of_element_located((By.XPATH, locators._password_field))).clear()

    # Entering login
    app.wait.until(EC.presence_of_element_located((By.XPATH, locators._login_field))).send_keys(_login)

    # Entering wrong password
    for i in _password:
        app.driver.find_element_by_xpath(locators._password_field).send_keys(i)
        time.sleep(0.5)
    # click login button
    app.driver.find_element_by_xpath(locators._login_button).click()

    # Check result
    actual_result = app.driver.find_element_by_xpath(locators._error_field).text
    assert _expected_error_message.lower() in actual_result.lower()
    time.sleep(3)


def test_empty_fields(app):
    # Check if login page is presented
    actual_title = app.driver.title
    if actual_title.lower() != locators._login_page_title.lower():
        app.driver.find_element_by_xpath(locators._logout_button).click()

    # Check if login button is disabled
    element_state = app.wait.until(EC.element_to_be_clickable((By.XPATH, locators._login_button)))
    assert element_state
