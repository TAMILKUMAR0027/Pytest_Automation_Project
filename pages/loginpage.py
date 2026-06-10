from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.rcontinue = (By.XPATH, "//h2[text()='New Customer']/following-sibling::a")
