import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage:

    user_title_administrator = "//span[contains(text(), 'administrator')]"
    main_page_title = "Система управления полномочиями сотрудников | inRights"
    login_page_title = "Вход в систему | inRights"
    error_field = "//label[contains(text()," \
                  "'Извините, пользователя с таким логином и паролем найти не удалось. Попробуйте ещё раз.')]"

    # Main page locator
    logout_button = "//a[@data-qtip='Выход']"

    def __init__(self, app):
        self.app = app
        self._elements = Elements(self.app)

    def open_login_page(self):
        self.app.driver.get("http://10.201.48.88:8080/inrights/app/")
        self.app.wait.until(EC.title_is("Вход в систему | inRights"))

    def enter_login(self, login):
        self._elements.login_field.send_keys(login)
        # self.app.driver.find_element_by_xpath(locator).send_keys(login)

    def enter_password(self, password):
        # Можно переделать в универсальный метод для посимвольного ввода

        for i in password:
            self._elements.password_field.send_keys(i)
            time.sleep(0.5)

    def click_login_button(self):
        self._elements.login_button.click()
        # self.app.driver.find_element_by_xpath(login_button).click()

    def is_login_succesfull(self, user_title_administrator=user_title_administrator,main_page_title=main_page_title ):
        self.app.wait.until(EC.presence_of_element_located((By.XPATH, user_title_administrator)))
        actual_title = self.app.driver.title
        assert main_page_title.lower() == actual_title.lower()

    def clear_login_field(self):
        self._elements.login_field.clear()
        # self.app.driver.find_element_by_xpath(login_field).clear()

    def clear_password_field(self):
        self._elements.password_field.clear()
        # self.app.driver.find_element_by_xpath(password_field).clear()

    # def is_login_page_presented(self, login_page_title=login_page_title, logout_button=logout_button):
    #     actual_title = self.app.driver.title
    #     if actual_title.lower() != login_page_title.lower():
    #         self.app.driver.find_element_by_xpath(logout_button).click()
    #     else:
    #         return

    def is_login_error_presented(self, error_field=error_field):
        expected_error_message = "Извините, пользователя с таким логином и паролем найти не удалось. Попробуйте ещё раз."
        actual_result = self.app.driver.find_element_by_xpath(error_field).text
        assert expected_error_message.lower() == actual_result.lower()

    def is_login_button_disabled(self):
        # login_button = self._elemeself.app.driver.find_element_by_xpath(login_button + '/..')
        attribute_value = self._elements.login_button.get_attribute("aria-disabled")
        if attribute_value == "false":
            button_state = False
        else:
            button_state = True

        assert button_state

class Elements:

    def __init__(self, app):
        self.app = app

    @property
    def login_field(self):
        login_field_locator = "//input[@name='login']"
        return self.app.driver.find_element_by_xpath(login_field_locator)

    @property
    def password_field(self):
        password_field_locator = "//input[@name='password']"
        return self.app.driver.find_element_by_xpath(password_field_locator)

    @property
    def login_button(self):
        login_button_locator = "//div[@class='x-box-inner']//a[1]"  # "//a[1]/span[1]"  # //div[@id='button-1022-tooltipEl']
        return self.app.driver.find_element_by_xpath(login_button_locator)

