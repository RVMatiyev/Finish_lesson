from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class BasketPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "button[value='Добавить в корзину']")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(1)>div>strong")
    MESSAGE_ABOUT_ADD = (By.CSS_SELECTOR, "div:nth-child(1)[class='alert alert-safe alert-noicon alert-success  fade in']")
    PRICE_IN_THE_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(3)>div>p strong")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, "p[class='price_color']")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, "div[class ='col-sm-6 product_main']>h1")

