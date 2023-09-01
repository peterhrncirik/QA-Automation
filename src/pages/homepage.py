from .basepage import BasePage
from ..locators.locators import HomePageLocators

class HomePage(BasePage):
    
    def enter_subscription_email(self, email):
        self.wait_for(HomePageLocators.SUBSCRIPTION_INPUT_FIELD).clear()
        self.wait_for(HomePageLocators.SUBSCRIPTION_INPUT_FIELD).send_keys(email)
        self.wait_for(HomePageLocators.SUBSCRIPTION_SUBMIT_BUTTON).click()

    def subscription_confirmation(self):
        return self.wait_for(HomePageLocators.SUBSCRIPTION_CONFIRMATION)

    def view_product(self, product=0):
        views_product_links = self.wait_for_elements(HomePageLocators.VIEW_PRODUCT_BUTTON)
        views_product_links[product].click()