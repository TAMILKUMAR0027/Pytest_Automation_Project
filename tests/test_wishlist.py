"""Wishlist test suite: add and remove products via various flows."""

import pytest

from actions.wishlist_actions import WishListActions
from actions.HomePageAction import HomePageAction
from actions.loginpageaction import LoginPageAction
from actions.accountpageaction import AccountPageAction
from utils.excelReader import get_data
from utils.loggerCreator import get_logger

LOGIN_DATA_PATH = "data_provider/DataProvider.xlsx"
LOGIN_DATA_SHEET = "loginDataValid"

PRODUCT_IMAC = "iMac"
PRODUCT_APPLE_CINEMA = "Apple Cinema 30"
PRODUCT_IPOD_NANO = "iPod Nano"
PRODUCT_IPOD_SHUFFLE = "iPod Shuffle"

SUCCESS_KEYWORD = "Success"
MODIFIED_KEYWORD = "modified"

logger = get_logger(__name__)


@pytest.fixture
def setup(driver):
    """Log in and return (driver, wait, wishlist_actions) for each test."""
    drv, wait = driver

    wishlist_actions = WishListActions(drv)

    assert "route=common/home" in drv.current_url
    logger.info("Landed on home page: %s", drv.current_url)

    username, password = get_data(LOGIN_DATA_PATH, LOGIN_DATA_SHEET)[0]
    logger.info("Using credentials for user: %s", username)

    home_page_action = HomePageAction(drv)
    home_page_action.click_myAcc()
    logger.info("Clicked 'My Account' link")

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
    logger.info("Wishlist success message: %s", message)
    assert message
    assert SUCCESS_KEYWORD in message


def _assert_removal_message(message):
    logger.info("Wishlist removal message: %s", message)
    assert message
    assert SUCCESS_KEYWORD in message or MODIFIED_KEYWORD in message


def _ensure_product_in_wishlist(wishlist_actions, product_name, scroll_method):
    if not wishlist_actions.is_product_present_in_wishlist(product_name):
        logger.info("'%s' not in wishlist, adding it now", product_name)
        scroll_method()
        wishlist_actions.add_product_to_wishlist_by_name(product_name)
        wishlist_actions.navigate_to_wishlist_via_account()
        wishlist_actions.wait_for_wishlist_page()
    else:
        logger.info("'%s' already present in wishlist", product_name)


@pytest.mark.Prasanna
def test_add_single_product_to_wishlist(setup):
    """Adding a single product from the home page shows it in the wishlist."""
    _, _, wishlist_actions = setup

    logger.info("Starting test: add single product '%s' to wishlist", PRODUCT_IMAC)

    wishlist_actions.scroll_to_top_products()
    wishlist_actions.hover_and_click_wishlist_button(PRODUCT_IMAC)
    logger.info("Clicked wishlist button for '%s'", PRODUCT_IMAC)

    _assert_success_message(wishlist_actions.get_wishlist_success_message_generic())

    wishlist_actions.click_wishlist_link_from_popup()
    wishlist_actions.wait_for_wishlist_page()
    logger.info("Navigated to wishlist page via popup link")

    page_title = wishlist_actions.get_current_page_title()
    logger.info("Wishlist page title: %s", page_title)
    assert "My Wish List" in page_title

    product_names = wishlist_actions.get_all_wishlist_product_names()
    logger.info("Products currently in wishlist: %s", product_names)
    assert product_names
    assert any(PRODUCT_IMAC in name for name in product_names)

    logger.info("Test passed: '%s' found in wishlist", PRODUCT_IMAC)


