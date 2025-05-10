import pytest

from pages.department_page import DepartmentPage


def test_department_create(driver):
    department_page =DepartmentPage(driver)

    department_page.open()
    department_page.click_add_department()
    department_page.enter_department_name("Meghna")
    department_page.click_save()

    success_message = department_page.get_success_message()
    assert "Department Created Successfully" in success_message
