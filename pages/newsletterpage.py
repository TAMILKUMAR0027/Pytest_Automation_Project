from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class NewsLetterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    yesRadioButton = (By.XPATH, "//label[@for='input-newsletter-yes']")
    noRadioButton = (By.XPATH, "//label[@for='input-newsletter-no']")
    continueButton = (
        By.XPATH,
        "//div[@class='buttons clearfix']/child::div[2]/child::input",
    )
