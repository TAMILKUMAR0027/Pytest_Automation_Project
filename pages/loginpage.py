from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    rcontinue = (By.XPATH, "//h2[text()='New Customer']/following-sibling::a")
    loginEmail = (By.XPATH, "//input[@name='email']")
    loginPassword = (By.XPATH, "//input[@name='password']")
    loginContinue = (By.XPATH, "//input[@type='submit']")
    invalidLoginErrorMsg = (
        By.XPATH,
        "//div[@id='account-login']/child::div[text()=' Warning: No match for E-Mail Address and/or Password.']",
    )
