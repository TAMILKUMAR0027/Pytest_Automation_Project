from actions.BaseAction import BaseAction
from pages.HomePage import HomePage


class HomePageAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.hp = HomePage(driver)

    def clickShopByCategory(self):
        self.click(self.hp.ShopByCategory)

    def clickMonitor(self):
        self.click(self.hp.Monitor)

    def click_myAcc(self):
        self.click(self.hp.myAccLink)
    def click_HpProduct(self):
        self.click(self.hp.Hp_Product)
    def click_CompareLink(self):
        self.click(self.hp.Compare_Link)
def click_CanonProduct(self):
    self.click(self.hp.Canon_Product)