import pytest

from pages.division_page import DivisionPage

@pytest.mark.ui
@pytest.mark.division
def test_division_create(driver):
    division_page = DivisionPage(driver)

    division_page.open()
    division_page.click_add_division()
    division_page.enter_division_name("Ajdfb5498eb")
    division_page.click_save()

    success_message = division_page.get_success_message()
    assert "Division Created Successfully" in success_message
