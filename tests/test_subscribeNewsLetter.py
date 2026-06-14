import pytest
from actions.accountpageaction import AccountPageAction
from actions.newsletterpageaction import NewsLetterPageAction
from actions.HomePageAction import HomePageAction
from actions.loginpageaction import LoginPageAction
from utils.excelReader import get_data
from utils.loggerCreator import get_logger

logger = get_logger(__name__)


@pytest.mark.Rishwanth
class TestSubscribeNewsLetter:

    @pytest.mark.parametrize(
        "username,password",
        get_data(
            "data_provider/DataProvider.xlsx",
            "loginDataValid",
        ),
    )
    def test_subscribe_newsLetter(self, driver, username, password):
        logger.info("Starting test: Subscribe Newsletter")

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

        apa.click_subscribe_newsLetter()
        logger.info("Clicked on Subscribe Newsletter option")

        nlpa = NewsLetterPageAction(drv)
        logger.info("NewsLetterPageAction object created")

        nlpa.click_yes_on_subscribe_rb()
        logger.info("Selected Yes radio button for newsletter subscription")

        result = apa.succes_msg_update_newsLetter()
        logger.info(f"Newsletter subscription update result: {result}")

        assert result is True

        logger.info("Test passed: Newsletter subscription updated successfully")
