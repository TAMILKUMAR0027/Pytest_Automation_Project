from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from pages.accountpage import AccountPage
from actions.BaseAction import BaseAction


class AccountPageAction(BaseAction):
    def __init__(self, driver):
        super().__init__(driver)
        self.apa = AccountPage(driver)

    def success_login(self):
        actual = self.get_text(self.apa.accountLoginSuccess)
        return "My Account" in actual
