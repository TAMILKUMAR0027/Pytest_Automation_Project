from actions.checkoutAction import CheckoutAction
from utils.configReader import ConfigReader

@pytest.mark.Samiha
class TestCheckout:

    def test_guest_checkout_with_new_address_cod(self, driver):

        drv, wait = driver

        action = CheckoutAction(drv)

        action.login_as_registered_user()

        drv.get(ConfigReader.get_url())

        action.click_hp_product()
        action.add_product_to_cart()
        action.click_shopping_cart_from_popup()
        action.click_checkout_from_cart_page()

        assert action.is_checkout_or_login_page_displayed()

        action.select_new_address()
        action.enter_billing_details()
        action.click_same_billing_address()

        action.select_flat_rate()
        action.select_cash_on_delivery()

        action.click_terms_and_conditions()
        action.continue_checkout()

        assert action.is_order_placed_successfully()

    def test_checkout_with_empty_cart(self, driver):

        drv, wait = driver

        action = CheckoutAction(drv)

        drv.get(
            "https://ecommerce-playground.lambdatest.io/index.php?route=checkout/cart"
        )

        assert action.is_empty_cart_message_displayed()

    def test_checkout_with_register_account(self, driver):

        drv, wait = driver

        action = CheckoutAction(drv)

        drv.get(ConfigReader.get_url())

        action.click_hp_product()
        action.add_product_to_cart()
        action.click_shopping_cart_from_popup()
        action.click_checkout_from_cart_page()

        assert action.is_checkout_or_login_page_displayed()

        action.select_register_account()
        action.enter_registration_details()
        action.agree_to_privacy_policy()
        action.continue_checkout()
