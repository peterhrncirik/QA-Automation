from src.pages.loginpage import LoginPage
from src.pages.signup import SignUp_FirstStep, MainSignUp, AccountCreated
import pytest

from time import sleep

"""
    Test Case 2: Login User with Correct Email & Password
"""

@pytest.fixture()
def test_register_new_user(driver, fake_user):

    """
        Test Data
    """

    PRE_SIGNUP_PAGE_HEADING = 'New User Signup!'
    MAIN_SIGNUP_PAGE_HEADING = 'Enter Account Information'
    ACCOUNT_CREATED_HEADING = 'Account Created!'
    ACCOUNT_DELETED_HEADING = 'Account Deleted!'

    """
        Start Test
    """

    # Do a pre-sign up
    pre_signup_page = SignUp_FirstStep(driver)
    pre_signup_page.redirect_to('signup')

    # Verify New User Signup! is visible
    pre_signup_page_heading = pre_signup_page.pre_signup_page_heading()
    assert pre_signup_page_heading.text.title() == PRE_SIGNUP_PAGE_HEADING

    pre_signup_page.enter_email(fake_user['email'])
    pre_signup_page.enter_username(fake_user['username'])
    pre_signup_page.submit()
    pre_signup_page.check_successful_redirect()

    # Main Sign Up
    main_signup_page = MainSignUp(driver)

    # Verify Enter Account Information Heading is visible
    page_heading_element = main_signup_page.page_heading()
    assert page_heading_element.text.title() == MAIN_SIGNUP_PAGE_HEADING
    
    # Fill in Title
    main_signup_page.select_title(fake_user['title'])

    # Fill in Password
    main_signup_page.enter_password(fake_user['password'])

    # Fill in Date of Birth
    main_signup_page.select_date_of_birth(fake_user['day'], fake_user['month'], fake_user['year'])

    # Check Newsletter Option
    main_signup_page.select_newsletter_option(fake_user['newsletter'])

    # Check Special Offers Option
    main_signup_page.select_special_offers(fake_user['special_offer'])

    # Fill in First Name
    main_signup_page.enter_first_name(fake_user['first_name'])

    # Fill in Last Name
    main_signup_page.enter_last_name(fake_user['last_name'])

    # Fill in Company
    main_signup_page.enter_company(fake_user['company'])

    # Fill in Address
    main_signup_page.enter_address_1(fake_user['address1'])

    # Select Country
    main_signup_page.select_country(fake_user['country'])

    # Fill in State
    main_signup_page.enter_state(fake_user['state'])

    # Fill in City
    main_signup_page.enter_city(fake_user['city'])

    # Fill in ZipCode
    main_signup_page.enter_zipcode(fake_user['zipcode'])

    # Fill in Mobile Number
    main_signup_page.enter_mobile_number(fake_user['mobile_number'])
    
    # Submit
    main_signup_page.submit_form()

    # Account created, redirect
    account_created_page = AccountCreated(driver)
    page_heading_element = account_created_page.page_heading()
    assert page_heading_element.text.title() == ACCOUNT_CREATED_HEADING

    # Click on Continue Button
    account_created_page.click_on_continue_button()

    # Logged-in

    # Verify 'Logged in as {username}' is visible
    logged_in_as_element = account_created_page.check_user_logged_in()
    assert logged_in_as_element.text == f'Logged in as {fake_user["username"]}'

    # Log-out
    account_created_page.logout()

    new_user = {
        'username': fake_user['username'],
        'email': fake_user['email'],
        'password': fake_user['password']
    }

    return new_user


def test_login_user_successful(driver, test_register_new_user):

    login_page = LoginPage(driver)
    login_page.redirect_to('login')

    assert login_page.page_heading().text == 'Login to your account'

    login_page.enter_email(test_register_new_user['email'])
    login_page.enter_password(test_register_new_user['password'])

    login_page.submit()

    logged_in_as_element = login_page.check_user_logged_in()
    assert logged_in_as_element.text == f'Logged in as {test_register_new_user["username"]}'

    login_page.delete_account()
    
    # Verify 'Account Deleted!' is visible 
    account_deleted_heading_element = login_page.account_deleted_heading()
    assert account_deleted_heading_element.text.title() == 'Account Deleted!'

    # Click on Continue Button
    login_page.click_on_continue_button()
    