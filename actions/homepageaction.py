from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from pages.homepage import HomePage


class HomePageAction:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.hp = HomePage(driver)

    def click_myAcc(self):
        self.wait.until(ec.visibility_of_element_located(self.hp.myAccLink)).click()
