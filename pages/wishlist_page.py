# pages/wishlist_page.py

from selenium.webdriver.common.by import By


class WishListPage:

    HOME_LOGO = (By.XPATH, "//img[@alt='Poco Electro']")
    HOME_LOGO_ALT = (By.XPATH, "//a[contains(@class,'navbar-brand')]")

    TOP_PRODUCTS_HEADING = (By.XPATH, "//h3[contains(text(),'Top Products')]")
    TOP_COLLECTION_HEADING = (By.XPATH, "//h3[contains(text(),'Top Collection')]")

    SUCCESS_NOTIFICATION = (
        By.XPATH,
        "//div[@id='notification-box-top']//div[contains(@class,'toast-body')]//p"
    )
    SUCCESS_NOTIFICATION_FALLBACK = (
        By.XPATH,
        "//div[@id='notification-box-top']//p"
    )

    WISHLIST_POPUP_LINK = (By.XPATH, "//a[@class='btn btn-secondary btn-block']")
    WISHLIST_HEADER_LINK = (By.XPATH, "//a[contains(@href,'account/wishlist')]")

    MY_WISHLIST_TITLE = (By.XPATH, "//h1[contains(text(),'My Wish List')]")
    REMOVAL_SUCCESS_ALERT = (
        By.XPATH,
        "//div[contains(@class,'alert-success') and contains(@class,'alert-dismissible')]"
    )

    WISHLIST_PRODUCT_NAMES = (
        By.XPATH,
        "//table[@class='table table-hover border']//child::td[2]"
    )
    WISHLIST_PRODUCT_PRICES = (
        By.XPATH,
        "//table[@class='table table-hover border']//child::td[5]"
    )

    SEARCH_BAR = (
        By.XPATH,
        "//div[@id='entry_217822']//input[@placeholder='Search For Products']"
    )

    IPOD_SHUFFLE_PRODUCT = (
        By.XPATH,
        "//img[@title='iPod Shuffle']"
    )

    IPOD_SHUFFLE_WISHLIST_BTN = (
        By.XPATH,
        "//div[@id='image-gallery-216811']//button"
    )

    @staticmethod
    def product_card(product_name):
        return (
            By.XPATH,
            f"//div[contains(@class,'product-thumb') and .//a[contains(normalize-space(),'{product_name}')]]"
        )

    @staticmethod
    def product_wishlist_button(product_name):
        return (
            By.XPATH,
            f"//div[contains(@class,'product-thumb') and .//a[contains(normalize-space(),'{product_name}')]]"
            "//button[contains(@class,'wishlist')]"
        )

    @staticmethod
    def product_link_for(product_name):
        return (
            By.XPATH,
            "//table[contains(@class,'table')]//tbody//tr//td[2]//a"
            f"[contains(normalize-space(),'{product_name}')]"
        )

    @staticmethod
    def row_for(product_name):
        return (
            By.XPATH,
            "//table[contains(@class,'table')]//tbody//tr"
            f"[.//td[2]//a[contains(normalize-space(),'{product_name}')]]"
        )

    @staticmethod
    def remove_button_for(product_name):
        return (
            By.XPATH,
            "//table[contains(@class,'table')]//tbody//tr"
            f"[.//td[2]//a[contains(normalize-space(),'{product_name}')]]"
            "//a[@title='Remove' or contains(@href,'remove')]"
        )