from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

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

    def alert(self):
        return self._wait.until(EC.alert_is_present())
    
    def get_page_title(self):
        return self.driver.title