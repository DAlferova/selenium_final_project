from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    MESSAGE_TEXT = (By.CSS_SELECTOR, ".alertinner strong")
    COST_BASKET = (By.CSS_SELECTOR, ".basket-mini")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main>p")
