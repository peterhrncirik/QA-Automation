from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

from src.pages.loginpage import LoginPage

import pytest

@pytest.fixture()
def test_setup():
    global driver, wait
    options = Options()
    # options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(1)
    wait = WebDriverWait(driver, 5)
    driver.get('https://www.automationexercise.com/')
    title = driver.title
    assert title == 'Automation Exercise'
    yield
    driver.close()
    driver.quit()

def test_incorrect_login(test_setup):
    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.enter_email('test@lalala.com')
    login_page.enter_password('MyPassword123')
    login_page.submit()
    
    error_message = wait.until(EC.visibility_of_element_located((By.XPATH, '//p[@style="color: red;"]')))
    assert 'Your email or password is incorrect!' in error_message.text


