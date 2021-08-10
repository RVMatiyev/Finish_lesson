from .base_page import BasePage
from .locators import BasketPageLocators


class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):
        button = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
        button.click()

    def message_about_add_correct_product(self):
        message = self.browser.find_element(*BasketPageLocators.PRODUCT_IN_BASKET)
        product_name = self.browser.find_element(*BasketPageLocators.NAME_OF_PRODUCT)
        assert message.text == product_name.text

    def message_is_present_about_add(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_ABOUT_ADD), "Message is not find"

    def price_of_basket_is_equal_to_product(self):
        price_basket = self.browser.find_element(*BasketPageLocators.PRICE_IN_THE_BASKET)
        price_product = self.browser.find_element(*BasketPageLocators.PRICE_OF_PRODUCT)
        assert price_basket.text == price_product.text


