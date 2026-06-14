import time
import pytest

from actions.checkoutAction import CheckoutAction
from utils.configReader import ConfigReader
from utils.excelReader import get_registration_data

@pytest.mark.Samiha
class TestCheckout:

    def test_login_checkout(self, driver):

        drv, wait = driver
        action = CheckoutAction(drv)

        drv.get(ConfigReader.get_url())

        action.click_hp_product()
        action.add_product_to_cart()
        action.click_shopping_cart_from_popup()
        action.click_checkout_from_cart_page()

        action.click_Login_Radio()
        action.login_from_checkout_page(ConfigReader.get("credentials", "email"),ConfigReader.get("credentials", "password"))
        
        action.enter_billing_details({
            "firstname": ConfigReader.get("billing", "first_name"),
            "lastname": ConfigReader.get("billing", "last_name"),
            "company": ConfigReader.get("billing", "company"),
            "address1": ConfigReader.get("billing", "address1"),
            "city": ConfigReader.get("billing", "city"),
            "postcode": ConfigReader.get("billing", "postcode"),
        })
      
        action.agree_to_privacy_policy()
        action.clickContinueCheckout()
        print(action.is_order_placed_successfully())

    def test_register_checkout(self, driver):

        drv, wait = driver
        action = CheckoutAction(drv)

        drv.get(ConfigReader.get_url())
        action.click_hp_product()
        action.add_product_to_cart()
        action.click_shopping_cart_from_popup()
        action.click_checkout_from_cart_page()
    

        action.select_register_account()
        data = get_registration_data("D:\Pytest_Automation_Project\data_provider\DataProvider.xlsx", "Registration")

        action.enter_registration_details(data)
        action.agree_to_privacy_policy()
        action.agree_to_account_privacy_policy()
        action.clickContinueCheckout()
        print(action.is_order_placed_successfully())

    def test_empty_cart_checkout(self, driver):
        drv, wait = driver
        action = CheckoutAction(drv)

        drv.get("https://ecommerce-playground.lambdatest.io/index.php?route=checkout/cart")
        print(action.is_empty_cart_message_displayed())