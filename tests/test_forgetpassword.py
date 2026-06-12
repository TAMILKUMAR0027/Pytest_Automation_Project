import pytest
from actions.Forgetpasswordpageaction import Forgetpasswordpageaction
from utils.configReader import ConfigReader

@pytest.mark.Jothika
class TestForgetpassword:
    def test_forgetpassword(self, driver):
        drv, wait = driver
        fpa=Forgetpasswordpageaction(drv)
       
        url=ConfigReader.get_url()
        fpa.clickMyaccount()
        fpa.clicklogin()
        fpa.clickForgetpassword()
        fpa.enterEmail()
        fpa.clicksubmit()
        fpa.successmsg()
      
    
    def test_invalidforgetpassword(self,driver):
        drv,wait=driver
        fpa=Forgetpasswordpageaction(drv)
       
        url=ConfigReader.get_url()
        fpa.clickMyaccount()
        fpa.clicklogin()
        fpa.clickForgetpassword()
        fpa.enterEmail()
        fpa.clicksubmit()
       
        fpa.warningmessage()