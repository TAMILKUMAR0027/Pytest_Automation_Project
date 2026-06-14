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
collected 28 items

tests/test_Filter.py .....                                               [ 17%]
tests/test_cart.py ..                                                    [ 25%]
tests/test_checkout.py FF.                                               [ 35%]
tests/test_forgetpassword.py ..                                          [ 42%]
tests/test_launch.py .                                                   [ 46%]
tests/test_login.py ..                                                   [ 53%]
tests/test_logout.py .                                                   [ 57%]
tests/test_register.py ..                                                [ 64%]
tests/test_shopbycategory.py FFFF                                        [ 78%]
tests/test_wishlist.py ......                                            [100%]

=================================== FAILURES ===================================
_______________________ TestCheckout.test_login_checkout _______________________

self = <tests.test_checkout.TestCheckout object at 0x7f92d1a61eb0>
driver = (<selenium.webdriver.chrome.webdriver.WebDriver (session="c3f3267b2fa7b0a9b20554e1c1d65087")>, <selenium.webdriver.support.wait.WebDriverWait (session="c3f3267b2fa7b0a9b20554e1c1d65087")>)

    def test_login_checkout(self, driver):
    
        drv, wait = driver
        action = CheckoutAction(drv)
    
        drv.get(ConfigReader.get_url())
    
        action.click_hp_product()
>       action.add_product_to_cart()

tests/test_checkout.py:22: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <actions.checkoutAction.CheckoutAction object at 0x7f92d1918e60>

    def add_product_to_cart(self):
>       self.click(self.cp.PRODUCT_PAGE_CHECKOUT_BTN1)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       AttributeError: 'CheckoutPage' object has no attribute 'PRODUCT_PAGE_CHECKOUT_BTN1'. Did you mean: 'CART_PAGE_CHECKOUT_BTN'?

actions/checkoutAction.py:23: AttributeError
---------------------------- Captured stderr setup -----------------------------
2026-06-13 12:57:01  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 12:57:01  INFO      conftest  Chrome Browser Launched Successfully
2026-06-13 12:57:01  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 12:57:02  INFO      conftest  Driver started → browser=chrome | mode=headless
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:62 Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:119 Chrome Browser Launched Successfully
INFO     conftest:conftest.py:175 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:184 Driver started → browser=chrome | mode=headless
--------------------------- Captured stderr teardown ---------------------------
2026-06-13 12:57:18  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:196 Quitting driver.
_____________________ TestCheckout.test_register_checkout ______________________

self = <tests.test_checkout.TestCheckout object at 0x7f92d1b5bb90>
driver = (<selenium.webdriver.chrome.webdriver.WebDriver (session="a28d329330b9a5e8310cabca4990a4c0")>, <selenium.webdriver.support.wait.WebDriverWait (session="a28d329330b9a5e8310cabca4990a4c0")>)

    def test_register_checkout(self, driver):
    
        drv, wait = driver
        action = CheckoutAction(drv)
    
>       action.open_home_and_add_product(ConfigReader.get_url())
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       AttributeError: 'CheckoutAction' object has no attribute 'open_home_and_add_product'

tests/test_checkout.py:56: AttributeError
---------------------------- Captured stderr setup -----------------------------
2026-06-13 12:57:18  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 12:57:19  INFO      conftest  Chrome Browser Launched Successfully
2026-06-13 12:57:19  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 12:57:19  INFO      conftest  Driver started → browser=chrome | mode=headless
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:62 Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:119 Chrome Browser Launched Successfully
INFO     conftest:conftest.py:175 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:184 Driver started → browser=chrome | mode=headless
--------------------------- Captured stderr teardown ---------------------------
2026-06-13 12:57:19  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:196 Quitting driver.
__ TestShopByCategory.test_category_navigation[Desktops & Monitors-Monitors] ___

