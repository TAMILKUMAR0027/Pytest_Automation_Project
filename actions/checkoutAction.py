from actions.BaseAction import BaseAction
from actions.loginpageaction import LoginPageAction
from pages.checkoutPage import CheckoutPage
from utils.configReader import ConfigReader
from utils.excelReader import get_data


class CheckoutAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.cp = CheckoutPage()

    def login_as_registered_user(self):

        self.driver.get(
            "https://ecommerce-playground.lambdatest.io/index.php?route=account/login"
        )

        email = ConfigReader.get("credentials", "email")
        password = ConfigReader.get("credentials", "password")

        login_action = LoginPageAction(self.driver)

        login_action.enter_login_credentials(
            email,
            password
        )

    def click_hp_product(self):
        self.click(self.cp.HP_PRODUCT_IMAGE)

    def add_product_to_cart(self):
        self.click(self.cp.PRODUCT_PAGE_CHECKOUT_BTN1)

    def click_shopping_cart_from_popup(self):
        self.click(self.cp.SHOPPING_CART_POPUP_LINK)

    def click_checkout_from_cart_page(self):
        self.click(self.cp.CART_PAGE_CHECKOUT_BTN)

    def is_checkout_or_login_page_displayed(self):
        return self.is_displayed(self.cp.NEW_ADDRESS_RADIO)

    def select_new_address(self):
        self.click(self.cp.NEW_ADDRESS_RADIO)

    def enter_billing_details(self):

        self.send_keys(
            self.cp.FIRST_NAME_INPUT,
            ConfigReader.get("billing", "first_name")
        )

        self.send_keys(
            self.cp.LAST_NAME_INPUT,
            ConfigReader.get("billing", "last_name")
        )

        self.send_keys(
            self.cp.COMPANY_INPUT,
            ConfigReader.get("billing", "company")
        )

        self.send_keys(
            self.cp.ADDRESS1_INPUT,
            ConfigReader.get("billing", "address1")
        )

        self.send_keys(
            self.cp.CITY_INPUT,
            ConfigReader.get("billing", "city")
        )

        self.send_keys(
            self.cp.POSTCODE_INPUT,
            ConfigReader.get("billing", "postcode")
        )

    def click_same_billing_address(self):
        self.click(self.cp.SAME_BILLING_ADDRESS_LABEL)

    def select_flat_rate(self):
        self.click(self.cp.FLAT_RATE_LABEL)

    def select_cash_on_delivery(self):
        self.click(self.cp.COD_LABEL)

    def click_terms_and_conditions(self):
        self.click(self.cp.TERMS_LABEL)

    def continue_checkout(self):
        self.click(self.cp.CONTINUE_CHECKOUT_BTN)

    def is_order_placed_successfully(self):
        return self.is_displayed(self.cp.ORDER_CONFIRMATION_MSG)

    def is_empty_cart_message_displayed(self):
        return self.is_displayed(self.cp.EMPTY_CART_MESSAGE)

    def select_register_account(self):
        self.click(self.cp.REGISTER_ACCOUNT_RADIO)

    def enter_registration_details(self):

        data = get_data(
            "testdata/RegisterData.xlsx",
            "Register"
        )

        self.send_keys(
            self.cp.REG_FIRST_NAME_INPUT,
            data[0][0]
        )

        self.send_keys(
            self.cp.REG_LAST_NAME_INPUT,
            data[0][1]
        )

        self.send_keys(
            self.cp.REG_EMAIL_INPUT,
            data[0][2]
        )

        self.send_keys(
            self.cp.REG_TELEPHONE_INPUT,
            data[0][3]
        )

        self.send_keys(
            self.cp.REG_PASSWORD_INPUT,
            data[0][4]
        )

        self.send_keys(
            self.cp.REG_CONFIRM_PASSWORD_INPUT,
            data[0][5]
        )

    def agree_to_privacy_policy(self):
        self.click(self.cp.PRIVACY_LABEL)