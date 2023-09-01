from src.pages.productspage import ProductPage
from src.pages.homepage import HomePage
from src.pages.cartpage import CartPage


"""
    Test Cases 13: Verify Quantity in Cart
"""

def test_quantity_in_cart(driver):

    INCREASE_QUANTITY_AMOUNT = 4

    home_page = HomePage(driver)

    # View the First Product
    home_page.view_product()

    # Redirects to Product Detail
    product_page = ProductPage(driver)
    assert '/product_details/' in driver.current_url

    # Increase Quantity 
    product_page.change_quantity(INCREASE_QUANTITY_AMOUNT)

    # Add to Cart & Redirect to Cart
    product_page.add_to_cart()
    product_page.redirect_to('cart')

    # Cart Page
    cart_page = CartPage(driver)
    products_in_cart = cart_page.check_products()

    for cart_product in products_in_cart:

        price, quantity, total_price = cart_product

        assert int(quantity) == INCREASE_QUANTITY_AMOUNT



