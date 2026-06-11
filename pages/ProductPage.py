from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    brand=By.XPATH,"//ul[@class='list-unstyled m-0']//a[contains(text(),'Apple')]"
    instock=By.XPATH,"//span[@class='badge badge-success']"