from.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class MainPage(BasePage):

    def is_element_present(self, how, what):
        """
        :param how: ID, CLASS, CSS_SELECTOR
        :param what: Name id, class or css selector
        :return:
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def go_to_login_page(self):
        get_link = self.browser.find_element(By.ID, 'login_link')
        get_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(By.ID, "login_link"), "Login link is not presented"
