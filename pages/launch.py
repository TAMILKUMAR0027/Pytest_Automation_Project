"""Page object for the homepage / launch verification."""

from selenium.webdriver.common.by import By


class LaunchPages:
    """Page Object for Home Page."""

    # Logo
    LOGO = (By.XPATH, "//img[@alt='Poco Electro']")

    # Products
    TOP_COLLECTION_PRODUCT = (
        By.XPATH,
        "//div[@class='swiper-wrapper']//a[@id='mz-product-listing-image-39218404-0-3']//div[@class='carousel-item active']//img[@title='HP LP3065']",
    )

    def __init__(self, driver):
        self.driver = driver

    def launch_application(self, url):
        """Launch the application."""
        self.driver.get(url)

    def get_current_url(self):
        """Return the current browser URL."""
        return self.driver.current_url

    def get_page_title(self):
        """Return the current page title."""
        return self.driver.title

    def get_logo(self):
        """Return True if the application logo is displayed."""
        elements = self.driver.find_elements(*self.LOGO)
        return len(elements) > 0 and elements[0].is_displayed()

    def is_top_collection_product_displayed(self):
        """Return True if the Top Collection product is displayed."""
        elements = self.driver.find_elements(*self.TOP_COLLECTION_PRODUCT)
        return len(elements) > 0 and elements[0].is_displayed()