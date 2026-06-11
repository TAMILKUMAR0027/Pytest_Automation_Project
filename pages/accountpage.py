from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    accountLoginSuccess = (By.XPATH, "//h2[text()='My Account']")
