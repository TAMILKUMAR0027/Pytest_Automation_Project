import pytest
from actions.HomePageAction import HomePageAction
from utils.excelReader import get_data
from actions.accountpageaction import AccountPageAction
from actions.launch_actions import LaunchActions
from actions.loginpageaction import LoginPageAction
from utils.configReader import ConfigReader
from utils.loggerCreator import get_logger

logger = get_logger(__name__)


@pytest.mark.Rishwanth
class TestEditAccountInfo:

    @pytest.mark.parametrize(
        "username,password",
        get_data(
            "data_provider/DataProvider.xlsx",
            "loginDataValid",
        ),
    )
    def test_EditAccInfo(self, driver, username, password):
        logger.info("Starting test: Edit Account Information")

        drv, wait = driver
        logger.info("Driver initialized successfully")

        telephone = ConfigReader.get_register_data("telephone")
        logger.info(f"Telephone value fetched from config: {telephone}")

        hp = HomePageAction(drv)
        logger.info("HomePageAction object created")

        hp.click_myAcc()
        logger.info("Clicked on My Account")

        lp = LoginPageAction(drv)
        logger.info("LoginPageAction object created")

        lp.enter_login_credentials(username, password)
        logger.info(f"Entered login credentials for user: {username}")

        apa = AccountPageAction(drv)
        logger.info("AccountPageAction object created")

        result = apa.click_editAccount_info(telephone)
        logger.info(f"Edit account information result: {result}")

        assert result is True

        logger.info("Test passed: Edit Account Information updated successfully")
