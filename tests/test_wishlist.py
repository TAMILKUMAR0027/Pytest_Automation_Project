"""Wishlist test suite: add and remove products via data-driven CSV."""

import pytest

from actions.wishlist_actions import WishListActions
from actions.HomePageAction import HomePageAction
from actions.loginpageaction import LoginPageAction
from actions.accountpageaction import AccountPageAction
from utils.excelReader import get_data
from utils.loggerCreator import get_logger
from utils.csvDataProvider import CsvDataProvider as CS

LOGIN_DATA_PATH = "data_provider/DataProvider.xlsx"
LOGIN_DATA_SHEET = "loginDataValid"
WISHLIST_CSV_PATH = "data_provider/wishlist_data.csv"

SUCCESS_KEYWORD = "Success"
MODIFIED_KEYWORD = "modified"

logger = get_logger(__name__)


def log_csv_data(data):
    logger.info("CSV test data loaded successfully")

    for key, value in data.items():
        logger.info("%s = %s", key, value)


@pytest.fixture
def setup(driver):
    """Log in and return driver, wait, and wishlist actions."""
    drv, wait = driver

    wishlist_actions = WishListActions(drv)

    assert "route=common/home" in drv.current_url
    logger.info("Landed on home page: %s", drv.current_url)

    login_data = get_data(LOGIN_DATA_PATH, LOGIN_DATA_SHEET)

    logger.info(
        "Loaded %d login record(s) from Excel file '%s' sheet '%s'",
        len(login_data),
        LOGIN_DATA_PATH,
        LOGIN_DATA_SHEET,
    )

    username, password = login_data[0]
    logger.info("Selected login username: %s", username)

    home_page_action = HomePageAction(drv)
    home_page_action.click_myAcc()
    logger.info("Clicked My Account link")

    login_page_action = LoginPageAction(drv)
    login_page_action.enter_login_credentials(username, password)
    logger.info("Submitted login credentials")

    account_page_action = AccountPageAction(drv)
    login_ok = account_page_action.success_login()

    assert login_ok is True
    logger.info("Login successful: %s", login_ok)

    home_url = wishlist_actions.login_after_home()
    logger.info("Navigated back to home page: %s", home_url)

    return drv, wait, wishlist_actions


def _assert_success_message(message):
    """Validate wishlist add success message."""
    logger.info("Wishlist success message: %s", message)

    assert message
    assert SUCCESS_KEYWORD in message


def _assert_removal_message(message):
    """Validate wishlist remove success or modified message."""
    logger.info("Wishlist removal message: %s", message)

    assert message
    assert SUCCESS_KEYWORD in message or MODIFIED_KEYWORD in message


def _ensure_product_in_wishlist(wishlist_actions, product_name, scroll_method):
    """Add product to wishlist if it is not already present."""
    if not wishlist_actions.is_product_present_in_wishlist(product_name):
        logger.info("Product '%s' not found in wishlist. Adding now.", product_name)

        scroll_method()
        wishlist_actions.add_product_to_wishlist_by_name(product_name)

        logger.info("Product '%s' added to wishlist", product_name)

        wishlist_actions.navigate_to_wishlist_via_account()
        wishlist_actions.wait_for_wishlist_page()

        logger.info("Returned to wishlist page after adding product")
    else:
        logger.info("Product '%s' already present in wishlist", product_name)


@pytest.mark.Prasanna
@pytest.mark.parametrize(
    "data",
    CS.get_csv_data_by_test_name(
        WISHLIST_CSV_PATH,
        "test_add_single_product_to_wishlist",
    ),
)
def test_add_single_product_to_wishlist(setup, data):
    """Add a single product from home page to wishlist."""
    _, _, wishlist_actions = setup

    log_csv_data(data)

    product_name = data["product_name"]
    expected_page = data["expected_page"]

    logger.info("Starting test: add single product '%s'", product_name)

    wishlist_actions.scroll_to_top_products()
    logger.info("Scrolled to top products section")

    wishlist_actions.hover_and_click_wishlist_button(product_name)
    logger.info("Clicked wishlist button for '%s'", product_name)

    _assert_success_message(
        wishlist_actions.get_wishlist_success_message_generic()
    )

    wishlist_actions.click_wishlist_link_from_popup()
    wishlist_actions.wait_for_wishlist_page()
    logger.info("Navigated to wishlist page from success popup")

    page_title = wishlist_actions.get_current_page_title()
    logger.info("Wishlist page title: %s", page_title)

    assert expected_page in page_title

    product_names = wishlist_actions.get_all_wishlist_product_names()
    logger.info("Wishlist products: %s", product_names)

    assert any(product_name in name for name in product_names)

    logger.info("Test passed: '%s' found in wishlist", product_name)


