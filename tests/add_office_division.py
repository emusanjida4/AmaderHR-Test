import pytest

from pages.office_division_page import OfficeDivisionPage

def test_officedivision_create(driver):
    office_division_page = OfficeDivisionPage(driver)

    office_division_page.open()
    office_division_page.click_add_division()
    office_division_page.enter_division_name("Meghna")
    office_division_page.click_save()

    success_message = office_division_page.get_success_message()
    assert "Division Created Successfully" in success_message
