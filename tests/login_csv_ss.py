import csv
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def load_login_data_from_csv(filepath):
    data = []
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append((row["username"], row["password"]))
    return data


@pytest.mark.parametrize("username,password", load_login_data_from_csv("data/login_data.csv"))
def test_login_to_ems(driver, username, password):
    driver.get("https://ems-test.amaderit.net/")

    wait = WebDriverWait(driver, 10)

    # Wait for input fields to load
    wait.until(EC.presence_of_element_located((By.ID, "username")))
    wait.until(EC.presence_of_element_located((By.ID, "password")))

    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)

    # Click login button
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Sign In']")))
    login_button.click()

    # Validate outcome
    #if username == "adming1" and password == "123456":
     #   assert "EMS : Administer/Dashboard" in driver.title, "Expected dashboard URL on successful login"
   # else:
 #       error_elements = driver.find_elements(By.CLASS_NAME, "alert")
  #      assert error_elements, "Expected error message for invalid login"