import pytest
from actions.Forgetpasswordpageaction import Forgetpasswordpageaction
from utils.configReader import ConfigReader
from utils import loggerCreator



logger=loggerCreator.get_logger(__name__)
@pytest.mark.Jothika
class TestForgetpassword:


    def test_forgetpassword(self, driver):
        drv, wait = driver
        fpa=Forgetpasswordpageaction(drv)
       
        url=ConfigReader.get_url()
        logger.info("Application launched successfully")
        fpa.clickMyaccount()
        logger.info("Clicked Myaccount")
        fpa.clicklogin()
        fpa.clickForgetpassword()
        logger.info("Selected forgetpassword option")
        fpa.enterEmail()
        logger.info("Passed valid email")
        fpa.clicksubmit()
        fpa.successmsg()
        logger.info("Received success message")
      
    
    def test_invalidforgetpassword(self,driver):
        drv,wait=driver
        fpa=Forgetpasswordpageaction(drv)
       
        url=ConfigReader.get_url()
        logger.info("Launched application successfully")
        fpa.clickMyaccount()
        fpa.clicklogin()
        fpa.clickForgetpassword()
        fpa.enterInvalidEmail()
        logger.info("Passed invalid email")
        fpa.clicksubmit()
        logger.info("Submitted the email")
        fpa.warningmessage()
        logger.info("Received a warning message")