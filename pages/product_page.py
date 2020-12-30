from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_basket(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Basket button is not found"

    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def check_item_is_added_to_basket(self):
        # check the message
        self.book_name_is_in_message()
        # check the price
        self.cost_basket_equal_to_price()

    def book_name_is_in_message(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        message_book_is_added = self.browser.find_element(*ProductPageLocators.MESSAGE_TEXT).text
        assert book_name == message_book_is_added, f"The book name '{book_name}' is not equal to the name " \
                                                   f"in the message:{message_book_is_added}"

    def cost_basket_equal_to_price(self):
        cost_basket = self.browser.find_element(*ProductPageLocators.COST_BASKET).text
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert book_price in cost_basket, f"The cost of your basket is not equal to the price of the book"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"
