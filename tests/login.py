import time
from selenium.webdriver.common.by import By



    # Check if login is successful
def test_login_to_parabank(driver):
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    driver.find_element(By.NAME, "username").send_keys("shihab05")
    driver.find_element(By.NAME, "password").send_keys("shihab1254@")


    driver.find_element(By.XPATH, "//input[@value='Log In']").click()
