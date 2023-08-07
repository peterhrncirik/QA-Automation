from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from faker import Faker
import random
import pytest

@pytest.fixture()
def driver():
    options = Options()
    # options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    driver.install_addon('ublock.xpi')
    driver.implicitly_wait(1)
    driver.get('https://www.automationexercise.com/')

    title = driver.title
    assert title == 'Automation Exercise'

    yield driver
    
    driver.quit()

@pytest.fixture()
def fake_user():

    fake = Faker()

    fake_user = {
        'username': fake.user_name(),
        'email': fake.email(),
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'address1': fake.address(),
        'password': fake.password(),
        'title': random.randint(1, 2),
        'day': str(random.randint(1, 31)),
        'month': str(random.randint(1, 12)),
        'year': str(random.randint(1900, 2021)),
        'newsletter': bool(random.getrandbits(1)),
        'special_offer': bool(random.getrandbits(1)),
        'company': fake.company(),
        'country': random.choice(['India', 'United States', 'Canada', 'Australia', 'Israel', 'New Zealand', 'Singapore']),
        'state': fake.state(),
        'city': fake.city(),
        'zipcode': fake.zipcode(),
        'mobile_number': fake.phone_number(),
    }


    yield fake_user

@pytest.fixture()
def fake_user_for_deletion():

    pass