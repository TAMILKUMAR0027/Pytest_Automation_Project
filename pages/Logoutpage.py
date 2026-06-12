from selenium.webdriver.common.by import By
from pages import BasePage

class LogoutPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
    
    myaccount=(By.XPATH,"//i[@class='icon fas fa-user']/parent::a")
    