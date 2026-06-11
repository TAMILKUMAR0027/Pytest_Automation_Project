from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from actions.BaseAction import BaseAction
from pages.accountsuccessregpage import RegAccSuccPage


class RegisterAccSuccessPageAction(BaseAction):
    def __init__(self, driver):
        super().__init__(driver)
        self.asr = RegAccSuccPage(driver)

    def success_register(self):
        actual = self.get_text(self.asr.regSuccess)
        return "Your Account Has Been Created!" in actual