@pytest.mark.Prasanna
def test_add_multiple_products_to_wishlist(setup):
    """Adding multiple products from the top collection shows all of them in the wishlist."""
    _, _, wishlist_actions = setup

    products = [PRODUCT_APPLE_CINEMA, PRODUCT_IPOD_NANO]
    logger.info("Starting test: add multiple products %s to wishlist", products)

    wishlist_actions.scroll_to_top_collection()

    for product_name in products:
        wishlist_actions.add_product_to_wishlist_by_name(product_name)
        logger.info("Added '%s' to wishlist", product_name)
        _assert_success_message(wishlist_actions.get_wishlist_success_message_generic())

    wishlist_actions.navigate_to_wishlist_via_account()
    wishlist_actions.wait_for_wishlist_page()
    logger.info("Navigated to wishlist page via account")

    product_names = wishlist_actions.get_all_wishlist_product_names()
    logger.info("Products currently in wishlist: %s", product_names)

    for product_name in products:
        assert any(product_name in name for name in product_names)

    logger.info("Test passed: all products %s found in wishlist", products)


@pytest.mark.Prasanna
def test_add_product_via_search(setup):
    """Adding a product found via search shows it in the wishlist."""
    _, _, wishlist_actions = setup

    logger.info("Starting test: add product '%s' via search", PRODUCT_IPOD_SHUFFLE)

    wishlist_actions.search_for_product(PRODUCT_IPOD_SHUFFLE)
    logger.info("Searched for product: %s", PRODUCT_IPOD_SHUFFLE)

    wishlist_actions.click_product_from_search_results(PRODUCT_IPOD_SHUFFLE)
    logger.info("Opened product page for: %s", PRODUCT_IPOD_SHUFFLE)

    wishlist_actions.click_heart_button_on_product_page()
    logger.info("Clicked wishlist (heart) button on product page")

    _assert_success_message(wishlist_actions.get_wishlist_success_message_generic())

    wishlist_actions.navigate_to_wishlist_via_account()
    wishlist_actions.wait_for_wishlist_page()
    logger.info("Navigated to wishlist page via account")

    product_names = wishlist_actions.get_all_wishlist_product_names()
    logger.info("Products currently in wishlist: %s", product_names)
    assert any(PRODUCT_IPOD_SHUFFLE in name for name in product_names)

    logger.info("Test passed: '%s' found in wishlist", PRODUCT_IPOD_SHUFFLE)


@pytest.mark.Prasanna
def test_remove_single_product_from_wishlist(setup):
    """Removing a single product from the wishlist shows a success/modified message."""
    _, _, wishlist_actions = setup

    logger.info("Starting test: remove single product '%s' from wishlist", PRODUCT_IMAC)

    wishlist_actions.navigate_to_wishlist_via_account()
    wishlist_actions.wait_for_wishlist_page()
    logger.info("Navigated to wishlist page")

    _ensure_product_in_wishlist(
        wishlist_actions, PRODUCT_IMAC, wishlist_actions.scroll_to_top_products
    )

    wishlist_actions.remove_product_from_wishlist(PRODUCT_IMAC)
    logger.info("Clicked remove button for '%s'", PRODUCT_IMAC)

    _assert_removal_message(wishlist_actions.get_removal_success_message())

    logger.info("Test passed: '%s' removed from wishlist", PRODUCT_IMAC)


@pytest.mark.Prasanna
@pytest.mark.parametrize("product_name", [PRODUCT_APPLE_CINEMA, PRODUCT_IPOD_NANO])
def test_remove_multiple_products_from_wishlist(setup, product_name):
    """Removing each product from the wishlist shows a success/modified message."""
    _, _, wishlist_actions = setup

    logger.info("Starting test: remove product '%s' from wishlist", product_name)

    wishlist_actions.navigate_to_wishlist_via_account()
    wishlist_actions.wait_for_wishlist_page()
    logger.info("Navigated to wishlist page")

    _ensure_product_in_wishlist(
        wishlist_actions, product_name, wishlist_actions.scroll_to_top_collection
    )

    wishlist_actions.remove_product_from_wishlist(product_name)
    logger.info("Clicked remove button for '%s'", product_name)

    _assert_removal_message(wishlist_actions.get_removal_success_message())

    logger.info("Test passed: '%s' removed from wishlist", product_name)