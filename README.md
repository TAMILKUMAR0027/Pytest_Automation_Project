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
collected 18 items

tests/test_Filter.py ....                                                [ 22%]
tests/test_checkout.py F.F                                               [ 38%]
tests/test_forgetpassword.py ..                                          [ 50%]
tests/test_launch.py .                                                   [ 55%]
tests/test_login.py .                                                    [ 61%]
tests/test_register.py .                                                 [ 66%]
tests/test_wishlist.py ..F...                                            [100%]

=================================== FAILURES ===================================
____________ TestCheckout.test_guest_checkout_with_new_address_cod _____________

self = <tests.test_checkout.TestCheckout object at 0x7fdc266e2f30>
driver = (<selenium.webdriver.chrome.webdriver.WebDriver (session="1bd0283aff665aee7e79f415f9245c04")>, <selenium.webdriver.support.wait.WebDriverWait (session="1bd0283aff665aee7e79f415f9245c04")>)

    def test_guest_checkout_with_new_address_cod(self, driver):
    
        drv, wait = driver
    
        action = CheckoutAction(drv)
    
        action.login_as_registered_user()
    
        drv.get(ConfigReader.get_url())
    
        action.click_hp_product()
        action.add_product_to_cart()
        action.click_shopping_cart_from_popup()
        action.click_checkout_from_cart_page()
    
        assert action.is_checkout_or_login_page_displayed()
    
        action.select_new_address()
        action.enter_billing_details()
        action.click_same_billing_address()
    
        action.select_flat_rate()
        action.select_cash_on_delivery()
    
        action.click_terms_and_conditions()
        action.continue_checkout()
    
>       assert action.is_order_placed_successfully()
E       assert False
E        +  where False = is_order_placed_successfully()
E        +    where is_order_placed_successfully = <actions.checkoutAction.CheckoutAction object at 0x7fdc265cab70>.is_order_placed_successfully

tests/test_checkout.py:35: AssertionError
---------------------------- Captured stderr setup -----------------------------
2026-06-12 10:07:20  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-12 10:07:21  INFO      conftest  Chrome Browser Launched Successfully
2026-06-12 10:07:21  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-12 10:07:22  INFO      conftest  Driver started → browser=chrome | mode=headless
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:62 Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:119 Chrome Browser Launched Successfully
INFO     conftest:conftest.py:175 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:184 Driver started → browser=chrome | mode=headless
--------------------------- Captured stderr teardown ---------------------------
2026-06-12 10:07:44  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:196 Quitting driver.
_______________ TestCheckout.test_checkout_with_register_account _______________

self = <tests.test_checkout.TestCheckout object at 0x7fdc266e3410>
driver = (<selenium.webdriver.chrome.webdriver.WebDriver (session="289250f2b2d1e63e70a469a419caee65")>, <selenium.webdriver.support.wait.WebDriverWait (session="289250f2b2d1e63e70a469a419caee65")>)

    def test_checkout_with_register_account(self, driver):
    
        drv, wait = driver
    
        action = CheckoutAction(drv)
    
        drv.get(ConfigReader.get_url())
    
        action.click_hp_product()
        action.add_product_to_cart()
        action.click_shopping_cart_from_popup()
        action.click_checkout_from_cart_page()
    
>       assert action.is_checkout_or_login_page_displayed()
E       assert False
E        +  where False = is_checkout_or_login_page_displayed()
E        +    where is_checkout_or_login_page_displayed = <actions.checkoutAction.CheckoutAction object at 0x7fdc265d7b60>.is_checkout_or_login_page_displayed

tests/test_checkout.py:62: AssertionError
---------------------------- Captured stderr setup -----------------------------
2026-06-12 10:07:48  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-12 10:07:48  INFO      conftest  Chrome Browser Launched Successfully
2026-06-12 10:07:48  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-12 10:07:49  INFO      conftest  Driver started → browser=chrome | mode=headless
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:62 Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:119 Chrome Browser Launched Successfully
INFO     conftest:conftest.py:175 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:184 Driver started → browser=chrome | mode=headless
--------------------------- Captured stderr teardown ---------------------------
2026-06-12 10:08:08  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:196 Quitting driver.
_________________________ test_add_product_via_search __________________________

self = <actions.wishlist_actions.WishListActions object at 0x7fdc24c122a0>

    def get_wishlist_success_message_generic(self):
        """Return the wishlist success notification text, using a fallback locator if needed."""
        try:
>           message = self.get_text(self.wishlist_page.SUCCESS_NOTIFICATION)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

