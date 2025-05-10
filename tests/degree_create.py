import pytest

from pages.degree_page import DegreePage

@pytest.mark.ui
@pytest.mark.degree
def test_degree_create(driver):
    degree_page = DegreePage(driver)

    degree_page.open()
    degree_page.click_add_degree()
    degree_page.enter_degree_name("SQA_IUBAT3")
    degree_page.click_save()

    success_message = degree_page.get_success_message()
    assert "Degree Created Successfully" in success_message
