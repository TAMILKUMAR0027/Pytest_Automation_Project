import pytest


from actions.accountregsuccesspageaction import RegisterAccSuccessPageAction
from actions.HomePageAction import HomePageAction
from actions.loginpageaction import LoginPageAction
from actions.registerpageaction import RegisterPageAction


class TestRegister:
    def test_validRegister(self):
        hp = HomePageAction(self.driver)
        hp.click_myAcc()
        lp = LoginPageAction(self.driver)
        lp.click_register_continue()
        rp = RegisterPageAction(self.driver)
        fname = ConfigReader.get_config_Data("register credentials", "fname")
        lname = get_config_Data("register credentials", "lname")
        email = get_config_Data("register credentials", "email")
        telephone = get_config_Data("register credentials", "telephone")
        password = get_config_Data("register credentials", "password")
        cpassword = get_config_Data("register credentials", "cpassword")
        rp.enter_register_credentials(
            fname, lname, email, telephone, password, cpassword
        )
        acpr = RegisterAccSuccessPageAction(self.driver)
        assert acpr.success_register
