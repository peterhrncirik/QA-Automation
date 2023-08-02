from src.pages.signup import SignUp_FirstStep, MainSignUp

"""
    Test Sign Up Functionality
"""

def test_pre_sign_up(driver):

    TEST_EMAIL = 'test@email1.com'
    TEST_USERNAME = 'Tester'

    pre_signup_page = SignUp_FirstStep(driver)
    pre_signup_page.go_to_pre_signup_page()
    pre_signup_page.enter_email(TEST_EMAIL)
    pre_signup_page.enter_username(TEST_USERNAME)
    pre_signup_page.submit()
    pre_signup_page.check_successful_redirect()

def test_main_sign_up(driver):

    pass