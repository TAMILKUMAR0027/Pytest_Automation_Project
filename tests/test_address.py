import pytest
from actions.HomePageAction import HomePageAction
from utils.excelReader import get_data
from actions.accountpageaction import AccountPageAction
from actions.loginpageaction import LoginPageAction
from utils.loggerCreator import get_logger

logger = get_logger(__name__)


@pytest.mark.Rishwanth
class TestAddressBook:

    @pytest.mark.parametrize(
        "username,password",
        get_data(
            "data_provider/DataProvider.xlsx",
            "loginDataValid",
        ),
    )
    def test_deleteAddressBook(self, driver, username, password):
        logger.info("Starting test: Delete Address Book")

        drv, wait = driver
        logger.info("Driver initialized successfully")

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

        result = apa.deleteExistingAddress()
        logger.info(f"Delete address book result: {result}")

        assert result is True

        logger.info("Test passed: Address Book deleted successfully")
