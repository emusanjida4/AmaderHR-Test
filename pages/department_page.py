from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class DepartmentPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_Department_button = (By.XPATH, "//a[normalize-space()='Add Department']")
        self.Department_name_input = (By.XPATH, "//input[@id='kt_maxlength_1']")
        self.save_button = (By.XPATH, "//button[normalize-space()='Save']")
        self.success_toast = (By.XPATH, "//div[@class='toast-message']")

    def open(self):
        self.driver.get("https://amaderit.net/demo/hr/department")

    def click_add_department(self):
        self.driver.find_element(*self.add_Department_button).click()

    def enter_department_name(self, name):
        self.driver.find_element(*self.Department_name_input).send_keys(name)

    def click_save(self):
        self.driver.find_element(*self.save_button).click()

    def get_success_message(self):
        return self.driver.wait.until(EC.visibility_of_element_located(self.success_toast)).text
