import os
import pytest
from selenium.webdriver.common.by import By

from actions.wishlist_actions import WishListActions
from actions.login_actions import LoginPageActions
from utils.csvDataProvider import CsvDataProvider
from utils.loggerCreator import get_logger

logger = get_logger(__name__)

CSV_PATH = os.path.join(
    os.path.dirname(__file__), "..", "data_provider", "wishlist_data.csv"
)


@pytest.fixture
def setup(driver):
    """Returns (drv, wait, wla, lpa) and ensures user is logged in."""
    drv, wait = driver
    wla = WishListActions(drv, wait)
    lpa = LoginPageActions(drv, wait)

    # ── Background: home page check ─────────────────────────────
    actual_url = drv.current_url
    assert "route=common/home" in actual_url, (
        f"[HOME PAGE] Page did not load correctly.\n"
        f"  Expected URL to contain: route=common/home\n"
        f"  Actual URL: {actual_url}"
    )
    logger.info("Home page verified. URL: %s", actual_url)

    # ── Background: login ───────────────────────────────────────
    drv.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")

    if "route=account/account" in drv.current_url:
        logger.info("Session already active — skipping login.")
    else:
        lpa.enter_email_and_pass("testlogin@gmail.com", "testlogin")
        lpa.click_login_button()

        actual_heading = lpa.login_success_msg()
        expected_heading = "My Account"
        assert actual_heading == expected_heading, (
            f"[LOGIN FAILED] Login did not succeed.\n"
            f"  Expected heading: {expected_heading}\n"
            f"  Actual heading: {actual_heading}\n"
            f"  Check credentials: testlogin@gmail.com / testlogin"
        )
        logger.info("Login verified. Welcome heading: %s", actual_heading)

    return drv, wait, wla, lpa


# =========================================================================
# TEST 1: Add a single product to wishlist (iMac via Top Products)
# =========================================================================

def test_add_single_product_to_wishlist(setup):
    drv, wait, wla, lpa = setup

    wla.scroll_to_top_products()
    logger.info("Scrolled to Top Products section.")

    data = CsvDataProvider.get_first_row(CSV_PATH, "AddSingleProduct")
    assert data is not None, f"[CSV ERROR] No row found for scenario key: 'AddSingleProduct' in {CSV_PATH}"

    product_name = data.get("productName")
    assert product_name, "[CSV ERROR] 'productName' column is missing/empty for scenario: 'AddSingleProduct'"

    wla.hover_and_click_wishlist_button(product_name)
    logger.info("Wishlist button clicked for product: %s", product_name)

    # Assert success notification
    actual_msg = wla.get_wishlist_success_message_generic()
    logger.info("Wishlist add toast message: %s", actual_msg)
    assert actual_msg, "[WISHLIST ADD] Success toast was empty/null."
    assert "Success" in actual_msg, (
        f"[WISHLIST ADD] Toast did not confirm success.\n"
        f"  Expected to contain: 'Success'\n"
        f"  Actual toast text: '{actual_msg}'"
    )

    # Click wishlist link from popup, navigate to wishlist page
    wla.click_wishlist_link_from_popup()

    # Assert redirect
    wla.wait_for_wishlist_page()
    actual_title = wla.get_current_page_title()
    expected_page = data.get("expectedPage")
    assert actual_title, "[REDIRECT] Page title is empty."
    assert expected_page in actual_title, (
        f"[REDIRECT] Page title mismatch.\n"
        f"  Expected to contain: '{expected_page}'\n"
        f"  Actual page title: '{actual_title}'"
    )

    # Assert wishlist table contents
    all_products = wla.get_all_wishlist_product_names()
    all_prices = wla.get_all_wishlist_product_prices()
    assert all_products, "[WISHLIST TABLE] Wishlist table is empty."

    expected_single = product_name
    found = any(expected_single in p for p in all_products)
    assert found, (
        f"[WISHLIST TABLE] Expected product not found.\n"
        f"  Expected (single-add): '{expected_single}'\n"
        f"  All products in table: {all_products}"
    )

    assert all_prices, "[WISHLIST TABLE] Price list is empty."
    for i, price in enumerate(all_prices):
        prod = all_products[i] if i < len(all_products) else f"row {i+1}"
        assert price.strip(), f"[WISHLIST TABLE] Price missing for product '{prod}', row {i+1}"


