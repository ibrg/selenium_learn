import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOption
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="choose")
    parser.addoption("--lang", action="store", default="fr")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    user_lang = request.config.getoption("lang")
    browser = None
    if browser_name == "firefox":
        driver = Service("../geckodriver")
        options = FirefoxOption()
        options.set_preference("intl.accept_languages", user_lang)
        browser = webdriver.Firefox(service=driver, options=options)
    elif browser_name == "chrome":
        options = Options()
        options.add_experimental_option("prefs", {"intl.accept_languages": user_lang})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("Choose browser chrome or firefox")
    yield browser
    browser.quit()
