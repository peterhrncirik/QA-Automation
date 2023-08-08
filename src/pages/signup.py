from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .basepage import BasePage
from src.locators.locators import PreSignUpPageLocators, MainSignUpPageLocators, AccountCreatedPageLocators

class SignUp_FirstStep(BasePage):

    """
        Pre Sign-Up Page Object Model
    """

    def pre_signup_page_heading(self):
        return self.find_element(PreSignUpPageLocators.PRE_SIGNUP_PAGE_HEADING)

    def enter_email(self, email):
        self.wait_for(PreSignUpPageLocators.EMAIL_INPUT).clear()
        self.wait_for(PreSignUpPageLocators.EMAIL_INPUT).send_keys(email)

    def enter_username(self, username):
        self.wait_for(PreSignUpPageLocators.USERNAME_INPUT).clear()
        self.wait_for(PreSignUpPageLocators.USERNAME_INPUT).send_keys(username)
            
    def submit(self):
        self.find_element(PreSignUpPageLocators.SIGNUP_BUTTON).click()

    def check_successful_redirect(self):
        assert PreSignUpPageLocators.SIGNUP_URL in self.driver.current_url

    def error_message(self):
        return self.find_element(PreSignUpPageLocators.ERROR_MESSAGE)

class MainSignUp(BasePage):

    """
        Main Sign-up Page Object Model
    """

    def page_heading(self):
        return self.find_element(MainSignUpPageLocators.PAGE_HEADING)

    def select_title(self, title):

        match title:

            case 1:
                self.wait_for(MainSignUpPageLocators.TITLE_CHECKBOX_MR).click()

            case 2:
                self.wait_for(MainSignUpPageLocators.TITLE_CHECKBOX_MRS).click()

    def enter_name(self, name):

        # Is pre-filled from pre-sign-up
        self.wait_for(MainSignUpPageLocators.NAME_INPUT).clear()
        self.wait_for(MainSignUpPageLocators.NAME_INPUT).send_keys(name)

    def enter_email(self, email):

        # Is pre-filled from pre-sign-up
        self.wait_for(MainSignUpPageLocators.EMAIL_INPUT).clear()
        self.wait_for(MainSignUpPageLocators.EMAIL_INPUT).send_keys(email)

    def enter_password(self, password):
        self.wait_for(MainSignUpPageLocators.PASSWORD_INPUT).clear()
        self.wait_for(MainSignUpPageLocators.PASSWORD_INPUT).send_keys(password)

    def select_date_of_birth(self, day, month, year):

        day_dropdown = self.wait_for(MainSignUpPageLocators.DATE_OF_BIRTH_DAY_SELECT)
        month_dropdown = self.wait_for(MainSignUpPageLocators.DATE_OF_BIRTH_MONTH_SELECT)
        year_dropdown = self.wait_for(MainSignUpPageLocators.DATE_OF_BIRTH_YEAR_SELECT)

        select_day = Select(day_dropdown)
        select_month = Select(month_dropdown)
        select_year = Select(year_dropdown)

        select_day.select_by_value(day)
        select_month.select_by_value(month)
        select_year.select_by_value(year)

    def select_newsletter_option(self, newsletter=False):

        if newsletter:
            self.wait_for(MainSignUpPageLocators.NEWSLETTER_CHECKBOX).click()
    
    def select_special_offers(self, special_offers=False):

        if special_offers:
            self.wait_for(MainSignUpPageLocators.SPECIAL_OFFERS_CHECKBOX).click()

    def enter_first_name(self, first_name):
        self.wait_for(MainSignUpPageLocators.FIRST_NAME_INPUT).clear()
        self.wait_for(MainSignUpPageLocators.FIRST_NAME_INPUT).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.wait_for(MainSignUpPageLocators.LAST_NAME_INPUT).clear()
        self.wait_for(MainSignUpPageLocators.LAST_NAME_INPUT).send_keys(last_name)

    def enter_company(self, company):
        self.wait_for(MainSignUpPageLocators.COMPANY_INPUT).clear()
        self.wait_for(MainSignUpPageLocators.COMPANY_INPUT).send_keys(company)

    def enter_address_1(self, address):
        self.wait_for(MainSignUpPageLocators.ADDRESS_INPUT_1).clear()
        self.wait_for(MainSignUpPageLocators.ADDRESS_INPUT_1).send_keys(address)
    
    def enter_address_2(self, address):
        self.wait_for(MainSignUpPageLocators.ADDRESS_INPUT_2).clear()
        self.wait_for(MainSignUpPageLocators.ADDRESS_INPUT_2).send_keys(address)

    def select_country(self, country):

        country_dropdown = self.wait_for(MainSignUpPageLocators.COUNTRY_SELECT)
        country_select = Select(country_dropdown)
        country_select.select_by_visible_text(country)

    def enter_state(self, state):
        self.wait_for(MainSignUpPageLocators.STATE_INPUT).clear()
        self.wait_for(MainSignUpPageLocators.STATE_INPUT).send_keys(state)

    def enter_city(self, city):
        self.wait_for(MainSignUpPageLocators.CITY_INPUT).clear()
        self.wait_for(MainSignUpPageLocators.CITY_INPUT).send_keys(city)

    def enter_zipcode(self, zipcode):
        self.wait_for(MainSignUpPageLocators.ZIPCODE_INPUT).clear()
        self.wait_for(MainSignUpPageLocators.ZIPCODE_INPUT).send_keys(zipcode)

    def enter_mobile_number(self, mobile_number):
        self.wait_for(MainSignUpPageLocators.MOBILE_NUMBER_INPUT).clear()
        self.wait_for(MainSignUpPageLocators.MOBILE_NUMBER_INPUT).send_keys(mobile_number)

    def submit_form(self):
        self.find_element(MainSignUpPageLocators.CREATE_ACCOUNT_BUTTON).click()

class AccountCreated(BasePage):

    def page_heading(self):
        return self.find_element(AccountCreatedPageLocators.PAGE_HEADING)
      
    def click_on_continue_button(self):
        self.find_element(AccountCreatedPageLocators.CONTINUE_BUTTON).click()

    def check_user_logged_in(self):
        return self.wait_for(AccountCreatedPageLocators.LOGGED_IN_AS)

    def logout(self):
        self.wait_for(AccountCreatedPageLocators.LOGOUT_BUTTON).click()

    def delete_account(self):
        self.wait_for(AccountCreatedPageLocators.DELETE_ACCOUNT_BUTTON).click()

    def account_deleted_heading(self):
        return self.wait_for(AccountCreatedPageLocators.ACCOUNT_DELETED_HEADING)