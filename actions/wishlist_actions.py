# actions/wishlist_actions.py

import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.wishlist_page import WishListPage
from utils.base_action import BaseAction


class WishListActions(BaseAction):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.wp = WishListPage

    def scroll_to_top_products(self):
        self.wait_for_page_load()
        self.scroll_to_element(self.wp.TOP_PRODUCTS_HEADING)

    def scroll_to_top_collection(self):
        self.wait_for_page_load()
        self.scroll_to_element(self.wp.TOP_COLLECTION_HEADING)

    def add_product_to_wishlist_by_name(self, product_name):
        self.wait_for_page_load()

        card_locator = self.wp.product_card(product_name)
        btn_locator = self.wp.product_wishlist_button(product_name)

        card = self.scroll_to_element(card_locator)
        btn = self.wait.until(EC.presence_of_element_located(btn_locator))

        ActionChains(self.driver).move_to_element(card).perform()
        time.sleep(0.5)

        self.driver.execute_script(
            """
            arguments[0].style.display='block';
            arguments[0].style.opacity='1';
            arguments[0].style.visibility='visible';
            """,
            btn
        )

        self.driver.execute_script("arguments[0].click();", btn)

        alert_text = self.dismiss_alert_if_present()
        if alert_text:
            raise Exception(f"Unexpected alert displayed: {alert_text}")

    def hover_and_click_wishlist_button(self, product_name):
        self.add_product_to_wishlist_by_name(product_name)

    def get_wishlist_success_message_generic(self):
        try:
            return self.get_text(self.wp.SUCCESS_NOTIFICATION)
        except TimeoutException:
            return self.get_text(self.wp.SUCCESS_NOTIFICATION_FALLBACK)

    def click_wishlist_link_from_popup(self):
        self.click(self.wp.WISHLIST_POPUP_LINK)

    def navigate_to_wishlist_via_account(self):
        fallback_url = "https://ecommerce-playground.lambdatest.io/index.php?route=account/wishlist"

        try:
            self.js_click(self.wp.WISHLIST_HEADER_LINK)
            self.wait.until(EC.visibility_of_element_located(self.wp.MY_WISHLIST_TITLE))
        except TimeoutException:
            self.driver.get(fallback_url)
            self.wait.until(EC.visibility_of_element_located(self.wp.MY_WISHLIST_TITLE))

    def wait_for_wishlist_page(self):
        self.dismiss_alert_if_present()
        self.wait.until(EC.visibility_of_element_located(self.wp.MY_WISHLIST_TITLE))

    def get_current_page_title(self):
        return self.driver.title

    def get_all_wishlist_product_names(self):
        return self.get_elements_text(self.wp.WISHLIST_PRODUCT_NAMES)

    def get_all_wishlist_product_prices(self):
        return self.get_elements_text(self.wp.WISHLIST_PRODUCT_PRICES)

    def is_product_present_in_wishlist(self, product_name):
        return self.is_present(self.wp.product_link_for(product_name))

    def remove_product_from_wishlist(self, product_name):
        self.wait_for_wishlist_page()

        remove_btn = self.wait.until(
            EC.element_to_be_clickable(self.wp.remove_button_for(product_name))
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", remove_btn
        )
        time.sleep(0.3)

        self.driver.execute_script("arguments[0].click();", remove_btn)

    def get_removal_success_message(self):
        return self.get_text(self.wp.REMOVAL_SUCCESS_ALERT).replace("×", "").strip()

    def search_for_product(self, product_name):
        self.wait_for_page_load()
        search = self.wait.until(EC.element_to_be_clickable(self.wp.SEARCH_BAR))
        search.clear()
        search.send_keys(product_name)
        search.send_keys(Keys.ENTER)

    def click_product_from_search_results(self, product_name):
        self.wait_for_page_load()
        product = self.wait.until(
            EC.element_to_be_clickable(self.wp.IPOD_SHUFFLE_PRODUCT)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", product
        )
        self.driver.execute_script("arguments[0].click();", product)

    def click_heart_button_on_product_page(self):
        self.wait_for_page_load()
        btn = self.wait.until(
            EC.element_to_be_clickable(self.wp.IPOD_SHUFFLE_WISHLIST_BTN)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", btn
        )
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", btn)