from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

from pages.ShopbyCategoryPage import ShopByCategoryPage
from utils.loggerCreator import get_logger

logger = get_logger(__name__)

class ShopByCategoryAction:

    def __init__(self, driver):
        self.driver = driver
        self.page = ShopByCategoryPage()
        self.wait = WebDriverWait(driver, 20)

    def launch_url(self, url):
        try:
            logger.info(f"Launching URL: {url}")
            self.driver.get(url)

            is_headless = os.getenv("CI", "").lower() == "true"
            if not is_headless:
                self.driver.maximize_window()

            logger.info("Application launched successfully")

        except Exception as e:
            logger.error(f"Failed to launch application: {e}")
            raise

    def click_shop_by_category(self):
        try:
            logger.info("Clicking Shop By Category menu")
            element = self.wait.until(EC.presence_of_element_located(self.page.SHOP_BY_CATEGORY_MENU))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)
            logger.info("Successfully clicked Shop By Category menu")

        except Exception as e:
            logger.error(f"Unable to click Shop By Category menu: {e}")
            raise

    def select_category(self, category):
        try:
            logger.info(f"Selecting category: {category}")

            if category.lower() == "desktops & monitors":
                locator = self.page.DESKTOPS_CATEGORY

            elif category.lower() == "web cameras":
                locator = self.page.CAMERAS

            elif category.lower() == "phone, tablets & ipod":
                locator = self.page.TABLETS

            elif category.lower() == "laptops & notebooks":
                locator = self.page.LAPTOPS

            else:
                logger.error(f"Invalid category: {category}")
                raise ValueError(f"Invalid category: {category}")

            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            logger.info(f"Successfully selected category: {category}")

        except Exception as e:
            logger.error(f"Failed to select category '{category}': {e}")
            raise

    def get_page_title(self):
        try:
            title = self.driver.title
            logger.info(f"Page title fetched successfully: {title}")
            return title
        except Exception as e:
            logger.error(f"Unable to fetch page title: {e}")
            raise