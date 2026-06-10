import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait

from configuration.configReader import ConfigReader
from utils.loggerCreator import get_logger

logger = get_logger(__name__)


class DriverSetup:
    driver = None
    wait = None

    @classmethod
    def setup(cls):
        browser = ConfigReader.get_browser()
        mode = ConfigReader.get_mode()
        url = ConfigReader.get_url()

        # ── CHROME ─────────────────────────────
        if browser == "chrome":
            options = ChromeOptions()

            if mode == "headless":
                options.add_argument("--headless=new")
                options.add_argument("--disable-gpu")

            options.add_argument("--start-maximized")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

            # ✅ FIX FOR TIMEOUT ISSUE
            options.page_load_strategy = "eager"

            cls.driver = webdriver.Chrome(options=options)

        # ── FIREFOX ────────────────────────────
        elif browser == "firefox":
            options = FirefoxOptions()

            if mode == "headless":
                options.add_argument("--headless")

            cls.driver = webdriver.Firefox(options=options)

            if mode != "headless":
                cls.driver.maximize_window()

        else:
            raise ValueError(f"Unsupported browser: {browser}")

        # ── TIMEOUTS ───────────────────────────
        cls.driver.set_page_load_timeout(ConfigReader.get_page_load_timeout())

        # ── OPEN URL (SAFE VERSION) ─────────────
        logger.info("Launching URL: %s", url)

        try:
            cls.driver.get(url)

        except Exception as e:
            logger.warning("Page load issue handled safely: %s", str(e))

        # ── WAIT FOR DOM READY ─────────────────
        WebDriverWait(cls.driver, 20).until(
            lambda d: d.execute_script("return document.readyState") in ["interactive", "complete"]
        )

        # ── EXPLICIT WAIT ──────────────────────
        cls.wait = WebDriverWait(cls.driver, ConfigReader.get_explicit_wait())

        return cls.driver, cls.wait

    @classmethod
    def teardown(cls):
        if cls.driver:
            logger.info("Closing browser")
            cls.driver.quit()
            cls.driver = None
            cls.wait = None


# ─────────────────────────────────────────────
# PYTEST FIXTURE
# ─────────────────────────────────────────────
@pytest.fixture(scope="function")
def driver(request):
    drv, wait = DriverSetup.setup()

    if request.cls is not None:
        request.cls.driver = drv
        request.cls.wait = wait

    yield drv, wait

    DriverSetup.teardown()