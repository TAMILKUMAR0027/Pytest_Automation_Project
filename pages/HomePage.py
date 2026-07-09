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
    Hp_Product = By.XPATH, "//a[@id='mz-product-listing-image-39218404-0-3']//div[@class='carousel-item active']//img[@title='HP LP3065']"
    Compare_Link = By.XPATH, "(//a[contains(@href,'product/compare')])[2]"
    Canon_Product = (
    By.XPATH,
    "//a[@id='mz-product-listing-image-39218404-0-0']//div[@class='carousel-item active']//img[@title='Canon EOS 5D']"
)
    