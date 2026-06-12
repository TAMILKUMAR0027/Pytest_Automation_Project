from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.ShopbyCategoryPage import ShopByCategoryPage


class ShopByCategoryAction:

    def __init__(self, driver):
        self.driver = driver
        self.page = ShopByCategoryPage()
        self.wait = WebDriverWait(driver, 20)

    def launch_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def click_shop_by_category(self):
        element = self.wait.until(
            EC.element_to_be_clickable(self.page.SHOP_BY_CATEGORY_MENU)
        )
        element.click()

    def select_category(self, category):

        if category.lower() == "desktops & monitors":
            locator = self.page.DESKTOPS_CATEGORY

        elif category.lower() == "web cameras":
            locator = self.page.CAMERAS

        elif category.lower() == "phone, tablets & ipod":
            locator = self.page.TABLETS

        elif category.lower() == "laptops & notebooks":
            locator = self.page.LAPTOPS

        else:
            raise ValueError(f"Invalid category: {category}")

        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def get_page_title(self):
        return self.driver.title