from src.pages.loginpage import LoginPage

from time import sleep

"""
    Test Case 4: Log-out user
"""

def test_login_and_logout_user(driver, working_login):

    login_page = LoginPage(driver)
    login_page.redirect_to('login')

    assert login_page.page_heading().text == 'Login to your account'

    login_page.enter_email(working_login['email'])
    login_page.enter_password(working_login['password'])

    login_page.submit()

    # Verify 'Logged in as {username}' is visible
    logged_in_as_element = login_page.check_user_logged_in()
    assert logged_in_as_element.text == f'Logged in as {working_login["username"]}'

    # Log-out
    login_page.logout()

    # Verify user is redirected to /login page
    assert '/login' in driver.current_url

