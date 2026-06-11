from actions.BaseAction import BaseAction
from pages.ProductPage import ProductPage


class ProductPageAction(BaseAction):
    def __init__(self, driver):
        super().__init__(driver)
    pp=ProductPage()
    def getBrand(self):
        self.get_text(self.pp.brand)