# =========================================================================
# TEST 2: Add multiple products via CSV (Top Collection)
# =========================================================================

def test_add_multiple_products_to_wishlist(setup):
    drv, wait, wla, lpa = setup

    rows = CsvDataProvider.get_data(CSV_PATH, "AddMultipleProduct1")
    rows += CsvDataProvider.get_data(CSV_PATH, "AddMultipleProduct2")
    assert rows, f"[CSV ERROR] No product rows found for AddMultipleProduct1/2 in {CSV_PATH}"

    wla.scroll_to_top_collection()
    logger.info("Scrolled to Top Collection section.")

    for row in rows:
        product_name = row.get("productName")
        assert product_name, "[CSV ERROR] 'productName' missing/empty in a row under AddMultipleProduct."

        wla.add_product_to_wishlist_by_name(product_name)
        logger.info("Added product to wishlist from CSV: %s", product_name)

        actual_msg = wla.get_wishlist_success_message_generic()
        assert "Success" in actual_msg, (
            f"[WISHLIST ADD] Toast did not confirm success for '{product_name}'. "
            f"Actual: '{actual_msg}'"
        )

    # Navigate to wishlist via account menu
    wla.navigate_to_wishlist_via_account()
    logger.info("Navigated to wishlist page via account menu.")

    actual_title = wla.get_current_page_title()
    assert "My Wish List" in actual_title, (
        f"[REDIRECT] Page title mismatch. Actual: '{actual_title}'"
    )

    all_products = wla.get_all_wishlist_product_names()
    all_prices = wla.get_all_wishlist_product_prices()
    assert all_products, "[WISHLIST TABLE] Wishlist table is empty."

    for row in rows:
        expected = row.get("productName")
        found = any(expected in p for p in all_products)
        logger.info("Product '%s' present in wishlist: %s", expected, found)
        assert found, (
            f"[WISHLIST TABLE] Expected product not found.\n"
            f"  Missing product: '{expected}'\n"
            f"  All products in table: {all_products}"
        )

    assert all_prices, "[WISHLIST TABLE] Price list is empty."
    for i, price in enumerate(all_prices):
        prod = all_products[i] if i < len(all_products) else f"row {i+1}"
        assert price.strip(), f"[WISHLIST TABLE] Price missing for product '{prod}', row {i+1}"


# =========================================================================
# TEST 3: Add a product via search and product detail page heart button
# =========================================================================

def test_add_product_via_search(setup):
    drv, wait, wla, lpa = setup

    data = CsvDataProvider.get_first_row(CSV_PATH, "AddSearchProduct")
    assert data is not None, f"[CSV ERROR] No row found for scenario key: 'AddSearchProduct' in {CSV_PATH}"

    product_name = data.get("productName")
    assert product_name, "[CSV ERROR] 'productName' missing/empty for scenario: 'AddSearchProduct'"

    wla.search_for_product(product_name)
    logger.info("Search submitted with term: %s", product_name)

    wla.click_product_from_search_results(product_name)
    logger.info("Clicked product from search results: %s", product_name)

    wla.click_heart_button_on_product_page()
    logger.info("Heart/wishlist button clicked on product detail page.")

    actual_msg = wla.get_wishlist_success_message_generic()
    assert actual_msg, "[WISHLIST ADD] Success toast was empty/null."
    assert "Success" in actual_msg, (
        f"[WISHLIST ADD] Toast did not confirm success. Actual: '{actual_msg}'"
    )

    # Navigate to wishlist via account menu
    wla.navigate_to_wishlist_via_account()
    wla.wait_for_wishlist_page()

    actual_title = wla.get_current_page_title()
    expected_page = data.get("expectedPage")
    assert expected_page in actual_title, (
        f"[REDIRECT] Page title mismatch. Expected: '{expected_page}', Actual: '{actual_title}'"
    )

    all_products = wla.get_all_wishlist_product_names()
    all_prices = wla.get_all_wishlist_product_prices()
    assert all_products, "[WISHLIST TABLE] Wishlist table is empty."

    found = any(product_name in p for p in all_products)
    assert found, (
        f"[WISHLIST TABLE] Expected product not found.\n"
        f"  Expected (search-add): '{product_name}'\n"
        f"  All products in table: {all_products}"
    )

    assert all_prices, "[WISHLIST TABLE] Price list is empty."


