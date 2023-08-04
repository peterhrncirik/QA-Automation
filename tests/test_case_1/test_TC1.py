from faker import Faker
from src.pages.signup import SignUp_FirstStep, MainSignUp
import random
from time import sleep

"""
    Test Case 1: Register User
"""


def test_register_new_user(driver):

    # Initialize Faker for dummy data
    fake = Faker()

    TEST_EMAIL = fake.email()
    TEST_USERNAME = fake.user_name()
    TEST_FIRST_NAME = fake.first_name()
    TEST_LAST_NAME = fake.last_name()
    TEST_ADDRESS_1 = fake.address()
    TEST_PASSWORD = "password"
    TEST_TITLE = 1 # Select Mr. (1) or Mrs. (2) Title
    DAY, MONTH, YEAR = ['14', '5', '1976']
    TEST_NEWSLETTER = True
    TEST_SPECIAL_OFFERS = False
    TEST_COMPANY = 'Automation Inc.'
    TEST_COUNTRY = random.choice(['India', 'United States', 'Canada', 'Australia', 'Israel', 'New Zealand', 'Singapore'])
    TEST_STATE = fake.state()
    TEST_CITY = fake.city()
    TEST_ZIPCODE = fake.zipcode()
    TEST_MOBILE_NUMBER = fake.phone_number()

    # Do a pre-sign up
    pre_signup_page = SignUp_FirstStep(driver)
    pre_signup_page.go_to_pre_signup_page()
    pre_signup_page.enter_email(TEST_EMAIL)
    pre_signup_page.enter_username(TEST_USERNAME)
    pre_signup_page.submit()
    pre_signup_page.check_successful_redirect()

    # Main Sign Up
    main_signup_page = MainSignUp(driver)
    main_signup_page.select_title(TEST_TITLE)
    main_signup_page.enter_password(TEST_PASSWORD)
    main_signup_page.select_date_of_birth(DAY, MONTH, YEAR)
    main_signup_page.select_newsletter_option(TEST_NEWSLETTER)
    main_signup_page.select_special_offers(TEST_SPECIAL_OFFERS)
    main_signup_page.enter_first_name(TEST_FIRST_NAME)
    main_signup_page.enter_last_name(TEST_LAST_NAME)
    main_signup_page.enter_company(TEST_COMPANY)
    main_signup_page.enter_address_1(TEST_ADDRESS_1)
    # main_signup_page.select_country(TEST_COUNTRY)
    main_signup_page.enter_state(TEST_STATE)
    main_signup_page.enter_city(TEST_CITY)
    main_signup_page.enter_zipcode(TEST_ZIPCODE)
    main_signup_page.enter_mobile_number(TEST_MOBILE_NUMBER)
    sleep(19)