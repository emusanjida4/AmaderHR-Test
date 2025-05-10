import pytest
from utils.cookie_utils import save_cookies, load_cookies
@pytest.mark.cookie
@pytest.mark.usefixtures("driver")
def test_cookie_add_modify_delete(driver):
    """Test adding, modifying, and saving a cookie."""
    driver.get("https://amaderit.net/demo/hr/")

    # Add a cookie
    test_cookie = {'name': 'TestCookie', 'value': 'InitialValue'}
    driver.add_cookie(test_cookie)

    # Validate the cookie was added
    cookie = driver.get_cookie('TestCookie')
    assert cookie is not None and cookie['value'] == 'InitialValue', "Failed to add cookie"
    print(f"Added cookie: {cookie}")

    # Modify the cookie
    driver.delete_cookie('TestCookie')
    updated_cookie = {'name': 'TestCookie', 'value': 'UpdatedValue'}
    driver.add_cookie(updated_cookie)

    # Validate the cookie was updated
    modified = driver.get_cookie('TestCookie')
    assert modified is not None and modified['value'] == 'UpdatedValue', "Failed to update cookie"
    print(f"Updated cookie: {modified}")

    # Save cookies to file based on current browser
    browser_name = driver.capabilities.get("browserName", "unknown")
    save_cookies(driver, browser_name)
    print("Cookies saved to file.")

    # Remove the cookie to simulate a fresh session
    driver.delete_cookie("TestCookie")
    assert driver.get_cookie("TestCookie") is None, "Cookie deletion failed"
    print("Cookie deleted.")


@pytest.mark.usefixtures("driver")
def test_cookie_load(driver):
    """Test loading saved cookies and restoring session."""
    driver.get("https://amaderit.net/demo/hr/")

    # Load cookies based on browser
    browser_name = driver.capabilities.get("browserName", "unknown")
    load_cookies(driver, browser_name)

    # Reload to apply cookies to session
    driver.get("https://amaderit.net/demo/hr/degree")

    # Verify login persistence via cookie
    assert "AmaderHR" in driver.page_source, "Login not restored via cookies"
    print("Login restored via cookies.")
