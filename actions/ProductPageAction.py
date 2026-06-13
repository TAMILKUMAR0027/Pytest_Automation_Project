from actions.BaseAction import BaseAction
from pages.ProductPage import ProductPage


class ProductPageAction(BaseAction):
    def __init__(self, driver):
        super().__init__(driver)
        self.pp = ProductPage(driver)

    def getBrand(self):
        return self.get_text(self.pp.brand)

    def getInstock(self):
        return self.get_text(self.pp.instock)

    def getOutStock(self):
        return self.get_text(self.pp.outStock)

    def click_add_to_cart(self):
        self.click(self.pp.addToCart)

    def click_view_cart(self):
        self.click(self.pp.viewCartbtn)
