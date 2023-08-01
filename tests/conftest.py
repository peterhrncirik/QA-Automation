from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pytest

@pytest.fixture()
def driver():
    options = Options()
    # options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(1)
    driver.get('https://www.automationexercise.com/')

    title = driver.title
    assert title == 'Automation Exercise'

    yield driver
    
    driver.quit()