from .basepage import BasePage
from src.locators.locators import ProductsPageLocators, ProductPageLocators
import random
from time import sleep

"""
    Products & Single Product Page Object Model
"""

class ProductsPage(BasePage):

    def page_heading(self):
        return self.wait_for(ProductsPageLocators.PAGE_HEADING)

    def get_products_list(self):

        try:
            return self.wait_for_elements(ProductsPageLocators.PRODUCTS_LIST)
        except:
            # Return None when doing Search and there is nothing found
            return None

    def view_product(self, product=0):
        views_product_links = self.wait_for_elements(ProductsPageLocators.VIEW_PRODUCT_BUTTON)
        views_product_links[product].click()

    def search_product(self, product):
        self.wait_for(ProductsPageLocators.SEARCH_INPUT).clear()
        self.wait_for(ProductsPageLocators.SEARCH_INPUT).send_keys(product)
        self.wait_for(ProductsPageLocators.SEARCH_SUBMIT_BUTTON).click()

    def add_to_cart(self, products_count=2):

        # Get all products
        products_elements = self.wait_for_elements(ProductsPageLocators.PRODUCTS_LIST_2)
        products_prices = []

        # Randomly Add 1-6 Products into Cart
        for product in random.sample(products_elements, products_count):


            price = product.find_element(*ProductsPageLocators.PRODUCT_PRICE)
            products_prices.append(price)

            add_to_cart = product.find_element(*ProductsPageLocators.ADD_TO_CART_BUTTON)

            add_to_cart.click()

            # Click Continue Shopping Button
            continue_shopping_button = self.wait_for(ProductsPageLocators.CONTINUE_SHOPPING_BUTTON)
            sleep(.5)
            continue_shopping_button.click()
            
        
        return products_prices
    


class ProductPage(BasePage):

    def product_name(self):
        return self.wait_for(ProductPageLocators.NAME)

    def product_details(self):
        # Returns all <p> tags, which are Category, Availability, Condition, Brand
        return self.wait_for_elements(ProductPageLocators.DETAILS)

    def product_price(self):
        return self.wait_for(ProductPageLocators.PRICE)
    

