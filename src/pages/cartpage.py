from .basepage import BasePage
from ..locators.locators import CartPageLocators

from time import sleep

class CartPage(BasePage):
    
    def enter_subscription_email(self, email):
        self.wait_for(CartPageLocators.SUBSCRIPTION_INPUT_FIELD).clear()
        self.wait_for(CartPageLocators.SUBSCRIPTION_INPUT_FIELD).send_keys(email)
        self.wait_for(CartPageLocators.SUBSCRIPTION_SUBMIT_BUTTON).click()

    def subscription_confirmation(self):
        return self.wait_for(CartPageLocators.SUBSCRIPTION_CONFIRMATION)

    def check_products(self, products=None):

        products = self.wait_for_elements(CartPageLocators.PRODUCTS_LIST)
        products_list = []

        for product in products:

            price = product.find_element(*CartPageLocators.PRODUCT_PRICE)
            quantity = product.find_element(*CartPageLocators.PRODUCT_QUANTITY)
            total_price = product.find_element(*CartPageLocators.PRODUCT_TOTAL)

            _, amount = price.text.split()
            _, total = total_price.text.split()

            products_list.append([amount, quantity.text, total])

        return products_list

    def proceed_to_checkout(self, with_modal=False):
        self.wait_for(CartPageLocators.PROCEED_TO_CHECKOUT_BUTTON).click()


        # Close Checkout Modal
        if with_modal:
            sleep(.5)
            self.wait_for(CartPageLocators.CONTINUE_ON_CART_BUTTON).click()