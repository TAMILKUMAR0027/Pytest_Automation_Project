from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class AddOnsPage:

    ADDONS_LINK = (By.XPATH, "//span[normalize-space()='AddOns']")
    WIDGETS_BUTTON = (By.XPATH, "//span[normalize-space()='Widgets']")

    NAME_FIELD = (By.NAME, "name")
    EMAIL_FIELD = (By.NAME, "email")
    SUBJECT_FIELD = (By.NAME, "subject")
    MESSAGE_FIELD = (By.NAME, "message")

    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit' and normalize-space()='Send message']")
    SUCCESS_MESSAGE = (
        By.XPATH,
        "//*[contains(text(),'Your enquiry has been successfully sent to the store owner!')]"
    )
    EMAIL_ERROR_MESSAGE = (
        By.XPATH,
        "//*[contains(text(),'E-Mail Address does not appear to be valid')]"
    )
    ENTRY_ID_HIDDEN_FIELD = (By.NAME, "entry_id")

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # ------------------------------------------------------------------ #
    # Internal helpers
    # ------------------------------------------------------------------ #

    def _wait_for_page_ready(self, timeout=30):
        """Wait for document.readyState == 'complete', not just DOM presence.

        Catches cases where the DOM is interactive but slow-loading
        third-party assets haven't finished, which can leave the page in
        a half-initialized JS state.
        """
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def _js_click(self, element):
        """Fallback click via JS. Bypasses hover-menu/overlay issues that a
        plain .click() can hit, especially in headless mode where CSS
        :hover dropdowns don't always behave like a real browser."""
        self.driver.execute_script("arguments[0].click();", element)

    def _get_entry_id_value(self):
        """Return the current value of the hidden entry_id field, or None
        if it can't be found. Used purely for diagnostics."""
        try:
            el = self.driver.find_element(*self.ENTRY_ID_HIDDEN_FIELD)
            return el.get_attribute("value")
        except Exception:
            return None

    def _dump_debug(self, name_prefix):
        """Save a screenshot + page source on failure, for diagnosing
        headless UI issues."""
        try:
            self.driver.save_screenshot(f"{name_prefix}.png")
            with open(f"{name_prefix}.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
        except Exception:
            pass

    # ------------------------------------------------------------------ #
    # Navigation
    # ------------------------------------------------------------------ #

    def click_addons_link(self):
        try:
            addons_el = self.wait.until(EC.presence_of_element_located(self.ADDONS_LINK))
            ActionChains(self.driver).move_to_element(addons_el).perform()
            # Confirm the hover dropdown actually opened before moving on.
            self.wait.until(EC.visibility_of_element_located(self.WIDGETS_BUTTON))
        except Exception:
            self._dump_debug("debug_addons_failure")
            raise

    def click_widgets_button(self):
        try:
            widgets_el = self.wait.until(EC.visibility_of_element_located(self.WIDGETS_BUTTON))
            try:
                ActionChains(self.driver).move_to_element(widgets_el).click().perform()
            except Exception:
                # Hover-based click failed (common in headless mode) - fall back to JS click.
                self._js_click(widgets_el)
            self._wait_for_page_ready()
        except Exception:
            self._dump_debug("debug_widgets_failure")
            raise

    # ------------------------------------------------------------------ #
    # Form fields
    # ------------------------------------------------------------------ #

    def enter_name(self, name):
        element = self.wait.until(EC.visibility_of_element_located(self.NAME_FIELD))
        element.clear()
        element.send_keys(name)

    def enter_email(self, email):
        element = self.wait.until(EC.visibility_of_element_located(self.EMAIL_FIELD))
        element.clear()
        element.send_keys(email)

    def enter_subject(self, subject):
        element = self.wait.until(EC.visibility_of_element_located(self.SUBJECT_FIELD))
        element.clear()
        element.send_keys(subject)

    def enter_message(self, message):
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.MESSAGE_FIELD))
            element.clear()
            element.send_keys(message)
        except Exception:
            self._dump_debug("debug_message_failure")
            raise

    # ------------------------------------------------------------------ #
    # Submit + results
    # ------------------------------------------------------------------ #

    def click_submit(self, logger=None):
        try:
            # entry_id is sometimes populated asynchronously by page JS.
            # Give it a short window to show up before submitting, and log
            # if it's still empty - a likely cause of a silent server-side
            # rejection with no visible client-side error.
            entry_id = self._get_entry_id_value()
            if not entry_id:
                try:
                    WebDriverWait(self.driver, 5).until(
                        lambda d: self._get_entry_id_value()
                    )
                    entry_id = self._get_entry_id_value()
                except Exception:
                    pass

            if logger:
                if entry_id:
                    logger.info("entry_id hidden field value before submit: %s", entry_id)
                else:
                    logger.warning(
                        "entry_id hidden field is empty before submit - "
                        "submission may be silently rejected server-side."
                    )

            submit_btn = self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON))
            try:
                submit_btn.click()
            except Exception:
                self._js_click(submit_btn)
        except Exception:
            self._dump_debug("debug_submit_failure")
            raise

    def get_success_message(self, timeout=45):
        """Wait for the AJAX success message. Uses a longer, independent
        timeout than the default page wait, since mz_sendMessage() is an
        async call and can be slower than a normal element wait."""
        try:
            # First confirm the node exists in the DOM at all (helps
            # distinguish "never rendered" from "rendered but not visible").
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(self.SUCCESS_MESSAGE)
            )
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
            )
            return element.text.strip()
        except Exception:
            self._dump_debug("debug_success_message_failure")
            raise

    def get_email_error_message(self, timeout=30):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.EMAIL_ERROR_MESSAGE)
            ).text.strip()
        except Exception:
            self._dump_debug("debug_email_error_failure")
            raise