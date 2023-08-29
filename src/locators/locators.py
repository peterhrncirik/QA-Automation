from selenium.webdriver.common.by import By

"""
    Classes containing locators for specific pages
"""
class HomePageLocators:

    SUBSCRIPTION_INPUT_FIELD = (By.ID, 'susbscribe_email')
    SUBSCRIPTION_SUBMIT_BUTTON = (By.ID, 'subscribe')
    SUBSCRIPTION_CONFIRMATION = (By.ID, 'success-subscribe')

class CartPageLocators:

    # Find products based on partial ID (product-1, product-2, ...)
    PRODUCTS_LIST = (By.CSS_SELECTOR, 'tr[id*=product-]')
    PRODUCT_PRICE = (By.CLASS_NAME, 'cart_price')
    PRODUCT_QUANTITY = (By.CLASS_NAME, 'cart_quantity')
    PRODUCT_TOTAL = (By.CLASS_NAME, 'cart_total')

    SUBSCRIPTION_INPUT_FIELD = (By.ID, 'susbscribe_email')
    SUBSCRIPTION_SUBMIT_BUTTON = (By.ID, 'subscribe')
    SUBSCRIPTION_CONFIRMATION = (By.ID, 'success-subscribe')

class RedirectLocators:

    HOME = (By.LINK_TEXT, 'Home')
    PRODUCTS = (By.PARTIAL_LINK_TEXT, 'Products')
    CART = (By.LINK_TEXT, 'Cart')
    LOGIN_SIGNUP = (By.LINK_TEXT, 'Signup / Login')
    TEST_CASES = (By.LINK_TEXT, 'Test Cases')
    API_TESTING = (By.LINK_TEXT, 'API Testing')
    CONTACT_US = (By.LINK_TEXT, 'Contact us')

class LoginPageLocators:

    # First h2, can therefore use By.TAG_NAME
    LOGIN_PAGE_HEADING = (By.TAG_NAME, 'h2')

    LOGGED_IN_AS = (By.PARTIAL_LINK_TEXT, 'Logged in as')

    EMAIL_INPUT = (By.XPATH, '//input[@data-qa="login-email"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@data-qa="login-password"]')
    
    SUBMIT_BUTTON = (By.XPATH, '//button[@data-qa="login-button"]')
    LOGOUT_BUTTON = (By.LINK_TEXT, 'Logout')

    ERROR_MESSAGE_LOCATOR = (By.XPATH, '//p[@style="color: red;"]')
    ERROR_MESSAGE = 'Your email or password is incorrect!'

    DELETE_ACCOUNT_BUTTON = (By.LINK_TEXT, 'Delete Account')
    ACCOUNT_DELETED_HEADING = (By.TAG_NAME, 'h2')
    CONTINUE_BUTTON = (By.XPATH, '//a[@data-qa="continue-button"]')

class PreSignUpPageLocators:

    PRE_SIGNUP_PAGE = (By.LINK_TEXT, 'Signup / Login')

    PRE_SIGNUP_PAGE_HEADING = (By.XPATH, '/html/body/section/div/div/div[3]/div/h2')
    
    LOGIN_PAGE_URL = '/login'
    SIGNUP_URL = '/signup'

    EMAIL_INPUT = (By.XPATH, '//input[@data-qa="signup-email"]')
    USERNAME_INPUT = (By.XPATH, '//input[@data-qa="signup-name"]')

    ERROR_MESSAGE = (By.XPATH, '//p[@style="color: red;"]')
    SIGNUP_BUTTON = (By.XPATH, '//button[@data-qa="signup-button"]')

class MainSignUpPageLocators:

    # Using Tag name as it's the first h2 on the page
    PAGE_HEADING = (By.TAG_NAME, 'h2')

    TITLE_CHECKBOX_MR = (By.ID, 'id_gender1')
    TITLE_CHECKBOX_MRS = (By.ID, 'id_gender2')

    NAME_INPUT = (By.ID, 'name')
    EMAIL_INPUT = (By.ID, 'email')

    PASSWORD_INPUT = (By.ID, 'password')

    DATE_OF_BIRTH_DAY_SELECT = (By.ID, 'days')
    DATE_OF_BIRTH_MONTH_SELECT = (By.ID, 'months')
    DATE_OF_BIRTH_YEAR_SELECT = (By.ID, 'years')

    NEWSLETTER_CHECKBOX = (By.ID, 'newsletter')
    SPECIAL_OFFERS_CHECKBOX = (By.ID, 'optin')

    FIRST_NAME_INPUT = (By.ID, 'first_name')
    LAST_NAME_INPUT = (By.ID, 'last_name')
    COMPANY_INPUT = (By.ID, 'company')
    ADDRESS_INPUT_1 = (By.ID, 'address1')
    ADDRESS_INPUT_2 = (By.ID, 'address2')
    COUNTRY_SELECT = (By.ID, 'country')
    STATE_INPUT = (By.ID, 'state')
    CITY_INPUT = (By.ID, 'city')
    ZIPCODE_INPUT = (By.ID, 'zipcode')
    MOBILE_NUMBER_INPUT = (By.ID, 'mobile_number')

    CREATE_ACCOUNT_BUTTON = (By.XPATH, '//button[@data-qa="create-account"]')

class AccountCreatedPageLocators:

    PAGE_HEADING = (By.TAG_NAME, 'h2')
    CONTINUE_BUTTON = (By.XPATH, '//a[@data-qa="continue-button"]')
    LOGGED_IN_AS = (By.PARTIAL_LINK_TEXT, 'Logged in as')
    LOGOUT_BUTTON = (By.LINK_TEXT, 'Logout')
    DELETE_ACCOUNT_BUTTON = (By.LINK_TEXT, 'Delete Account')
    ACCOUNT_DELETED_HEADING = (By.TAG_NAME, 'h2')

class ContactUsPageLocators:

    PAGE_HEADINGS = (By.TAG_NAME, 'h2')
    NAME_FIELD = (By.XPATH, '//input[@data-qa="name"]')
    EMAIL_FIELD = (By.XPATH, '//input[@data-qa="email"]')
    SUBJECT_FIELD = (By.XPATH, '//input[@data-qa="subject"]')
    MESSAGE_FIELD = (By.XPATH, '//textarea[@data-qa="message"]')
    SUBMIT_BUTTON = (By.XPATH, '//input[@data-qa="submit-button"]')
    SUCCESS_MESSAGE = (By.CLASS_NAME, 'status')
    HOME_BUTTON = (By.CLASS_NAME, 'btn-success')

class ProductsPageLocators:

    PAGE_HEADING = (By.CLASS_NAME, 'title')
    PRODUCTS_LIST = (By.CLASS_NAME, 'single-products')
    VIEW_PRODUCT_BUTTON = (By.LINK_TEXT, 'View Product')
    PRODUCT_PRICE = (By.TAG_NAME, 'h2')
    SEARCH_INPUT = (By.ID, 'search_product')
    SEARCH_SUBMIT_BUTTON = (By.ID, 'submit_search')
    PRODUCTS_LIST_2 = (By.CLASS_NAME, f'productinfo')
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, f'add-to-cart')
    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, 'button[data-dismiss="modal"]')
    
class ProductPageLocators:

    NAME = (By.CSS_SELECTOR, '.product-information > h2')
    DETAILS = (By.CSS_SELECTOR, '.product-information > p')
    PRICE = (By.CSS_SELECTOR, '.product-information > span > span')