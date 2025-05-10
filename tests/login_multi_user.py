import time
import pytest
from selenium.webdriver.common.by import By

# Sample user credentials
@pytest.mark.parametrize("username,password", [
    ("adming1", "123456"),        # valid credentials
    ("wronguser", "123456"),      # invalid username
    ("adming1", "wrongpass"),     # invalid password
    ("", ""),                     # empty credentials
])
def test_login_to_ems(driver, username, password):
    driver.get("https://ems-test.amaderit.net/")
    time.sleep(2)

    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[normalize-space()='Sign In']").click()
    time.sleep(3)

    # Checking if the login is successful or err is showing properly
    if username == "adming1" and password == "123456":
        assert "EMS : Administer/Dashboard" in driver.title, "Expected login success but failed."
    else:
        error_elements = driver.find_elements(By.CLASS_NAME, "alert")
        assert error_elements, "Expected an error message for invalid login, but didn't find one."