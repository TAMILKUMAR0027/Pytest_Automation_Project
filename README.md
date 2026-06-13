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
collected 26 items

tests/test_Filter.py .....                                               [ 19%]
tests/test_checkout.py FF.                                               [ 30%]
tests/test_forgetpassword.py ..                                          [ 38%]
tests/test_launch.py .                                                   [ 42%]
tests/test_login.py .F                                                   [ 50%]
tests/test_logout.py .                                                   [ 53%]
tests/test_register.py ..                                                [ 61%]
tests/test_shopbycategory.py FFFF                                        [ 76%]
tests/test_wishlist.py ...FFF                                            [100%]

=================================== FAILURES ===================================
_______________________ TestCheckout.test_login_checkout _______________________

self = <tests.test_checkout.TestCheckout object at 0x7fa00b4822d0>
driver = (<selenium.webdriver.chrome.webdriver.WebDriver (session="86a04c57ebf41644e74c4feaf6a4e693")>, <selenium.webdriver.support.wait.WebDriverWait (session="86a04c57ebf41644e74c4feaf6a4e693")>)

    def test_login_checkout(self, driver):
    
        drv, wait = driver
        action = CheckoutAction(drv)
    
        drv.get(ConfigReader.get_url())
    
        action.click_hp_product()
>       action.add_product_to_cart()

tests/test_checkout.py:22: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <actions.checkoutAction.CheckoutAction object at 0x7fa00b482030>

    def add_product_to_cart(self):
>       self.click(self.cp.PRODUCT_PAGE_CHECKOUT_BTN1)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       AttributeError: 'CheckoutPage' object has no attribute 'PRODUCT_PAGE_CHECKOUT_BTN1'. Did you mean: 'CART_PAGE_CHECKOUT_BTN'?

actions/checkoutAction.py:23: AttributeError
---------------------------- Captured stderr setup -----------------------------
2026-06-13 09:04:21  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 09:04:22  INFO      conftest  Chrome Browser Launched Successfully
2026-06-13 09:04:22  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 09:04:22  INFO      conftest  Driver started → browser=chrome | mode=headless
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:62 Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:119 Chrome Browser Launched Successfully
INFO     conftest:conftest.py:175 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:184 Driver started → browser=chrome | mode=headless
--------------------------- Captured stderr teardown ---------------------------
2026-06-13 09:04:38  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:196 Quitting driver.
_____________________ TestCheckout.test_register_checkout ______________________

self = <tests.test_checkout.TestCheckout object at 0x7fa00b476360>
driver = (<selenium.webdriver.chrome.webdriver.WebDriver (session="07298178dacde60f41bd22f3855ac331")>, <selenium.webdriver.support.wait.WebDriverWait (session="07298178dacde60f41bd22f3855ac331")>)

    def test_register_checkout(self, driver):
    
        drv, wait = driver
        action = CheckoutAction(drv)
    
>       action.open_home_and_add_product(ConfigReader.get_url())
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       AttributeError: 'CheckoutAction' object has no attribute 'open_home_and_add_product'

tests/test_checkout.py:56: AttributeError
---------------------------- Captured stderr setup -----------------------------
2026-06-13 09:04:39  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 09:04:39  INFO      conftest  Chrome Browser Launched Successfully
2026-06-13 09:04:39  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 09:04:39  INFO      conftest  Driver started → browser=chrome | mode=headless
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:62 Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:119 Chrome Browser Launched Successfully
INFO     conftest:conftest.py:175 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:184 Driver started → browser=chrome | mode=headless
--------------------------- Captured stderr teardown ---------------------------
2026-06-13 09:04:39  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:196 Quitting driver.
__________ TestLogin.test_invalidLogin[space143@gmail.com-testlogin] ___________

self = <tests.test_login.TestLogin object at 0x7fa00b64bd40>
driver = (<selenium.webdriver.chrome.webdriver.WebDriver (session="02ce4573c01943fd52c6163abd2a3725")>, <selenium.webdriver.support.wait.WebDriverWait (session="02ce4573c01943fd52c6163abd2a3725")>)
username1 = 'space143@gmail.com', password1 = 'testlogin'

    @pytest.mark.parametrize(
        "username1,password1",
        get_data(
            "data_provider/DataProvider.xlsx",
            "loginDataInvalid",
        ),
    )
    def test_invalidLogin(self, driver, username1, password1):
        drv, wait = driver
    
        logger.info("Invalid login test started")
    
        hp = HomePageAction(drv)
        hp.click_myAcc()
        logger.info("Clicked My Account")
    
        lp = LoginPageAction(drv)
        lp.enter_login_credentials(username1, password1)
        logger.info(f"Entered invalid username: {username1}")
    
