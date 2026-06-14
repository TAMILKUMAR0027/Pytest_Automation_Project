from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from actions.BaseAction import BaseAction
from pages.ProductPage import ProductPage
from pages.HomePage import HomePage
from pages.checkoutPage import CheckoutPage
from utils.configReader import ConfigReader


class CheckoutAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.cp = CheckoutPage()
        self.hp=HomePage(driver)
        self.pp=ProductPage(driver)

    def click_hp_product(self):
        self.click(self.hp.Hp_Product)

    def add_product_to_cart(self):
        self.click(self.pp.addToCart)

    def click_shopping_cart_from_popup(self):
        self.click(self.pp.viewCartbtn)

    def click_checkout_from_cart_page(self):
        self.click(self.cp.CART_PAGE_CHECKOUT_BTN)

    def click_Login_Radio(self):
        self.click(self.cp.LOGIN_RADIO)

    def login_from_checkout_page(self, email=None, password=None):

        email = email or ConfigReader.get("credentials", "email")
        password = password or ConfigReader.get("credentials", "password")

        self.send_keys(self.cp.LOGIN_EMAIL, email)
        self.send_keys(self.cp.LOGIN_PASSWORD, password)

        login_btn = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.cp.LOGIN_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", login_btn)
        login_btn.click()

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.cp.FIRST_NAME_INPUT))

    def enter_billing_details(self, data=None):

        data = data or {
            "firstname": ConfigReader.get("billing", "first_name"),
            "lastname": ConfigReader.get("billing", "last_name"),
            "company": ConfigReader.get("billing", "company"),
            "address1": ConfigReader.get("billing", "address1"),
            "city": ConfigReader.get("billing", "city"),
            "postcode": ConfigReader.get("billing", "postcode"),
        }

        self.send_keys(self.cp.FIRST_NAME_INPUT, data["firstname"])
        self.send_keys(self.cp.LAST_NAME_INPUT, data["lastname"])
        self.send_keys(self.cp.COMPANY_INPUT, data["company"])
        self.send_keys(self.cp.ADDRESS1_INPUT, data["address1"])
        self.send_keys(self.cp.CITY_INPUT, data["city"])
        self.send_keys(self.cp.POSTCODE_INPUT, data["postcode"])

    def click_same_billing_address(self):
        self.click(self.cp.SAME_BILLING_ADDRESS_LABEL)

    def select_flat_rate(self):

        flat_rate = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.cp.FLAT_RATE_LABEL))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", flat_rate)
        self.driver.execute_script("arguments[0].click();", flat_rate)

    def select_cash_on_delivery(self):

        cod = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.cp.COD_LABEL))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", cod)
        self.driver.execute_script("arguments[0].click();", cod)

    def click_terms_and_conditions(self):

        terms = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.cp.TERMS_LABEL))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", terms)
        self.driver.execute_script("arguments[0].click();", terms)

    def continue_checkout(self):

        btn = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.cp.CONTINUE_CHECKOUT_BTN))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        self.driver.execute_script("arguments[0].click();", btn)

    def select_register_account(self):
        self.click(self.cp.REGISTER_ACCOUNT_RADIO)

    def enter_registration_details(self, data):

        self.send_keys(self.cp.REG_FIRST_NAME_INPUT, data["firstname"])
        self.send_keys(self.cp.REG_LAST_NAME_INPUT, data["lastname"])
        self.send_keys(self.cp.REG_EMAIL_INPUT, data["email"])
        self.send_keys(self.cp.REG_TELEPHONE_INPUT, str(data["telephone"]))
        self.send_keys(self.cp.REG_PASSWORD_INPUT, data["password"])
        self.send_keys(self.cp.REG_CONFIRM_PASSWORD_INPUT, data["confirm_password"])

    def agree_to_privacy_policy(self):

        privacy = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.cp.PRIVACY_LABEL))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", privacy)
        self.driver.execute_script("arguments[0].click();", privacy)
    def agree_to_account_privacy_policy(self):

        privacy = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.cp.ACCOUNT_PRIVACY_LABEL))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", privacy)
        self.driver.execute_script("arguments[0].click();", privacy)

    def clickContinueCheckout(self):
        self.click(self.cp.CONTINUE_CHECKOUT_BTN)
    def is_order_placed_successfully(self):
        return self.is_displayed(self.cp.ORDER_CONFIRMATION_MSG)
    def is_empty_cart_message_displayed(self):
        return self.is_displayed(self.cp.EMPTY_CART_MESSAGE)