from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

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
