from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.fname = (By.XPATH, "//input[@name='firstname']")
        self.lname = (By.XPATH, "//input[@name='lastname']")
        self.email = (By.XPATH, "//input[@name='email']")
        self.telephone = (By.XPATH, "//input[@name='telephone']")
        self.password = (By.XPATH, "//input[@name='password']")
        self.cpassword = (By.XPATH, "//input[@name='confirm']")
        self.privacyCB = (By.XPATH, "//input[@name='agree']")
        self.regContinue = (By.XPATH, "//input[@type='submit']")
