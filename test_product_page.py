"""
pytest -v -s --tb=line --language=en test_product_page.py
first link:
http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear
second link:
http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019
"""
from .pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_basket()
    product_page.add_to_basket()  # добавляем в корзину товар
    product_page.solve_quiz_and_get_code()
    product_page.check_item_is_added_to_basket()  # проверяем что товар добавлен
    # time.sleep(10)

