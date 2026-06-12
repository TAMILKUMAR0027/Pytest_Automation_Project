# tests/test_wishlist.py

import pytest

from actions.wishlist_actions import WishListActions
from actions.login_actions import LoginPageActions


@pytest.fixture
def setup(driver):
    drv, wait = driver

    wla = WishListActions(drv, wait)
    lpa = LoginPageActions(drv, wait)

    assert "route=common/home" in drv.current_url

    drv.get(
        "https://ecommerce-playground.lambdatest.io/index.php?route=account/login"
    )

    lpa.enter_email_and_pass("testlogin@gmail.com", "testlogin")
    lpa.click_login_button()

    assert lpa.login_success_msg() == "My Account"

    return drv, wait, wla, lpa


def test_add_single_product_to_wishlist(setup):
    drv, wait, wla, lpa = setup

    product_name = "iMac"

    wla.scroll_to_top_products()
    wla.hover_and_click_wishlist_button(product_name)

    actual_msg = wla.get_wishlist_success_message_generic()

    assert actual_msg
    assert "Success" in actual_msg

    wla.click_wishlist_link_from_popup()
    wla.wait_for_wishlist_page()

    assert "My Wish List" in wla.get_current_page_title()

    all_products = wla.get_all_wishlist_product_names()

    assert all_products
    assert any(product_name in product for product in all_products)


def test_add_multiple_products_to_wishlist(setup):
    drv, wait, wla, lpa = setup

    products = ["Apple Cinema 30", "iPod Nano"]

    wla.scroll_to_top_collection()

    for product_name in products:
        wla.add_product_to_wishlist_by_name(product_name)

        actual_msg = wla.get_wishlist_success_message_generic()

        assert actual_msg
        assert "Success" in actual_msg

    wla.navigate_to_wishlist_via_account()
    wla.wait_for_wishlist_page()

    all_products = wla.get_all_wishlist_product_names()

    for product_name in products:
        assert any(product_name in product for product in all_products)


def test_add_product_via_search(setup):
    drv, wait, wla, lpa = setup

    product_name = "iPod Shuffle"

    wla.search_for_product(product_name)
    wla.click_product_from_search_results(product_name)
    wla.click_heart_button_on_product_page()

    actual_msg = wla.get_wishlist_success_message_generic()

    assert actual_msg
    assert "Success" in actual_msg

    wla.navigate_to_wishlist_via_account()
    wla.wait_for_wishlist_page()

    all_products = wla.get_all_wishlist_product_names()

    assert any(product_name in product for product in all_products)


def test_remove_single_product_from_wishlist(setup):
    drv, wait, wla, lpa = setup

    product_name = "iMac"

    wla.navigate_to_wishlist_via_account()
    wla.wait_for_wishlist_page()

    if not wla.is_product_present_in_wishlist(product_name):
        wla.scroll_to_top_products()
        wla.add_product_to_wishlist_by_name(product_name)
        wla.navigate_to_wishlist_via_account()

    wla.remove_product_from_wishlist(product_name)

    actual_msg = wla.get_removal_success_message()

    assert actual_msg
    assert "Success" in actual_msg or "modified" in actual_msg


@pytest.mark.parametrize("product_name", ["Apple Cinema 30", "iPod Nano"])
def test_remove_multiple_products_from_wishlist(setup, product_name):
    drv, wait, wla, lpa = setup

    wla.navigate_to_wishlist_via_account()
    wla.wait_for_wishlist_page()

    if not wla.is_product_present_in_wishlist(product_name):
        wla.scroll_to_top_collection()
        wla.add_product_to_wishlist_by_name(product_name)
        wla.navigate_to_wishlist_via_account()

    wla.remove_product_from_wishlist(product_name)

    actual_msg = wla.get_removal_success_message()

    assert actual_msg
    assert "Success" in actual_msg or "modified" in actual_msg