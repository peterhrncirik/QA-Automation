from src.pages.homepage import HomePage

"""
    Test Case 7: Verify Test Case Page Loads Correctly
"""

def test_test_cases_page(driver):

    home_page = HomePage(driver)
    home_page.redirect_to('test_cases')

    assert '/test_cases' in driver.current_url