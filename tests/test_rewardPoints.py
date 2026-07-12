import pytest
from actions.HomePageAction import HomePageAction
from actions.accountpageaction import AccountPageAction
from actions.loginpageaction import LoginPageAction
from utils.excelReader import get_data
from utils.loggerCreator import get_logger

logger = get_logger(__name__)


@pytest.mark.Rishwanth
class TestRewardPoints:

    @pytest.mark.parametrize(
        "username,password",
        get_data(
            "data_provider/DataProvider.xlsx",
            "loginDataValid",
        ),
    )
    def test_rewardPoints(self, driver, username, password):
        logger.info("Starting test: Reward Points")

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

        apa.rewardPointsLinkClick()
        logger.info("Clicked on Reward Points link")

        result = apa.assertRewardPoitPageRedirection()
        logger.info(f"Reward Points page assertion result: {result}")

        assert result is True

        logger.info("Test passed: Reward Points page verified successfully")
