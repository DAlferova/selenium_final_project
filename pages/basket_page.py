"""

"""
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_header()
        self.should_not_be_add_to_basket_button()

    def should_be_basket_header(self):
        basket_header = self.browser.find_element(*BasketPageLocators.BASKET_HEADER).text
        assert basket_header == 'Basket', "Header is not equal to Basket"

    def should_not_be_add_to_basket_button(self):
        assert self.is_not_element_present(*BasketPageLocators.ADD_TO_BASKET_BUTTON), "The add to basket button found"
