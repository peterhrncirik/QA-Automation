from src.pages.loginpage import LoginPage

"""
    Test Login Functionality
"""

def test_incorrect_login(driver):
    
    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.enter_email('test@lalala.com')
    login_page.enter_password('MyPassword123')
    login_page.submit()
    login_page.check_error_message()
    


