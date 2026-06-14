from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class ComparePage(BasePage):

    Compare_Message = (
        By.XPATH,
        "//p[normalize-space()='You have not chosen any products to compare.']"
    )

    def __init__(self, driver):
        super().__init__(driver)