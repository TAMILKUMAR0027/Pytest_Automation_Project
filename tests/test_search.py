"""
tests/test_search.py
"""

import os
import pytest

from actions.search_action import SearchAction
from utils.excelReader import get_data
from utils.loggerCreator import get_logger

logger = get_logger(__name__)

# ─── Excel Path ───────────────────────────────────────────────────────────────

SEARCH_EXCEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data_provider", "SearchProduct.xlsx",
)
SEARCH_SHEET = "SearchData"

# ─── Load Data at Collection Time ────────────────────────────────────────────
# get_data() returns [[keyword, manufacturer], ...]
_RAW_ROWS: list[list] = get_data(SEARCH_EXCEL_PATH, SEARCH_SHEET)

# (keyword, manufacturer) tuples — used by keyword + manufacturer tests
_SEARCH_ROWS: list[tuple[str, str]] = [
    (str(row[0]).strip(), str(row[1]).strip())
    for row in _RAW_ROWS if row[0]
]

# keywords only — used by keyword-name tests
_KEYWORDS: list[str] = [kw for kw, _ in _SEARCH_ROWS]

# ─── Fixed Test Data ──────────────────────────────────────────────────────────

NO_RESULT_KEYWORDS = ["Kiot", "ffgok"]
EMPTY_KEYWORD      = ""


# =============================================================================
# @Smoke @KeywordSearch
# Scenario Outline: Validate search results match the entered keyword
#
#   And  the user enters "<keyword>" and presses Enter
#   Then the application should display products based on the keyword
#   And  the application should display products matching the keyword in their name
# =============================================================================

@pytest.mark.Prasanna
@pytest.mark.smoke
@pytest.mark.keyword_search
@pytest.mark.parametrize(
    "keyword",
    _KEYWORDS + [EMPTY_KEYWORD],
    ids=[*_KEYWORDS, "empty_keyword"],
)
def test_keyword_search_results_and_names(driver, keyword):
    drv, _ = driver
    search  = SearchAction(drv)

    logger.info(f"[KeywordSearch] Starting search for keyword: '{keyword}'")

    search.click_search_bar()
    search.enter_keyword_and_press_enter(keyword)

    # ── Empty keyword edge case ───────────────────────────────────────────────
    if keyword.strip() == "":
        logger.info("[KeywordSearch] Empty keyword — asserting page responded")
        product_shown   = search.is_product_list_displayed()
        no_result_shown = search.is_no_product_message_displayed()
        assert product_shown or no_result_shown, (
            "Neither products nor a no-results message appeared for an empty search."
        )
        logger.info("[KeywordSearch] Empty keyword — page responded correctly")
        return

    # ── Products displayed ────────────────────────────────────────────────────
    assert search.is_product_list_displayed(), (
        f"Expected product results for keyword '{keyword}' but none were displayed."
    )
    logger.info(f"[KeywordSearch] Products displayed for keyword: '{keyword}'")

    # ── Every card name contains the keyword ─────────────────────────────────
    assert search.is_keyword_present_in_all_results(keyword), (
        f"One or more product cards did not contain keyword '{keyword}' in their name."
    )
    logger.info(f"[KeywordSearch] All product names matched keyword: '{keyword}'")


# =============================================================================
# @Smoke @NoResultSearch
# Scenario Outline: Validate no-results message for unmatched keywords
#
#   And  the user enters "<keyword>" and presses Enter
#   Then the application should display the no-results message
# =============================================================================

@pytest.mark.Prasanna
@pytest.mark.smoke
@pytest.mark.no_result_search
@pytest.mark.parametrize("keyword", NO_RESULT_KEYWORDS)
def test_no_result_search(driver, keyword):
    drv, _ = driver
    search  = SearchAction(drv)

    logger.info(f"[NoResultSearch] Searching for no-result keyword: '{keyword}'")

    search.click_search_bar()
    search.enter_keyword_and_press_enter(keyword)

    # ── No product cards ──────────────────────────────────────────────────────
    assert not search.is_product_list_displayed(), (
        f"Expected NO products for keyword '{keyword}' but product cards appeared."
    )
    logger.info(f"[NoResultSearch] Confirmed no products shown for: '{keyword}'")

    # ── No-results message visible ────────────────────────────────────────────
    assert search.is_no_product_message_displayed(), (
        f"No-results message was not displayed for keyword '{keyword}'."
    )

    message = search.get_no_product_message()
    assert message.strip(), (
        f"No-results message text was blank for keyword '{keyword}'."
    )
    logger.info(f"[NoResultSearch] No-results message: '{message}' for keyword: '{keyword}'")


# =============================================================================
# @Regression @ManufacturerFilter
# Scenario: Validate search results show only manufacturer products
#
#   And  the user enters the product "<keyword>" and presses Enter
#   Then the application should display products based on the keyword
#   And  the application should list only the manufacturer products
#        based on "<expected_manufacturer>"
# =============================================================================

@pytest.mark.Prasanna
@pytest.mark.regression
@pytest.mark.manufacturer_filter
@pytest.mark.parametrize(
    "keyword, expected_manufacturer",
    _SEARCH_ROWS,
    ids=[f"{kw}-{mfr}" for kw, mfr in _SEARCH_ROWS],
)
def test_manufacturer_filter_search(driver, keyword, expected_manufacturer):
    drv, _ = driver
    search  = SearchAction(drv)

    logger.info(
        f"[ManufacturerFilter] Searching '{keyword}', "
        f"expecting manufacturer: '{expected_manufacturer}'"
    )

    search.click_search_bar()
    search.enter_keyword_and_press_enter(keyword)

    # ── Products displayed ────────────────────────────────────────────────────
    assert search.is_product_list_displayed(), (
        f"Expected products for keyword '{keyword}' but none were displayed."
    )
    logger.info(f"[ManufacturerFilter] Products displayed for keyword: '{keyword}'")

    # ── Manufacturer label matches ────────────────────────────────────────────
    # verify_manufacturer() raises ManufacturerMismatchException on failure
    search.verify_manufacturer(expected_manufacturer)
    logger.info(
        f"[ManufacturerFilter] Manufacturer '{expected_manufacturer}' "
        f"verified for keyword: '{keyword}'"
    )