from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    ShopByCategory = By.XPATH, "//a[normalize-space()='Shop by Category']"
    Monitor = By.XPATH, "//span[normalize-space()='Desktops and Monitors']"
    myAccLink = (
        By.XPATH,
        "//div[@class='info']/preceding-sibling::i[@class='icon fas fa-user']",
    )