self = <tests.test_shopbycategory.TestShopByCategory object at 0x7f92d1a73470>
driver = (<selenium.webdriver.chrome.webdriver.WebDriver (session="a7bf4d2e7bbf6e1ceac482b103d65db2")>, <selenium.webdriver.support.wait.WebDriverWait (session="a7bf4d2e7bbf6e1ceac482b103d65db2")>)
category = 'Desktops & Monitors', expected_title = 'Monitors'

    @pytest.mark.parametrize(
        "category, expected_title",
        [
            ("Desktops & Monitors", "Monitors"),
            ("Web Cameras", "Web Cameras"),
            ("Phone, Tablets & Ipod", "Tablets"),
            ("Laptops & Notebooks", "Laptops"),
        ]
    )
    def test_category_navigation(self, driver, category, expected_title):
    
        drv, wait = driver
        action = ShopByCategoryAction(drv)
        action.launch_url("https://ecommerce-playground.lambdatest.io")
>       action.click_shop_by_category()

tests/test_shopbycategory.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
actions/ShopbycategoryAction.py:33: in click_shop_by_category
    element = self.wait.until(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <selenium.webdriver.support.wait.WebDriverWait (session="a7bf4d2e7bbf6e1ceac482b103d65db2")>
method = <function element_to_be_clickable.<locals>._predicate at 0x7f92d191da80>
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
2026-06-13 12:58:11  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 12:58:11  INFO      conftest  Chrome Browser Launched Successfully
2026-06-13 12:58:11  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 12:58:12  INFO      conftest  Driver started → browser=chrome | mode=headless
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:62 Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:119 Chrome Browser Launched Successfully
INFO     conftest:conftest.py:175 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:184 Driver started → browser=chrome | mode=headless
----------------------------- Captured stderr call -----------------------------
2026-06-13 12:58:12  INFO      actions.ShopbycategoryAction  Launching URL: https://ecommerce-playground.lambdatest.io
2026-06-13 12:58:13  INFO      actions.ShopbycategoryAction  Application launched successfully
2026-06-13 12:58:13  INFO      actions.ShopbycategoryAction  Clicking Shop By Category menu
2026-06-13 12:58:33  ERROR     actions.ShopbycategoryAction  Unable to click Shop By Category menu: Message: 

------------------------------ Captured log call -------------------------------
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:19 Launching URL: https://ecommerce-playground.lambdatest.io
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:23 Application launched successfully
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:32 Clicking Shop By Category menu
ERROR    actions.ShopbycategoryAction:ShopbycategoryAction.py:43 Unable to click Shop By Category menu: Message:
--------------------------- Captured stderr teardown ---------------------------
2026-06-13 12:58:33  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:196 Quitting driver.
_____ TestShopByCategory.test_category_navigation[Web Cameras-Web Cameras] _____

self = <tests.test_shopbycategory.TestShopByCategory object at 0x7f92d1749400>
driver = (<selenium.webdriver.chrome.webdriver.WebDriver (session="09bdf4191565b5f3f02a03cd37c6c70a")>, <selenium.webdriver.support.wait.WebDriverWait (session="09bdf4191565b5f3f02a03cd37c6c70a")>)
category = 'Web Cameras', expected_title = 'Web Cameras'

    @pytest.mark.parametrize(
        "category, expected_title",
        [
            ("Desktops & Monitors", "Monitors"),
            ("Web Cameras", "Web Cameras"),
            ("Phone, Tablets & Ipod", "Tablets"),
            ("Laptops & Notebooks", "Laptops"),
        ]
    )
    def test_category_navigation(self, driver, category, expected_title):
    
        drv, wait = driver
        action = ShopByCategoryAction(drv)
        action.launch_url("https://ecommerce-playground.lambdatest.io")
>       action.click_shop_by_category()

tests/test_shopbycategory.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
actions/ShopbycategoryAction.py:33: in click_shop_by_category
    element = self.wait.until(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <selenium.webdriver.support.wait.WebDriverWait (session="09bdf4191565b5f3f02a03cd37c6c70a")>
method = <function element_to_be_clickable.<locals>._predicate at 0x7f92d191c4a0>
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
2026-06-13 12:58:33  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 12:58:33  INFO      conftest  Chrome Browser Launched Successfully
2026-06-13 12:58:33  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 12:58:34  INFO      conftest  Driver started → browser=chrome | mode=headless
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:62 Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:119 Chrome Browser Launched Successfully
INFO     conftest:conftest.py:175 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:184 Driver started → browser=chrome | mode=headless
----------------------------- Captured stderr call -----------------------------
2026-06-13 12:58:34  INFO      actions.ShopbycategoryAction  Launching URL: https://ecommerce-playground.lambdatest.io
2026-06-13 12:58:34  INFO      actions.ShopbycategoryAction  Application launched successfully
2026-06-13 12:58:34  INFO      actions.ShopbycategoryAction  Clicking Shop By Category menu
2026-06-13 12:58:54  ERROR     actions.ShopbycategoryAction  Unable to click Shop By Category menu: Message: 

------------------------------ Captured log call -------------------------------
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:19 Launching URL: https://ecommerce-playground.lambdatest.io
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:23 Application launched successfully
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:32 Clicking Shop By Category menu
ERROR    actions.ShopbycategoryAction:ShopbycategoryAction.py:43 Unable to click Shop By Category menu: Message:
--------------------------- Captured stderr teardown ---------------------------
2026-06-13 12:58:54  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:196 Quitting driver.
__ TestShopByCategory.test_category_navigation[Phone, Tablets & Ipod-Tablets] __

self = <tests.test_shopbycategory.TestShopByCategory object at 0x7f92d1748350>
driver = (<selenium.webdriver.chrome.webdriver.WebDriver (session="76514caab9902a3ad5a718842fda53c2")>, <selenium.webdriver.support.wait.WebDriverWait (session="76514caab9902a3ad5a718842fda53c2")>)
category = 'Phone, Tablets & Ipod', expected_title = 'Tablets'

    @pytest.mark.parametrize(
        "category, expected_title",
        [
            ("Desktops & Monitors", "Monitors"),
            ("Web Cameras", "Web Cameras"),
            ("Phone, Tablets & Ipod", "Tablets"),
            ("Laptops & Notebooks", "Laptops"),
        ]
    )
    def test_category_navigation(self, driver, category, expected_title):
    
        drv, wait = driver
        action = ShopByCategoryAction(drv)
        action.launch_url("https://ecommerce-playground.lambdatest.io")
>       action.click_shop_by_category()

tests/test_shopbycategory.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
actions/ShopbycategoryAction.py:33: in click_shop_by_category
    element = self.wait.until(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <selenium.webdriver.support.wait.WebDriverWait (session="76514caab9902a3ad5a718842fda53c2")>
method = <function element_to_be_clickable.<locals>._predicate at 0x7f92d191c900>
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
2026-06-13 12:58:55  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 12:58:55  INFO      conftest  Chrome Browser Launched Successfully
2026-06-13 12:58:55  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 12:58:55  INFO      conftest  Driver started → browser=chrome | mode=headless
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:62 Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:119 Chrome Browser Launched Successfully
INFO     conftest:conftest.py:175 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:184 Driver started → browser=chrome | mode=headless
----------------------------- Captured stderr call -----------------------------
2026-06-13 12:58:55  INFO      actions.ShopbycategoryAction  Launching URL: https://ecommerce-playground.lambdatest.io
2026-06-13 12:58:56  INFO      actions.ShopbycategoryAction  Application launched successfully
2026-06-13 12:58:56  INFO      actions.ShopbycategoryAction  Clicking Shop By Category menu
2026-06-13 12:59:16  ERROR     actions.ShopbycategoryAction  Unable to click Shop By Category menu: Message: 

------------------------------ Captured log call -------------------------------
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:19 Launching URL: https://ecommerce-playground.lambdatest.io
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:23 Application launched successfully
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:32 Clicking Shop By Category menu
ERROR    actions.ShopbycategoryAction:ShopbycategoryAction.py:43 Unable to click Shop By Category menu: Message:
--------------------------- Captured stderr teardown ---------------------------
2026-06-13 12:59:16  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:196 Quitting driver.
___ TestShopByCategory.test_category_navigation[Laptops & Notebooks-Laptops] ___

self = <tests.test_shopbycategory.TestShopByCategory object at 0x7f92d1748230>
driver = (<selenium.webdriver.chrome.webdriver.WebDriver (session="1365da7dcde01b3dc56350258dfe74db")>, <selenium.webdriver.support.wait.WebDriverWait (session="1365da7dcde01b3dc56350258dfe74db")>)
category = 'Laptops & Notebooks', expected_title = 'Laptops'

    @pytest.mark.parametrize(
        "category, expected_title",
        [
            ("Desktops & Monitors", "Monitors"),
            ("Web Cameras", "Web Cameras"),
            ("Phone, Tablets & Ipod", "Tablets"),
            ("Laptops & Notebooks", "Laptops"),
        ]
    )
    def test_category_navigation(self, driver, category, expected_title):
    
        drv, wait = driver
        action = ShopByCategoryAction(drv)
        action.launch_url("https://ecommerce-playground.lambdatest.io")
>       action.click_shop_by_category()

tests/test_shopbycategory.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
actions/ShopbycategoryAction.py:33: in click_shop_by_category
    element = self.wait.until(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <selenium.webdriver.support.wait.WebDriverWait (session="1365da7dcde01b3dc56350258dfe74db")>
method = <function element_to_be_clickable.<locals>._predicate at 0x7f92d1783100>
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
2026-06-13 12:59:16  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 12:59:17  INFO      conftest  Chrome Browser Launched Successfully
2026-06-13 12:59:17  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 12:59:17  INFO      conftest  Driver started → browser=chrome | mode=headless
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:62 Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:119 Chrome Browser Launched Successfully
INFO     conftest:conftest.py:175 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:184 Driver started → browser=chrome | mode=headless
----------------------------- Captured stderr call -----------------------------
2026-06-13 12:59:17  INFO      actions.ShopbycategoryAction  Launching URL: https://ecommerce-playground.lambdatest.io
2026-06-13 12:59:18  INFO      actions.ShopbycategoryAction  Application launched successfully
2026-06-13 12:59:18  INFO      actions.ShopbycategoryAction  Clicking Shop By Category menu
2026-06-13 12:59:38  ERROR     actions.ShopbycategoryAction  Unable to click Shop By Category menu: Message: 

------------------------------ Captured log call -------------------------------
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:19 Launching URL: https://ecommerce-playground.lambdatest.io
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:23 Application launched successfully
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:32 Clicking Shop By Category menu
ERROR    actions.ShopbycategoryAction:ShopbycategoryAction.py:43 Unable to click Shop By Category menu: Message:
--------------------------- Captured stderr teardown ---------------------------
2026-06-13 12:59:38  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:196 Quitting driver.
=============================== warnings summary ===============================
tests/test_shopbycategory.py:7
  /home/runner/work/Pytest_Automation_Project/Pytest_Automation_Project/tests/test_shopbycategory.py:7: PytestUnknownMarkWarning: Unknown pytest.mark.ShopByCategory - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.ShopByCategory

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ============================
FAILED tests/test_checkout.py::TestCheckout::test_login_checkout - AttributeError: 'CheckoutPage' object has no attribute 'PRODUCT_PAGE_CHECKOUT_BTN1'. Did you mean: 'CART_PAGE_CHECKOUT_BTN'?
FAILED tests/test_checkout.py::TestCheckout::test_register_checkout - AttributeError: 'CheckoutAction' object has no attribute 'open_home_and_add_product'
FAILED tests/test_shopbycategory.py::TestShopByCategory::test_category_navigation[Desktops & Monitors-Monitors] - selenium.common.exceptions.TimeoutException: Message:
FAILED tests/test_shopbycategory.py::TestShopByCategory::test_category_navigation[Web Cameras-Web Cameras] - selenium.common.exceptions.TimeoutException: Message:
FAILED tests/test_shopbycategory.py::TestShopByCategory::test_category_navigation[Phone, Tablets & Ipod-Tablets] - selenium.common.exceptions.TimeoutException: Message:
FAILED tests/test_shopbycategory.py::TestShopByCategory::test_category_navigation[Laptops & Notebooks-Laptops] - selenium.common.exceptions.TimeoutException: Message:
============= 6 failed, 22 passed, 1 warning in 251.01s (0:04:11) ==============
```
