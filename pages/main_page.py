from.base_page import BasePage
from pages.locators import MainPageLocators
from pages.login_page import LoginPage


class MainPage(BasePage):

    def go_to_login_page(self):
        get_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        get_link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)
