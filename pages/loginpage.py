from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.rcontinue = (By.XPATH, "//h2[text()='New Customer']/following-sibling::a")
