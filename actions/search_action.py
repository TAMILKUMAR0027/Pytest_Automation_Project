"""
Search-specific action methods.

Mirrors SearchAction.java — every method delegates low-level Selenium
operations to BaseAction so tests stay free of driver boilerplate.
"""

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from actions.BaseAction import BaseAction
from pages.search_page import (
    SEARCH_BAR,
    RESULT_CARDS,
    NO_RESULT_MSG,
    MANUFACTURER_LABEL,
)

import time


# ─── Custom Exceptions ────────────────────────────────────────────────────────

class SearchResultException(Exception):
    """Raised when a keyword search returns zero product cards unexpectedly."""

    def __init__(self, keyword: str, count: int):
        super().__init__(
            f"Expected results for keyword '{keyword}' but got {count} products."
        )


class ManufacturerMismatchException(Exception):
    """Raised when the on-page manufacturer label differs from the expected value."""

    def __init__(self, expected: str, actual: str):
        super().__init__(
            f"Manufacturer mismatch — expected: '{expected}', actual: '{actual}'."
        )


# ─── SearchAction ─────────────────────────────────────────────────────────────

class SearchAction(BaseAction):
    """
    All search-flow interactions.

    Inherits BaseAction which exposes:
        click(), send_keys(), get_text(), is_displayed(),
        wait_for_page_load(), find_elements(), …
    """

    # =========================================================================
    # SEARCH BAR ACTIONS
    # =========================================================================

    def click_search_bar(self) -> None:
        """
        Wait for page stability, then click the search bar.
        Falls back to JS click on TimeoutException (mirrors Java behaviour).
        """
        self.wait_for_page_load()
        try:
            self.click(SEARCH_BAR)
        except TimeoutException:
            self.js_click(SEARCH_BAR)

    def enter_keyword_and_press_enter(self, keyword: str) -> None:
        """
        Clear the search bar, type *keyword*, and submit with ENTER.
        Handles the empty-string case (clears the field and submits).
        """
        self.wait_for_page_load()
        try:
            self.send_keys(SEARCH_BAR, keyword)
            self.driver.find_element(*SEARCH_BAR).send_keys(Keys.ENTER)
        except TimeoutException as exc:
            raise TimeoutException(
                f"Search bar not visible for keyword entry: '{keyword}'"
            ) from exc

    # =========================================================================
    # RESULT VALIDATION ACTIONS
    # =========================================================================

    def _wait_for_results_or_error(self, timeout: int = 15) -> None:
        """
        Block until product cards OR the no-results message is rendered.
        Mirrors the Java dual-condition wait pattern.
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            lambda d: bool(d.find_elements(*RESULT_CARDS))
                      or self.is_displayed(NO_RESULT_MSG)
        )

    def is_product_list_displayed(self) -> bool:
        """
        Return True when product result cards are present after a search.
        Return False when only the no-results message is visible.
        """
        self._wait_for_results_or_error()
        return bool(self.driver.find_elements(*RESULT_CARDS))

    def get_product_count(self) -> int:
        """
        Return the number of product cards visible after a search.
        Returns 0 when the no-results message is shown.
        """
        self._wait_for_results_or_error()
        return len(self.driver.find_elements(*RESULT_CARDS))

    def is_keyword_present_in_all_results(self, keyword: str) -> bool:
        """
        Verify that every result card's display name contains *keyword*
        (case-insensitive).

        Raises:
            SearchResultException — if the result list is unexpectedly empty.

        Returns:
            True  — all card names contain the keyword.
            False — at least one card name does not contain the keyword
                    (the offending name is printed to stdout).
        """
        self._wait_for_results_or_error()

        cards = self.driver.find_elements(*RESULT_CARDS)

        if not cards:
            raise SearchResultException(keyword, 0)

        kw = keyword.lower().strip()
        for card in cards:
            name = card.text.strip().lower()
            if kw not in name:
                print(f"[MISMATCH] product name '{name}' does not contain '{kw}'")
                return False

        return True

    # =========================================================================
    # NO-RESULT MESSAGE HELPERS
    # =========================================================================

    def get_no_product_message(self) -> str:
        """
        Wait for the no-results element to be visible, then return its text.
        """
        self.wait_for_page_load()
        return self.get_text(NO_RESULT_MSG)

    def is_no_product_message_displayed(self) -> bool:
        """Return True if the no-results message is currently visible."""
        return self.is_displayed(NO_RESULT_MSG)

    # =========================================================================
    # URL HELPER
    # =========================================================================

    def get_current_url(self) -> str:
        """Return the current browser URL."""
        return self.driver.current_url

    # =========================================================================
    # MANUFACTURER CHECK
    # =========================================================================

    def verify_manufacturer(self, expected_manufacturer: str) -> None:
        """
        Read the manufacturer filter label and assert it matches
        *expected_manufacturer* (case-insensitive).

        Raises:
            ManufacturerMismatchException — when the labels differ.
        """
        self.wait_for_page_load()
        actual = self.get_text(MANUFACTURER_LABEL).strip()

        if actual.lower() != expected_manufacturer.strip().lower():
            raise ManufacturerMismatchException(expected_manufacturer, actual)

        print(f"[OK] Manufacturer verified: {actual}")