>       assert lp.provide_error_msg_invalid_login() is True
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_login.py:60: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
actions/loginpageaction.py:23: in provide_error_msg_invalid_login
    actual = self.get_text(self.lp.invalidLoginErrorMsg)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
actions/BaseAction.py:38: in get_text
    return self.wait.until(ec.visibility_of_element_located(locator)).text
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <selenium.webdriver.support.wait.WebDriverWait (session="02ce4573c01943fd52c6163abd2a3725")>
method = <function visibility_of_element_located.<locals>._predicate at 0x7fa00b2ef880>
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
E       #0 0x5623d951929a <unknown>
E       #1 0x5623d8efb449 <unknown>
E       #2 0x5623d8f4fbaf <unknown>
E       #3 0x5623d8f4fe01 <unknown>
E       #4 0x5623d8f9aae4 <unknown>
E       #5 0x5623d8f97cbf <unknown>
E       #6 0x5623d8f43132 <unknown>
E       #7 0x5623d8f43f41 <unknown>
E       #8 0x5623d94df737 <unknown>
E       #9 0x5623d94ddf39 <unknown>
E       #10 0x5623d94c8c26 <unknown>
E       #11 0x5623d94deada <unknown>
E       #12 0x5623d94b0bd0 <unknown>
E       #13 0x5623d9505c28 <unknown>
E       #14 0x5623d9505dc5 <unknown>
E       #15 0x5623d9517e1e <unknown>
E       #16 0x7fe124a9caa4 <unknown>
E       #17 0x7fe124b29c6c <unknown>

../../../.local/lib/python3.12/site-packages/selenium/webdriver/support/wait.py:121: TimeoutException
---------------------------- Captured stderr setup -----------------------------
2026-06-13 09:05:22  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 09:05:22  INFO      conftest  Chrome Browser Launched Successfully
2026-06-13 09:05:22  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 09:05:23  INFO      conftest  Driver started → browser=chrome | mode=headless
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:62 Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:119 Chrome Browser Launched Successfully
INFO     conftest:conftest.py:175 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:184 Driver started → browser=chrome | mode=headless
----------------------------- Captured stderr call -----------------------------
2026-06-13 09:05:23  INFO      tests.test_login  Invalid login test started
2026-06-13 09:05:24  INFO      tests.test_login  Clicked My Account
2026-06-13 09:05:24  INFO      tests.test_login  Entered invalid username: space143@gmail.com
------------------------------ Captured log call -------------------------------
INFO     tests.test_login:test_login.py:50 Invalid login test started
INFO     tests.test_login:test_login.py:54 Clicked My Account
INFO     tests.test_login:test_login.py:58 Entered invalid username: space143@gmail.com
--------------------------- Captured stderr teardown ---------------------------
2026-06-13 09:05:39  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:196 Quitting driver.
__ TestShopByCategory.test_category_navigation[Desktops & Monitors-Monitors] ___

self = <tests.test_shopbycategory.TestShopByCategory object at 0x7fa00b349520>
driver = (<selenium.webdriver.chrome.webdriver.WebDriver (session="eba1eb72e304c8b8155901f825470979")>, <selenium.webdriver.support.wait.WebDriverWait (session="eba1eb72e304c8b8155901f825470979")>)
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

self = <selenium.webdriver.support.wait.WebDriverWait (session="eba1eb72e304c8b8155901f825470979")>
method = <function element_to_be_clickable.<locals>._predicate at 0x7fa00b1ebe20>
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
2026-06-13 09:05:48  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 09:05:49  INFO      conftest  Chrome Browser Launched Successfully
2026-06-13 09:05:49  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 09:05:49  INFO      conftest  Driver started → browser=chrome | mode=headless
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:62 Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:119 Chrome Browser Launched Successfully
INFO     conftest:conftest.py:175 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:184 Driver started → browser=chrome | mode=headless
----------------------------- Captured stderr call -----------------------------
2026-06-13 09:05:49  INFO      actions.ShopbycategoryAction  Launching URL: https://ecommerce-playground.lambdatest.io
2026-06-13 09:05:50  INFO      actions.ShopbycategoryAction  Application launched successfully
2026-06-13 09:05:50  INFO      actions.ShopbycategoryAction  Clicking Shop By Category menu
2026-06-13 09:06:10  ERROR     actions.ShopbycategoryAction  Unable to click Shop By Category menu: Message: 

