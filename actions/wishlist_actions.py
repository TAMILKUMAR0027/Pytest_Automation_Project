"""Action class encapsulating wishlist-related user interactions."""

import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

from actions.BaseAction import BaseAction
from pages.wishlist_page import WishListPage
from utils.loggerCreator import get_logger

logger = get_logger(__name__)

HOME_PAGE_URL = "https://ecommerce-playground.lambdatest.io/"
WISHLIST_FALLBACK_URL = (
    "https://ecommerce-playground.lambdatest.io/index.php?route=account/wishlist"
)
HOVER_PAUSE_SECONDS = 0.5
REMOVE_CLICK_PAUSE_SECONDS = 0.3


class WishListActions(BaseAction):
    """Provides high-level wishlist operations on top of BaseAction primitives."""

    def __init__(self, driver):
        super().__init__(driver)
        self.wishlist_page = WishListPage

    def login_after_home(self):
        """After login, navigate back to the home page."""
        logger.info("Navigating to home page: %s", HOME_PAGE_URL)
        self.driver.get(HOME_PAGE_URL)
        self.wait_for_page_load()
        self.wait.until(
            ec.visibility_of_element_located(self.wishlist_page.TOP_PRODUCTS_HEADING)
        )
        logger.info("Home page loaded successfully")
        return self.driver.current_url

    def scroll_to_top_products(self):
        """Scroll to the 'Top Products' section on the home page."""
        self.wait_for_page_load()
        self.scroll_into_view(self.wishlist_page.TOP_PRODUCTS_HEADING)
        logger.info("Scrolled to 'Top Products' section")

    def scroll_to_top_collection(self):
        """Scroll to the 'Top Collection' section on the home page."""
        self.wait_for_page_load()
        self.scroll_into_view(self.wishlist_page.TOP_COLLECTION_HEADING)
        logger.info("Scrolled to 'Top Collection' section")

    def navigate_to_wishlist_via_account(self):
        """Navigate to the wishlist page via the header link, falling back to direct URL."""
        try:
            self.js_click(self.wishlist_page.WISHLIST_HEADER_LINK)
            self.wait.until(
                ec.visibility_of_element_located(self.wishlist_page.MY_WISHLIST_TITLE)
            )
            logger.info("Navigated to wishlist page via header link")
        except TimeoutException:
            logger.warning(
                "Header wishlist link failed, falling back to URL: %s",
                WISHLIST_FALLBACK_URL,
            )
            self.driver.get(WISHLIST_FALLBACK_URL)
            self.wait.until(
                ec.visibility_of_element_located(self.wishlist_page.MY_WISHLIST_TITLE)
            )
            logger.info("Navigated to wishlist page via fallback URL")

    def wait_for_wishlist_page(self):
        """Dismiss any stray alert and wait for the wishlist page title to be visible."""
        alert_text = self.dismiss_alert_if_present()
        if alert_text:
            logger.info("Dismissed alert before wishlist page load: %s", alert_text)
        self.wait.until(
            ec.visibility_of_element_located(self.wishlist_page.MY_WISHLIST_TITLE)
        )
        logger.info("Wishlist page is visible")

    def get_current_page_title(self):
        """Return the current browser tab title."""
        title = self.driver.title
        logger.info("Current page title: %s", title)
        return title

    # ------------------------------------------------------------------
    # Adding products
    # ------------------------------------------------------------------

    def add_product_to_wishlist_by_name(self, product_name):
        """Hover over a product card and click its wishlist button."""
        self.wait_for_page_load()
        logger.info("Adding product '%s' to wishlist", product_name)

        card_locator = self.wishlist_page.product_card(product_name)
        button_locator = self.wishlist_page.product_wishlist_button(product_name)

        card = self.scroll_into_view(card_locator)
        wishlist_button = self.wait.until(ec.presence_of_element_located(button_locator))

        ActionChains(self.driver).move_to_element(card).perform()
        time.sleep(HOVER_PAUSE_SECONDS)

        self._force_make_visible(wishlist_button)
        self.js_click_element(wishlist_button)
        logger.info("Clicked wishlist button for '%s'", product_name)

        alert_text = self.dismiss_alert_if_present()
        if alert_text:
            logger.error("Unexpected alert displayed: %s", alert_text)
            raise RuntimeError(f"Unexpected alert displayed: {alert_text}")

    def hover_and_click_wishlist_button(self, product_name):
        """Alias for add_product_to_wishlist_by_name (hover + click wishlist icon)."""
        self.add_product_to_wishlist_by_name(product_name)

    def search_for_product(self, product_name):
        """Search for a product using the site search bar."""
        self.wait_for_page_load()
        search_box = self.wait.until(
            ec.element_to_be_clickable(self.wishlist_page.SEARCH_BAR)
        )
        search_box.clear()
        search_box.send_keys(product_name)
        search_box.send_keys(Keys.ENTER)
        logger.info("Searched for product: %s", product_name)

    def click_product_from_search_results(self, _product_name):
        """Click the iPod Shuffle product from search results."""
        self.wait_for_page_load()
        product = self.wait.until(
            ec.element_to_be_clickable(self.wishlist_page.IPOD_SHUFFLE_PRODUCT)
        )
        self.scroll_into_view_element(product)
        self.js_click_element(product)
        logger.info("Opened product page for: %s", _product_name)

    def click_heart_button_on_product_page(self):
        """Click the wishlist (heart) button on the iPod Shuffle product page."""
        self.wait_for_page_load()
        wishlist_button = self.wait.until(
            ec.element_to_be_clickable(self.wishlist_page.IPOD_SHUFFLE_WISHLIST_BTN)
        )
        self.scroll_into_view_element(wishlist_button)
        time.sleep(HOVER_PAUSE_SECONDS)
        self.js_click_element(wishlist_button)
        logger.info("Clicked wishlist (heart) button on product page")

    # ------------------------------------------------------------------
    # Messages
    # ------------------------------------------------------------------

    def get_wishlist_success_message_generic(self):
        """Return the wishlist success notification text, using a fallback locator if needed."""
        try:
            message = self.get_text(self.wishlist_page.SUCCESS_NOTIFICATION)
        except TimeoutException:
            logger.warning("Primary success notification not found, using fallback")
            message = self.get_text(self.wishlist_page.SUCCESS_NOTIFICATION_FALLBACK)
        logger.info("Success notification text: %s", message)
        return message

    def click_wishlist_link_from_popup(self):
        """Click the 'View Wish List' link inside the success popup."""
        self.click(self.wishlist_page.WISHLIST_POPUP_LINK)
        logger.info("Clicked 'View Wish List' link from popup")

    def get_removal_success_message(self):
        """Return the cleaned-up text of the removal success alert."""
        raw_text = self.get_text(self.wishlist_page.REMOVAL_SUCCESS_ALERT)
        cleaned = raw_text.replace("\u00d7", "").strip()
        logger.info("Removal success message: %s", cleaned)
        return cleaned

    # ------------------------------------------------------------------
    # Wishlist contents
    # ------------------------------------------------------------------

    def get_all_wishlist_product_names(self):
        """Return the list of product names currently in the wishlist."""
        names = self.get_elements_text(self.wishlist_page.WISHLIST_PRODUCT_NAMES)
        logger.info("Wishlist product names: %s", names)
        return names

    def get_all_wishlist_product_prices(self):
        """Return the list of product prices currently in the wishlist."""
        prices = self.get_elements_text(self.wishlist_page.WISHLIST_PRODUCT_PRICES)
        logger.info("Wishlist product prices: %s", prices)
        return prices

    def is_product_present_in_wishlist(self, product_name):
        """Return True if the given product appears in the wishlist table."""
        present = self.is_present(self.wishlist_page.product_link_for(product_name))
        logger.info("Product '%s' present in wishlist: %s", product_name, present)
        return present

    def remove_product_from_wishlist(self, product_name):
        """Remove the given product from the wishlist."""
        self.wait_for_wishlist_page()

        remove_button = self.wait.until(
            ec.element_to_be_clickable(self.wishlist_page.remove_button_for(product_name))
        )
        self.scroll_into_view_element(remove_button)
        time.sleep(REMOVE_CLICK_PAUSE_SECONDS)
        self.js_click_element(remove_button)
        logger.info("Removed product '%s' from wishlist", product_name)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _force_make_visible(self, element):
        self.driver.execute_script(
            "arguments[0].style.display='block';"
            "arguments[0].style.opacity='1';"
            "arguments[0].style.visibility='visible';",
            element,
        )

    def js_click_element(self, element):
        """Click a WebElement via JavaScript."""
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_into_view_element(self, element):
        """Scroll a WebElement into the center of the viewport."""
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)