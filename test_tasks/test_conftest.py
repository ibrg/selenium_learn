import time

import pytest, time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.smoke
def test_browser(browser):
    browser.get(link)
    time.sleep(5)
    browser.find_element(By.ID, 'login_link')
