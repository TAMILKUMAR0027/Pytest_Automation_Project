from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class LogoutPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
    
    logout=By.XPATH, "//a[contains(@href,'route=account/logout')]"
    logoutmsg=By.XPATH,"//i[@class='fas fa-check-circle text-success']/parent::h1"