@pytest.mark.Prasanna
@pytest.mark.parametrize(
    "data",
    CS.get_csv_data_by_test_name(
        WISHLIST_CSV_PATH,
        "test_add_multiple_products_to_wishlist",
    ),
)
def test_add_multiple_products_to_wishlist(setup, data):
    """Add multiple products from top collection to wishlist."""
    _, _, wishlist_actions = setup

    log_csv_data(data)

    product_name = data["product_name"]

    logger.info("Starting test: add product '%s' from top collection", product_name)

    wishlist_actions.scroll_to_top_collection()
    logger.info("Scrolled to top collection section")

    wishlist_actions.add_product_to_wishlist_by_name(product_name)
    logger.info("Added '%s' to wishlist", product_name)

    _assert_success_message(
        wishlist_actions.get_wishlist_success_message_generic()
    )

    wishlist_actions.navigate_to_wishlist_via_account()
    wishlist_actions.wait_for_wishlist_page()
    logger.info("Navigated to wishlist page via account")

    product_names = wishlist_actions.get_all_wishlist_product_names()
    logger.info("Wishlist products: %s", product_names)

    assert any(product_name in name for name in product_names)

    logger.info("Test passed: '%s' found in wishlist", product_name)


@pytest.mark.Prasanna
@pytest.mark.parametrize(
    "data",
    CS.get_csv_data_by_test_name(
        WISHLIST_CSV_PATH,
        "test_add_product_via_search",
    ),
)
def test_add_product_via_search(setup, data):
    """Add product to wishlist using search flow."""
    _, _, wishlist_actions = setup

    log_csv_data(data)

    product_name = data["product_name"]

    logger.info("Starting test: add product '%s' via search", product_name)

    wishlist_actions.search_for_product(product_name)
    logger.info("Searched product: %s", product_name)

    wishlist_actions.click_product_from_search_results(product_name)
    logger.info("Opened product from search results: %s", product_name)

    wishlist_actions.click_heart_button_on_product_page()
    logger.info("Clicked wishlist heart button on product page")

    _assert_success_message(
        wishlist_actions.get_wishlist_success_message_generic()
    )

    wishlist_actions.navigate_to_wishlist_via_account()
    wishlist_actions.wait_for_wishlist_page()
    logger.info("Navigated to wishlist page via account")

    product_names = wishlist_actions.get_all_wishlist_product_names()
    logger.info("Wishlist products: %s", product_names)

    assert any(product_name in name for name in product_names)

    logger.info("Test passed: '%s' found in wishlist", product_name)


@pytest.mark.Prasanna
@pytest.mark.parametrize(
    "data",
    CS.get_csv_data_by_test_name(
        WISHLIST_CSV_PATH,
        "test_remove_single_product_from_wishlist",
    ),
)
def test_remove_single_product_from_wishlist(setup, data):
    """Remove a single product from wishlist."""
    _, _, wishlist_actions = setup

    log_csv_data(data)

    product_name = data["product_name"]

    logger.info("Starting test: remove single product '%s'", product_name)

    wishlist_actions.navigate_to_wishlist_via_account()
    wishlist_actions.wait_for_wishlist_page()
    logger.info("Navigated to wishlist page")

    _ensure_product_in_wishlist(
        wishlist_actions,
        product_name,
        wishlist_actions.scroll_to_top_products,
    )

    wishlist_actions.remove_product_from_wishlist(product_name)
    logger.info("Clicked remove button for '%s'", product_name)

    _assert_removal_message(
        wishlist_actions.get_removal_success_message()
    )

    logger.info("Test passed: '%s' removed from wishlist", product_name)


@pytest.mark.Prasanna
@pytest.mark.parametrize(
    "data",
    CS.get_csv_data_by_test_name(
        WISHLIST_CSV_PATH,
        "test_remove_multiple_products_from_wishlist",
    ),
)
def test_remove_multiple_products_from_wishlist(setup, data):
    """Remove multiple products from wishlist using CSV data."""
    _, _, wishlist_actions = setup

    log_csv_data(data)

    product_name = data["product_name"]

    logger.info("Starting test: remove product '%s'", product_name)

    wishlist_actions.navigate_to_wishlist_via_account()
    wishlist_actions.wait_for_wishlist_page()
    logger.info("Navigated to wishlist page")

    _ensure_product_in_wishlist(
        wishlist_actions,
        product_name,
        wishlist_actions.scroll_to_top_collection,
    )

    wishlist_actions.remove_product_from_wishlist(product_name)
    logger.info("Clicked remove button for '%s'", product_name)

    _assert_removal_message(
        wishlist_actions.get_removal_success_message()
    )

    logger.info("Test passed: '%s' removed from wishlist", product_name)