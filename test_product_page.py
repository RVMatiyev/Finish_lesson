from .pages.product_page import ProductPage
import pytest
import time

def test_guest_add_to_basket(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.guest_can_add_product_to_basket()



def test_correct_name_of_product(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()
    page.message_about_add_correct_product()

def test_correct_price(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()
    page.message_is_present_about_add()
    page.price_of_basket_is_equal_to_product()


@pytest.mark.parametrize('link', ["/?promo=offer0", "/?promo=offer1", "/?promo=offer2", "/?promo=offer3", "/?promo=offer4", "/?promo=offer5",
                                  "/?promo=offer6", "/?promo=offer7", "/?promo=offer8", "/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{link}/"
    page = ProductPage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.message_is_present_about_add()
    page.price_of_basket_is_equal_to_product()
    time.sleep(20)