from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.fname = (By.XPATH, "//input[@name='firstname']")
        self.lname = (By.XPATH, "//input[@name='lastname']")
        self.email = (By.XPATH, "//input[@name='email']")
        self.telephone = (By.XPATH, "//input[@name='telephone']")
        self.password = (By.XPATH, "//input[@name='password']")
        self.cpassword = (By.XPATH, "//input[@name='confirm']")
        self.privacyCB = (By.XPATH, "//label[@for='input-agree']")
        self.regContinue = (By.XPATH, "//input[@value='Continue']")
        self.regFail = (
            By.XPATH,
            "//div[@class='alert alert-danger alert-dismissible']",
        )
        self.privacyPolicy_msg = (
            By.CSS_SELECTOR,
            ".alert.alert-danger.alert-dismissible",
        )
