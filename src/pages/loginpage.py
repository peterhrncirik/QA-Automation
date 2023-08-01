from selenium.webdriver.common.by import By
from .commonops import CommonOps

"""
    Login Page Object Model
"""


class LoginPage(CommonOps):

    LOGIN_PAGE_LINK = (By.LINK_TEXT, 'Signup / Login')
    LOGIN_PAGE_URL = '/login'

    EMAIL_INPUT = (By.XPATH, '//input[@data-qa="login-email"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@data-qa="login-password"]')
    
    SUBMIT_BUTTON = (By.XPATH, '//button[@data-qa="login-button"]')

    ERROR_MESSAGE_LOCATOR = (By.XPATH, '//p[@style="color: red;"]')
    ERROR_MESSAGE = 'Your email or password is incorrect!'

    def go_to_login_page(self):
        self.wait_for(self.LOGIN_PAGE_LINK).click()
        assert self.LOGIN_PAGE_URL in self.driver.current_url

    def enter_email(self, email):
        self.wait_for(self.EMAIL_INPUT).clear()
        self.wait_for(self.EMAIL_INPUT).send_keys(email)

    def enter_password(self, password):
        self.wait_for(self.PASSWORD_INPUT).clear()
        self.wait_for(self.PASSWORD_INPUT).send_keys(password)
            
    def submit(self):
        self.find(self.SUBMIT_BUTTON).click()

    def check_error_message(self):
        error_message = self.wait_for(self.ERROR_MESSAGE_LOCATOR)
        assert error_message.text == self.ERROR_MESSAGE
