from src.pages.productspage import ProductsPage, ProductPage

from time import sleep

"""
    Test Case 8: Verify All Products & Product Detail Page
"""

def test_products_page(driver):

    PAGE_HEADING = 'ALL PRODUCTS'
    PRODUCT_DETAIL_URL = '/product_details/'

    products_page = ProductsPage(driver)
    products_page.redirect_to('products')

    # Check Page Heading
    page_heading_element = products_page.page_heading()
    assert page_heading_element.text == PAGE_HEADING

    # Check Products List
    products_list_element = products_page.get_products_list()
    # Check if length > 0, meaning a product is displayed on the page
    assert len(products_list_element) > 0, 'No product is visible'

    # Check First Product
    # product=0 as in First Item in the List
    products_page.view_product(product=0)

    # Check Correct Redirect
    assert PRODUCT_DETAIL_URL in driver.current_url

    # Initialize new POM - Product Page
    product_page = ProductPage(driver)

    # Check Product Detail Page - Visibility of Various Elements

    # product_details() method returns list of <p> tags, unpack with specific element
    category, availability, condition, brand = product_page.product_details()

    assert category.is_displayed(), 'Product Category not Displayed'
    assert availability.is_displayed(), 'Product Availabity not Displayed'
    assert condition.is_displayed(), 'Product Condition not Displayed'
    assert brand.is_displayed(), 'Product Brand not Displayed'

    assert product_page.product_name().is_displayed(), 'Product Name not Displayed'
    assert product_page.product_price().is_displayed(), 'Product Price not Displayed'
