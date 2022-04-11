from pages.main_page import MainPage


def open_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    return page


def test_guest_can_go_to_login_page(browser):
    page = open_page(browser)
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()


# def test_guest_should_see_login_link(browser):
#     page = open_page(browser)
#     page.should_be_login_link()
