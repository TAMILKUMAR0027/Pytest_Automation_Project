from actions.BaseAction import BaseAction
from pages.FilterPage import FilterPage


class FilterPageAction(BaseAction):
    def __init__(self, driver):
        super().__init__(driver)
    fp=FilterPage()
    def clickManufactureBrand(self):
        self.click(self.fp.Manufacture)
    def clickiPodProduct(self):
        self.click(self.fp.iPodProduct)
    