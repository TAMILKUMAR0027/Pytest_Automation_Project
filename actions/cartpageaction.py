from pages.ProductPage import ProductPage
from pages.cartpage import CartPage
from pages.launch import LaunchPages
from actions.BaseAction import BaseAction


class CartPageAction(BaseAction):
    def __init__(self, driver):
        super().__init__(driver)
        self.cp = CartPage(driver)
        self.pp = ProductPage(driver)
        self.lp = LaunchPages(driver)

    def single_product_addCheck(self):
        actual = self.get_text(self.cp.cartProduct)
        return "HP LP3065" in actual

    def quantity_update_check(self, quantity):
        self.clear(self.cp.quantity_input)
        self.send_keys(self.cp.quantity_input, quantity)
        self.click(self.cp.quantity_update)
        actual = self.get_text(self.cp.quantity_update_success)
        return "You have modified your shopping cart!" in actual
