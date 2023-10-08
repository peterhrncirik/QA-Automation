from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert

from src.locators.locators import RedirectLocators
from src import settings

class BasePage:

    """
     Class containing shared functionality for all pages
    """

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, settings.WAIT_TIME)
        self._action = ActionChains(self.driver)

    def wait_for(self, locator):
        return self._wait.until(EC.presence_of_element_located(locator))
    
    def wait_for_element_to_be_clickable(self, locator):
        return self._wait.until(EC.element_to_be_clickable(locator))

    def wait_for_elements(self, locator):
        return self._wait.until(EC.presence_of_all_elements_located(locator))
    
    def find_element(self, locator):

        # return self.driver.find_element(*locator)
        # Rewriting to WebDriverWait with exception handling

        try:
            return self._wait.until(EC.presence_of_element_located(locator))
        except NoSuchElementException as e:
            print(f'Element with {locator[0]} of {locator[1]} not found', e)

    def context_click(self, element):

        """
            Context click executes right click / context menu click
        """

        return self._action.context_click(element)

    def accept_alert(self):
        alert = self._wait.until(EC.alert_is_present())
        alert.accept()
    
    def get_page_title(self):
        return self.driver.title
    
    def redirect_to(self, to_page):
        
        address = None
        url = None

        match to_page:
            case 'home':
                address = RedirectLocators.HOME
                url = '/'
            case 'products':
                address = RedirectLocators.PRODUCTS
                url = '/products'
            case 'cart':
                address = RedirectLocators.CART
                url = '/view_cart'
            case 'signup':
                address = RedirectLocators.LOGIN_SIGNUP
                url = '/login'
            case 'login':
                address = RedirectLocators.LOGIN_SIGNUP
                url = '/login'
            case 'test_cases':
                address = RedirectLocators.TEST_CASES
                url = '/test_cases'
            case 'contact_us':
                address = RedirectLocators.CONTACT_US
                url = '/contact_us'
            case 'delete_account':
                address = RedirectLocators.DELETE_ACCOUNT
                url = '/delete_account'

        self.wait_for(address).click()
        assert url in self.driver.current_url