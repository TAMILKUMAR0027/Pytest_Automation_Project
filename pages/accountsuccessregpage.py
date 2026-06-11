from selenium.webdriver.common.by import By


class RegAccSuccPage:
    def __init__(self, driver):
        self.driver = driver
        self.regSuccess = (By.XPATH, "//div[@id='content']/child::h1")
