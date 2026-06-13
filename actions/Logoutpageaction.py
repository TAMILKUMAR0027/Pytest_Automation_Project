from pages.Logoutpage import LogoutPage
from actions.BaseAction import BaseAction
from actions.HomePageAction import HomePageAction
from actions.loginpageaction import LoginPageAction
from actions.accountpageaction import AccountPageAction
from pages.HomePage import HomePage
from utils.configReader import ConfigReader
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Logoutpageaction(BaseAction):
    def __init__(self, driver):
        super().__init__(driver)
        self.lp=LogoutPage(driver)
        self.hpa=HomePageAction(driver)
        self.lgnpa=LoginPageAction(driver)
        self.apa=AccountPageAction(driver)
        self.hp=HomePage(driver)
        
        
    def clickaccount(self):
        self.hpa.click_myAcc()
    def login(self):
        email=ConfigReader.get_mail()
        password=ConfigReader.get_pwd()
        self.lgnpa.enter_login_credentials(email,password)
    def successlogin(self):
       return self.apa.success_login()

    def moveto_myaccount(self):
        my_account = self.wait.until(EC.visibility_of_element_located(self.hp.myAccLink))
        ActionChains(self.driver).move_to_element(my_account).perform()
      
    def clicklogout(self):
       
        self.click(self.lp.logout)
    def logoutsuccess(self):
        self.is_displayed(self.lp.logoutmsg)
        