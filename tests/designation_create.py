import pytest

from pages.bank_page import BankNamePage
from pages.designation_page import DesignationPage


def test_designation_create(driver):
    designation_page = DesignationPage(driver)

    designation_page.open()
    designation_page.click_add_designation()
    designation_page.enter_designation_name("Head")
    designation_page.click_save()

    success_message = designation_page.get_success_message()
    assert "Designation Created Successfully" in success_message
