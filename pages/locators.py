from selenium.webdriver.common.by import By


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    ADD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success > div.alertinner > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success > div.alertinner")
    PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages p > strong")
