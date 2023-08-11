from src.pages.contactpage import ContactUsPage

"""
    Test Case 6: Contact Us Form
"""

def test_contact_us(driver, fake_user):

    contact_us_page = ContactUsPage(driver)
    contact_us_page.redirect_to('contact_us')

    page_heading_element = contact_us_page.page_heading()

    # Returns all h2s on page, select the second one by indexing [1]
    assert page_heading_element[1].text == 'GET IN TOUCH'

    # Fill out FOrm
    contact_us_page.enter_name(fake_user['first_name'])
    contact_us_page.enter_email(fake_user['email'])
    contact_us_page.enter_subject('Test subject')
    contact_us_page.enter_message('Test message')

    # Submit
    contact_us_page.submit()

    # Confirm Pop-up Alert
    contact_us_page.accept_alert()

    # Verify Success Message
    success_message_element = contact_us_page.success_message()
    assert success_message_element.text == 'Success! Your details have been submitted successfully.'

    # Click Home Button to Redirect Home
    contact_us_page.redirect_to_main_page()
    assert driver.title == 'Automation Exercise' 

