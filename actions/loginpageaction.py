from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from pages.loginpage import LoginPage


class LoginPageAction:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.lp = LoginPage(driver)

    def click_register_continue(self):
        self.wait.until(ec.visibility_of_element_located(self.lp.rcontinue)).click()
