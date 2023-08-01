from selenium.webdriver.common.by import By
from .commonops import CommonOps

"""
    Sign Up Page Object Model
"""

class SignUp_FirstStep(CommonOps):

    PRE_SIGNUP_PAGE = (By.LINK_TEXT, 'Signup / Login')
    
    LOGIN_PAGE_URL = '/login'
    SIGNUP_URL = '/signup'

    EMAIL_INPUT = (By.XPATH, '//input[@data-qa="signup-email"]')
    USERNAME_INPUT = (By.XPATH, '//input[@data-qa="signup-name"]')

    SIGNUP_BUTTON = (By.XPATH, '//button[@data-qa="signup-button"]')

    def go_to_pre_signup_page(self):
        self.wait_for(self.PRE_SIGNUP_PAGE).click()
        assert self.LOGIN_PAGE_URL in self.driver.current_url

    def enter_email(self, email):
        self.wait_for(self.EMAIL_INPUT).clear()
        self.wait_for(self.EMAIL_INPUT).send_keys(email)

    def enter_username(self, username):
        self.wait_for(self.USERNAME_INPUT).clear()
        self.wait_for(self.USERNAME_INPUT).send_keys(username)
            
    def submit(self):
        self.find(self.SIGNUP_BUTTON).click()

    def check_successful_redirect(self):
        assert self.SIGNUP_URL in self.driver.current_url