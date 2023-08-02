from src.pages.loginpage import LoginPage

"""
    Test Login Functionality
"""

def test_incorrect_login(driver):

    TEST_EMAIL = 'test@email.com'
    TEST_PASSWORD = 'Password123'

    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.enter_email(TEST_EMAIL)
    login_page.enter_password(TEST_PASSWORD)
    login_page.submit()
    login_page.check_error_message()
    


