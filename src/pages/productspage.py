from .basepage import BasePage
from src.locators.locators import ProductsPageLocators, ProductPageLocators

"""
    Products & Single Product Page Object Model
"""

class ProductsPage(BasePage):

    def page_heading(self):
        return self.wait_for(ProductsPageLocators.PAGE_HEADINGS)

    def get_products_list(self):
        return self.wait_for_elements(ProductsPageLocators.PRODUCTS_LIST)

    def view_product(self, product=0):
        views_product_links = self.wait_for_elements(ProductsPageLocators.VIEW_PRODUCT_BUTTON)
        views_product_links[product].click()

class ProductPage(BasePage):

    def product_name(self):
        return self.wait_for(ProductPageLocators.NAME)

    def product_details(self):
        # Returns all <p> tags, which are Category, Availability, Condition, Brand
        return self.wait_for_elements(ProductPageLocators.DETAILS)

    def product_price(self):
        return self.wait_for(ProductPageLocators.PRICE)

