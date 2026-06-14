import pytest

from actions.HomePageAction import HomePageAction
from actions.accountregsuccesspageaction import RegisterAccSuccessPageAction
from actions.loginpageaction import LoginPageAction
from actions.registerpageaction import RegisterPageAction
from utils.configReader import ConfigReader
from utils.loggerCreator import get_logger

logger = get_logger(__name__)


@pytest.mark.Rishwanth
class TestRegister:

    def test_validRegister(self, driver):
        drv, wait = driver

        logger.info("Valid register test started")

        hp = HomePageAction(drv)
        hp.click_myAcc()
        logger.info("Clicked My Account")

        lp = LoginPageAction(drv)
        lp.click_register_continue()
        logger.info("Clicked Register link")

        rp = RegisterPageAction(drv)

        fname = ConfigReader.get_register_data("fname")
        lname = ConfigReader.get_register_data("lname")
        telephone = ConfigReader.get_register_data("telephone")
        password = ConfigReader.get_register_data("password")
        cpassword = ConfigReader.get_register_data("cpassword")

        logger.info("Valid register test data fetched from config file")

        rp.enter_register_credentials(fname, lname, telephone, password, cpassword)
        logger.info(f"Entered valid register credentials for user: {fname} {lname}")

        acpr = RegisterAccSuccessPageAction(drv)

        assert acpr.success_register() is True
        logger.info("Valid register test passed successfully")

    def test_inValidRegister(self, driver):
        drv, wait = driver

        logger.info("Invalid register test started")

        hp = HomePageAction(drv)
        hp.click_myAcc()
        logger.info("Clicked My Account")

        lp = LoginPageAction(drv)
        lp.click_register_continue()
        logger.info("Clicked Register link")

        rp = RegisterPageAction(drv)

        fname = ConfigReader.get_register_data("fname")
        lname = ConfigReader.get_register_data("lname")
        email = ConfigReader.get_register_data("email")
        telephone = ConfigReader.get_register_data("telephone")
        password = ConfigReader.get_register_data("password")
        cpassword = ConfigReader.get_register_data("cpassword")

        logger.info("Invalid register test data fetched from config file")

        rp.enter_invalidregister_credentials(
            fname, lname, email, telephone, password, cpassword
        )
        logger.info(f"Entered invalid register credentials for user: {fname} {lname}")

        assert rp.reg_fail_msg() is True
        logger.info("Invalid register failure message displayed successfully")

    def test_WarningMsg_for_uncheck_pp(self, driver):
        drv, wait = driver

        logger.info("inValid register test started")

        hp = HomePageAction(drv)
        hp.click_myAcc()
        logger.info("Clicked My Account")

        lp = LoginPageAction(drv)
        lp.click_register_continue()
        logger.info("Clicked Register link")

        rp = RegisterPageAction(drv)

        fname = ConfigReader.get_register_data("fname")
        lname = ConfigReader.get_register_data("lname")
        telephone = ConfigReader.get_register_data("telephone")
        password = ConfigReader.get_register_data("password")
        cpassword = ConfigReader.get_register_data("cpassword")

        logger.info("Valid register test data fetched from config file")

        assert (
            rp.enter_registerDetails_without_pp(
                fname, lname, telephone, password, cpassword
            )
            is True
        )
        logger.info(
            f"Entered valid register credentials for user: {fname} {lname} and uncheck Privacy policy and Warning Msg Thrown"
        )

        acpr = RegisterAccSuccessPageAction(drv)
