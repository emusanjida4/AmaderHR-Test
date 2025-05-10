import pytest

from pages.bank_page import BankNamePage

def test_bank_create(driver):
    bank_page = BankNamePage(driver)

    bank_page.open()
    bank_page.click_add_bank()
    bank_page.enter_bank_name("Meghna")
    bank_page.click_save()

    success_message = bank_page.get_success_message()
    assert "Bank Created Successfully" in success_message
