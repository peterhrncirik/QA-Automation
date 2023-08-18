from src.pages.productspage import ProductsPage, ProductPage
import random
from time import sleep

"""
    Test Case 9: Search Product
"""

def test_search_product(driver):

    PAGE_HEADING = 'ALL PRODUCTS'
    SEARCH_PAGE_HEADING = 'SEARCHED PRODUCTS'

    # List of Possible Products
    PRODUCTS = ['shirt', 'dress', 'top', 'short', 'jeans', 'tshirt', 'error']

    # Select Random Product for Search
    PRODUCT = random.choice(PRODUCTS)

    products_page = ProductsPage(driver)
    products_page.redirect_to('products')

    # Check Page Heading
    page_heading_element = products_page.page_heading()
    assert page_heading_element.text == PAGE_HEADING

    # Execute Search
    products_page.search_product(PRODUCT)

    # Check for Redirect & Correct Search URL
    assert f'/products?search={PRODUCT}' in driver.current_url 

    # Check Search Page Heading
    assert products_page.page_heading().text == SEARCH_PAGE_HEADING

    # Check Results
    products_list_element = products_page.get_products_list()

    match PRODUCT:
        case 'error':
            assert products_list_element is None, 'Searching for "error" still returns a result'
        case _:
            assert len(products_list_element) > 0, 'Searching does not return any product'


