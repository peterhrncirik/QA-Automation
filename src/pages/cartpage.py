from .basepage import BasePage
from ..locators.locators import CartPageLocators

class CartPage(BasePage):
    
    def enter_subscription_email(self, email):
        self.wait_for(CartPageLocators.SUBSCRIPTION_INPUT_FIELD).clear()
        self.wait_for(CartPageLocators.SUBSCRIPTION_INPUT_FIELD).send_keys(email)
        self.wait_for(CartPageLocators.SUBSCRIPTION_SUBMIT_BUTTON).click()

    def subscription_confirmation(self):
        return self.wait_for(CartPageLocators.SUBSCRIPTION_CONFIRMATION)
