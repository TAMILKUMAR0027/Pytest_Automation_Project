import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException,
    MoveTargetOutOfBoundsException,
    JavascriptException,
)
from selenium.webdriver.common.action_chains import ActionChains

from pages.wishlist_page import WishListPage
from utils.loggerCreator import get_logger

logger = get_logger(__name__)


class UnknownProductException(Exception):
    def __init__(self, method_name, product_name):
        super().__init__(
            f"[{method_name}] No locator/case mapped for product: '{product_name}'. "
            f"Add a case + locator in WishListPage."
        )


class ToastNotDisplayedException(Exception):
    def __init__(self, method_name, timeout_seconds):
        super().__init__(
            f"[{method_name}] No success toast/banner appeared within {timeout_seconds}s."
        )


class UnexpectedJsAlertException(Exception):
    def __init__(self, context, alert_text):
        super().__init__(
            f"[{context}] Unexpected JS alert appeared: '{alert_text}'"
        )


class PageNavigationException(Exception):
    def __init__(self, expected_page, attempted_url, actual_url):
        super().__init__(
            f"[Navigation] Failed to reach '{expected_page}'. "
            f"Attempted URL: {attempted_url}. Actual URL: {actual_url}"
        )


class WishListActions:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.wp = WishListPage(driver)
        self.long_wait = WebDriverWait(driver, 15)

    # =====================================================================
    # PRIVATE UTILITY METHODS
    # =====================================================================

    def _pause(self, seconds):
        time.sleep(seconds)

    def _dismiss_alert_if_present(self):
        """Checks for any browser JS alert and dismisses it if present."""
        try:
            short_wait = WebDriverWait(self.driver, 3)
            alert = short_wait.until(EC.alert_is_present())
            text = alert.text
            alert.dismiss()
            logger.info("Dismissed JS alert: %s", text)
            return text
        except TimeoutException:
            return None

    def _force_reveal_element(self, element, product_label):
        """Force-reveals a hidden wishlist button via JS style overrides."""
        try:
            self.driver.execute_script(
                "var b = arguments[0];"
                "b.style.setProperty('display', 'block', 'important');"
                "b.style.setProperty('opacity', '1', 'important');"
                "b.style.setProperty('visibility', 'visible', 'important');",
                element,
            )
        except JavascriptException as e:
            raise RuntimeError(
                f"[forceRevealElement - {product_label}] JS execution failed: {e}"
            )
        except Exception as e:
            raise RuntimeError(
                f"Wishlist button for [{product_label}] not interactable after "
                f"forceRevealElement — Check locator in WishListPage. Cause: {e}"
            )

    def _js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def _scroll_into_view(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

    def _hover_and_click_wishlist(self, product_card, wishlist_btn, product_label):
        """
        Core wishlist hover-and-click flow:
          1. Scroll the product card into view
          2. Hover over the card to trigger CSS hover state
          3. Force-reveal the wishlist button via JS
          4. If already wishlisted ('wished' class), toggle off first
          5. JS-click the wishlist button
          6. Fail if an unexpected AJAX alert fires
        """
        actions = ActionChains(self.driver)

        # Step 1: Scroll card into viewport
        self._scroll_into_view(product_card)
        self._pause(0.5)

        # Step 2: Hover to trigger CSS hover state
        try:
            actions.move_to_element(product_card).perform()
        except MoveTargetOutOfBoundsException as e:
            raise RuntimeError(
                f"[{product_label}] product card outside scrollable viewport: {e}"
            )
        self._pause(0.7)

        # Step 3: Force-reveal the wishlist button
        self._force_reveal_element(wishlist_btn, product_label)

        # Step 4: Toggle off 'wished' state if already added
        try:
            btn_class = wishlist_btn.get_attribute("class")
            if btn_class and "wished" in btn_class:
                logger.info("[%s] Already wishlisted — removing first...", product_label)
                self._js_click(wishlist_btn)
                self._pause(1.2)
                self._dismiss_alert_if_present()
                self._pause(0.5)
                actions.move_to_element(product_card).perform()
                self._pause(0.7)
                self._force_reveal_element(wishlist_btn, product_label)
                self._pause(0.3)
        except StaleElementReferenceException:
            logger.warning(
                "[%s] Stale element during wished-state check — DOM rebuilt, continuing.",
                product_label,
            )
        except Exception as e:
            logger.info("[%s] Could not check wished state: %s", product_label, e)

        # Step 5: Click the wishlist button
        try:
            self._js_click(wishlist_btn)
            logger.info("[%s] Wishlist button clicked successfully", product_label)
        except JavascriptException as e:
            raise RuntimeError(
                f"[Wishlist button click - {product_label}] JS click failed: {e}"
            )

        # Step 6: Guard against AJAX error alerts
        alert_text = self._dismiss_alert_if_present()
        if alert_text is not None:
            raise UnexpectedJsAlertException(
                f"{product_label} wishlist click", alert_text
            )

    def _click_home_logo(self):
        """Navigates back to the homepage by clicking the site logo."""
        try:
            el = self.wait.until(EC.element_to_be_clickable(self.wp.HOME_LOGO))
            self._js_click(el)
        except TimeoutException:
            try:
                el = self.wait.until(EC.element_to_be_clickable(self.wp.HOME_LOGO_ALT))
                self._js_click(el)
            except TimeoutException:
                logger.info("Home logo not clickable, continuing...")

    def _wait_for_page_load(self):
        WebDriverWait(self.driver, 15).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    # =====================================================================
    # SCROLL / NAVIGATION ACTIONS
    # =====================================================================

    def scroll_to_top_products(self):
        """Navigates home and scrolls to the 'Top Products' section."""
        self._click_home_logo()
        self._wait_for_page_load()
        heading = self.wait.until(EC.visibility_of_element_located(self.wp.TOP_PRODUCTS_HEADING))
        self._scroll_into_view(heading)
        logger.info("Scrolled to Top Products section")

    def scroll_to_top_collection(self):
        """Navigates home and scrolls to the 'Top Collection' section."""
        self._click_home_logo()
        self._wait_for_page_load()
        heading = self.wait.until(EC.visibility_of_element_located(self.wp.TOP_COLLECTION_HEADING))
        self._scroll_into_view(heading)
        logger.info("Scrolled to Top Collection section")

    def navigate_to_wishlist_via_account(self):
        """Navigates to the wishlist page via the account header link, with URL fallback."""
        fallback_url = "https://ecommerce-playground.lambdatest.io/index.php?route=account/wishlist"

        try:
            link = self.long_wait.until(
                EC.visibility_of_element_located(self.wp.WISHLIST_HEADER_LINK)
            )
            self._js_click(link)
            self.wait.until(EC.visibility_of_element_located(self.wp.MY_WISHLIST_TITLE))
            logger.info("Navigated to wishlist page via JS click")
        except TimeoutException:
            logger.info("Timeout on header link — falling back to URL...")
            self.driver.get(fallback_url)
            try:
                self.wait.until(EC.visibility_of_element_located(self.wp.MY_WISHLIST_TITLE))
                logger.info("Navigated to wishlist page via URL fallback")
            except TimeoutException:
                raise PageNavigationException(
                    "My Wish List", fallback_url, self.driver.current_url
                )

    # =====================================================================
    # ADD-TO-WISHLIST ACTIONS — Individual Products
    # =====================================================================

    def add_imac_to_wishlist(self):
        self._wait_for_page_load()
        card = self.wait.until(EC.visibility_of_element_located(self.wp.IMAC_LISTING_BOX))
        btn = self.driver.find_element(*self.wp.IMAC_WISHLIST_BTN)
        self._hover_and_click_wishlist(card, btn, "iMac")

    def add_apple_cinema_to_wishlist(self):
        self._wait_for_page_load()
        card = self.wait.until(EC.visibility_of_element_located(self.wp.APPLE_CINEMA_PRODUCT))
        btn = self.driver.find_element(*self.wp.APPLE_CINEMA_WISHLIST_BTN)
        self._hover_and_click_wishlist(card, btn, "Apple Cinema 30")

    def add_ipod_nano_to_wishlist(self):
        self._wait_for_page_load()
        card = self.wait.until(EC.visibility_of_element_located(self.wp.IPOD_NANO_PRODUCT))
        btn = self.driver.find_element(*self.wp.IPOD_NANO_WISHLIST_BTN)
        self._hover_and_click_wishlist(card, btn, "iPod Nano")

    def hover_and_click_wishlist_button(self, product_name):
        """Dispatcher: routes a product name to the correct add-to-wishlist method."""
        name = product_name.lower()
        if name == "imac":
            self.add_imac_to_wishlist()
        elif name == "apple cinema 30":
            self.add_apple_cinema_to_wishlist()
        elif name == "ipod nano":
            self.add_ipod_nano_to_wishlist()
        else:
            raise UnknownProductException("hover_and_click_wishlist_button", product_name)

    def add_product_to_wishlist_by_name(self, product_name):
        """Alias dispatcher for adding by name."""
        name = product_name.lower()
        if name == "apple cinema 30":
            self.add_apple_cinema_to_wishlist()
        elif name == "ipod nano":
            self.add_ipod_nano_to_wishlist()
        elif name == "imac":
            self.add_imac_to_wishlist()
        else:
            raise UnknownProductException("add_product_to_wishlist_by_name", product_name)

    # =====================================================================
    # SEARCH ACTIONS
    # =====================================================================

    def search_for_product(self, search_term):
        """Types the given search term into the search bar and submits with ENTER."""
        self._wait_for_page_load()
        try:
            search_bar = self.wait.until(EC.element_to_be_clickable(self.wp.SEARCH_BAR))
            search_bar.clear()
            search_bar.send_keys(search_term)
            search_bar.send_keys(Keys.ENTER)
            logger.info("Searched for: %s", search_term)
        except TimeoutException as e:
            raise TimeoutException(
                f"Search bar not found/clickable — "
                f"Locator: //div[@id='entry_217822']//input[@placeholder='Search For Products']: {e}"
            )

    def click_product_from_search_results(self, product_name):
        """Clicks a product link from the search results grid."""
        name = product_name.lower()
        if name == "ipod shuffle":
            try:
                self._wait_for_page_load()
                el = self.wait.until(EC.element_to_be_clickable(self.wp.IPOD_SHUFFLE_PRODUCT))
                self._scroll_into_view(el)
                self._pause(0.4)
                self._js_click(el)
                logger.info("Clicked from search results: %s", product_name)
            except TimeoutException as e:
                raise TimeoutException(
                    f"iPod Shuffle in search results not found — "
                    f"Locator: //a[@id='mz-product-grid-image-34-212469']"
                    f"//img[@title='iPod Shuffle']: {e}"
                )
        else:
            raise UnknownProductException("click_product_from_search_results", product_name)

    def click_heart_button_on_product_page(self):
        """Clicks the heart/wishlist button on the iPod Shuffle product detail page."""
        try:
            self._wait_for_page_load()
            btn = self.wait.until(
                EC.visibility_of_element_located(self.wp.IPOD_SHUFFLE_WISHLIST_BTN)
            )
            self._scroll_into_view(btn)
            self._pause(0.4)

            self._force_reveal_element(btn, "iPod Shuffle - Product Page Heart")

            # Toggle off existing 'wished' state if needed
            try:
                btn_class = btn.get_attribute("class")
                if btn_class and "wished" in btn_class:
                    logger.info("[iPod Shuffle] Already wishlisted — removing first...")
                    self._js_click(btn)
                    self._pause(1.2)
                    self._dismiss_alert_if_present()
                    self._pause(0.5)
                    self._force_reveal_element(btn, "iPod Shuffle - Product Page Heart")
                    self._pause(0.3)
            except StaleElementReferenceException:
                logger.warning(
                    "[iPod Shuffle] Stale element during wished-state check on detail page — continuing."
                )
            except Exception as e:
                logger.info("[iPod Shuffle] Could not check wished state: %s", e)

            # Main wishlist button click
            btn = self.wait.until(
                EC.element_to_be_clickable(self.wp.IPOD_SHUFFLE_WISHLIST_BTN)
            )
            self._js_click(btn)
            logger.info("Clicked heart button on product detail page for iPod Shuffle")

            # Guard against AJAX error alert
            alert_text = self._dismiss_alert_if_present()
            if alert_text is not None:
                raise UnexpectedJsAlertException(
                    "iPod Shuffle heart button click on detail page", alert_text
                )

        except TimeoutException as e:
            raise TimeoutException(
                f"iPod Shuffle heart button never visible — "
                f"Locator: //div[@id='image-gallery-216811']"
                f"//button[@title='Add to Wish List']: {e}"
            )

    # =====================================================================
    # SUCCESS MESSAGE / TOAST HELPERS
    # =====================================================================

    def get_wishlist_success_message_generic(self):
        """Waits up to 25 seconds for the success toast, falling back to simpler locator."""
        toast_msg = (By.XPATH, "//div[@id='notification-box-top']//div[contains(@class,'toast-body')]//p")
        toast_fallback = (By.XPATH, "//div[@id='notification-box-top']//p")

        try:
            toast = WebDriverWait(self.driver, 25).until(
                EC.visibility_of_element_located(toast_msg)
            )
            return toast.text
        except TimeoutException:
            try:
                toast2 = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located(toast_fallback)
                )
                return toast2.text
            except TimeoutException:
                raise ToastNotDisplayedException("get_wishlist_success_message_generic", 35)

    def get_wishlist_success_message(self, product_name_fragment):
        """Waits for a product-specific toast, falling back to generic notification."""
        fresh_toast = (
            By.XPATH,
            "//div[@id='notification-box-top']"
            f"//*[contains(text(),'{product_name_fragment}')]"
            "/ancestor::div[contains(@class,'toast')]//p"
        )

        try:
            self.wait.until(EC.visibility_of_element_located(fresh_toast))
            return self.driver.find_element(*fresh_toast).text
        except TimeoutException:
            try:
                fallback = self.driver.find_element(*self.wp.SUCCESS_NOTIFICATION_FALLBACK)
                return fallback.text
            except Exception:
                raise ToastNotDisplayedException(
                    f"get_wishlist_success_message - product: {product_name_fragment}", 15
                )

    def click_wishlist_link_from_popup(self):
        """Clicks the 'go to wishlist' link inside the success popup."""
        link = self.wait.until(EC.element_to_be_clickable(self.wp.WISHLIST_POPUP_LINK))
        link.click()
        logger.info("Clicked wishlist link from popup")

    # =====================================================================
    # WISHLIST PAGE HELPERS
    # =====================================================================

    def wait_for_wishlist_page(self):
        """Dismisses any stale JS alert, then waits for the wishlist page title."""
        alert_text = self._dismiss_alert_if_present()
        if alert_text is not None:
            logger.info("Dismissed stale JS alert: %s", alert_text)
        self.wait.until(EC.visibility_of_element_located(self.wp.MY_WISHLIST_TITLE))

    def get_current_page_title(self):
        return self.driver.title

    def get_all_wishlist_product_names(self):
        """Collects all product name texts from the wishlist table."""
        self.wait.until(EC.visibility_of_element_located(self.wp.MY_WISHLIST_TITLE))
        self.long_wait.until(
            EC.visibility_of_all_elements_located(self.wp.WISHLIST_PRODUCT_NAMES)
        )

        names = []
        elements = self.driver.find_elements(*self.wp.WISHLIST_PRODUCT_NAMES)
        for el in elements:
            name = el.text.strip()
            if name:
                names.append(name)
                logger.info("  Wishlist row: %s", name)

        logger.info("Total products in wishlist: %d", len(names))
        return names

    def get_all_wishlist_product_prices(self):
        """Collects all price texts from the wishlist table."""
        self.long_wait.until(
            EC.visibility_of_all_elements_located(self.wp.WISHLIST_PRODUCT_PRICES)
        )
        elements = self.driver.find_elements(*self.wp.WISHLIST_PRODUCT_PRICES)
        return [el.text.strip() for el in elements]

    def is_product_present_in_wishlist(self, product_name):
        """Checks whether a named product is present in the wishlist table."""
        locator = self.wp.product_link_for(product_name)
        return len(self.driver.find_elements(*locator)) > 0

    def remove_product_from_wishlist(self, product_name):
        """Removes a product from the wishlist by clicking its Remove link."""
        self.wait.until(EC.visibility_of_element_located(self.wp.MY_WISHLIST_TITLE))

        remove_btn_locator = self.wp.remove_button_for(product_name)
        row_locator = self.wp.row_for(product_name)

        try:
            btn = self.long_wait.until(EC.element_to_be_clickable(remove_btn_locator))
            self._scroll_into_view(btn)
            self._pause(0.3)

            # Capture row reference now to detect staleness after click
            row = self.driver.find_element(*row_locator)

            self._js_click(btn)
            logger.info("Clicked remove for: %s", product_name)

            try:
                self.long_wait.until(EC.staleness_of(row))
                logger.info("Page reloaded after removing: %s", product_name)
            except TimeoutException:
                logger.info("Staleness wait timed out, continuing...")

        except TimeoutException as e:
            raise TimeoutException(
                f"Remove button for [{product_name}] not found — "
                f"confirm product exists in wishlist before removing: {e}"
            )

    def get_removal_success_message(self):
        """Reads the alert-success banner text after a wishlist removal."""
        alert_div = self.wp.REMOVAL_SUCCESS_ALERT

        try:
            self.long_wait.until(EC.visibility_of_element_located(alert_div))
            alert = self.driver.find_element(*alert_div)

            full_text = self.driver.execute_script(
                "var el = arguments[0]; var text = '';"
                "for (var i = 0; i < el.childNodes.length; i++) {"
                "  if (el.childNodes[i].nodeType === 3) {"
                "    text += el.childNodes[i].textContent;"
                "  }"
                "}"
                "return text.trim();",
                alert,
            )

            if not full_text:
                full_text = alert.text.replace("×", "").strip()

            logger.info("Removal alert text: %s", full_text)
            return full_text

        except TimeoutException as e:
            raise TimeoutException(
                f"Removal success alert never appeared — "
                f"Expected: 'Success: You have modified your wish list!' — "
                f"Locator: //div[contains(@class,'alert-success')]: {e}"
            )