------------------------------ Captured log call -------------------------------
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:19 Launching URL: https://ecommerce-playground.lambdatest.io
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:23 Application launched successfully
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:32 Clicking Shop By Category menu
ERROR    actions.ShopbycategoryAction:ShopbycategoryAction.py:43 Unable to click Shop By Category menu: Message:
--------------------------- Captured stderr teardown ---------------------------
2026-06-13 09:06:10  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:196 Quitting driver.
_____ TestShopByCategory.test_category_navigation[Web Cameras-Web Cameras] _____

self = <tests.test_shopbycategory.TestShopByCategory object at 0x7fa00b34a300>
driver = (<selenium.webdriver.chrome.webdriver.WebDriver (session="abc920248a7f9ffaa2f5e23f9feea38f")>, <selenium.webdriver.support.wait.WebDriverWait (session="abc920248a7f9ffaa2f5e23f9feea38f")>)
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

self = <selenium.webdriver.support.wait.WebDriverWait (session="abc920248a7f9ffaa2f5e23f9feea38f")>
method = <function element_to_be_clickable.<locals>._predicate at 0x7fa00b1928e0>
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
2026-06-13 09:06:10  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 09:06:10  INFO      conftest  Chrome Browser Launched Successfully
2026-06-13 09:06:10  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 09:06:11  INFO      conftest  Driver started → browser=chrome | mode=headless
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:62 Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:119 Chrome Browser Launched Successfully
INFO     conftest:conftest.py:175 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:184 Driver started → browser=chrome | mode=headless
----------------------------- Captured stderr call -----------------------------
2026-06-13 09:06:11  INFO      actions.ShopbycategoryAction  Launching URL: https://ecommerce-playground.lambdatest.io
2026-06-13 09:06:12  INFO      actions.ShopbycategoryAction  Application launched successfully
2026-06-13 09:06:12  INFO      actions.ShopbycategoryAction  Clicking Shop By Category menu
2026-06-13 09:06:32  ERROR     actions.ShopbycategoryAction  Unable to click Shop By Category menu: Message: 

------------------------------ Captured log call -------------------------------
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:19 Launching URL: https://ecommerce-playground.lambdatest.io
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:23 Application launched successfully
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:32 Clicking Shop By Category menu
ERROR    actions.ShopbycategoryAction:ShopbycategoryAction.py:43 Unable to click Shop By Category menu: Message:
--------------------------- Captured stderr teardown ---------------------------
2026-06-13 09:06:32  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:196 Quitting driver.
__ TestShopByCategory.test_category_navigation[Phone, Tablets & Ipod-Tablets] __

self = <tests.test_shopbycategory.TestShopByCategory object at 0x7fa00b34a240>
driver = (<selenium.webdriver.chrome.webdriver.WebDriver (session="b6b5bc1182a8ad82c42e60441c339670")>, <selenium.webdriver.support.wait.WebDriverWait (session="b6b5bc1182a8ad82c42e60441c339670")>)
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

self = <selenium.webdriver.support.wait.WebDriverWait (session="b6b5bc1182a8ad82c42e60441c339670")>
method = <function element_to_be_clickable.<locals>._predicate at 0x7fa00b340e00>
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
2026-06-13 09:06:32  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 09:06:32  INFO      conftest  Chrome Browser Launched Successfully
2026-06-13 09:06:32  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 09:06:33  INFO      conftest  Driver started → browser=chrome | mode=headless
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:62 Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:119 Chrome Browser Launched Successfully
INFO     conftest:conftest.py:175 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:184 Driver started → browser=chrome | mode=headless
----------------------------- Captured stderr call -----------------------------
2026-06-13 09:06:33  INFO      actions.ShopbycategoryAction  Launching URL: https://ecommerce-playground.lambdatest.io
2026-06-13 09:06:33  INFO      actions.ShopbycategoryAction  Application launched successfully
2026-06-13 09:06:33  INFO      actions.ShopbycategoryAction  Clicking Shop By Category menu
2026-06-13 09:06:54  ERROR     actions.ShopbycategoryAction  Unable to click Shop By Category menu: Message: 

