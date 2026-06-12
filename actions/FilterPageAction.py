import time

from actions.BaseAction import BaseAction
from pages.FilterPage import FilterPage


class FilterPageAction(BaseAction):
    def __init__(self, driver):
        super().__init__(driver)
        self.fp=FilterPage(driver)
    def clickManufactureBrand(self):
        self.click(self.fp.Manufacture)
    def clickiPodProduct(self):
        self.click(self.fp.iPodProduct)
    def clickInstockOption(self):
        self.click(self.fp.inStockOption)
    def clickCanonProduct(self):
        self.click(self.fp.canonProduct)
    def movePriceSlider(self):
        self.move_slider(self.fp.FilterSlider,-100)
    def getPriceValue(self):
        return self.get_input_value(self.fp.price)
    def clickOutOfStockOption(self):
        self.js_click(self.fp.outStockOption)
    def clickIpodProduct(self):
        self.click(self.fp.iPodProduct)
    def selectDropDown(self, value="25"):
     self.select_by_visible_text(
        self.fp.filterDropDown,
        str(value)
    )
    def getAllProducts(self):
     return self.find_elements(self.fp.allProducts)