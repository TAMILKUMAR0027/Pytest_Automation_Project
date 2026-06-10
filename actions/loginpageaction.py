from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from pages.loginpage import LoginPage


class LoginPageAction:
    def __init__(self, driver):
        super().__init__(driver)
        self.lp = LoginPage()

    def click_register_continue(self):
        self.click(self.lp.rcontinue)
