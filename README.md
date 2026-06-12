# Pytest Selenium Automation Framework

A robust and scalable Selenium WebDriver automation framework built with **Python** and **Pytest**.

---

## Features

- ✅ **Cross-browser support** (Chrome & Firefox)
- ✅ **Headless & Normal mode** support
- ✅ **Page Object Model (POM)** design pattern
- ✅ **Centralized configuration** via `config.ini`
- ✅ **Automatic driver management** (webdriver-manager)
- ✅ **Explicit & Implicit waits** with configurable timeouts
- ✅ **Rich logging** and reporting
- ✅ **Pytest markers** for selective test execution
- ✅ **Allure & HTML reporting** support
- ✅ **Parallel test execution** ready (`pytest-xdist`)

---

## Project Structure

```bash
D:\Pytest_Automation_Project
├── configuration/          # Config files (config.ini)
├── pages/                  # Page Object classes (POM)
├── tests/                  # Test cases
├── utils/                  # Utility functions & logger
├── actions/                # Reusable actions (if any)
├── data_provider/          # Test data (Excel, JSON, etc.)
├── logs/                   # Log files
├── conftest.py             # Fixtures & Driver Setup
├── pytest.ini              # Pytest configuration & markers
├── requirements.txt
├── .gitignore
└── README.md




Installation

Clone or navigate to the project directory:

Bashcd D:\Pytest_Automation_Project

Install dependencies:

Bashpip install -r requirements.txt

Configuration
Edit configuration/config.ini:
ini[browser]
browser = firefox        # chrome or firefox
mode = normal            # normal or headless

[application]
url = https://ecommerce-playground.lambdatest.io/index.php?route=common/home
title = Your Store

[timeouts]
implicit_wait = 10
explicit_wait = 15
page_load_timeout = 30

Running Tests
Basic Commands
Bash# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_launch.py -v

# Run with markers
pytest -m smoke
pytest -m "sanity and regression"
pytest -m "not slow"
Other Useful Commands
Bash# Run in parallel (using 4 workers)
pytest -n 4

# Generate HTML report
pytest --html=reports/report.html --self-contained-html

# Generate Allure report
pytest --alluredir=allure-results
allure serve allure-results

Writing Tests
Example test structure:
Python@pytest.mark.smoke
@pytest.mark.regression
def test_homepage_verification(self, driver):
    drv, wait = driver
    lp = LaunchPages(drv)
    # Your test logic...

Tech Stack

Python 3.x
Pytest 9.0+
Selenium 4.44+
Webdriver-manager
Allure Reporting
Pytest-HTML
Logging


Requirements
See full list in requirements.txt

Contributing

Create a new branch for your feature.
Follow the existing POM structure.
Add proper logging and assertions.
Test with both Chrome and Firefox.


Author
Pytest Automation Project - Tamil Kumar, Prasanna Venkatesh K, Rishwanth, Samiha, Jothika
Automated UI Testing Framework

Happy Testing! 🚀
text---

### How to use:

1. Copy the entire content above.
2. Go to your project folder.
3. Replace the existing `README.md` (currently empty) with this content.

Would you like a shorter version or one with screenshots/badges as well?

## Latest Execution
```
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-9.0.3, pluggy-1.6.0
rootdir: /home/runner/work/Pytest_Automation_Project/Pytest_Automation_Project
configfile: pytest.ini
testpaths: tests
plugins: rerunfailures-16.3, soft-assertions-0.1.2, xdist-3.8.0, allure-pytest-2.16.0, metadata-3.1.1, html-4.2.0, ordering-0.6, ast-transformer-1.0.3
collected 14 items

tests/test_Filter_By_Price.py .                                          [  7%]
tests/test_Instock_product.py .                                          [ 14%]
tests/test_filterBymanufacture.py .                                      [ 21%]
tests/test_forgetpassword.py ..                                          [ 35%]
tests/test_launch.py .                                                   [ 42%]
tests/test_login.py .                                                    [ 50%]
tests/test_register.py .                                                 [ 57%]
tests/test_wishlist.py F.FFFF                                            [100%]

=================================== FAILURES ===================================
_____________________ test_add_single_product_to_wishlist ______________________

setup = (<selenium.webdriver.chrome.webdriver.WebDriver (session="cafdf96cbc0e197015e3f9a8ec7c4954")>, <selenium.webdriver.sup...ait (session="cafdf96cbc0e197015e3f9a8ec7c4954")>, <actions.wishlist_actions.WishListActions object at 0x7f5c46559ca0>)

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
>       wishlist_actions.wait_for_wishlist_page()

