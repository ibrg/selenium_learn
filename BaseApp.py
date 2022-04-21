import math
import time
from selenium.common.exceptions import NoAlertPresentException

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open_page(self):
        return self.browser.get(self.url)

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            ec.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}")

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        time.sleep(10)
        try:
            new_alert = self.browser.switch_to.alert
            alert_text = new_alert.text
            print(f"Your code: {alert_text}")
            new_alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
