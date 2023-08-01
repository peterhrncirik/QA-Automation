from src.pages.signup import SignUp_FirstStep

"""
    Test Sign Up Functionality
"""

def test_pre_sign_up(driver):

    login_page = SignUp_FirstStep(driver)
    login_page.go_to_pre_signup_page()
    login_page.enter_email('test@lalala.com')
    login_page.enter_username('MyPassword123')
    login_page.submit()
    login_page.check_successful_redirect()