import pytest

from actions.HomePageAction import HomePageAction
from actions.loginpageaction import LoginPageAction
from actions.accountpageaction import AccountPageAction
from utils.excelReader import get_data
from utils.loggerCreator import get_logger

logger = get_logger(__name__)


@pytest.mark.Rishwanth
class TestLogin:

    @pytest.mark.parametrize(
        "username,password",
        get_data(
            r"D:\Pytest_Automation_Project\Pytest_Automation_Project\data_provider\DataProvider.xlsx",
            "loginDataValid",
        ),
    )
    def test_validLogin(self, driver, username, password):
        drv, wait = driver

        logger.info("Valid login test started")

        hp = HomePageAction(drv)
        hp.click_myAcc()
        logger.info("Clicked My Account")

        lp = LoginPageAction(drv)
        lp.enter_login_credentials(username, password)
        logger.info(f"Entered valid username: {username}")

        apa = AccountPageAction(drv)

        assert apa.success_login() is True
        logger.info("Valid login test passed successfully")

    @pytest.mark.parametrize(
        "username1,password1",
        get_data(
            r"D:\Pytest_Automation_Project\Pytest_Automation_Project\data_provider\DataProvider.xlsx",
            "loginDataInvalid",
        ),
    )
    def test_invalidLogin(self, driver, username1, password1):
        drv, wait = driver

        logger.info("Invalid login test started")

        hp = HomePageAction(drv)
        hp.click_myAcc()
        logger.info("Clicked My Account")

        lp = LoginPageAction(drv)
        lp.enter_login_credentials(username1, password1)
        logger.info(f"Entered invalid username: {username1}")

        assert lp.provide_error_msg_invalid_login() is True
        logger.info("Invalid login error message displayed successfully")
