from .basepage import BasePage
from ..locators.locators import CheckOutPageLocators

from time import sleep

class CheckOutPage(BasePage):

    def get_delivery_address(self):

        address_element = self.wait_for_elements(CheckOutPageLocators.ADDRESS)

        address_details = {
            'name': address_element[1].text,
            'company': address_element[2].text,
            'address1': address_element[3].text,
            'address2': address_element[5].text,
            'country': address_element[6].text,
            'phone': address_element[7].text,
        }

        return address_details
    
    def add_comment(self, comment=None):

        if comment:
            self.wait_for(CheckOutPageLocators.COMMENT_AREA).click()
            self.wait_for(CheckOutPageLocators.COMMENT_AREA).send_keys(comment)
    
    def place_order(self):
        self.wait_for(CheckOutPageLocators.PLACE_ORDER_BUTTON).click()