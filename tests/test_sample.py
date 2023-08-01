from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

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

def test_login():
    driver.find_element(By.LINK_TEXT, 'Signup / Login').click()
    driver.find_element(By.XPATH, '//input[@data-qa="login-email"]').send_keys('test@email.com')
    driver.find_element(By.XPATH, '//input[@data-qa="login-password"]').send_keys('123Password')
    driver.find_element(By.XPATH, '//button[@data-qa="login-button"]').click()
    error_message = wait.until(EC.visibility_of_element_located((By.XPATH, '//p[@style="color: red;"]')))
    assert 'Your email or password is incorrect!' in error_message.text

def test_teardown():
    driver.close()
    driver.quit()