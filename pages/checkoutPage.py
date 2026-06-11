from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    hp_product_link = (By.XPATH, "//img[@title='HP LP3065']")
    add_to_cart_btn = (By.XPATH, "(//button[@title='Add to Cart'])[1]")
    popup_checkout_btn = (By.XPATH, "//a[contains(@href,'route=checkout/checkout')]")
    new_address_radio = (By.ID, "input-payment-address-new")

    first_name = (By.ID, "input-payment-firstname")
    last_name = (By.ID, "input-payment-lastname")
    company = (By.ID, "input-payment-company")
    address1 = (By.ID, "input-payment-address-1")
    city = (By.ID, "input-payment-city")
    postcode = (By.ID, "input-payment-postcode")
    country = (By.ID, "input-payment-country")
    region = (By.ID, "input-payment-zone")

    same_address = (By.ID, "input-shipping-address-same")
    cod_option = (By.XPATH, "//label[contains(.,'Cash On Delivery')]")
    flat_rate = (By.XPATH, "//label[contains(.,'Flat Shipping Rate')]")
    terms = (By.XPATH, "//label[@for='input-agree']")
    continue_btn = (By.ID, "button-save")

    confirm_message = (By.CSS_SELECTOR, "#content h1")
    empty_cart_message = (By.XPATH, "//div[@id='content']//p")