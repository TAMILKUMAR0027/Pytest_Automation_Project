from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from pages.registerpage import RegisterPage


class RegisterPageAction:
    def __int__(self, driver):
        super().__init__(driver)
        self.rp = RegisterPage()

    def enter_register_credentials(
        self, fname, lname, email, telephone, password, cpassword
    ):
        self.send_keys(self.rp.fname, fname)
        self.send_keys(self.rp.lname, lname)
        self.send_keys(self.rp.email, email)
        self.send_keys(self.rp.telephone, telephone)
        self.send_keys(self.rp.password, password)
        self.send_keys(self.rp.cpassword, cpassword)
        self.click(self.rp.privacyCB)
        self.click(self.rp.regContinue)