------------------------------ Captured log call -------------------------------
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:19 Launching URL: https://ecommerce-playground.lambdatest.io
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:23 Application launched successfully
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:32 Clicking Shop By Category menu
ERROR    actions.ShopbycategoryAction:ShopbycategoryAction.py:43 Unable to click Shop By Category menu: Message:
--------------------------- Captured stderr teardown ---------------------------
2026-06-13 09:06:54  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:196 Quitting driver.
___ TestShopByCategory.test_category_navigation[Laptops & Notebooks-Laptops] ___

self = <tests.test_shopbycategory.TestShopByCategory object at 0x7fa00b349f10>
driver = (<selenium.webdriver.chrome.webdriver.WebDriver (session="f823a599e1fb279bf84ee72fc87395e8")>, <selenium.webdriver.support.wait.WebDriverWait (session="f823a599e1fb279bf84ee72fc87395e8")>)
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

self = <selenium.webdriver.support.wait.WebDriverWait (session="f823a599e1fb279bf84ee72fc87395e8")>
method = <function element_to_be_clickable.<locals>._predicate at 0x7fa00b1922a0>
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
2026-06-13 09:06:54  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 09:06:54  INFO      conftest  Chrome Browser Launched Successfully
2026-06-13 09:06:54  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 09:06:55  INFO      conftest  Driver started → browser=chrome | mode=headless
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:62 Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:119 Chrome Browser Launched Successfully
INFO     conftest:conftest.py:175 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:184 Driver started → browser=chrome | mode=headless
----------------------------- Captured stderr call -----------------------------
2026-06-13 09:06:55  INFO      actions.ShopbycategoryAction  Launching URL: https://ecommerce-playground.lambdatest.io
2026-06-13 09:06:55  INFO      actions.ShopbycategoryAction  Application launched successfully
2026-06-13 09:06:55  INFO      actions.ShopbycategoryAction  Clicking Shop By Category menu
2026-06-13 09:07:15  ERROR     actions.ShopbycategoryAction  Unable to click Shop By Category menu: Message: 

------------------------------ Captured log call -------------------------------
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:19 Launching URL: https://ecommerce-playground.lambdatest.io
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:23 Application launched successfully
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:32 Clicking Shop By Category menu
ERROR    actions.ShopbycategoryAction:ShopbycategoryAction.py:43 Unable to click Shop By Category menu: Message:
--------------------------- Captured stderr teardown ---------------------------
2026-06-13 09:07:15  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:196 Quitting driver.
___________________ test_remove_single_product_from_wishlist ___________________

setup = (<selenium.webdriver.chrome.webdriver.WebDriver (session="7b5b5621834a6ebf0381564ea6a2a1da")>, <selenium.webdriver.sup...ait (session="7b5b5621834a6ebf0381564ea6a2a1da")>, <actions.wishlist_actions.WishListActions object at 0x7fa00b300a10>)

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
actions/BaseAction.py:52: in scroll_into_view
    element = self.wait.until(ec.presence_of_element_located(locator))
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <selenium.webdriver.support.wait.WebDriverWait (session="7b5b5621834a6ebf0381564ea6a2a1da")>
method = <function presence_of_element_located.<locals>._predicate at 0x7fa00b1937e0>
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
E       #0 0x563fbbba629a <unknown>
E       #1 0x563fbb588449 <unknown>
E       #2 0x563fbb5dcbaf <unknown>
E       #3 0x563fbb5dce01 <unknown>
E       #4 0x563fbb627ae4 <unknown>
E       #5 0x563fbb624cbf <unknown>
E       #6 0x563fbb5d0132 <unknown>
E       #7 0x563fbb5d0f41 <unknown>
E       #8 0x563fbbb6c737 <unknown>
E       #9 0x563fbbb6af39 <unknown>
E       #10 0x563fbbb55c26 <unknown>
E       #11 0x563fbbb6bada <unknown>
E       #12 0x563fbbb3dbd0 <unknown>
E       #13 0x563fbbb92c28 <unknown>
E       #14 0x563fbbb92dc5 <unknown>
E       #15 0x563fbbba4e1e <unknown>
E       #16 0x7f3c9449caa4 <unknown>
E       #17 0x7f3c94529c6c <unknown>

