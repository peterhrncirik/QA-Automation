from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

"""
    Base Page Object Model
    Defines basic functionality for every page that inherits from Base Page
"""

class BasePage():

    def __init__(self, driver, base_url='https://www.automationexercise.com/'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        return self.driver.find_element(*locator)
    
    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def get_title(self):
        return self.driver.title
    
    def get_url(self):
        return self.driver.current_url
    
    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print(f'Element not Found (TimeOutException) -> {locator[1]}')
            self.driver.quit()
