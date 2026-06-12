import logging
import pytest
from pages.launch import LaunchPages
from utils.configReader import ConfigReader

logger = logging.getLogger(__name__)


class TestHome:

    @pytest.mark.smoke
    @pytest.mark.Prasanna
    def test_homepage_verification(self, driver):
        """
        Single comprehensive test for homepage.
        URL is automatically launched by the fixture.
        """
        drv, wait = driver         
        lp = LaunchPages(drv)

        url = ConfigReader.get_url()

        logger.info("Verifying homepage after automatic launch...")

        # 1. Verify Correct URL
        actual_url = lp.get_current_url()
        logger.info("Expected URL : %s", url)
        logger.info("Actual URL   : %s", actual_url)
        assert actual_url == url, (
            f"URL mismatch!\n  Expected : {url}\n  Actual   : {actual_url}"
        )

        # 2. Verify Page Title
        actual_title = lp.get_page_title()
        logger.info("Page Title: %s", actual_title)
        assert "Your Store" in actual_title, (
            f"Page title mismatch. Actual Title: {actual_title}"
        )

        # 3. Verify Application Logo is displayed
        logo_displayed = lp.get_logo()
        logger.info("Logo displayed: %s", logo_displayed)
        assert logo_displayed, "Logo is NOT displayed on the homepage"

        logger.info(" All homepage verifications passed successfully!") 