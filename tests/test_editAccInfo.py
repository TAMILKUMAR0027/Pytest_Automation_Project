import pytest
from actions.HomePageAction import HomePageAction
from utils.excelReader import get_data
from actions.accountpageaction import AccountPageAction
from actions.launch_actions import LaunchActions
from actions.loginpageaction import LoginPageAction
from utils.configReader import ConfigReader


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
        drv, wait = driver
        telephone = ConfigReader.get_register_data("telephone")
        hp = HomePageAction(drv)
        hp.click_myAcc()

        lp = LoginPageAction(drv)
        lp.enter_login_credentials(username, password)

        apa = AccountPageAction(drv)
        assert apa.click_editAccount_info(telephone) is True
