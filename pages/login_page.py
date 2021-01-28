import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage:
    login_field = "//input[@name='login']"
    password_field = "//input[@name='password']"
    login_button = "//a[1]/span[1]"  # //div[@id='button-1022-tooltipEl']
    user_title_administrator = "//span[contains(text(), 'administrator')]"
    main_page_title = "Система управления полномочиями сотрудников | inRights"
    login_page_title = "Вход в систему | inRights"
    error_field = "//label[contains(text()," \
                  "'Извините, пользователя с таким логином и паролем найти не удалось. Попробуйте ещё раз.')]"

    # Main page locator
    logout_button = "//a[@data-qtip='Выход']"

    def __init__(self, app):
        self.app = app

    def open_login_page(self):
        self.app.driver.get("http://10.201.48.88:8080/inrights/app/")
        self.app.wait.until(EC.title_is("Вход в систему | inRights"))

    def enter_login(self, login, locator=login_field):
        self.app.driver.find_element_by_xpath(locator).send_keys(login)

    def enter_password(self, password, locator=password_field):
        # Можно переделать в универсальный метод для посимвольного ввода

        for i in password:
            self.app.driver.find_element_by_xpath(locator).send_keys(i)
            time.sleep(0.5)

    def click_login_button(self, login_button=login_button):
        self.app.driver.find_element_by_xpath(login_button).click()

    def is_login_succesfull(self, user_title_administrator=user_title_administrator,main_page_title=main_page_title ):
        self.app.wait.until(EC.presence_of_element_located((By.XPATH, user_title_administrator)))
        actual_title = self.app.driver.title
        assert main_page_title.lower() == actual_title.lower()

    def clear_login_field(self, login_field=login_field):
        self.app.driver.find_element_by_xpath(login_field).clear()

    def clear_password_field(self, password_field=password_field):
        self.app.driver.find_element_by_xpath(password_field).clear()

    def is_login_page_presented(self, login_page_title=login_page_title, logout_button=logout_button):
        actual_title = self.app.driver.title
        if actual_title.lower() != login_page_title.lower():
            self.app.driver.find_element_by_xpath(logout_button).click()
        else:
            return

    def is_login_error_presented(self, error_field=error_field):
        expected_error_message = "Извините, пользователя с таким логином и паролем найти не удалось. Попробуйте ещё раз."
        actual_result = self.app.driver.find_element_by_xpath(error_field).text
        assert expected_error_message.lower() == actual_result.lower()

    def is_login_button_disabled(self, login_button=login_button):
        login_button = self.app.driver.find_element_by_xpath(login_button + '/..')
        attribute_value = login_button.get_attribute("aria-disabled")
        if attribute_value == "false":
            button_state = False
        else:
            button_state = True

        assert button_state