actions/wishlist_actions.py:163: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
actions/BaseAction.py:37: in get_text
    return self.wait.until(ec.visibility_of_element_located(locator)).text
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <selenium.webdriver.support.wait.WebDriverWait (session="94fda2f70b51d75233c7a75bf6dbbf27")>
method = <function visibility_of_element_located.<locals>._predicate at 0x7fdc29904540>
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
E       #0 0x5623342e229a <unknown>
E       #1 0x562333cc4449 <unknown>
E       #2 0x562333d18baf <unknown>
E       #3 0x562333d18e01 <unknown>
E       #4 0x562333d63ae4 <unknown>
E       #5 0x562333d60cbf <unknown>
E       #6 0x562333d0c132 <unknown>
E       #7 0x562333d0cf41 <unknown>
E       #8 0x5623342a8737 <unknown>
E       #9 0x5623342a6f39 <unknown>
E       #10 0x562334291c26 <unknown>
E       #11 0x5623342a7ada <unknown>
E       #12 0x562334279bd0 <unknown>
E       #13 0x5623342cec28 <unknown>
E       #14 0x5623342cedc5 <unknown>
E       #15 0x5623342e0e1e <unknown>
E       #16 0x7f3977a9caa4 <unknown>
E       #17 0x7f3977b29c6c <unknown>

../../../.local/lib/python3.12/site-packages/selenium/webdriver/support/wait.py:121: TimeoutException

During handling of the above exception, another exception occurred:

setup = (<selenium.webdriver.chrome.webdriver.WebDriver (session="94fda2f70b51d75233c7a75bf6dbbf27")>, <selenium.webdriver.sup...ait (session="94fda2f70b51d75233c7a75bf6dbbf27")>, <actions.wishlist_actions.WishListActions object at 0x7fdc24c122a0>)

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
    
>       _assert_success_message(wishlist_actions.get_wishlist_success_message_generic())
                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_wishlist.py:154: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
actions/wishlist_actions.py:166: in get_wishlist_success_message_generic
    message = self.get_text(self.wishlist_page.SUCCESS_NOTIFICATION_FALLBACK)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
actions/BaseAction.py:37: in get_text
    return self.wait.until(ec.visibility_of_element_located(locator)).text
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <selenium.webdriver.support.wait.WebDriverWait (session="94fda2f70b51d75233c7a75bf6dbbf27")>
method = <function visibility_of_element_located.<locals>._predicate at 0x7fdc26324860>
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
E       #0 0x5623342e229a <unknown>
E       #1 0x562333cc4449 <unknown>
E       #2 0x562333d18baf <unknown>
E       #3 0x562333d18e01 <unknown>
E       #4 0x562333d63ae4 <unknown>
E       #5 0x562333d60cbf <unknown>
E       #6 0x562333d0c132 <unknown>
E       #7 0x562333d0cf41 <unknown>
E       #8 0x5623342a8737 <unknown>
E       #9 0x5623342a6f39 <unknown>
E       #10 0x562334291c26 <unknown>
E       #11 0x5623342a7ada <unknown>
E       #12 0x562334279bd0 <unknown>
E       #13 0x5623342cec28 <unknown>
E       #14 0x5623342cedc5 <unknown>
E       #15 0x5623342e0e1e <unknown>
E       #16 0x7f3977a9caa4 <unknown>
E       #17 0x7f3977b29c6c <unknown>

