from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from pages.accountsuccessregpage import RegAccSuccPage


class RegisterAccSuccessPageAction:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.asr = RegAccSuccPage(driver)

    def success_register(self):

        actual = self.wait.until(
            ec.visibility_of_element_located(self.asr.regSuccess)
        ).text

        return "Your Account Has Been Created!" in actual
