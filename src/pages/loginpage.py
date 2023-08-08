from .basepage import BasePage
from src.locators.locators import LoginPageLocators

"""
    Login Page Object Model
"""


class LoginPage(BasePage):

    def page_heading(self):
        return self.wait_for(LoginPageLocators.LOGIN_PAGE_HEADING)

    def enter_email(self, email):
        self.wait_for(LoginPageLocators.EMAIL_INPUT).clear()
        self.wait_for(LoginPageLocators.EMAIL_INPUT).send_keys(email)

    def enter_password(self, password):
        self.wait_for(LoginPageLocators.PASSWORD_INPUT).clear()
        self.wait_for(LoginPageLocators.PASSWORD_INPUT).send_keys(password)
            
    def submit(self):
        self.find_element(LoginPageLocators.SUBMIT_BUTTON).click()

    def incorrect_login_error_message(self):
        return self.wait_for(LoginPageLocators.ERROR_MESSAGE_LOCATOR)

    def check_user_logged_in(self):
        return self.wait_for(LoginPageLocators.LOGGED_IN_AS)

    def delete_account(self):
        self.wait_for(LoginPageLocators.DELETE_ACCOUNT_BUTTON).click()

    def account_deleted_heading(self):
        return self.wait_for(LoginPageLocators.ACCOUNT_DELETED_HEADING)

    def click_on_continue_button(self):
        self.find_element(LoginPageLocators.CONTINUE_BUTTON).click()