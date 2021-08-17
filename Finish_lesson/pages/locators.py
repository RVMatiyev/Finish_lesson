from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket") #кнопка
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages div.alertinner strong") # название товара в корзине
    PRODUCT_NAME_IN_STORE = (By.CSS_SELECTOR, "#content_inner h1:first-child") # название товара
    PRODUCT_PRICE_BASKET = (By.CSS_SELECTOR, ".alert-info p:first-child strong") # цена товара в корзине
    PRODUCT_PRICE_STORE = (By.CSS_SELECTOR, "#content_inner p.price_color") # цена товара
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div.alertinner") # аллерт о добавлении товара


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#content_inner h2")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")