../../../.local/lib/python3.12/site-packages/selenium/webdriver/support/wait.py:121: TimeoutException
---------------------------- Captured stderr setup -----------------------------
2026-06-13 09:07:50  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 09:07:50  INFO      conftest  Chrome Browser Launched Successfully
2026-06-13 09:07:50  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 09:07:51  INFO      conftest  Driver started → browser=chrome | mode=headless
2026-06-13 09:07:51  INFO      tests.test_wishlist  Landed on home page: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 09:07:51  INFO      tests.test_wishlist  Using credentials for user: testlogin@gmail.com
2026-06-13 09:07:51  INFO      tests.test_wishlist  Clicked 'My Account' link
2026-06-13 09:07:52  INFO      tests.test_wishlist  Submitted login credentials
2026-06-13 09:07:52  INFO      tests.test_wishlist  Login successful: True
2026-06-13 09:07:52  INFO      actions.wishlist_actions  Navigating to home page: https://ecommerce-playground.lambdatest.io/
2026-06-13 09:07:53  INFO      actions.wishlist_actions  Home page loaded successfully
2026-06-13 09:07:53  INFO      tests.test_wishlist  Navigated back to home page: https://ecommerce-playground.lambdatest.io/
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
2026-06-13 09:07:53  INFO      tests.test_wishlist  Starting test: remove single product 'iMac' from wishlist
2026-06-13 09:07:53  INFO      actions.wishlist_actions  Navigated to wishlist page via header link
2026-06-13 09:07:56  INFO      actions.wishlist_actions  Wishlist page is visible
2026-06-13 09:07:56  INFO      tests.test_wishlist  Navigated to wishlist page
2026-06-13 09:07:56  INFO      actions.wishlist_actions  Product 'iMac' present in wishlist: False
2026-06-13 09:07:56  INFO      tests.test_wishlist  'iMac' not in wishlist, adding it now
------------------------------ Captured log call -------------------------------
INFO     tests.test_wishlist:test_wishlist.py:172 Starting test: remove single product 'iMac' from wishlist
INFO     actions.wishlist_actions:wishlist_actions.py:65 Navigated to wishlist page via header link
INFO     actions.wishlist_actions:wishlist_actions.py:85 Wishlist page is visible
INFO     tests.test_wishlist:test_wishlist.py:176 Navigated to wishlist page
INFO     actions.wishlist_actions:wishlist_actions.py:201 Product 'iMac' present in wishlist: False
INFO     tests.test_wishlist:test_wishlist.py:72 'iMac' not in wishlist, adding it now
--------------------------- Captured stderr teardown ---------------------------
2026-06-13 09:08:11  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:196 Quitting driver.
_________ test_remove_multiple_products_from_wishlist[Apple Cinema 30] _________

setup = (<selenium.webdriver.chrome.webdriver.WebDriver (session="be1e8b03b8fe5c46ceb8ab72718f7727")>, <selenium.webdriver.sup...ait (session="be1e8b03b8fe5c46ceb8ab72718f7727")>, <actions.wishlist_actions.WishListActions object at 0x7fa00b247b30>)
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
actions/BaseAction.py:52: in scroll_into_view
    element = self.wait.until(ec.presence_of_element_located(locator))
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <selenium.webdriver.support.wait.WebDriverWait (session="be1e8b03b8fe5c46ceb8ab72718f7727")>
method = <function presence_of_element_located.<locals>._predicate at 0x7fa00b192d40>
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
E       #0 0x558ecec9829a <unknown>
E       #1 0x558ece67a449 <unknown>
E       #2 0x558ece6cebaf <unknown>
E       #3 0x558ece6cee01 <unknown>
E       #4 0x558ece719ae4 <unknown>
E       #5 0x558ece716cbf <unknown>
E       #6 0x558ece6c2132 <unknown>
E       #7 0x558ece6c2f41 <unknown>
E       #8 0x558ecec5e737 <unknown>
E       #9 0x558ecec5cf39 <unknown>
E       #10 0x558ecec47c26 <unknown>
E       #11 0x558ecec5dada <unknown>
E       #12 0x558ecec2fbd0 <unknown>
E       #13 0x558ecec84c28 <unknown>
E       #14 0x558ecec84dc5 <unknown>
E       #15 0x558ecec96e1e <unknown>
E       #16 0x7f86e4a9caa4 <unknown>
E       #17 0x7f86e4b29c6c <unknown>

