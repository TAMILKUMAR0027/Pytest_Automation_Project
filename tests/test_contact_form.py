import uuid

import pytest

from pages.launch import LaunchPages
from pages.addons_page import AddOnsPage
from utils.configReader import ConfigReader
from utils.loggerCreator import get_logger


logger = get_logger(__name__)


def _log_browser_console_errors(driver):
    """Best-effort dump of JS console errors. Only works on Chromium-based
    drivers (Firefox/geckodriver doesn't support get_log('browser')), so
    this is wrapped defensively and never fails the test on its own."""
    try:
        for entry in driver.get_log("browser"):
            if entry.get("level") == "SEVERE":
                logger.warning("Browser console error: %s", entry.get("message"))
    except Exception:
        # Not supported on this driver (e.g. Firefox) - safe to ignore.
        pass


class TestContactForm:

    @pytest.mark.smoke
    @pytest.mark.Prasanna
    def test_contact_form_success_message(self, driver):
        drv, wait = driver

        launch_page = LaunchPages(drv, wait)
        
        addons_page = AddOnsPage(drv, wait)

        url = ConfigReader.get_url()

        logger.info("Launching application URL: %s", url)
        launch_page.launch_application(url)

        logger.info("Clicking AddOns link")
        addons_page.click_addons_link()

        logger.info("Clicking Widgets button")
        addons_page.click_widgets_button()

        # Unique email per run avoids any server-side duplicate-submission
        # handling silently no-op'ing repeat submissions with the same data.
        unique_email = f"test+{uuid.uuid4().hex[:8]}@gmail.com"

        logger.info("Entering contact form details")
        addons_page.enter_name("Prasanna")
        addons_page.enter_email(unique_email)
        addons_page.enter_subject("Automation Testing")
        addons_page.enter_message("This is a test enquiry message")

        logger.info("Submitting contact form")
        addons_page.click_submit(logger=logger)

        try:
            actual_message = addons_page.get_success_message()
        finally:
            _log_browser_console_errors(drv)

        expected_message = "Your enquiry has been successfully sent to the store owner!"

        logger.info("Expected Message: %s", expected_message)
        logger.info("Actual Message  : %s", actual_message)

        assert expected_message in actual_message, "Success message is not displayed"

        logger.info("Contact form submitted successfully")

    @pytest.mark.regression
    @pytest.mark.Prasanna
    def test_contact_form_invalid_email_validation(self, driver):
        drv, wait = driver

        launch_page = LaunchPages(drv, wait)
        addons_page = AddOnsPage(drv, wait)

        url = ConfigReader.get_url()

        logger.info("Launching application URL: %s", url)
        launch_page.launch_application(url)

        logger.info("Clicking AddOns link")
        addons_page.click_addons_link()

        logger.info("Clicking Widgets button")
        addons_page.click_widgets_button()

        logger.info("Entering contact form details with invalid email")
        addons_page.enter_name("Prasanna")
        addons_page.enter_email("invalidemail")
        addons_page.enter_subject("Automation Testing")
        addons_page.enter_message("This is invalid email validation test")

        logger.info("Submitting contact form")
        addons_page.click_submit(logger=logger)

        try:
            actual_error = addons_page.get_email_error_message()
        finally:
            _log_browser_console_errors(drv)

        expected_error = "E-Mail Address does not appear to be valid!"

        logger.info("Expected Error: %s", expected_error)
        logger.info("Actual Error  : %s", actual_error)

        assert expected_error in actual_error, "Email validation error is not displayed"

        logger.info("Invalid email validation verified successfully")