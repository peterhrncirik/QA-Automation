from src.pages.signup import SignUp_FirstStep

from time import sleep

"""
    Test Case 5: Register User with Existing E-mail
"""

def test_register_user_existing_email(driver, working_login):

    PRE_SIGNUP_PAGE_HEADING = 'New User Signup!'
    ERROR_MESSAGE = 'Email Address already exist!'

    # Do a pre-sign up
    pre_signup_page = SignUp_FirstStep(driver)
    pre_signup_page.redirect_to('signup')

    # Verify New User Signup! is visible
    pre_signup_page_heading = pre_signup_page.pre_signup_page_heading()
    assert pre_signup_page_heading.text.title() == PRE_SIGNUP_PAGE_HEADING

    pre_signup_page.enter_email(working_login['email'])
    pre_signup_page.enter_username(working_login['username'])
    pre_signup_page.submit()
    
    # Check Error Message
    error_message_element = pre_signup_page.error_message()
    assert error_message_element.text == ERROR_MESSAGE