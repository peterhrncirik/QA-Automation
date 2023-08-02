from selenium.webdriver.common.by import By

"""
    Classes containing locators for specific pages
"""

class LoginPageLocators:

    LOGIN_PAGE_LINK = (By.LINK_TEXT, 'Signup / Login')
    LOGIN_PAGE_URL = '/login'

    EMAIL_INPUT = (By.XPATH, '//input[@data-qa="login-email"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@data-qa="login-password"]')
    
    SUBMIT_BUTTON = (By.XPATH, '//button[@data-qa="login-button"]')

    ERROR_MESSAGE_LOCATOR = (By.XPATH, '//p[@style="color: red;"]')
    ERROR_MESSAGE = 'Your email or password is incorrect!'