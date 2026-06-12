import os
import glob
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from utils.configReader import ConfigReader
from utils.loggerCreator import get_logger

logger = get_logger(__name__)


class DriverSetup:
    """Centralized WebDriver setup."""

    driver = None
    wait = None

    @staticmethod
    def _clear_stale_locks():
        """Remove stale webdriver-manager lock files."""
        lock_pattern = os.path.join(
            os.path.expanduser("~"),
            ".wdm",
            ".wdm-lock-*"
        )

        for lock_file in glob.glob(lock_pattern):
            try:
                os.remove(lock_file)
                logger.info(f"Removed stale WDM lock: {lock_file}")
            except OSError:
                pass

    @classmethod
    def setup(cls):
        """Creates WebDriver, opens URL, and returns driver + wait."""

        cls._clear_stale_locks()

        browser = ConfigReader.get_browser().lower()
        mode = ConfigReader.get_mode().lower()

        if mode == "normal" and os.getenv("CI", "").lower() == "true":
            mode = "headless"

        url = ConfigReader.get_url()

        if not url or not url.startswith(("http://", "https://")):
            raise ValueError(
                f"Invalid URL from config.ini: '{url}'"
            )

        logger.info(
            f"Config → browser={browser} | mode={mode} | url={url}"
        )

        # =====================================================
        # CHROME
        # =====================================================

        if browser == "chrome":

            options = ChromeOptions()

            # Browser Stability
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--remote-allow-origins=*")

            # Disable Notifications & Popups
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-popup-blocking")

            # Disable Automation Banner
            options.add_experimental_option(
                "excludeSwitches",
                ["enable-automation"]
            )

            options.add_experimental_option(
                "useAutomationExtension",
                False
            )

            # Chrome Preferences
            prefs = {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.password_manager_leak_detection": False,
                "profile.default_content_setting_values.notifications": 2
            }

            options.add_experimental_option("prefs", prefs)

            # Headless / Normal Mode
            if mode == "headless":
                options.add_argument("--headless=new")
                options.add_argument("--window-size=1920,1080")
            else:
                options.add_argument("--start-maximized")

            cls.driver = webdriver.Chrome(
                service=ChromeService(
                    ChromeDriverManager().install()
                ),
                options=options
            )

            logger.info("Chrome Browser Launched Successfully")

        # =====================================================
        # FIREFOX
        # =====================================================

        elif browser == "firefox":

            options = FirefoxOptions()

            if mode == "headless":
                options.add_argument("--headless")
                options.add_argument("--width=1920")
                options.add_argument("--height=1080")

            cls.driver = webdriver.Firefox(
                service=FirefoxService(
                    GeckoDriverManager().install()
                ),
                options=options
            )

            if mode != "headless":
                cls.driver.maximize_window()

            logger.info("Firefox Browser Launched Successfully")

        # =====================================================
        # INVALID BROWSER
        # =====================================================

        else:
            logger.error(f"Invalid Browser Name: {browser}")

            raise ValueError(
                f"Unsupported browser '{browser}'. "
                f"Use chrome or firefox."
            )

        # =====================================================
        # COMMON SETTINGS
        # =====================================================

        # Optional (recommended to keep disabled if using explicit waits)
        # cls.driver.implicitly_wait(10)

        cls.driver.set_page_load_timeout(
            ConfigReader.get_page_load_timeout()
        )

        cls.driver.set_script_timeout(30)

        if mode != "headless":
            cls.driver.maximize_window()

        # Launch URL
        logger.info(f"Launching URL: {url}")
        cls.driver.get(url)

        # Explicit Wait
        cls.wait = WebDriverWait(
            cls.driver,
            ConfigReader.get_explicit_wait()
        )

        logger.info(
            f"Driver started → browser={browser} | mode={mode}"
        )

        return cls.driver, cls.wait

    @classmethod
    def teardown(cls):
        """Quit driver."""

        try:
            if cls.driver:
                logger.info("Quitting driver.")
                cls.driver.quit()

                cls.driver = None
                cls.wait = None

        except Exception as e:
            logger.error(
                f"Error while closing browser: {str(e)}"
            )


# ============================================================
# PYTEST FIXTURE
# ============================================================

@pytest.fixture(scope="function")
def driver(request):
    """
    Usage:

    def test_example(driver):
        drv, wait = driver
    """

    drv, wait = DriverSetup.setup()

    if request.cls is not None:
        request.cls.driver = drv
        request.cls.wait = wait

    yield drv, wait

    DriverSetup.teardown()
