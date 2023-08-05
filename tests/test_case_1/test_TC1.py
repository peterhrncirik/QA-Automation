from faker import Faker
from src.pages.signup import SignUp_FirstStep, MainSignUp, AccountCreated
import random
from time import sleep

"""
    Test Case 1: Register User
"""

def test_register_new_user(driver):

    """
        Test Data
    """

    # Initialize Faker for dummy data
    fake = Faker()

    PRE_SIGNUP_PAGE_HEADING = 'New User Signup!'
    MAIN_SIGNUP_PAGE_HEADING = 'Enter Account Information'
    TEST_EMAIL = fake.email()
    TEST_USERNAME = fake.user_name()
    TEST_FIRST_NAME = fake.first_name()
    TEST_LAST_NAME = fake.last_name()
    TEST_ADDRESS_1 = fake.address()
    TEST_PASSWORD = "password"
    TEST_TITLE = 1 # Select Mr. (1) or Mrs. (2) Title
    DAY, MONTH, YEAR = [str(random.randint(1, 31)), str(random.randint(1, 12)), str(random.randint(1900, 2021))]
    TEST_NEWSLETTER = True
    TEST_SPECIAL_OFFERS = True
    TEST_COMPANY = fake.company()
    TEST_COUNTRY = random.choice(['India', 'United States', 'Canada', 'Australia', 'Israel', 'New Zealand', 'Singapore'])
    TEST_STATE = fake.state()
    TEST_CITY = fake.city()
    TEST_ZIPCODE = fake.zipcode()
    TEST_MOBILE_NUMBER = fake.phone_number()
    ACCOUNT_CREATED_HEADING = 'Account Created!'
    ACCOUNT_DELETED_HEADING = 'Account Deleted!'

    """
        Start Test
    """

    # Do a pre-sign up
    pre_signup_page = SignUp_FirstStep(driver)
    pre_signup_page.go_to_pre_signup_page()

    # Verify New User Signup! is visible
    pre_signup_page_heading = pre_signup_page.pre_signup_page_heading()
    assert pre_signup_page_heading.text.title() == PRE_SIGNUP_PAGE_HEADING

    pre_signup_page.enter_email(TEST_EMAIL)
    pre_signup_page.enter_username(TEST_USERNAME)
    pre_signup_page.submit()
    pre_signup_page.check_successful_redirect()

    # Main Sign Up
    main_signup_page = MainSignUp(driver)

    # Verify Enter Account Information Heading is visible
    page_heading_element = main_signup_page.page_heading()
    assert page_heading_element.text.title() == MAIN_SIGNUP_PAGE_HEADING
    
    # Fill in Title
    main_signup_page.select_title(TEST_TITLE)

    # Fill in Password
    main_signup_page.enter_password(TEST_PASSWORD)

    # Fill in Date of Birth
    main_signup_page.select_date_of_birth(DAY, MONTH, YEAR)

    # Check Newsletter Option
    main_signup_page.select_newsletter_option(TEST_NEWSLETTER)

    # Check Special Offers Option
    main_signup_page.select_special_offers(TEST_SPECIAL_OFFERS)

    # Fill in First Name
    main_signup_page.enter_first_name(TEST_FIRST_NAME)

    # Fill in Last Name
    main_signup_page.enter_last_name(TEST_LAST_NAME)

    # Fill in Company
    main_signup_page.enter_company(TEST_COMPANY)

    # Fill in Address
    main_signup_page.enter_address_1(TEST_ADDRESS_1)

    # Select Country
    main_signup_page.select_country(TEST_COUNTRY)

    # Fill in State
    main_signup_page.enter_state(TEST_STATE)

    # Fill in City
    main_signup_page.enter_city(TEST_CITY)

    # Fill in ZipCode
    main_signup_page.enter_zipcode(TEST_ZIPCODE)

    # Fill in Mobile Number
    main_signup_page.enter_mobile_number(TEST_MOBILE_NUMBER)
    
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
    assert logged_in_as_element.text == f'Logged in as {TEST_USERNAME}'

    # Click on Delete Account
    account_created_page.delete_account()

    # Verify 'Account Deleted!' is visible 
    account_deleted_heading_element = account_created_page.page_heading()
    assert account_deleted_heading_element.text.title() == ACCOUNT_DELETED_HEADING

    # Click on Continue Button
    account_created_page.click_on_continue_button()
    

