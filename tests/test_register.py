import pytest

from actions.HomePageAction import HomePageAction
from actions.accountregsuccesspageaction import RegisterAccSuccessPageAction
from actions.loginpageaction import LoginPageAction
from actions.registerpageaction import RegisterPageAction
from utils.configReader import ConfigReader


class TestRegister:

    def test_validRegister(self, driver):
        drv, wait = driver

        hp = HomePageAction(drv)
        hp.click_myAcc()

        lp = LoginPageAction(drv)
        lp.click_register_continue()

        rp = RegisterPageAction(drv)

        fname = ConfigReader.get_register_data("fname")
        lname = ConfigReader.get_register_data("lname")
        telephone = ConfigReader.get_register_data("telephone")
        password = ConfigReader.get_register_data("password")
        cpassword = ConfigReader.get_register_data("cpassword")
        rp.enter_register_credentials(
            fname,
            lname,
            telephone,
            password,
            cpassword
        )
        acpr = RegisterAccSuccessPageAction(drv)

        assert acpr.success_register() is True