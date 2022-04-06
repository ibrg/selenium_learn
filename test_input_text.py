import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service


class TestRegistation(unittest.TestCase):
    def setUp(self) -> None:
        driver = Service('./geckodriver')
        self.browser = webdriver.Firefox(service=driver)
        self.first_name = 'TestName'
        self.last_name = 'LastName'
        self.email = 'test@mail.tru'
        self.phone = '+123456789'
        self.address = 'Towm, City'

    def test_registration_first(self):
        link = 'http://suninjuly.github.io/registration1.html'
        browser = self.browser
        browser.get(link)
        h1 = browser.find_element(By.TAG_NAME, 'h1').text
        self.assertEqual(h1, 'Registration', 'Success!')

    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()