tests/test_wishlist.py:95: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
actions/wishlist_actions.py:82: in wait_for_wishlist_page
    self.wait.until(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <selenium.webdriver.support.wait.WebDriverWait (session="cafdf96cbc0e197015e3f9a8ec7c4954")>
method = <function visibility_of_element_located.<locals>._predicate at 0x7f5c463b16c0>
message = ''

    def until(self, method: Callable[[D], Literal[False] | T], message: str = "") -> T:
        """Wait until the method returns a value that is not False.
    
        Calls the method provided with the driver as an argument until the
        return value does not evaluate to ``False``.
    
        Args:
            method: A callable object that takes a WebDriver instance as an
                argument.
            message: Optional message for TimeoutException.
    
        Returns:
            The result of the last call to `method`.
    
        Raises:
            TimeoutException: If 'method' does not return a truthy value within
                the WebDriverWait object's timeout.
    
        Example:
            >>> from selenium.webdriver.common.by import By
            >>> from selenium.webdriver.support.ui import WebDriverWait
            >>> from selenium.webdriver.support import expected_conditions as EC
            >>>
            >>> # Wait until an element is visible on the page
            >>> wait = WebDriverWait(driver, 10)
            >>> element = wait.until(EC.visibility_of_element_located((By.ID, "exampleId")))
            >>> print(element.text)
        """
        screen = None
        stacktrace = None
    
        end_time = time.monotonic() + self._timeout
        while True:
            try:
                value = method(self._driver)
                if value:
                    return value
            except self._ignored_exceptions as exc:
                screen = getattr(exc, "screen", None)
                stacktrace = getattr(exc, "stacktrace", None)
            if time.monotonic() > end_time:
                break
            time.sleep(self._poll)
>       raise TimeoutException(message, screen, stacktrace)
E       selenium.common.exceptions.TimeoutException: Message: 
E       Stacktrace:
E       #0 0x55893bc0229a <unknown>
E       #1 0x55893b5e4449 <unknown>
E       #2 0x55893b638baf <unknown>
E       #3 0x55893b638e01 <unknown>
E       #4 0x55893b683ae4 <unknown>
E       #5 0x55893b680cbf <unknown>
E       #6 0x55893b62c132 <unknown>
E       #7 0x55893b62cf41 <unknown>
E       #8 0x55893bbc8737 <unknown>
E       #9 0x55893bbc6f39 <unknown>
E       #10 0x55893bbb1c26 <unknown>
E       #11 0x55893bbc7ada <unknown>
E       #12 0x55893bb99bd0 <unknown>
E       #13 0x55893bbeec28 <unknown>
E       #14 0x55893bbeedc5 <unknown>
E       #15 0x55893bc00e1e <unknown>
E       #16 0x7fe99889caa4 <unknown>
E       #17 0x7fe998929c6c <unknown>

../../../.local/lib/python3.12/site-packages/selenium/webdriver/support/wait.py:121: TimeoutException
---------------------------- Captured stderr setup -----------------------------
2026-06-12 07:04:03  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-12 07:04:03  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-12 07:04:04  INFO      conftest  Driver started → browser=chrome | mode=headless
2026-06-12 07:04:04  INFO      tests.test_wishlist  Landed on home page: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-12 07:04:04  INFO      tests.test_wishlist  Using credentials for user: testlogin@gmail.com
2026-06-12 07:04:05  INFO      tests.test_wishlist  Clicked 'My Account' link
2026-06-12 07:04:06  INFO      tests.test_wishlist  Submitted login credentials
2026-06-12 07:04:06  INFO      tests.test_wishlist  Login successful: True
2026-06-12 07:04:06  INFO      actions.wishlist_actions  Navigating to home page: https://ecommerce-playground.lambdatest.io/
2026-06-12 07:04:06  INFO      actions.wishlist_actions  Home page loaded successfully
2026-06-12 07:04:06  INFO      tests.test_wishlist  Navigated back to home page: https://ecommerce-playground.lambdatest.io/
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:56 Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:95 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:101 Driver started → browser=chrome | mode=headless
INFO     tests.test_wishlist:test_wishlist.py:34 Landed on home page: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     tests.test_wishlist:test_wishlist.py:37 Using credentials for user: testlogin@gmail.com
INFO     tests.test_wishlist:test_wishlist.py:41 Clicked 'My Account' link
INFO     tests.test_wishlist:test_wishlist.py:45 Submitted login credentials
INFO     tests.test_wishlist:test_wishlist.py:50 Login successful: True
INFO     actions.wishlist_actions:wishlist_actions.py:37 Navigating to home page: https://ecommerce-playground.lambdatest.io/
INFO     actions.wishlist_actions:wishlist_actions.py:43 Home page loaded successfully
INFO     tests.test_wishlist:test_wishlist.py:53 Navigated back to home page: https://ecommerce-playground.lambdatest.io/
----------------------------- Captured stderr call -----------------------------
2026-06-12 07:04:06  INFO      tests.test_wishlist  Starting test: add single product 'iMac' to wishlist
2026-06-12 07:04:06  INFO      actions.wishlist_actions  Scrolled to 'Top Products' section
2026-06-12 07:04:07  INFO      actions.wishlist_actions  Adding product 'iMac' to wishlist
2026-06-12 07:04:07  INFO      actions.wishlist_actions  Clicked wishlist button for 'iMac'
2026-06-12 07:04:10  INFO      tests.test_wishlist  Clicked wishlist button for 'iMac'
2026-06-12 07:04:10  INFO      actions.wishlist_actions  Success notification text: Success: You have added
iMac
to your
wish list
!
2026-06-12 07:04:10  INFO      tests.test_wishlist  Wishlist success message: Success: You have added
iMac
to your
wish list
!
2026-06-12 07:04:10  INFO      actions.wishlist_actions  Clicked 'View Wish List' link from popup
------------------------------ Captured log call -------------------------------
INFO     tests.test_wishlist:test_wishlist.py:86 Starting test: add single product 'iMac' to wishlist
INFO     actions.wishlist_actions:wishlist_actions.py:50 Scrolled to 'Top Products' section
INFO     actions.wishlist_actions:wishlist_actions.py:100 Adding product 'iMac' to wishlist
INFO     actions.wishlist_actions:wishlist_actions.py:113 Clicked wishlist button for 'iMac'
INFO     tests.test_wishlist:test_wishlist.py:90 Clicked wishlist button for 'iMac'
INFO     actions.wishlist_actions:wishlist_actions.py:167 Success notification text: Success: You have added
iMac
to your
wish list
!
INFO     tests.test_wishlist:test_wishlist.py:59 Wishlist success message: Success: You have added
iMac
to your
wish list
!
INFO     actions.wishlist_actions:wishlist_actions.py:173 Clicked 'View Wish List' link from popup
--------------------------- Captured stderr teardown ---------------------------
2026-06-12 07:04:29  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:108 Quitting driver.
_________________________ test_add_product_via_search __________________________

setup = (<selenium.webdriver.chrome.webdriver.WebDriver (session="ade66fcd6d3e9fbf1243d1af95efcd2e")>, <selenium.webdriver.sup...ait (session="ade66fcd6d3e9fbf1243d1af95efcd2e")>, <actions.wishlist_actions.WishListActions object at 0x7f5c46683410>)

    @pytest.mark.Prasanna
    def test_add_product_via_search(setup):
        """Adding a product found via search shows it in the wishlist."""
        _, _, wishlist_actions = setup
    
        logger.info("Starting test: add product '%s' via search", PRODUCT_IPOD_SHUFFLE)
    
        wishlist_actions.search_for_product(PRODUCT_IPOD_SHUFFLE)
        logger.info("Searched for product: %s", PRODUCT_IPOD_SHUFFLE)
    
>       wishlist_actions.click_product_from_search_results(PRODUCT_IPOD_SHUFFLE)

tests/test_wishlist.py:148: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
actions/wishlist_actions.py:138: in click_product_from_search_results
    product = self.wait.until(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <selenium.webdriver.support.wait.WebDriverWait (session="ade66fcd6d3e9fbf1243d1af95efcd2e")>
method = <function element_to_be_clickable.<locals>._predicate at 0x7f5c463b00e0>
message = ''

    def until(self, method: Callable[[D], Literal[False] | T], message: str = "") -> T:
        """Wait until the method returns a value that is not False.
    
        Calls the method provided with the driver as an argument until the
        return value does not evaluate to ``False``.
    
        Args:
            method: A callable object that takes a WebDriver instance as an
                argument.
            message: Optional message for TimeoutException.
    
        Returns:
            The result of the last call to `method`.
    
        Raises:
            TimeoutException: If 'method' does not return a truthy value within
                the WebDriverWait object's timeout.
    
        Example:
            >>> from selenium.webdriver.common.by import By
            >>> from selenium.webdriver.support.ui import WebDriverWait
            >>> from selenium.webdriver.support import expected_conditions as EC
            >>>
            >>> # Wait until an element is visible on the page
            >>> wait = WebDriverWait(driver, 10)
            >>> element = wait.until(EC.visibility_of_element_located((By.ID, "exampleId")))
            >>> print(element.text)
        """
        screen = None
        stacktrace = None
    
        end_time = time.monotonic() + self._timeout
        while True:
            try:
                value = method(self._driver)
                if value:
                    return value
            except self._ignored_exceptions as exc:
                screen = getattr(exc, "screen", None)
                stacktrace = getattr(exc, "stacktrace", None)
            if time.monotonic() > end_time:
                break
            time.sleep(self._poll)
>       raise TimeoutException(message, screen, stacktrace)
E       selenium.common.exceptions.TimeoutException: Message:

../../../.local/lib/python3.12/site-packages/selenium/webdriver/support/wait.py:121: TimeoutException
---------------------------- Captured stderr setup -----------------------------
2026-06-12 07:04:44  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-12 07:04:44  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-12 07:04:45  INFO      conftest  Driver started → browser=chrome | mode=headless
2026-06-12 07:04:45  INFO      tests.test_wishlist  Landed on home page: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-12 07:04:45  INFO      tests.test_wishlist  Using credentials for user: testlogin@gmail.com
2026-06-12 07:04:45  INFO      tests.test_wishlist  Clicked 'My Account' link
2026-06-12 07:04:46  INFO      tests.test_wishlist  Submitted login credentials
2026-06-12 07:04:46  INFO      tests.test_wishlist  Login successful: True
2026-06-12 07:04:46  INFO      actions.wishlist_actions  Navigating to home page: https://ecommerce-playground.lambdatest.io/
2026-06-12 07:04:47  INFO      actions.wishlist_actions  Home page loaded successfully
2026-06-12 07:04:47  INFO      tests.test_wishlist  Navigated back to home page: https://ecommerce-playground.lambdatest.io/
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:56 Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:95 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:101 Driver started → browser=chrome | mode=headless
INFO     tests.test_wishlist:test_wishlist.py:34 Landed on home page: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     tests.test_wishlist:test_wishlist.py:37 Using credentials for user: testlogin@gmail.com
INFO     tests.test_wishlist:test_wishlist.py:41 Clicked 'My Account' link
INFO     tests.test_wishlist:test_wishlist.py:45 Submitted login credentials
INFO     tests.test_wishlist:test_wishlist.py:50 Login successful: True
INFO     actions.wishlist_actions:wishlist_actions.py:37 Navigating to home page: https://ecommerce-playground.lambdatest.io/
INFO     actions.wishlist_actions:wishlist_actions.py:43 Home page loaded successfully
INFO     tests.test_wishlist:test_wishlist.py:53 Navigated back to home page: https://ecommerce-playground.lambdatest.io/
----------------------------- Captured stderr call -----------------------------
2026-06-12 07:04:47  INFO      tests.test_wishlist  Starting test: add product 'iPod Shuffle' via search
2026-06-12 07:04:47  INFO      actions.wishlist_actions  Searched for product: iPod Shuffle
2026-06-12 07:04:47  INFO      tests.test_wishlist  Searched for product: iPod Shuffle
------------------------------ Captured log call -------------------------------
INFO     tests.test_wishlist:test_wishlist.py:143 Starting test: add product 'iPod Shuffle' via search
INFO     actions.wishlist_actions:wishlist_actions.py:133 Searched for product: iPod Shuffle
INFO     tests.test_wishlist:test_wishlist.py:146 Searched for product: iPod Shuffle
--------------------------- Captured stderr teardown ---------------------------
2026-06-12 07:05:03  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:108 Quitting driver.
___________________ test_remove_single_product_from_wishlist ___________________

setup = (<selenium.webdriver.chrome.webdriver.WebDriver (session="9b398b398e456d1b8ea28eda65b0bb9a")>, <selenium.webdriver.sup...ait (session="9b398b398e456d1b8ea28eda65b0bb9a")>, <actions.wishlist_actions.WishListActions object at 0x7f5c465586e0>)

    @pytest.mark.Prasanna
    def test_remove_single_product_from_wishlist(setup):
        """Removing a single product from the wishlist shows a success/modified message."""
        _, _, wishlist_actions = setup
    
        logger.info("Starting test: remove single product '%s' from wishlist", PRODUCT_IMAC)
    
        wishlist_actions.navigate_to_wishlist_via_account()
        wishlist_actions.wait_for_wishlist_page()
        logger.info("Navigated to wishlist page")
    
>       _ensure_product_in_wishlist(
            wishlist_actions, PRODUCT_IMAC, wishlist_actions.scroll_to_top_products
        )

tests/test_wishlist.py:178: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
tests/test_wishlist.py:73: in _ensure_product_in_wishlist
    scroll_method()
actions/wishlist_actions.py:49: in scroll_to_top_products
    self.scroll_into_view(self.wishlist_page.TOP_PRODUCTS_HEADING)
actions/BaseAction.py:51: in scroll_into_view
    element = self.wait.until(ec.presence_of_element_located(locator))
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <selenium.webdriver.support.wait.WebDriverWait (session="9b398b398e456d1b8ea28eda65b0bb9a")>
method = <function presence_of_element_located.<locals>._predicate at 0x7f5c463b2660>
message = ''

    def until(self, method: Callable[[D], Literal[False] | T], message: str = "") -> T:
        """Wait until the method returns a value that is not False.
    
        Calls the method provided with the driver as an argument until the
        return value does not evaluate to ``False``.
    
        Args:
            method: A callable object that takes a WebDriver instance as an
                argument.
            message: Optional message for TimeoutException.
    
        Returns:
            The result of the last call to `method`.
    
        Raises:
            TimeoutException: If 'method' does not return a truthy value within
                the WebDriverWait object's timeout.
    
        Example:
            >>> from selenium.webdriver.common.by import By
            >>> from selenium.webdriver.support.ui import WebDriverWait
            >>> from selenium.webdriver.support import expected_conditions as EC
            >>>
            >>> # Wait until an element is visible on the page
            >>> wait = WebDriverWait(driver, 10)
            >>> element = wait.until(EC.visibility_of_element_located((By.ID, "exampleId")))
            >>> print(element.text)
        """
        screen = None
        stacktrace = None
    
        end_time = time.monotonic() + self._timeout
        while True:
            try:
                value = method(self._driver)
                if value:
                    return value
            except self._ignored_exceptions as exc:
                screen = getattr(exc, "screen", None)
                stacktrace = getattr(exc, "stacktrace", None)
            if time.monotonic() > end_time:
                break
            time.sleep(self._poll)
>       raise TimeoutException(message, screen, stacktrace)
E       selenium.common.exceptions.TimeoutException: Message: 
E       Stacktrace:
E       #0 0x56394334529a <unknown>
E       #1 0x563942d27449 <unknown>
E       #2 0x563942d7bbaf <unknown>
E       #3 0x563942d7be01 <unknown>
E       #4 0x563942dc6ae4 <unknown>
E       #5 0x563942dc3cbf <unknown>
E       #6 0x563942d6f132 <unknown>
E       #7 0x563942d6ff41 <unknown>
E       #8 0x56394330b737 <unknown>
E       #9 0x563943309f39 <unknown>
E       #10 0x5639432f4c26 <unknown>
E       #11 0x56394330aada <unknown>
E       #12 0x5639432dcbd0 <unknown>
E       #13 0x563943331c28 <unknown>
E       #14 0x563943331dc5 <unknown>
E       #15 0x563943343e1e <unknown>
E       #16 0x7f8cd109caa4 <unknown>
E       #17 0x7f8cd1129c6c <unknown>

../../../.local/lib/python3.12/site-packages/selenium/webdriver/support/wait.py:121: TimeoutException
---------------------------- Captured stderr setup -----------------------------
2026-06-12 07:05:03  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-12 07:05:03  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-12 07:05:04  INFO      conftest  Driver started → browser=chrome | mode=headless
2026-06-12 07:05:04  INFO      tests.test_wishlist  Landed on home page: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-12 07:05:04  INFO      tests.test_wishlist  Using credentials for user: testlogin@gmail.com
2026-06-12 07:05:04  INFO      tests.test_wishlist  Clicked 'My Account' link
2026-06-12 07:05:05  INFO      tests.test_wishlist  Submitted login credentials
2026-06-12 07:05:05  INFO      tests.test_wishlist  Login successful: True
2026-06-12 07:05:05  INFO      actions.wishlist_actions  Navigating to home page: https://ecommerce-playground.lambdatest.io/
2026-06-12 07:05:06  INFO      actions.wishlist_actions  Home page loaded successfully
2026-06-12 07:05:06  INFO      tests.test_wishlist  Navigated back to home page: https://ecommerce-playground.lambdatest.io/
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:56 Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:95 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:101 Driver started → browser=chrome | mode=headless
INFO     tests.test_wishlist:test_wishlist.py:34 Landed on home page: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     tests.test_wishlist:test_wishlist.py:37 Using credentials for user: testlogin@gmail.com
INFO     tests.test_wishlist:test_wishlist.py:41 Clicked 'My Account' link
INFO     tests.test_wishlist:test_wishlist.py:45 Submitted login credentials
INFO     tests.test_wishlist:test_wishlist.py:50 Login successful: True
INFO     actions.wishlist_actions:wishlist_actions.py:37 Navigating to home page: https://ecommerce-playground.lambdatest.io/
INFO     actions.wishlist_actions:wishlist_actions.py:43 Home page loaded successfully
INFO     tests.test_wishlist:test_wishlist.py:53 Navigated back to home page: https://ecommerce-playground.lambdatest.io/
----------------------------- Captured stderr call -----------------------------
2026-06-12 07:05:06  INFO      tests.test_wishlist  Starting test: remove single product 'iMac' from wishlist
2026-06-12 07:05:06  INFO      actions.wishlist_actions  Navigated to wishlist page via header link
2026-06-12 07:05:09  INFO      actions.wishlist_actions  Wishlist page is visible
2026-06-12 07:05:09  INFO      tests.test_wishlist  Navigated to wishlist page
2026-06-12 07:05:09  INFO      actions.wishlist_actions  Product 'iMac' present in wishlist: False
2026-06-12 07:05:09  INFO      tests.test_wishlist  'iMac' not in wishlist, adding it now
------------------------------ Captured log call -------------------------------
INFO     tests.test_wishlist:test_wishlist.py:172 Starting test: remove single product 'iMac' from wishlist
INFO     actions.wishlist_actions:wishlist_actions.py:65 Navigated to wishlist page via header link
INFO     actions.wishlist_actions:wishlist_actions.py:85 Wishlist page is visible
INFO     tests.test_wishlist:test_wishlist.py:176 Navigated to wishlist page
INFO     actions.wishlist_actions:wishlist_actions.py:201 Product 'iMac' present in wishlist: False
INFO     tests.test_wishlist:test_wishlist.py:72 'iMac' not in wishlist, adding it now
--------------------------- Captured stderr teardown ---------------------------
2026-06-12 07:05:25  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:108 Quitting driver.
_________ test_remove_multiple_products_from_wishlist[Apple Cinema 30] _________

setup = (<selenium.webdriver.chrome.webdriver.WebDriver (session="3dedbe7b27063e002fe0caa439fbaf17")>, <selenium.webdriver.sup...ait (session="3dedbe7b27063e002fe0caa439fbaf17")>, <actions.wishlist_actions.WishListActions object at 0x7f5c4655ba10>)
product_name = 'Apple Cinema 30'

    @pytest.mark.Prasanna
    @pytest.mark.parametrize("product_name", [PRODUCT_APPLE_CINEMA, PRODUCT_IPOD_NANO])
    def test_remove_multiple_products_from_wishlist(setup, product_name):
        """Removing each product from the wishlist shows a success/modified message."""
        _, _, wishlist_actions = setup
    
        logger.info("Starting test: remove product '%s' from wishlist", product_name)
    
        wishlist_actions.navigate_to_wishlist_via_account()
        wishlist_actions.wait_for_wishlist_page()
        logger.info("Navigated to wishlist page")
    
>       _ensure_product_in_wishlist(
            wishlist_actions, product_name, wishlist_actions.scroll_to_top_collection
        )

tests/test_wishlist.py:202: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
tests/test_wishlist.py:73: in _ensure_product_in_wishlist
    scroll_method()
actions/wishlist_actions.py:55: in scroll_to_top_collection
    self.scroll_into_view(self.wishlist_page.TOP_COLLECTION_HEADING)
actions/BaseAction.py:51: in scroll_into_view
    element = self.wait.until(ec.presence_of_element_located(locator))
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <selenium.webdriver.support.wait.WebDriverWait (session="3dedbe7b27063e002fe0caa439fbaf17")>
method = <function presence_of_element_located.<locals>._predicate at 0x7f5c463b2b60>
message = ''

    def until(self, method: Callable[[D], Literal[False] | T], message: str = "") -> T:
        """Wait until the method returns a value that is not False.
    
        Calls the method provided with the driver as an argument until the
        return value does not evaluate to ``False``.
    
        Args:
            method: A callable object that takes a WebDriver instance as an
                argument.
            message: Optional message for TimeoutException.
    
        Returns:
            The result of the last call to `method`.
    
        Raises:
            TimeoutException: If 'method' does not return a truthy value within
                the WebDriverWait object's timeout.
    
        Example:
            >>> from selenium.webdriver.common.by import By
            >>> from selenium.webdriver.support.ui import WebDriverWait
            >>> from selenium.webdriver.support import expected_conditions as EC
            >>>
            >>> # Wait until an element is visible on the page
            >>> wait = WebDriverWait(driver, 10)
            >>> element = wait.until(EC.visibility_of_element_located((By.ID, "exampleId")))
            >>> print(element.text)
        """
        screen = None
        stacktrace = None
    
        end_time = time.monotonic() + self._timeout
        while True:
            try:
                value = method(self._driver)
                if value:
                    return value
            except self._ignored_exceptions as exc:
                screen = getattr(exc, "screen", None)
                stacktrace = getattr(exc, "stacktrace", None)
            if time.monotonic() > end_time:
                break
            time.sleep(self._poll)
>       raise TimeoutException(message, screen, stacktrace)
E       selenium.common.exceptions.TimeoutException: Message: 
E       Stacktrace:
E       #0 0x5559ccad329a <unknown>
E       #1 0x5559cc4b5449 <unknown>
E       #2 0x5559cc509baf <unknown>
E       #3 0x5559cc509e01 <unknown>
E       #4 0x5559cc554ae4 <unknown>
E       #5 0x5559cc551cbf <unknown>
E       #6 0x5559cc4fd132 <unknown>
E       #7 0x5559cc4fdf41 <unknown>
E       #8 0x5559cca99737 <unknown>
E       #9 0x5559cca97f39 <unknown>
E       #10 0x5559cca82c26 <unknown>
E       #11 0x5559cca98ada <unknown>
E       #12 0x5559cca6abd0 <unknown>
E       #13 0x5559ccabfc28 <unknown>
E       #14 0x5559ccabfdc5 <unknown>
E       #15 0x5559ccad1e1e <unknown>
E       #16 0x7f9f5c09caa4 <unknown>
E       #17 0x7f9f5c129c6c <unknown>

../../../.local/lib/python3.12/site-packages/selenium/webdriver/support/wait.py:121: TimeoutException
---------------------------- Captured stderr setup -----------------------------
2026-06-12 07:05:25  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-12 07:05:25  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-12 07:05:26  INFO      conftest  Driver started → browser=chrome | mode=headless
2026-06-12 07:05:26  INFO      tests.test_wishlist  Landed on home page: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-12 07:05:26  INFO      tests.test_wishlist  Using credentials for user: testlogin@gmail.com
2026-06-12 07:05:26  INFO      tests.test_wishlist  Clicked 'My Account' link
2026-06-12 07:05:27  INFO      tests.test_wishlist  Submitted login credentials
2026-06-12 07:05:27  INFO      tests.test_wishlist  Login successful: True
2026-06-12 07:05:27  INFO      actions.wishlist_actions  Navigating to home page: https://ecommerce-playground.lambdatest.io/
2026-06-12 07:05:28  INFO      actions.wishlist_actions  Home page loaded successfully
2026-06-12 07:05:28  INFO      tests.test_wishlist  Navigated back to home page: https://ecommerce-playground.lambdatest.io/
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:56 Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:95 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:101 Driver started → browser=chrome | mode=headless
INFO     tests.test_wishlist:test_wishlist.py:34 Landed on home page: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     tests.test_wishlist:test_wishlist.py:37 Using credentials for user: testlogin@gmail.com
INFO     tests.test_wishlist:test_wishlist.py:41 Clicked 'My Account' link
INFO     tests.test_wishlist:test_wishlist.py:45 Submitted login credentials
INFO     tests.test_wishlist:test_wishlist.py:50 Login successful: True
INFO     actions.wishlist_actions:wishlist_actions.py:37 Navigating to home page: https://ecommerce-playground.lambdatest.io/
INFO     actions.wishlist_actions:wishlist_actions.py:43 Home page loaded successfully
INFO     tests.test_wishlist:test_wishlist.py:53 Navigated back to home page: https://ecommerce-playground.lambdatest.io/
----------------------------- Captured stderr call -----------------------------
2026-06-12 07:05:28  INFO      tests.test_wishlist  Starting test: remove product 'Apple Cinema 30' from wishlist
2026-06-12 07:05:28  INFO      actions.wishlist_actions  Navigated to wishlist page via header link
2026-06-12 07:05:31  INFO      actions.wishlist_actions  Wishlist page is visible
2026-06-12 07:05:31  INFO      tests.test_wishlist  Navigated to wishlist page
2026-06-12 07:05:31  INFO      actions.wishlist_actions  Product 'Apple Cinema 30' present in wishlist: False
2026-06-12 07:05:31  INFO      tests.test_wishlist  'Apple Cinema 30' not in wishlist, adding it now
------------------------------ Captured log call -------------------------------
INFO     tests.test_wishlist:test_wishlist.py:196 Starting test: remove product 'Apple Cinema 30' from wishlist
INFO     actions.wishlist_actions:wishlist_actions.py:65 Navigated to wishlist page via header link
INFO     actions.wishlist_actions:wishlist_actions.py:85 Wishlist page is visible
INFO     tests.test_wishlist:test_wishlist.py:200 Navigated to wishlist page
INFO     actions.wishlist_actions:wishlist_actions.py:201 Product 'Apple Cinema 30' present in wishlist: False
INFO     tests.test_wishlist:test_wishlist.py:72 'Apple Cinema 30' not in wishlist, adding it now
--------------------------- Captured stderr teardown ---------------------------
2026-06-12 07:05:47  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:108 Quitting driver.
____________ test_remove_multiple_products_from_wishlist[iPod Nano] ____________

setup = (<selenium.webdriver.chrome.webdriver.WebDriver (session="19b4ba18a414b074229095b223ecefe6")>, <selenium.webdriver.sup...ait (session="19b4ba18a414b074229095b223ecefe6")>, <actions.wishlist_actions.WishListActions object at 0x7f5c4655be60>)
product_name = 'iPod Nano'

    @pytest.mark.Prasanna
    @pytest.mark.parametrize("product_name", [PRODUCT_APPLE_CINEMA, PRODUCT_IPOD_NANO])
    def test_remove_multiple_products_from_wishlist(setup, product_name):
        """Removing each product from the wishlist shows a success/modified message."""
        _, _, wishlist_actions = setup
    
        logger.info("Starting test: remove product '%s' from wishlist", product_name)
    
        wishlist_actions.navigate_to_wishlist_via_account()
        wishlist_actions.wait_for_wishlist_page()
        logger.info("Navigated to wishlist page")
    
>       _ensure_product_in_wishlist(
            wishlist_actions, product_name, wishlist_actions.scroll_to_top_collection
        )

tests/test_wishlist.py:202: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
tests/test_wishlist.py:73: in _ensure_product_in_wishlist
    scroll_method()
actions/wishlist_actions.py:55: in scroll_to_top_collection
    self.scroll_into_view(self.wishlist_page.TOP_COLLECTION_HEADING)
actions/BaseAction.py:51: in scroll_into_view
    element = self.wait.until(ec.presence_of_element_located(locator))
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <selenium.webdriver.support.wait.WebDriverWait (session="19b4ba18a414b074229095b223ecefe6")>
method = <function presence_of_element_located.<locals>._predicate at 0x7f5c463b2e80>
message = ''

    def until(self, method: Callable[[D], Literal[False] | T], message: str = "") -> T:
        """Wait until the method returns a value that is not False.
    
        Calls the method provided with the driver as an argument until the
        return value does not evaluate to ``False``.
    
        Args:
            method: A callable object that takes a WebDriver instance as an
                argument.
            message: Optional message for TimeoutException.
    
        Returns:
            The result of the last call to `method`.
    
        Raises:
            TimeoutException: If 'method' does not return a truthy value within
                the WebDriverWait object's timeout.
    
        Example:
            >>> from selenium.webdriver.common.by import By
            >>> from selenium.webdriver.support.ui import WebDriverWait
            >>> from selenium.webdriver.support import expected_conditions as EC
            >>>
            >>> # Wait until an element is visible on the page
            >>> wait = WebDriverWait(driver, 10)
            >>> element = wait.until(EC.visibility_of_element_located((By.ID, "exampleId")))
            >>> print(element.text)
        """
        screen = None
        stacktrace = None
    
        end_time = time.monotonic() + self._timeout
        while True:
            try:
                value = method(self._driver)
                if value:
                    return value
            except self._ignored_exceptions as exc:
                screen = getattr(exc, "screen", None)
                stacktrace = getattr(exc, "stacktrace", None)
            if time.monotonic() > end_time:
                break
            time.sleep(self._poll)
>       raise TimeoutException(message, screen, stacktrace)
E       selenium.common.exceptions.TimeoutException: Message: 
E       Stacktrace:
E       #0 0x562f73cdb29a <unknown>
E       #1 0x562f736bd449 <unknown>
E       #2 0x562f73711baf <unknown>
E       #3 0x562f73711e01 <unknown>
E       #4 0x562f7375cae4 <unknown>
E       #5 0x562f73759cbf <unknown>
E       #6 0x562f73705132 <unknown>
E       #7 0x562f73705f41 <unknown>
E       #8 0x562f73ca1737 <unknown>
E       #9 0x562f73c9ff39 <unknown>
E       #10 0x562f73c8ac26 <unknown>
E       #11 0x562f73ca0ada <unknown>
E       #12 0x562f73c72bd0 <unknown>
E       #13 0x562f73cc7c28 <unknown>
E       #14 0x562f73cc7dc5 <unknown>
E       #15 0x562f73cd9e1e <unknown>
E       #16 0x7f159c29caa4 <unknown>
E       #17 0x7f159c329c6c <unknown>

../../../.local/lib/python3.12/site-packages/selenium/webdriver/support/wait.py:121: TimeoutException
---------------------------- Captured stderr setup -----------------------------
2026-06-12 07:05:47  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-12 07:05:47  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-12 07:05:48  INFO      conftest  Driver started → browser=chrome | mode=headless
2026-06-12 07:05:48  INFO      tests.test_wishlist  Landed on home page: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-12 07:05:48  INFO      tests.test_wishlist  Using credentials for user: testlogin@gmail.com
2026-06-12 07:05:48  INFO      tests.test_wishlist  Clicked 'My Account' link
2026-06-12 07:05:49  INFO      tests.test_wishlist  Submitted login credentials
2026-06-12 07:05:49  INFO      tests.test_wishlist  Login successful: True
2026-06-12 07:05:49  INFO      actions.wishlist_actions  Navigating to home page: https://ecommerce-playground.lambdatest.io/
2026-06-12 07:05:50  INFO      actions.wishlist_actions  Home page loaded successfully
2026-06-12 07:05:50  INFO      tests.test_wishlist  Navigated back to home page: https://ecommerce-playground.lambdatest.io/
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:56 Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:95 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:101 Driver started → browser=chrome | mode=headless
INFO     tests.test_wishlist:test_wishlist.py:34 Landed on home page: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     tests.test_wishlist:test_wishlist.py:37 Using credentials for user: testlogin@gmail.com
INFO     tests.test_wishlist:test_wishlist.py:41 Clicked 'My Account' link
INFO     tests.test_wishlist:test_wishlist.py:45 Submitted login credentials
INFO     tests.test_wishlist:test_wishlist.py:50 Login successful: True
INFO     actions.wishlist_actions:wishlist_actions.py:37 Navigating to home page: https://ecommerce-playground.lambdatest.io/
INFO     actions.wishlist_actions:wishlist_actions.py:43 Home page loaded successfully
INFO     tests.test_wishlist:test_wishlist.py:53 Navigated back to home page: https://ecommerce-playground.lambdatest.io/
----------------------------- Captured stderr call -----------------------------
2026-06-12 07:05:50  INFO      tests.test_wishlist  Starting test: remove product 'iPod Nano' from wishlist
2026-06-12 07:05:50  INFO      actions.wishlist_actions  Navigated to wishlist page via header link
2026-06-12 07:05:53  INFO      actions.wishlist_actions  Wishlist page is visible
2026-06-12 07:05:53  INFO      tests.test_wishlist  Navigated to wishlist page
2026-06-12 07:05:53  INFO      actions.wishlist_actions  Product 'iPod Nano' present in wishlist: False
2026-06-12 07:05:53  INFO      tests.test_wishlist  'iPod Nano' not in wishlist, adding it now
------------------------------ Captured log call -------------------------------
INFO     tests.test_wishlist:test_wishlist.py:196 Starting test: remove product 'iPod Nano' from wishlist
INFO     actions.wishlist_actions:wishlist_actions.py:65 Navigated to wishlist page via header link
INFO     actions.wishlist_actions:wishlist_actions.py:85 Wishlist page is visible
INFO     tests.test_wishlist:test_wishlist.py:200 Navigated to wishlist page
INFO     actions.wishlist_actions:wishlist_actions.py:201 Product 'iPod Nano' present in wishlist: False
INFO     tests.test_wishlist:test_wishlist.py:72 'iPod Nano' not in wishlist, adding it now
--------------------------- Captured stderr teardown ---------------------------
2026-06-12 07:06:09  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:108 Quitting driver.
=========================== short test summary info ============================
FAILED tests/test_wishlist.py::test_add_single_product_to_wishlist - selenium.common.exceptions.TimeoutException: Message: 
Stacktrace:
#0 0x55893bc0229a <unknown>
#1 0x55893b5e4449 <unknown>
#2 0x55893b638baf <unknown>
#3 0x55893b638e01 <unknown>
#4 0x55893b683ae4 <unknown>
#5 0x55893b680cbf <unknown>
#6 0x55893b62c132 <unknown>
#7 0x55893b62cf41 <unknown>
#8 0x55893bbc8737 <unknown>
#9 0x55893bbc6f39 <unknown>
#10 0x55893bbb1c26 <unknown>
#11 0x55893bbc7ada <unknown>
#12 0x55893bb99bd0 <unknown>
#13 0x55893bbeec28 <unknown>
#14 0x55893bbeedc5 <unknown>
#15 0x55893bc00e1e <unknown>
#16 0x7fe99889caa4 <unknown>
#17 0x7fe998929c6c <unknown>
FAILED tests/test_wishlist.py::test_add_product_via_search - selenium.common.exceptions.TimeoutException: Message:
FAILED tests/test_wishlist.py::test_remove_single_product_from_wishlist - selenium.common.exceptions.TimeoutException: Message: 
Stacktrace:
#0 0x56394334529a <unknown>
#1 0x563942d27449 <unknown>
#2 0x563942d7bbaf <unknown>
#3 0x563942d7be01 <unknown>
#4 0x563942dc6ae4 <unknown>
#5 0x563942dc3cbf <unknown>
#6 0x563942d6f132 <unknown>
#7 0x563942d6ff41 <unknown>
#8 0x56394330b737 <unknown>
#9 0x563943309f39 <unknown>
#10 0x5639432f4c26 <unknown>
#11 0x56394330aada <unknown>
#12 0x5639432dcbd0 <unknown>
#13 0x563943331c28 <unknown>
#14 0x563943331dc5 <unknown>
#15 0x563943343e1e <unknown>
#16 0x7f8cd109caa4 <unknown>
#17 0x7f8cd1129c6c <unknown>
FAILED tests/test_wishlist.py::test_remove_multiple_products_from_wishlist[Apple Cinema 30] - selenium.common.exceptions.TimeoutException: Message: 
Stacktrace:
#0 0x5559ccad329a <unknown>
#1 0x5559cc4b5449 <unknown>
#2 0x5559cc509baf <unknown>
#3 0x5559cc509e01 <unknown>
#4 0x5559cc554ae4 <unknown>
#5 0x5559cc551cbf <unknown>
#6 0x5559cc4fd132 <unknown>
#7 0x5559cc4fdf41 <unknown>
#8 0x5559cca99737 <unknown>
#9 0x5559cca97f39 <unknown>
#10 0x5559cca82c26 <unknown>
#11 0x5559cca98ada <unknown>
#12 0x5559cca6abd0 <unknown>
#13 0x5559ccabfc28 <unknown>
#14 0x5559ccabfdc5 <unknown>
#15 0x5559ccad1e1e <unknown>
#16 0x7f9f5c09caa4 <unknown>
#17 0x7f9f5c129c6c <unknown>
FAILED tests/test_wishlist.py::test_remove_multiple_products_from_wishlist[iPod Nano] - selenium.common.exceptions.TimeoutException: Message: 
Stacktrace:
#0 0x562f73cdb29a <unknown>
#1 0x562f736bd449 <unknown>
#2 0x562f73711baf <unknown>
#3 0x562f73711e01 <unknown>
#4 0x562f7375cae4 <unknown>
#5 0x562f73759cbf <unknown>
#6 0x562f73705132 <unknown>
#7 0x562f73705f41 <unknown>
#8 0x562f73ca1737 <unknown>
#9 0x562f73c9ff39 <unknown>
#10 0x562f73c8ac26 <unknown>
#11 0x562f73ca0ada <unknown>
#12 0x562f73c72bd0 <unknown>
#13 0x562f73cc7c28 <unknown>
#14 0x562f73cc7dc5 <unknown>
#15 0x562f73cd9e1e <unknown>
#16 0x7f159c29caa4 <unknown>
#17 0x7f159c329c6c <unknown>
=================== 5 failed, 9 passed in 190.86s (0:03:10) ====================
```
