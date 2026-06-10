import logging
from selenium.webdriver.common.by import By

logger = logging.getLogger(__name__)


class LaunchPages:
    """Page class for homepage verification"""

    # Locators
    LOGO = (By.XPATH, "//img[@alt='Poco Electro']")

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self) -> str:
        url = self.driver.current_url
        logger.info("Current URL: %s", url)
        return url

    def get_page_title(self) -> str:
        title = self.driver.title
        logger.info("Page Title: %s", title)
        return title

    def get_logo(self) -> bool:
        is_displayed = self.driver.find_element(*self.LOGO).is_displayed()
        logger.info("Logo displayed: %s", is_displayed)
        return is_displayed