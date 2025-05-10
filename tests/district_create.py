import pytest

from pages.district_page import DistrictPage

def test_district_create(driver):
    district_page = DistrictPage(driver)

    district_page.open()
    district_page.click_add_district()
    district_page.enter_district_name("Meghna")
    district_page.click_save()

    success_message = district_page.get_success_message()
    assert "District Created Successfully" in success_message