../../../.local/lib/python3.12/site-packages/selenium/webdriver/support/wait.py:121: TimeoutException
---------------------------- Captured stderr setup -----------------------------
2026-06-12 10:09:26  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-12 10:09:26  INFO      conftest  Chrome Browser Launched Successfully
2026-06-12 10:09:26  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-12 10:09:27  INFO      conftest  Driver started → browser=chrome | mode=headless
2026-06-12 10:09:27  INFO      tests.test_wishlist  Landed on home page: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-12 10:09:27  INFO      tests.test_wishlist  Using credentials for user: testlogin@gmail.com
2026-06-12 10:09:28  INFO      tests.test_wishlist  Clicked 'My Account' link
2026-06-12 10:09:28  INFO      tests.test_wishlist  Submitted login credentials
2026-06-12 10:09:29  INFO      tests.test_wishlist  Login successful: True
2026-06-12 10:09:29  INFO      actions.wishlist_actions  Navigating to home page: https://ecommerce-playground.lambdatest.io/
2026-06-12 10:09:30  INFO      actions.wishlist_actions  Home page loaded successfully
2026-06-12 10:09:30  INFO      tests.test_wishlist  Navigated back to home page: https://ecommerce-playground.lambdatest.io/
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:62 Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:119 Chrome Browser Launched Successfully
INFO     conftest:conftest.py:175 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:184 Driver started → browser=chrome | mode=headless
INFO     tests.test_wishlist:test_wishlist.py:34 Landed on home page: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     tests.test_wishlist:test_wishlist.py:37 Using credentials for user: testlogin@gmail.com
INFO     tests.test_wishlist:test_wishlist.py:41 Clicked 'My Account' link
INFO     tests.test_wishlist:test_wishlist.py:45 Submitted login credentials
INFO     tests.test_wishlist:test_wishlist.py:50 Login successful: True
INFO     actions.wishlist_actions:wishlist_actions.py:37 Navigating to home page: https://ecommerce-playground.lambdatest.io/
INFO     actions.wishlist_actions:wishlist_actions.py:43 Home page loaded successfully
INFO     tests.test_wishlist:test_wishlist.py:53 Navigated back to home page: https://ecommerce-playground.lambdatest.io/
----------------------------- Captured stderr call -----------------------------
2026-06-12 10:09:30  INFO      tests.test_wishlist  Starting test: add product 'iPod Shuffle' via search
2026-06-12 10:09:30  INFO      actions.wishlist_actions  Searched for product: iPod Shuffle
2026-06-12 10:09:30  INFO      tests.test_wishlist  Searched for product: iPod Shuffle
2026-06-12 10:09:32  INFO      actions.wishlist_actions  Opened product page for: iPod Shuffle
2026-06-12 10:09:32  INFO      tests.test_wishlist  Opened product page for: iPod Shuffle
2026-06-12 10:09:33  INFO      actions.wishlist_actions  Clicked wishlist (heart) button on product page
2026-06-12 10:09:33  INFO      tests.test_wishlist  Clicked wishlist (heart) button on product page
2026-06-12 10:09:48  WARNING   actions.wishlist_actions  Primary success notification not found, using fallback
------------------------------ Captured log call -------------------------------
INFO     tests.test_wishlist:test_wishlist.py:143 Starting test: add product 'iPod Shuffle' via search
INFO     actions.wishlist_actions:wishlist_actions.py:133 Searched for product: iPod Shuffle
INFO     tests.test_wishlist:test_wishlist.py:146 Searched for product: iPod Shuffle
INFO     actions.wishlist_actions:wishlist_actions.py:143 Opened product page for: iPod Shuffle
INFO     tests.test_wishlist:test_wishlist.py:149 Opened product page for: iPod Shuffle
INFO     actions.wishlist_actions:wishlist_actions.py:154 Clicked wishlist (heart) button on product page
INFO     tests.test_wishlist:test_wishlist.py:152 Clicked wishlist (heart) button on product page
WARNING  actions.wishlist_actions:wishlist_actions.py:165 Primary success notification not found, using fallback
--------------------------- Captured stderr teardown ---------------------------
2026-06-12 10:10:03  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:196 Quitting driver.
=========================== short test summary info ============================
FAILED tests/test_checkout.py::TestCheckout::test_guest_checkout_with_new_address_cod - assert False
 +  where False = is_order_placed_successfully()
 +    where is_order_placed_successfully = <actions.checkoutAction.CheckoutAction object at 0x7fdc265cab70>.is_order_placed_successfully
FAILED tests/test_checkout.py::TestCheckout::test_checkout_with_register_account - assert False
 +  where False = is_checkout_or_login_page_displayed()
 +    where is_checkout_or_login_page_displayed = <actions.checkoutAction.CheckoutAction object at 0x7fdc265d7b60>.is_checkout_or_login_page_displayed
FAILED tests/test_wishlist.py::test_add_product_via_search - selenium.common.exceptions.TimeoutException: Message: 
Stacktrace:
#0 0x5623342e229a <unknown>
#1 0x562333cc4449 <unknown>
#2 0x562333d18baf <unknown>
#3 0x562333d18e01 <unknown>
#4 0x562333d63ae4 <unknown>
#5 0x562333d60cbf <unknown>
#6 0x562333d0c132 <unknown>
#7 0x562333d0cf41 <unknown>
#8 0x5623342a8737 <unknown>
#9 0x5623342a6f39 <unknown>
#10 0x562334291c26 <unknown>
#11 0x5623342a7ada <unknown>
#12 0x562334279bd0 <unknown>
#13 0x5623342cec28 <unknown>
#14 0x5623342cedc5 <unknown>
#15 0x5623342e0e1e <unknown>
#16 0x7f3977a9caa4 <unknown>
#17 0x7f3977b29c6c <unknown>
=================== 3 failed, 15 passed in 237.31s (0:03:57) ===================
```