../../../.local/lib/python3.12/site-packages/selenium/webdriver/support/wait.py:121: TimeoutException
---------------------------- Captured stderr setup -----------------------------
2026-06-13 09:08:11  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 09:08:12  INFO      conftest  Chrome Browser Launched Successfully
2026-06-13 09:08:12  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 09:08:12  INFO      conftest  Driver started → browser=chrome | mode=headless
2026-06-13 09:08:12  INFO      tests.test_wishlist  Landed on home page: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 09:08:12  INFO      tests.test_wishlist  Using credentials for user: testlogin@gmail.com
2026-06-13 09:08:13  INFO      tests.test_wishlist  Clicked 'My Account' link
2026-06-13 09:08:13  INFO      tests.test_wishlist  Submitted login credentials
2026-06-13 09:08:14  INFO      tests.test_wishlist  Login successful: True
2026-06-13 09:08:14  INFO      actions.wishlist_actions  Navigating to home page: https://ecommerce-playground.lambdatest.io/
2026-06-13 09:08:14  INFO      actions.wishlist_actions  Home page loaded successfully
2026-06-13 09:08:14  INFO      tests.test_wishlist  Navigated back to home page: https://ecommerce-playground.lambdatest.io/
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
2026-06-13 09:08:14  INFO      tests.test_wishlist  Starting test: remove product 'Apple Cinema 30' from wishlist
2026-06-13 09:08:15  INFO      actions.wishlist_actions  Navigated to wishlist page via header link
2026-06-13 09:08:18  INFO      actions.wishlist_actions  Wishlist page is visible
2026-06-13 09:08:18  INFO      tests.test_wishlist  Navigated to wishlist page
2026-06-13 09:08:18  INFO      actions.wishlist_actions  Product 'Apple Cinema 30' present in wishlist: False
2026-06-13 09:08:18  INFO      tests.test_wishlist  'Apple Cinema 30' not in wishlist, adding it now
------------------------------ Captured log call -------------------------------
INFO     tests.test_wishlist:test_wishlist.py:196 Starting test: remove product 'Apple Cinema 30' from wishlist
INFO     actions.wishlist_actions:wishlist_actions.py:65 Navigated to wishlist page via header link
INFO     actions.wishlist_actions:wishlist_actions.py:85 Wishlist page is visible
INFO     tests.test_wishlist:test_wishlist.py:200 Navigated to wishlist page
INFO     actions.wishlist_actions:wishlist_actions.py:201 Product 'Apple Cinema 30' present in wishlist: False
INFO     tests.test_wishlist:test_wishlist.py:72 'Apple Cinema 30' not in wishlist, adding it now
--------------------------- Captured stderr teardown ---------------------------
2026-06-13 09:08:33  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:196 Quitting driver.
____________ test_remove_multiple_products_from_wishlist[iPod Nano] ____________

setup = (<selenium.webdriver.chrome.webdriver.WebDriver (session="6c1e295425ab0ed7f3e6914d694fa017")>, <selenium.webdriver.sup...ait (session="6c1e295425ab0ed7f3e6914d694fa017")>, <actions.wishlist_actions.WishListActions object at 0x7fa00b16f5c0>)
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
actions/BaseAction.py:52: in scroll_into_view
    element = self.wait.until(ec.presence_of_element_located(locator))
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <selenium.webdriver.support.wait.WebDriverWait (session="6c1e295425ab0ed7f3e6914d694fa017")>
method = <function presence_of_element_located.<locals>._predicate at 0x7fa00b193740>
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
E       #0 0x55dc4b11629a <unknown>
E       #1 0x55dc4aaf8449 <unknown>
E       #2 0x55dc4ab4cbaf <unknown>
E       #3 0x55dc4ab4ce01 <unknown>
E       #4 0x55dc4ab97ae4 <unknown>
E       #5 0x55dc4ab94cbf <unknown>
E       #6 0x55dc4ab40132 <unknown>
E       #7 0x55dc4ab40f41 <unknown>
E       #8 0x55dc4b0dc737 <unknown>
E       #9 0x55dc4b0daf39 <unknown>
E       #10 0x55dc4b0c5c26 <unknown>
E       #11 0x55dc4b0dbada <unknown>
E       #12 0x55dc4b0adbd0 <unknown>
E       #13 0x55dc4b102c28 <unknown>
E       #14 0x55dc4b102dc5 <unknown>
E       #15 0x55dc4b114e1e <unknown>
E       #16 0x7f53e2c9caa4 <unknown>
E       #17 0x7f53e2d29c6c <unknown>

