"""Page object for the homepage / launch verification."""

from selenium.webdriver.common.by import By


class LaunchPages:
    """Locators and simple accessors for the homepage."""

    LOGO = (By.XPATH, "//img[@alt='Poco Electro']")

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """Return the current browser URL."""
        return self.driver.current_url

    def get_page_title(self):
        """Return the current page title."""
        return self.driver.title

    def get_logo(self):
        """Return True if the application logo is displayed."""
        elements = self.driver.find_elements(*self.LOGO)
        return bool(elements) and elements[0].is_displayed()