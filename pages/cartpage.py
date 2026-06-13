from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    cartProduct = (
        By.XPATH,
        "//td[@class='text-left']//a[contains(text(),'HP LP3065')]",
    )

    quantity_input = (By.XPATH, "//input[contains(@name,'quantity')]")
    quantity_update = (
        By.XPATH,
        "//button[@type='submit' and contains(@class,'btn-primary')]",
    )
    quantity_update_success = (
        By.CSS_SELECTOR,
        ".alert.alert-success.alert-dismissible",
    )
