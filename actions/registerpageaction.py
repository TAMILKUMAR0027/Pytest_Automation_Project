import time

from actions.BaseAction import BaseAction
from pages.registerpage import RegisterPage


class RegisterPageAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.rp = RegisterPage(driver)

    def enter_register_credentials(self, fname, lname, telephone, password, cpassword):

        self.send_keys(self.rp.fname, fname)

        self.email = f"test{int(time.time())}@gmail.com"

        self.send_keys(self.rp.lname, lname)
        self.send_keys(self.rp.email, self.email)
        self.send_keys(self.rp.telephone, telephone)
        self.send_keys(self.rp.password, password)
        self.send_keys(self.rp.cpassword, cpassword)

        self.click(self.rp.privacyCB)
        self.click(self.rp.regContinue)

        print("Generated Email:", self.email)

    def enter_invalidregister_credentials(
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

    def reg_fail_msg(self):
        actual = self.get_text(self.rp.regFail)
        actual = " ".join(actual.split())

        print("Actual register error message:", actual)

        return "E-Mail Address is already registered" in actual

    def enter_registerDetails_without_pp(
        self, fname, lname, telephone, password, cpassword
    ):

        self.send_keys(self.rp.fname, fname)

        self.email = f"test{int(time.time())}@gmail.com"

        self.send_keys(self.rp.lname, lname)
        self.send_keys(self.rp.email, self.email)
        self.send_keys(self.rp.telephone, telephone)
        self.send_keys(self.rp.password, password)
        self.send_keys(self.rp.cpassword, cpassword)
        self.click(self.rp.regContinue)
        actual = self.get_text(self.rp.privacyPolicy_msg)
        return "You must agree to the Privacy Policy!" in actual
