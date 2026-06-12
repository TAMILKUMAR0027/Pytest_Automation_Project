import os
import glob
import subprocess
import platform

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
    driver = None
    wait = None

    @staticmethod
    def _clear_stale_locks():
        lock_pattern = os.path.join(
            os.path.expanduser("~"),
            ".wdm",
            ".wdm-lock-*"
        )

        for lock_file in glob.glob(lock_pattern):
            try:
                os.remove(lock_file)
                logger.info(f"Removed stale lock file: {lock_file}")
            except OSError:
                pass

    @staticmethod
    def _kill_stale_processes():
        try:
            if platform.system().lower() == "windows":
                subprocess.run(
                    ["taskkill", "/F", "/IM", "chrome.exe"],
                    capture_output=True
                )
                subprocess.run(
                    ["taskkill", "/F", "/IM", "chromedriver.exe"],
                    capture_output=True
                )

                logger.info(
                    "Killed stale Chrome and ChromeDriver processes"
                )

        except Exception as e:
            logger.warning(
                f"Unable to kill stale processes: {str(e)}"
            )

    @classmethod
    def setup(cls):
        cls._clear_stale_locks()
        cls._kill_stale_processes()

        browser = ConfigReader.get_browser().lower()
        mode = ConfigReader.get_mode().lower()
        url = ConfigReader.get_url()

        if os.getenv("CI", "").lower() == "true":
            mode = "headless"

        if not url or not url.startswith(("http://", "https://")):
            raise ValueError(
                f"Invalid URL in config.ini: {url}"
            )

        logger.info(
            f"Config -> browser={browser} | mode={mode} | url={url}"
        )

        # ======================
        # CHROME
        # ======================
        if browser == "chrome":

            options = ChromeOptions()

            if mode == "headless":
                options.add_argument("--headless=new")
                options.add_argument("--window-size=1920,1080")

            else:
                options.add_argument("--start-maximized")

            # Stability options
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-software-rasterizer")
            options.add_argument("--disable-background-networking")
            options.add_argument("--disable-renderer-backgrounding")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-popup-blocking")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-infobars")
            options.add_argument(
                "--disable-blink-features=AutomationControlled"
            )

            # IMPORTANT:
            # Removed fixed debugging port
            # options.add_argument("--remote-debugging-port=9222")

            options.add_experimental_option(
                "excludeSwitches",
                ["enable-automation"]
            )

            options.add_experimental_option(
                "useAutomationExtension",
                False
            )

            prefs = {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.password_manager_leak_detection": False,
                "profile.default_content_setting_values.notifications": 2
            }

            options.add_experimental_option(
                "prefs",
                prefs
            )

            driver_path = ChromeDriverManager().install()

            logger.info(
                f"ChromeDriver downloaded at: {driver_path}"
            )

            service = ChromeService(driver_path)

            cls.driver = webdriver.Chrome(
                service=service,
                options=options
            )

            logger.info(
                "Chrome browser launched successfully"
            )

        # ======================
        # FIREFOX
        # ======================
        elif browser == "firefox":

            options = FirefoxOptions()

            if mode == "headless":
                options.add_argument("--headless")
                options.add_argument("--width=1920")
                options.add_argument("--height=1080")

            service = FirefoxService(
                GeckoDriverManager().install()
            )

            cls.driver = webdriver.Firefox(
                service=service,
                options=options
            )

            if mode != "headless":
                cls.driver.maximize_window()

            logger.info(
                "Firefox browser launched successfully"
            )

        else:
            raise ValueError(
                f"Unsupported browser: {browser}"
            )

        cls.driver.set_page_load_timeout(
            ConfigReader.get_page_load_timeout()
        )

        cls.driver.set_script_timeout(30)

        if mode != "headless":
            cls.driver.maximize_window()

        logger.info(f"Launching URL: {url}")

        cls.driver.get(url)

        cls.wait = WebDriverWait(
            cls.driver,
            ConfigReader.get_explicit_wait()
        )

        logger.info(
            f"Driver started successfully -> "
            f"browser={browser}, mode={mode}"
        )

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
            logger.error(
                f"Error while closing browser: {str(e)}"
            )


@pytest.fixture(scope="function")
def driver(request):

    drv, wait = DriverSetup.setup()

    if request.cls:
        request.cls.driver = drv
        request.cls.wait = wait

    yield drv, wait

    DriverSetup.teardown()
