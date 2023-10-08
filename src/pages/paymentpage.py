from .basepage import BasePage
from ..locators.locators import PaymentPageLocators


class PaymentPage(BasePage):

    def add_payment_details(self, name, card_number, cvc, expiration_month, expiration_year):

        name_on_card_input = self.wait_for(PaymentPageLocators.NAME_ON_CARD)
        card_number_input = self.wait_for(PaymentPageLocators.CARD_NUMBER)
        cvc_input = self.wait_for(PaymentPageLocators.CVC)
        month_input = self.wait_for(PaymentPageLocators.MONTH)
        year_input = self.wait_for(PaymentPageLocators.YEAR)

        name_on_card_input.send_keys(name)
        card_number_input.send_keys(card_number)
        cvc_input.send_keys(cvc)
        month_input.send_keys(expiration_month)
        year_input.send_keys(expiration_year)

    def pay_and_confirm(self):

        self.wait_for(PaymentPageLocators.PAY_BUTTON).click()

        confirmation_message = self.wait_for(PaymentPageLocators.CONFIRMATION_MESSAGE).text

        return confirmation_message
