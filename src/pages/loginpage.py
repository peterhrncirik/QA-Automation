from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.link_to_login_page = (By.LINK_TEXT, 'Signup / Login')
        self.email_locator = (By.XPATH, '//input[@data-qa="login-email"]')
        self.password_locator = (By.XPATH, '//input[@data-qa="login-password"]')
        self.button_locator = (By.XPATH, '//button[@data-qa="login-button"]')

    def go_to_login_page(self):
        self.driver.find_element(*self.link_to_login_page).click()

    def enter_email(self, email):
        self.driver.find_element(*self.email_locator).clear()
        self.driver.find_element(*self.email_locator).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_locator).clear()
        self.driver.find_element(*self.password_locator).send_keys(password)
            
    def submit(self):
        self.driver.find_element(*self.button_locator).click()
