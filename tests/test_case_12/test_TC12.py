from src.pages.productspage import ProductsPage
from src.pages.cartpage import CartPage
import random

from time import sleep

"""
    Test Cases 12: Add Products in Cart
"""

def test_adding_products_to_cart(driver, fake_user):

    products_page = ProductsPage(driver)
    products_page.redirect_to('products')

    all_products = products_page.get_products_list()

    # Randomly Select Products Between 1 - 6
    amount_to_insert_to_cart = random.randint(1, 6)

    # Add 2 Random Products to Cart
    products_page.add_to_cart(products_count=amount_to_insert_to_cart)

    # Redirect to Cart
    cart_page = CartPage(driver)
    cart_page.redirect_to('cart')

    # Verify Correct Products are in Cart
    products_in_cart = cart_page.check_products()

    # Check Correct Amount of Products in Cart
    assert len(products_in_cart) == amount_to_insert_to_cart

    for cart_product in products_in_cart:

        price, quantity, total_price = cart_product

        # Make Sure Calculated Total is Correct
        assert int(price) * int(quantity) == int(total_price)



