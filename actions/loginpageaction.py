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

    def provide_error_msg_invalid_login(self):
        actual = self.get_text(self.lp.invalidLoginErrorMsg)
        actual = " ".join(actual.split())
        invalid_msg = "Warning: No match for E-Mail Address and/or Password."
        attempt_exceeded_msg = " Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour."
        return invalid_msg in actual or attempt_exceeded_msg in actual
