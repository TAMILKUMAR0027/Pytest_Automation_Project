import pytest

from actions.HomePageAction import HomePageAction
from actions.loginpageaction import LoginPageAction
from actions.accountpageaction import AccountPageAction
from utils.excelReader import get_data


@pytest.mark.parametrize(
    "username,password",
    get_data(
        "D:\Pytest_Automation_Project\Pytest_Automation_Project\data_provider\DataProvider.xlsx",
        "loginDataValid",
    ),
)
class TestLogin:
    @pytest.mark.Rishwanth
    def test_validLogin(self, driver, username, password):
        drv, wait = driver

        hp = HomePageAction(drv)
        hp.click_myAcc()

        lp = LoginPageAction(drv)
        lp.enter_login_credentials(username, password)

        apa = AccountPageAction(drv)

        assert apa.success_login() is True
