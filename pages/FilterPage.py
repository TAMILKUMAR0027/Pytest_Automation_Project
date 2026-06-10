from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class FilterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    Manufacture=By.XPATH,"//label[@for='mz-fm-0-8']"
    iPodProduct=By.XPATH,"//div[@class='carousel-item active']//img[@title='iPod Touch']"
    