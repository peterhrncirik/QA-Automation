from .basepage import BasePage
from src.locators.locators import LoginPageLocators

"""
    Login Page Object Model
"""


class LoginPage(BasePage):

    def enter_email(self, email):
        self.wait_for(LoginPageLocators.EMAIL_INPUT).clear()
        self.wait_for(LoginPageLocators.EMAIL_INPUT).send_keys(email)

    def enter_password(self, password):
        self.wait_for(LoginPageLocators.PASSWORD_INPUT).clear()
        self.wait_for(LoginPageLocators.PASSWORD_INPUT).send_keys(password)
            
    def submit(self):
        self.find_element(LoginPageLocators.SUBMIT_BUTTON).click()

    def check_error_message(self):
        error_message = self.wait_for(LoginPageLocators.ERROR_MESSAGE_LOCATOR)
        assert error_message.text == LoginPageLocators.ERROR_MESSAGE
