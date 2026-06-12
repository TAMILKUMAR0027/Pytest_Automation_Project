import configparser
import os


class ConfigReader:
    """
    Reads values from configuration/config.ini

    Usage:
        url = ConfigReader.get_url()
        browser = ConfigReader.get_browser()
        fname = ConfigReader.get_register_data("fname")
    """

    _config = None

    _config_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "configuration", "config.ini"
    )

    @classmethod
    def _load(cls):
        if cls._config is None:
            cls._config = configparser.ConfigParser()
            cls._config.read(cls._config_path)

        return cls._config

    @classmethod
    def get(cls, section: str, key: str):
        return cls._load().get(section, key)

    # ─────────────────────────────────────────────
    # Application
    # ─────────────────────────────────────────────

    @classmethod
    def get_url(cls):
        return cls.get("application", "url")

    @classmethod
    def get_title(cls):
        return cls.get("application", "title")

    # ─────────────────────────────────────────────
    # Browser
    # ─────────────────────────────────────────────

    @classmethod
    def get_browser(cls):
        return cls.get("browser", "browser").lower().strip()

    @classmethod
    def get_mode(cls):
        return cls.get("browser", "mode").lower().strip()

    # ─────────────────────────────────────────────
    # Timeouts
    # ─────────────────────────────────────────────

    @classmethod
    def get_explicit_wait(cls):
        return int(cls.get("timeouts", "explicit_wait"))

    @classmethod
    def get_page_load_timeout(cls):
        return int(cls.get("timeouts", "page_load_timeout"))

    # ─────────────────────────────────────────────
    # Register Credentials
    # ─────────────────────────────────────────────

    @classmethod
    def get_first_name(cls):
        return cls.get("register credentials", "fname")

    @classmethod
    def get_last_name(cls):
        return cls.get("register credentials", "lname")

    @classmethod
    def get_email(cls):
        return cls.get("invalid register", "email")

    @classmethod
    def get_telephone(cls):
        return cls.get("register credentials", "telephone")

    @classmethod
    def get_password(cls):
        return cls.get("register credentials", "password")

    @classmethod
    def get_confirm_password(cls):
        return cls.get("register credentials", "cpassword")

    # Generic method

    @classmethod
    def get_register_data(cls, key):
        return cls.get("register credentials", key)

    # ForgetPassword credential

    @classmethod

    def get_validemail(cls):
        return cls.get("Forget password data","email")
    

    def get_email(cls):
        return cls.get("Forget password data", "email")


    @classmethod
    def get_message(cls):
        return cls.get("Forget password data", "successmsg")

    @classmethod
    def get_invalidemail(cls):
        return cls.get("Forget password data", "invalidemail")

    @classmethod
    def get_warning(cls):

        return cls.get("Forget password data", "warningmsg")
    # ─────────────────────────────────────────────
    # Billing Data
    # ─────────────────────────────────────────────

    @classmethod
    def get_billing_first_name(cls):
        return cls.get("billing", "first_name")

    @classmethod
    def get_billing_last_name(cls):
        return cls.get("billing", "last_name")

    @classmethod
    def get_billing_company(cls):
        return cls.get("billing", "company")

    @classmethod
    def get_billing_address1(cls):
        return cls.get("billing", "address1")

    @classmethod
    def get_billing_city(cls):
        return cls.get("billing", "city")

    @classmethod
    def get_billing_postcode(cls):
        return cls.get("billing", "postcode")

    @classmethod
    def get_billing_country(cls):
        return cls.get("billing", "country")

    @classmethod
    def get_billing_region(cls):
        return cls.get("billing", "region")

    # ─────────────────────────────────────────────
    # Registration Data
    # ─────────────────────────────────────────────

    @classmethod
    def get_reg_first_name(cls):
        return cls.get("registration", "reg_first_name")

    @classmethod
    def get_reg_last_name(cls):
        return cls.get("registration", "reg_last_name")

    @classmethod
    def get_reg_email(cls):
        return cls.get("registration", "reg_email")

    @classmethod
    def get_reg_telephone(cls):
        return cls.get("registration", "reg_telephone")

    @classmethod
    def get_reg_password(cls):
        return cls.get("registration", "reg_password")

    @classmethod
    def get_reg_confirm_password(cls):
        return cls.get("registration", "reg_confirm_password")

    @classmethod
    def get_reg_company(cls):
        return cls.get("registration", "reg_company")

    @classmethod
    def get_reg_address1(cls):
        return cls.get("registration", "reg_address1")

    @classmethod
    def get_reg_address2(cls):
        return cls.get("registration", "reg_address2")

    @classmethod
    def get_reg_city(cls):
        return cls.get("registration", "reg_city")

    @classmethod
    def get_reg_postcode(cls):
        return cls.get("registration", "reg_postcode")

    @classmethod
    def get_reg_country(cls):
        return cls.get("registration", "reg_country")

    @classmethod
    def get_reg_region(cls):
        return cls.get("registration", "reg_region")

    # ─────────────────────────────────────────────
    # Messages
    # ─────────────────────────────────────────────

    @classmethod
    def get_login_success_message(cls):
        return cls.get("messages", "login_success")

    @classmethod
    def get_expected_order_message(cls):
        return cls.get("messages", "expected_order_msg")

    
    #Logout credentials
    @classmethod
    def get_mail(cls):
        return cls.get("credentials","email")
    
    @classmethod
    def get_pwd(cls):
        return cls.get("credentials","password")
    
    
