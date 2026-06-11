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
    
    