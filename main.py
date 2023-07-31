from selenium import webdriver
from selenium.webdriver.common.by import By


"""
 Basic Driver Configuration
"""

driver = webdriver.Firefox()
driver.get('https://www.automationexercise.com/')

title = driver.title
assert title == 'Automation Exercise'

driver.implicitly_wait(1)