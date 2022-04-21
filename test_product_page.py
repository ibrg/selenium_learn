from pages.ProductPage import ProductPageHelper

# link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear)'

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'


def test_product_page(browser):
    product_page = ProductPageHelper(browser, link)
    product_page.open_page()
    product_page.check_correct_url()
    product_page.click_on_the_add_to_cart_button()
    product_page.solve_quiz_and_get_code()
    product_page.check_message_alert_product_name()
    product_page.check_message_alert_product_price()
