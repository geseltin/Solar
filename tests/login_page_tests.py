

def test_valid_login(app):

    # Credentials
    login = "administrator"
    password = "5ecr3t"

    app.loginPage.open_login_page()
    app.loginPage.enter_login(login)
    app.loginPage.enter_password(password)
    app.loginPage.click_login_button()
    app.loginPage.is_login_succesfull()


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


def test_invalid_password(app):
    # Credentials
    login = "Administrator"
    password = "Qwe12345"

    app.loginPage.is_login_page_presented()
    app.loginPage.clear_login_field()
    app.loginPage.clear_password_field()
    app.loginPage.enter_login(login)
    app.loginPage.enter_password(password)
    app.loginPage.is_login_error_presented()
    app.loginPage.is_login_error_presented()


def test_empty_fields(app):

    app.loginPage.open_login_page()
    app.loginPage.clear_login_field()
    app.loginPage.clear_password_field()
    app.loginPage.is_login_button_disabled()
