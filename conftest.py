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

        cls._clear_stale_locks()

        browser = ConfigReader.get_browser().lower()
        mode = ConfigReader.get_mode().lower()

        # Force headless in CI
        if os.getenv("CI", "").lower() == "true":
            mode = "headless"

        url = ConfigReader.get_url()

        if not url or not url.startswith(("http://", "https://")):
            raise ValueError(f"Invalid URL: {url}")

        logger.info(f"Config → browser={browser} | mode={mode} | url={url}")

        # =========================
        # CHROME SETUP (FIXED)
        # =========================
        if browser == "chrome":

            options = ChromeOptions()

            # ===== CRITICAL CI STABILITY FLAGS =====
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--remote-allow-origins=*")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-popup-blocking")

            # prevent automation detection instability
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option("useAutomationExtension", False)

            prefs = {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.default_content_setting_values.notifications": 2
            }
            options.add_experimental_option("prefs", prefs)

            # ===== HEADLESS / NORMAL MODE =====
            if mode == "headless":
                options.add_argument("--headless=new")
                options.add_argument("--window-size=1920,1080")
                options.add_argument("--remote-debugging-port=9222")
            else:
                options.add_argument("--start-maximized")

            # start driver
            service = ChromeService(ChromeDriverManager().install())

            try:
                cls.driver = webdriver.Chrome(service=service, options=options)
                logger.info("Chrome browser launched successfully")
            except Exception as e:
                logger.error(f"Chrome launch failed: {e}")
                raise

        # =========================
        # FIREFOX SETUP
        # =========================
        elif browser == "firefox":

            options = FirefoxOptions()

            if mode == "headless":
                options.add_argument("--headless")

            service = FirefoxService(GeckoDriverManager().install())

            cls.driver = webdriver.Firefox(service=service, options=options)

            if mode != "headless":
                cls.driver.maximize_window()

            logger.info("Firefox browser launched successfully")

        else:
            raise ValueError(f"Unsupported browser: {browser}")

        # =========================
        # COMMON SETTINGS
        # =========================
        cls.driver.set_page_load_timeout(ConfigReader.get_page_load_timeout())
        cls.driver.set_script_timeout(30)

        # open URL
        logger.info(f"Launching URL: {url}")
        cls.driver.get(url)

        # explicit wait
        cls.wait = WebDriverWait(cls.driver, ConfigReader.get_explicit_wait())

        return cls.driver, cls.wait

    @classmethod
    def teardown(cls):
        try:
            if cls.driver:
                logger.info("Closing browser")
                cls.driver.quit()
                cls.driver = None
                cls.wait = None
        except Exception as e:
            logger.error(f"Error closing browser: {e}")


# =========================
# PYTEST FIXTURE
# =========================
@pytest.fixture(scope="function")
def driver(request):

    drv, wait = DriverSetup.setup()

    if request.cls is not None:
        request.cls.driver = drv
        request.cls.wait = wait

    yield drv, wait

    DriverSetup.teardown()
