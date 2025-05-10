from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class DivisionPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_division_button = (By.XPATH, "//a[normalize-space()='Add Division']")
        self.division_name_input = (By.XPATH, "//input[@placeholder='Enter division name here']")
        self.save_button = (By.XPATH, "//button[normalize-space()='Save']")
        self.success_toast = (By.XPATH, "//div[@class='toast toast-success']")

    def open(self):
        self.driver.get("https://amaderit.net/demo/hr/division")

    def click_add_division(self):
        self.driver.find_element(*self.add_division_button).click()

    def enter_division_name(self, name):
        self.driver.find_element(*self.division_name_input).send_keys(name)

    def click_save(self):
        self.driver.find_element(*self.save_button).click()

    def get_success_message(self):
        return self.driver.wait.until(EC.visibility_of_element_located(self.success_toast)).text