# =========================================================================
# TEST 4: Remove a single product from the wishlist (RemoveProduct1)
# =========================================================================

def test_remove_single_product_from_wishlist(setup):
    drv, wait, wla, lpa = setup

    data = CsvDataProvider.get_first_row(CSV_PATH, "RemoveProduct1")
    assert data is not None, f"[CSV ERROR] No row found for scenario key: 'RemoveProduct1' in {CSV_PATH}"

    product_name = data.get("productName")
    assert product_name, "[CSV ERROR] 'productName' missing/empty for scenario: 'RemoveProduct1'"

    # Navigate to wishlist page first to check presence
    wla.navigate_to_wishlist_via_account()
    wla.wait_for_wishlist_page()

    present_before = wla.is_product_present_in_wishlist(product_name)
    logger.info("Product '%s' present before removal: %s", product_name, present_before)

    if not present_before:
        logger.info("'%s' not in wishlist — adding it before removal.", product_name)
        wla.scroll_to_top_collection()
        wla.add_product_to_wishlist_by_name(product_name)
        wla.navigate_to_wishlist_via_account()
        wla.wait_for_wishlist_page()

    wla.remove_product_from_wishlist(product_name)
    logger.info("Removal clicked for product: %s", product_name)

    # Assert removal success message
    actual_msg = wla.get_removal_success_message()
    logger.info("Wishlist removal alert message: %s", actual_msg)
    assert actual_msg, "[WISHLIST REMOVE] Removal alert message is empty/null."
    assert ("Success" in actual_msg) or ("modified" in actual_msg), (
        f"[WISHLIST REMOVE] Alert did not confirm removal success.\n"
        f"  Expected to contain: 'Success' or 'modified'\n"
        f"  Actual alert text: '{actual_msg}'"
    )


# =========================================================================
# TEST 5: Remove multiple products (data-driven via inline list)
# =========================================================================

@pytest.mark.parametrize("product_name", ["Apple Cinema 30", "iPod Nano"])
def test_remove_multiple_products_from_wishlist(setup, product_name):
    drv, wait, wla, lpa = setup

    wla.navigate_to_wishlist_via_account()
    wla.wait_for_wishlist_page()

    present_before = wla.is_product_present_in_wishlist(product_name)
    logger.info("Product '%s' present before removal: %s", product_name, present_before)

    if not present_before:
        logger.info("'%s' not in wishlist — adding it before removal.", product_name)
        wla.scroll_to_top_collection()
        wla.add_product_to_wishlist_by_name(product_name)
        wla.navigate_to_wishlist_via_account()
        wla.wait_for_wishlist_page()

    wla.remove_product_from_wishlist(product_name)
    logger.info("Removal clicked for product: %s", product_name)

    actual_msg = wla.get_removal_success_message()
    assert actual_msg, "[WISHLIST REMOVE] Removal alert message is empty/null."
    assert ("Success" in actual_msg) or ("modified" in actual_msg), (
        f"[WISHLIST REMOVE] Alert did not confirm removal success. Actual: '{actual_msg}'"
    )