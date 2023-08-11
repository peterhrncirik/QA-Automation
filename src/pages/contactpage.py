from .basepage import BasePage
from src.locators.locators import ContactUsPageLocators

"""
    Contact Us Page Object Model
"""

class ContactUsPage(BasePage):

    def page_heading(self):
        # Returns all h2s on page
        return self.wait_for_elements(ContactUsPageLocators.PAGE_HEADINGS)
    
    def enter_name(self, name):
        self.wait_for(ContactUsPageLocators.NAME_FIELD).clear()
        self.wait_for(ContactUsPageLocators.NAME_FIELD).send_keys(name)

    def enter_email(self, email):
        self.wait_for(ContactUsPageLocators.EMAIL_FIELD).clear()
        self.wait_for(ContactUsPageLocators.EMAIL_FIELD).send_keys(email)

    def enter_subject(self, subject):
        self.wait_for(ContactUsPageLocators.SUBJECT_FIELD).clear()
        self.wait_for(ContactUsPageLocators.SUBJECT_FIELD).send_keys(subject)

    def enter_message(self, message):
        self.wait_for(ContactUsPageLocators.MESSAGE_FIELD).clear()
        self.wait_for(ContactUsPageLocators.MESSAGE_FIELD).send_keys(message)

    def upload_file(self, file):
        pass

    def submit(self):
        self.wait_for(ContactUsPageLocators.SUBMIT_BUTTON).click()

    def redirect_to_main_page(self):
        self.wait_for(ContactUsPageLocators.HOME_BUTTON).click()

    def success_message(self):
        return self.wait_for(ContactUsPageLocators.SUCCESS_MESSAGE)