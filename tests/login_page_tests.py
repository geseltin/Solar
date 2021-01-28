import time


def test_valid_login(app):

    # Credentials
    login = "administrator"
    password = "5ecr3t"

    app.loginPage.open_login_page()
    app.loginPage.enter_login(login)
    app.loginPage.enter_password(password)
    app.loginPage.click_login_button()
    app.loginPage.is_login_succesfull()

    time.sleep(3)


def test_invalid_login(app):

    # Credentials
    login = "oknysh_idm"
    password = "5ecr3t"

    app.loginPage.is_login_page_presented()
    app.loginPage.open_login_page()
    app.loginPage.clear_login_field()
    app.loginPage.clear_password_field()
    app.loginPage.enter_login(login)
    app.loginPage.enter_password(password)
    app.loginPage.click_login_button()
    app.loginPage.is_login_error_presented()

    time.sleep(3)


def test_invalid_password(app):
    # Credentials
    login = "Administrator"
    password = "Qwe12345"
    # Expected error message
    expected_error_message = "Извините, пользователя с таким логином и паролем найти не удалось. Попробуйте ещё раз."

    app.loginPage.is_login_page_presented()
    app.loginPage.clear_login_field()
    app.loginPage.clear_password_field()
    app.loginPage.enter_login(login)
    app.loginPage.enter_password(password)
    app.loginPage.is_login_error_presented()
    app.loginPage.is_login_error_presented()

    time.sleep(3)


def test_empty_fields(app):

    app.loginPage.open_login_page()
    app.loginPage.clear_login_field()
    app.loginPage.clear_password_field()
    app.loginPage.is_login_button_disabled()
