from .basepage import BasePage
from ..locators.locators import HomePageLocators

from time import sleep

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

    def add_to_cart(self):
        add_to_cart = self.wait_for(HomePageLocators.ADD_TO_CART_BUTTON)
        add_to_cart.click()

        # Close Added! Modal
        sleep(.5)
        self.wait_for(HomePageLocators.CONTINUE_SHOPPING_BUTTON).click()