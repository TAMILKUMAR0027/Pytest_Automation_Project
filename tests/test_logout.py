import pytest
from actions.Logoutpageaction import Logoutpageaction
from utils.configReader import ConfigReader
from utils import loggerCreator



logger=loggerCreator.get_logger(__name__)
@pytest.mark.Jothika
class TestLogout:


    def test_logout(self, driver):
        drv, wait = driver
        lga=Logoutpageaction(drv)

        url=ConfigReader.get_url()
        logger.info("Application launch successful")
        lga.clickaccount()
        lga.login()
        logger.info("Entering login credentials")
        lga.successlogin()
        
        logger.info("Login successful")
        lga.moveto_myaccount()
        logger.info("Moved to Myaccount")
        lga.clicklogout()
        logger.info("Clicked Logout button")
        lga.logoutsuccess()
        logger.info("Logged out successfully")