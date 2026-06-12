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
<<<<<<< Updated upstream
    def click_myAcc(self):
        self.click(self.hp.myAccLink)
=======

    def click_myAcc(self):
        self.click(self.hp.myAccLink)
>>>>>>> Stashed changes
