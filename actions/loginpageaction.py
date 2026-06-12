from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from actions.BaseAction import BaseAction
from pages.loginpage import LoginPage


class LoginPageAction(BaseAction):
    def __init__(self, driver):
        super().__init__(driver)
        self.lp = LoginPage(driver)

    def click_register_continue(self):
        self.click(self.lp.rcontinue)

    def enter_login_credentials(self, lemail, lpass):

        self.send_keys(self.lp.loginEmail, lemail)
        self.send_keys(self.lp.loginPassword, lpass)
        self.click(self.lp.loginContinue)
