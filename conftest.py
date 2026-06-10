import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from configuration.configReader import ConfigReader
from utils.loggerCreator import get_logger

logger = get_logger(__name__)


class DriverSetup:
    """Centralized WebDriver setup."""

    driver = None
    wait   = None

    @classmethod
    def setup(cls):
        """Creates WebDriver, opens the URL from config.ini, and creates WebDriverWait."""
        browser = ConfigReader.get_browser()
        mode    = ConfigReader.get_mode()
        url     = ConfigReader.get_url()

        # ── Chrome ────────────────────────────────────────────
        if browser == "chrome":
            options = ChromeOptions()
            if mode == "headless":
                options.add_argument("--headless=new")
                options.add_argument("--disable-gpu")
            options.add_argument("--start-maximized")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            cls.driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=options,
            )

        # ── Firefox ───────────────────────────────────────────
        elif browser == "firefox":
            options = FirefoxOptions()
            if mode == "headless":
                options.add_argument("--headless")
            cls.driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=options,
            )
            if mode != "headless":
                cls.driver.maximize_window()

        else:
            raise ValueError(
                f"Unsupported browser '{browser}'. "
                "Set browser = chrome or firefox in config.ini"
            )

        # ── Timeouts ──────────────────────────────────────────
        cls.driver.implicitly_wait(ConfigReader.get_implicit_wait())
        cls.driver.set_page_load_timeout(ConfigReader.get_page_load_timeout())

        # ── Launch URL ────────────────────────────────────────
        logger.info("Launching URL: %s", url)
        cls.driver.get(url)

        # ── Explicit Wait ─────────────────────────────────────
        cls.wait = WebDriverWait(cls.driver, ConfigReader.get_explicit_wait())

        logger.info("Driver started → browser=%s, mode=%s", browser, mode)
        return cls.driver, cls.wait

    @classmethod
    def teardown(cls):
        """Quits the driver and resets state."""
        if cls.driver:
            logger.info("Quitting driver.")
            cls.driver.quit()
            cls.driver = None
            cls.wait   = None


# ─────────────────────────────────────────────────────────────
# Fixtures
# ─────────────────────────────────────────────────────────────

@pytest.fixture(scope="function")
def driver(request):
    """
    Yields (driver, wait) for each test.
    URL is launched automatically from config.ini.

    Usage:
        def test_something(driver):
            drv, wait = driver
            wait.until(EC.title_contains("Your Store"))
    """
    drv, wait = DriverSetup.setup()

    # Inject into test class if used inside a class
    if request.cls is not None:
        request.cls.driver = drv
        request.cls.wait   = wait

    yield drv, wait

    DriverSetup.teardown()