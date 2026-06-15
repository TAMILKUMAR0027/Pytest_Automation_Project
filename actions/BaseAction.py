"""Base class providing common Selenium helper methods for all page actions."""

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

DEFAULT_WAIT_SECONDS = 15
ALERT_WAIT_SECONDS = 3


class BaseAction:
    """Common reusable Selenium actions shared across all page action classes."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_WAIT_SECONDS)
        self.long_wait = WebDriverWait(driver, DEFAULT_WAIT_SECONDS)

    def click(self, locator):
        """Click an element, falling back to a JS click if it is not directly clickable."""
        try:
            element = self.wait.until(ec.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            element = self.wait.until(ec.presence_of_element_located(locator))
            self._scroll_into_view(element)
            self._js_click_element(element)

    def send_keys(self, locator, value):
        """Clear a field and type the given value into it."""
        element = self.wait.until(ec.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def get_text(self, locator):
        """Return the visible text of an element."""
        return self.wait.until(ec.visibility_of_element_located(locator)).text

    def is_displayed(self, locator):
        """Return True if the element is present and displayed, else False."""
        elements = self.driver.find_elements(*locator)
        return bool(elements) and elements[0].is_displayed()

    def js_click(self, locator):
        """Click an element via JavaScript."""
        element = self.driver.find_element(*locator)
        self._js_click_element(element)

    def scroll_into_view(self, locator):
        """Scroll the given element into the center of the viewport and return it."""
        element = self.wait.until(ec.presence_of_element_located(locator))
        self._scroll_into_view(element)
        return element

    def move_slider(self, locator, x_offset, y_offset=0):
        """Drag an element by the given x/y offset."""
        element = self.wait.until(ec.visibility_of_element_located(locator))
        ActionChains(self.driver).click_and_hold(element).move_by_offset(
            x_offset, y_offset
        ).release().perform()

    def wait_for_page_load(self):
        """Wait until the document's readyState is 'complete'."""
        self.long_wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def is_present(self, locator):
        """Return True if at least one matching element exists in the DOM."""
        return len(self.driver.find_elements(*locator)) > 0

    def get_input_value(self, locator):
        """Return the 'value' attribute of an input element."""
        element = self.wait.until(ec.visibility_of_element_located(locator))
        return element.get_attribute("value")

    def get_elements_text(self, locator):
        """Return a list of non-empty, stripped text values for all matching elements."""
        elements = self.long_wait.until(ec.visibility_of_all_elements_located(locator))
        return [el.text.strip() for el in elements if el.text.strip()]

    def dismiss_alert_if_present(self):
        """Dismiss a JS alert if one appears within ALERT_WAIT_SECONDS; return its text."""
        try:
            alert = WebDriverWait(self.driver, ALERT_WAIT_SECONDS).until(
                ec.alert_is_present()
            )
            text = alert.text
            alert.dismiss()
            return text
        except TimeoutException:
            return None

    def _scroll_into_view(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

    def _js_click_element(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def select_by_visible_text(self, locator, text):
        element = self.wait.until(ec.element_to_be_clickable(locator))
        Select(element).select_by_visible_text(text)

    def find_elements(self, locator):
        return self.wait.until(ec.presence_of_all_elements_located(locator))

    def clear(self, locator):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        element.clear()
        if element.get_attribute("value") != "":
            element.send_keys(Keys.CONTROL, "a")
            element.send_keys(Keys.BACKSPACE)