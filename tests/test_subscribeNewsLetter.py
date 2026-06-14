import pytest
from actions.accountpageaction import AccountPageAction
from actions.newsletterpageaction import NewsLetterPageAction
from actions.HomePageAction import HomePageAction
from actions.loginpageaction import LoginPageAction
from utils.excelReader import get_data
from utils.loggerCreator import get_logger


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
        drv, wait = driver
        hp = HomePageAction(drv)
        hp.click_myAcc()

        lp = LoginPageAction(drv)
        lp.enter_login_credentials(username, password)

        apa = AccountPageAction(drv)
        apa.click_subscribe_newsLetter()

        nlpa = NewsLetterPageAction(drv)
        nlpa.click_yes_on_subscribe_rb()
        assert apa.succes_msg_update_newsLetter() is True