../../../.local/lib/python3.12/site-packages/selenium/webdriver/support/wait.py:121: TimeoutException
---------------------------- Captured stderr setup -----------------------------
2026-06-13 09:08:33  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 09:08:33  INFO      conftest  Chrome Browser Launched Successfully
2026-06-13 09:08:33  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 09:08:34  INFO      conftest  Driver started → browser=chrome | mode=headless
2026-06-13 09:08:34  INFO      tests.test_wishlist  Landed on home page: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-13 09:08:34  INFO      tests.test_wishlist  Using credentials for user: testlogin@gmail.com
2026-06-13 09:08:35  INFO      tests.test_wishlist  Clicked 'My Account' link
2026-06-13 09:08:35  INFO      tests.test_wishlist  Submitted login credentials
2026-06-13 09:08:36  INFO      tests.test_wishlist  Login successful: True
2026-06-13 09:08:36  INFO      actions.wishlist_actions  Navigating to home page: https://ecommerce-playground.lambdatest.io/
2026-06-13 09:08:36  INFO      actions.wishlist_actions  Home page loaded successfully
2026-06-13 09:08:36  INFO      tests.test_wishlist  Navigated back to home page: https://ecommerce-playground.lambdatest.io/
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
2026-06-13 09:08:36  INFO      tests.test_wishlist  Starting test: remove product 'iPod Nano' from wishlist
2026-06-13 09:08:36  INFO      actions.wishlist_actions  Navigated to wishlist page via header link
2026-06-13 09:08:39  INFO      actions.wishlist_actions  Wishlist page is visible
2026-06-13 09:08:39  INFO      tests.test_wishlist  Navigated to wishlist page
2026-06-13 09:08:39  INFO      actions.wishlist_actions  Product 'iPod Nano' present in wishlist: False
2026-06-13 09:08:39  INFO      tests.test_wishlist  'iPod Nano' not in wishlist, adding it now
------------------------------ Captured log call -------------------------------
INFO     tests.test_wishlist:test_wishlist.py:196 Starting test: remove product 'iPod Nano' from wishlist
INFO     actions.wishlist_actions:wishlist_actions.py:65 Navigated to wishlist page via header link
INFO     actions.wishlist_actions:wishlist_actions.py:85 Wishlist page is visible
INFO     tests.test_wishlist:test_wishlist.py:200 Navigated to wishlist page
INFO     actions.wishlist_actions:wishlist_actions.py:201 Product 'iPod Nano' present in wishlist: False
INFO     tests.test_wishlist:test_wishlist.py:72 'iPod Nano' not in wishlist, adding it now
--------------------------- Captured stderr teardown ---------------------------
2026-06-13 09:08:55  INFO      conftest  Quitting driver.
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
FAILED tests/test_login.py::TestLogin::test_invalidLogin[space143@gmail.com-testlogin] - selenium.common.exceptions.TimeoutException: Message: 
Stacktrace:
#0 0x5623d951929a <unknown>
#1 0x5623d8efb449 <unknown>
#2 0x5623d8f4fbaf <unknown>
#3 0x5623d8f4fe01 <unknown>
#4 0x5623d8f9aae4 <unknown>
#5 0x5623d8f97cbf <unknown>
#6 0x5623d8f43132 <unknown>
#7 0x5623d8f43f41 <unknown>
#8 0x5623d94df737 <unknown>
#9 0x5623d94ddf39 <unknown>
#10 0x5623d94c8c26 <unknown>
#11 0x5623d94deada <unknown>
#12 0x5623d94b0bd0 <unknown>
#13 0x5623d9505c28 <unknown>
#14 0x5623d9505dc5 <unknown>
#15 0x5623d9517e1e <unknown>
#16 0x7fe124a9caa4 <unknown>
#17 0x7fe124b29c6c <unknown>
FAILED tests/test_shopbycategory.py::TestShopByCategory::test_category_navigation[Desktops & Monitors-Monitors] - selenium.common.exceptions.TimeoutException: Message:
FAILED tests/test_shopbycategory.py::TestShopByCategory::test_category_navigation[Web Cameras-Web Cameras] - selenium.common.exceptions.TimeoutException: Message:
FAILED tests/test_shopbycategory.py::TestShopByCategory::test_category_navigation[Phone, Tablets & Ipod-Tablets] - selenium.common.exceptions.TimeoutException: Message:
FAILED tests/test_shopbycategory.py::TestShopByCategory::test_category_navigation[Laptops & Notebooks-Laptops] - selenium.common.exceptions.TimeoutException: Message:
FAILED tests/test_wishlist.py::test_remove_single_product_from_wishlist - selenium.common.exceptions.TimeoutException: Message: 
Stacktrace:
#0 0x563fbbba629a <unknown>
#1 0x563fbb588449 <unknown>
#2 0x563fbb5dcbaf <unknown>
#3 0x563fbb5dce01 <unknown>
#4 0x563fbb627ae4 <unknown>
#5 0x563fbb624cbf <unknown>
#6 0x563fbb5d0132 <unknown>
#7 0x563fbb5d0f41 <unknown>
#8 0x563fbbb6c737 <unknown>
#9 0x563fbbb6af39 <unknown>
#10 0x563fbbb55c26 <unknown>
#11 0x563fbbb6bada <unknown>
#12 0x563fbbb3dbd0 <unknown>
#13 0x563fbbb92c28 <unknown>
#14 0x563fbbb92dc5 <unknown>
#15 0x563fbbba4e1e <unknown>
#16 0x7f3c9449caa4 <unknown>
#17 0x7f3c94529c6c <unknown>
FAILED tests/test_wishlist.py::test_remove_multiple_products_from_wishlist[Apple Cinema 30] - selenium.common.exceptions.TimeoutException: Message: 
Stacktrace:
#0 0x558ecec9829a <unknown>
#1 0x558ece67a449 <unknown>
#2 0x558ece6cebaf <unknown>
#3 0x558ece6cee01 <unknown>
#4 0x558ece719ae4 <unknown>
#5 0x558ece716cbf <unknown>
#6 0x558ece6c2132 <unknown>
#7 0x558ece6c2f41 <unknown>
#8 0x558ecec5e737 <unknown>
#9 0x558ecec5cf39 <unknown>
#10 0x558ecec47c26 <unknown>
#11 0x558ecec5dada <unknown>
#12 0x558ecec2fbd0 <unknown>
#13 0x558ecec84c28 <unknown>
#14 0x558ecec84dc5 <unknown>
#15 0x558ecec96e1e <unknown>
#16 0x7f86e4a9caa4 <unknown>
#17 0x7f86e4b29c6c <unknown>
FAILED tests/test_wishlist.py::test_remove_multiple_products_from_wishlist[iPod Nano] - selenium.common.exceptions.TimeoutException: Message: 
Stacktrace:
#0 0x55dc4b11629a <unknown>
#1 0x55dc4aaf8449 <unknown>
#2 0x55dc4ab4cbaf <unknown>
#3 0x55dc4ab4ce01 <unknown>
#4 0x55dc4ab97ae4 <unknown>
#5 0x55dc4ab94cbf <unknown>
#6 0x55dc4ab40132 <unknown>
#7 0x55dc4ab40f41 <unknown>
#8 0x55dc4b0dc737 <unknown>
#9 0x55dc4b0daf39 <unknown>
#10 0x55dc4b0c5c26 <unknown>
#11 0x55dc4b0dbada <unknown>
#12 0x55dc4b0adbd0 <unknown>
#13 0x55dc4b102c28 <unknown>
#14 0x55dc4b102dc5 <unknown>
#15 0x55dc4b114e1e <unknown>
#16 0x7f53e2c9caa4 <unknown>
#17 0x7f53e2d29c6c <unknown>
============= 10 failed, 16 passed, 1 warning in 302.21s (0:05:02) =============
```
