from BaseApp import BasePage
from .locators import ProductPageLocators


class ProductPageHelper(BasePage):

    def check_correct_url(self):
        assert "?promo=newYear" in self.browser.current_url

    def click_on_the_add_to_cart_button(self):
        self.find_element(ProductPageLocators.ADD_BUTTON).click()

    def check_message_alert_product_name(self):
        alert = self.find_element(ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE).text
        product_name = self.find_element(ProductPageLocators.PRODUCT_NAME).text
        assert product_name in alert,  "Not find product name."

    def check_message_alert_product_price(self):
        alert_info = self.find_element(ProductPageLocators.PRICE_MESSAGE).text
        product_price = self.find_element(ProductPageLocators.PRODUCT_PRICE).text
        assert product_price in alert_info, "Not find product price."
