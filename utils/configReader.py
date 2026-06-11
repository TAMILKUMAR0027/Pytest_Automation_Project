import configparser
import os


class ConfigReader:
    """
    Reads values from configuration/config.ini.

    Usage:
        from configuration.configReader import ConfigReader
        url = ConfigReader.get_url()
    """

    _config = None
    _config_path = os.path.join(os.path.dirname(__file__),r"E:\Pytest_Automation\configuration\config.ini")

    @classmethod
    def _load(cls):
        if cls._config is None:
            cls._config = configparser.ConfigParser()
            cls._config.read(cls._config_path)
        return cls._config

    @classmethod
    def get(cls, section: str, key: str) -> str:
        return cls._load().get(section, key)

    # ── Application ──────────────────────────────────────────
    @classmethod
    def get_url(cls) -> str:
        return cls.get("application", "url")

    @classmethod
    def get_title(cls) -> str:
        return cls.get("application", "title")

    # ── Browser ───────────────────────────────────────────────
    @classmethod
    def get_browser(cls) -> str:
        """Returns: chrome | firefox"""
        return cls.get("browser", "browser").lower().strip()

    @classmethod
    def get_mode(cls) -> str:
        """Returns: normal | headless"""
        return cls.get("browser", "mode").lower().strip()

    # ── Timeouts ──────────────────────────────────────────────
    @classmethod
    def get_explicit_wait(cls) -> int:
        return int(cls.get("timeouts", "explicit_wait"))

    @classmethod
    def get_page_load_timeout(cls) -> int:
        return int(cls.get("timeouts", "page_load_timeout"))

