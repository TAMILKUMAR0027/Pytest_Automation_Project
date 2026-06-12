"""Action class for verifying initial application launch / homepage state."""

from pages.launch import LaunchPages
from actions.BaseAction import BaseAction
from utils.configReader import ConfigReader
from utils.loggerCreator import get_logger

logger = get_logger(__name__)

EXPECTED_TITLE_KEYWORD = "Your Store"


class LaunchActions(BaseAction):
    """High-level actions for validating the app launch / homepage."""

    def __init__(self, driver):
        super().__init__(driver)
        self.launch_page = LaunchPages(driver)

    def verify_homepage(self):
        """Verify URL, title, and logo on the launched homepage."""
        expected_url = ConfigReader.get_url()

        actual_url = self.launch_page.get_current_url()
        logger.info("Expected URL : %s", expected_url)
        logger.info("Actual URL   : %s", actual_url)
        if actual_url != expected_url:
            logger.error("URL mismatch! Expected: %s, Actual: %s", expected_url, actual_url)
        assert actual_url == expected_url, (
            f"URL mismatch!\n  Expected : {expected_url}\n  Actual   : {actual_url}"
        )

        actual_title = self.launch_page.get_page_title()
        logger.info("Page Title: %s", actual_title)
        assert EXPECTED_TITLE_KEYWORD in actual_title, (
            f"Page title mismatch. Actual Title: {actual_title}"
        )

        logo_displayed = self.launch_page.get_logo()
        logger.info("Logo displayed: %s", logo_displayed)
        assert logo_displayed, "Logo is NOT displayed on the homepage"

        logger.info("All homepage verifications passed successfully!")