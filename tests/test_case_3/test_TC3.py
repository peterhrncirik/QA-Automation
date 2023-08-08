from src.pages.loginpage import LoginPage

from time import sleep

"""
    Test Case 3: Login User with Incorrect Email & Password
"""

def test_login_user_unsuccessful(driver, fake_user):

    ERROR_MESSAGE = 'Your email or password is incorrect!'

    login_page = LoginPage(driver)
    login_page.redirect_to('login')

    assert login_page.page_heading().text == 'Login to your account'

    login_page.enter_email(fake_user['email'])
    login_page.enter_password(fake_user['password'])

    login_page.submit()

    message_element = login_page.incorrect_login_error_message()
    assert message_element.text == ERROR_MESSAGE