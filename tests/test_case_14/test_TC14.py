from src.pages.productspage import ProductPage
from src.pages.homepage import HomePage
from src.pages.cartpage import CartPage
from src.pages.signup import SignUp_FirstStep, MainSignUp, AccountCreated
from src.pages.checkoutpage import CheckOutPage
from src.pages.paymentpage import PaymentPage

"""
    Test Cases 14: Place Order: Register During Checkout
"""

def test_register_during_checkout(driver, fake_user):

    home_page = HomePage(driver)

    # Add Products to Cart
    home_page.add_to_cart()

    # Redirect to Cart Page
    home_page.redirect_to('cart')
    cart_page = CartPage(driver)

    # Proceed to Checkout
    cart_page.proceed_to_checkout(with_modal=True)
    cart_page.redirect_to('login')

    # Do a pre-sign up
    pre_signup_page = SignUp_FirstStep(driver)
    pre_signup_page.redirect_to('signup')


    PRE_SIGNUP_PAGE_HEADING = 'New User Signup!'
    MAIN_SIGNUP_PAGE_HEADING = 'Enter Account Information'

    # Verify New User Signup! is visible
    pre_signup_page_heading = pre_signup_page.pre_signup_page_heading()
    assert pre_signup_page_heading.text.title() == PRE_SIGNUP_PAGE_HEADING

    pre_signup_page.enter_email(fake_user['email'])
    pre_signup_page.enter_username(fake_user['username'])
    pre_signup_page.submit()
    pre_signup_page.check_successful_redirect()

    # Main Sign Up
    main_signup_page = MainSignUp(driver)

    # Verify Enter Account Information Heading is visible
    page_heading_element = main_signup_page.page_heading()
    assert page_heading_element.text.title() == MAIN_SIGNUP_PAGE_HEADING
    
    # Fill Out Registration Form
    main_signup_page.select_title(fake_user['title'])
    main_signup_page.enter_password(fake_user['password'])
    main_signup_page.select_date_of_birth(fake_user['day'], fake_user['month'], fake_user['year'])
    main_signup_page.select_newsletter_option(fake_user['newsletter'])
    main_signup_page.select_special_offers(fake_user['special_offer'])
    main_signup_page.enter_first_name(fake_user['first_name'])
    main_signup_page.enter_last_name(fake_user['last_name'])
    main_signup_page.enter_company(fake_user['company'])
    main_signup_page.enter_address_1(fake_user['address1'])
    main_signup_page.select_country(fake_user['country'])
    main_signup_page.enter_state(fake_user['state'])
    main_signup_page.enter_city(fake_user['city'])
    main_signup_page.enter_zipcode(fake_user['zipcode'])
    main_signup_page.enter_mobile_number(fake_user['mobile_number'])
    
    # Submit
    main_signup_page.submit_form()

    # Account created, redirect
    account_created_page = AccountCreated(driver)
    page_heading_element = account_created_page.page_heading()
    assert page_heading_element.text.title() == 'Account Created!'

    # Click on Continue Button
    account_created_page.click_on_continue_button()

    # Logged-in

    # Verify 'Logged in as {username}' is visible
    logged_in_as_element = account_created_page.check_user_logged_in()
    assert logged_in_as_element.text == f'Logged in as {fake_user["username"]}'

    # Proceed to Checkout
    account_created_page.redirect_to('cart')
    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()

    # Check Out Page
    check_out_page = CheckOutPage(driver)

    # Verify Address Details
    delivery_address_details = check_out_page.get_delivery_address()

    # Get the title based on registration random choice
    person_title = 'Mr' if fake_user['title'] == 1 else 'Mrs'

    # Ensure delivery address matches user's details
    assert delivery_address_details['name'] == f"{person_title}. {fake_user['first_name']} {fake_user['last_name']}", 'Delivery - name does not match'
    assert delivery_address_details['company'] == fake_user['company'], 'Delivery - company does not match'
    assert delivery_address_details['address1'] == fake_user['address1'].replace('\n', ''), 'Delivery - address does not match'
    assert delivery_address_details['address2'] == f"{fake_user['city']} {fake_user['state']} {fake_user['zipcode']}", 'Delivery - address does not match'
    assert delivery_address_details['phone'] == fake_user['mobile_number'], 'Delivery - Phone does not match'

    # Enter Comment & Click Place Order
    check_out_page.add_comment(comment='Please hurry up! :)')
    check_out_page.place_order()

    # Enter Payment Details
    assert '/payment' in driver.current_url
    payment_page = PaymentPage(driver)
    payment_page.add_payment_details(
        name=f"{fake_user['first_name']} {fake_user['last_name']}",
        card_number=fake_user['credit_card_number'],
        cvc=fake_user['card_cvc'],
        expiration_month=fake_user['card_expiry'].split('/')[0],
        expiration_year=fake_user['card_expiry'].split('/')[1],
    )

    # Click Pay & Confirm Order Button
    confirmation_message = payment_page.pay_and_confirm()
    assert 'payment_done' in driver.current_url
    assert confirmation_message == 'Congratulations! Your order has been confirmed!'

    # Delete Account 
    payment_page.redirect_to('delete_account')
    assert '/delete_account' in driver.current_url



