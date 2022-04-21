import pytest
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service


@pytest.fixture(scope='function')
def browser():
    driver = Service('./geckodriver')
    browser = Firefox(service=driver)
    yield browser
    browser.quit()
