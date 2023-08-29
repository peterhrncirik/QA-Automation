from src.pages.homepage import HomePage
from src.pages.cartpage import CartPage

"""
    Test Cases 10 & 11: Verify Subscription on Home Page & Cart Page
"""

def test_subscription_home_page(driver, fake_user):

    home_page = HomePage(driver)

    home_page.enter_subscription_email(fake_user['email'])

    confirmation_element = home_page.subscription_confirmation()

    assert confirmation_element.text == 'You have been successfully subscribed!'

def test_subscription_cart_page(driver, fake_user):

    cart_page = CartPage(driver)
    cart_page.redirect_to('cart')

    cart_page.enter_subscription_email(fake_user['email'])

    confirmation_element = cart_page.subscription_confirmation()

    assert confirmation_element.text == 'You have been successfully subscribed!'


