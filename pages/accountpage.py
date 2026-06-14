from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    accountLoginSuccess = (By.XPATH, "//h2[text()='My Account']")
    subscribe_newsletter = (
        By.XPATH,
        "//div[@class='row']/child::div[5]/child::a[contains(text(),'Subscribe')]",
    )
    subscribeUpdate_Succ_msg = (By.XPATH, "//div[@id='account-account']/child::div[1]")
    editAccInfo = (By.XPATH, "//a[normalize-space()='Edit your account information']")
    telephoneEdit = (By.XPATH, "//input[@id='input-telephone']")
    editContinue = (By.XPATH, "//input[@value='Continue']")
    editSuccessMsg = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
