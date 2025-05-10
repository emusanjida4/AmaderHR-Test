import pytest

from pages.institute_page   import InstitutePage



def test_institute_create(driver):
    institute_page = InstitutePage(driver)

    institute_page.open()
    institute_page.click_add_institute()
    institute_page.enter_institute_name("IUBAT1")
    institute_page.click_save()

    success_message = institute_page.get_success_message()
    assert "Institute Created Successfully" in success_message
