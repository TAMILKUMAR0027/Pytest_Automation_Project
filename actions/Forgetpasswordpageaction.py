from pages.Forgetpasswordpage import Forgetpasswordpage
from actions.BaseAction import BaseAction
from actions.HomePageAction import HomePageAction
from utils.configReader import ConfigReader

class Forgetpasswordpageaction(BaseAction):
    def __init__(self,driver):
        super().__init__(driver)
        self.fp=Forgetpasswordpage(driver)
        self.homepage=HomePageAction(driver)

    
    
    def clickMyaccount(self):
        self.homepage.click_myAcc()
    def clicklogin(self):
        self.click(self.fp.login)
    def clickForgetpassword(self):
        self.click(self.fp.forgetpassword)
    def enterEmail(self):
        email=ConfigReader.get_validemail()
        self.send_keys(self.fp.email,email)
    def enterInvalidEmail(self):
        invalidemail=ConfigReader.get_invalidemail()
        self.send_keys(self.fp.email,invalidemail)

    def clicksubmit(self):
        self.click(self.fp.button)
    def successmsg(self):
        actual=self.get_text(self.fp.message)
        expected=ConfigReader.get_message()
        assert actual==expected

    def warningmessage(self):
        actual=self.get_text(self.fp.warningmsg)
        expected=ConfigReader.get_warning()
        assert actual==expected
