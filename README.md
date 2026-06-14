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
tests/test_login.py .F                                                   [ 53%]
tests/test_logout.py .                                                   [ 57%]
tests/test_register.py ..                                                [ 64%]
tests/test_shopbycategory.py FFFF                                        [ 78%]
tests/test_wishlist.py ..F...                                            [100%]

=================================== FAILURES ===================================
_______________________ TestCheckout.test_login_checkout _______________________

self = <tests.test_checkout.TestCheckout object at 0x7f5114206e10>
driver = (<selenium.webdriver.chrome.webdriver.WebDriver (session="1ee68e6ee926441665d1d7e79f504d9f")>, <selenium.webdriver.support.wait.WebDriverWait (session="1ee68e6ee926441665d1d7e79f504d9f")>)

    def test_login_checkout(self, driver):
    
        drv, wait = driver
        action = CheckoutAction(drv)
    
        drv.get(ConfigReader.get_url())
    
        action.click_hp_product()
>       action.add_product_to_cart()

tests/test_checkout.py:22: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <actions.checkoutAction.CheckoutAction object at 0x7f510fee8e30>

    def add_product_to_cart(self):
>       self.click(self.cp.PRODUCT_PAGE_CHECKOUT_BTN1)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       AttributeError: 'CheckoutPage' object has no attribute 'PRODUCT_PAGE_CHECKOUT_BTN1'. Did you mean: 'CART_PAGE_CHECKOUT_BTN'?

actions/checkoutAction.py:23: AttributeError
---------------------------- Captured stderr setup -----------------------------
2026-06-14 06:15:12  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-14 06:15:12  INFO      conftest  Chrome Browser Launched Successfully
2026-06-14 06:15:12  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-14 06:15:12  INFO      conftest  Driver started → browser=chrome | mode=headless
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:62 Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:119 Chrome Browser Launched Successfully
INFO     conftest:conftest.py:175 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:184 Driver started → browser=chrome | mode=headless
--------------------------- Captured stderr teardown ---------------------------
2026-06-14 06:15:29  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:196 Quitting driver.
_____________________ TestCheckout.test_register_checkout ______________________

self = <tests.test_checkout.TestCheckout object at 0x7f511412f3b0>
driver = (<selenium.webdriver.chrome.webdriver.WebDriver (session="97b1185c69bc5cbe8fdbda999473d68e")>, <selenium.webdriver.support.wait.WebDriverWait (session="97b1185c69bc5cbe8fdbda999473d68e")>)

    def test_register_checkout(self, driver):
    
        drv, wait = driver
        action = CheckoutAction(drv)
    
>       action.open_home_and_add_product(ConfigReader.get_url())
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       AttributeError: 'CheckoutAction' object has no attribute 'open_home_and_add_product'

tests/test_checkout.py:56: AttributeError
---------------------------- Captured stderr setup -----------------------------
2026-06-14 06:15:29  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-14 06:15:29  INFO      conftest  Chrome Browser Launched Successfully
2026-06-14 06:15:29  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-14 06:15:30  INFO      conftest  Driver started → browser=chrome | mode=headless
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:62 Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:119 Chrome Browser Launched Successfully
INFO     conftest:conftest.py:175 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:184 Driver started → browser=chrome | mode=headless
--------------------------- Captured stderr teardown ---------------------------
2026-06-14 06:15:30  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:196 Quitting driver.
__________ TestLogin.test_invalidLogin[camera143@gmail.com-testlogin] __________

self = <tests.test_login.TestLogin object at 0x7f510fea3260>
driver = (<selenium.webdriver.chrome.webdriver.WebDriver (session="da1da6f36ade576eefbd2cd70aa11a47")>, <selenium.webdriver.support.wait.WebDriverWait (session="da1da6f36ade576eefbd2cd70aa11a47")>)
username1 = 'camera143@gmail.com', password1 = 'testlogin'

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
actions/BaseAction.py:39: in get_text
    return self.wait.until(ec.visibility_of_element_located(locator)).text
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <selenium.webdriver.support.wait.WebDriverWait (session="da1da6f36ade576eefbd2cd70aa11a47")>
method = <function visibility_of_element_located.<locals>._predicate at 0x7f510fd2ade0>
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
E       #0 0x55a72439c29a <unknown>
E       #1 0x55a723d7e449 <unknown>
E       #2 0x55a723dd2baf <unknown>
E       #3 0x55a723dd2e01 <unknown>
E       #4 0x55a723e1dae4 <unknown>
E       #5 0x55a723e1acbf <unknown>
E       #6 0x55a723dc6132 <unknown>
E       #7 0x55a723dc6f41 <unknown>
E       #8 0x55a724362737 <unknown>
E       #9 0x55a724360f39 <unknown>
E       #10 0x55a72434bc26 <unknown>
E       #11 0x55a724361ada <unknown>
E       #12 0x55a724333bd0 <unknown>
E       #13 0x55a724388c28 <unknown>
E       #14 0x55a724388dc5 <unknown>
E       #15 0x55a72439ae1e <unknown>
E       #16 0x7f9355a9caa4 <unknown>
E       #17 0x7f9355b29c6c <unknown>

../../../.local/lib/python3.12/site-packages/selenium/webdriver/support/wait.py:121: TimeoutException
---------------------------- Captured stderr setup -----------------------------
2026-06-14 06:16:11  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-14 06:16:12  INFO      conftest  Chrome Browser Launched Successfully
2026-06-14 06:16:12  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-14 06:16:12  INFO      conftest  Driver started → browser=chrome | mode=headless
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:62 Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:119 Chrome Browser Launched Successfully
INFO     conftest:conftest.py:175 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:184 Driver started → browser=chrome | mode=headless
----------------------------- Captured stderr call -----------------------------
2026-06-14 06:16:12  INFO      tests.test_login  Invalid login test started
2026-06-14 06:16:13  INFO      tests.test_login  Clicked My Account
2026-06-14 06:16:13  INFO      tests.test_login  Entered invalid username: camera143@gmail.com
------------------------------ Captured log call -------------------------------
INFO     tests.test_login:test_login.py:50 Invalid login test started
INFO     tests.test_login:test_login.py:54 Clicked My Account
INFO     tests.test_login:test_login.py:58 Entered invalid username: camera143@gmail.com
--------------------------- Captured stderr teardown ---------------------------
2026-06-14 06:16:28  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:196 Quitting driver.
__ TestShopByCategory.test_category_navigation[Desktops & Monitors-Monitors] ___

self = <tests.test_shopbycategory.TestShopByCategory object at 0x7f510feebc20>
driver = (<selenium.webdriver.chrome.webdriver.WebDriver (session="25db1c42fa251ea75d2e5a38e6460a71")>, <selenium.webdriver.support.wait.WebDriverWait (session="25db1c42fa251ea75d2e5a38e6460a71")>)
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

self = <selenium.webdriver.support.wait.WebDriverWait (session="25db1c42fa251ea75d2e5a38e6460a71")>
method = <function element_to_be_clickable.<locals>._predicate at 0x7f510fec58a0>
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
2026-06-14 06:16:37  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-14 06:16:37  INFO      conftest  Chrome Browser Launched Successfully
2026-06-14 06:16:37  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-14 06:16:38  INFO      conftest  Driver started → browser=chrome | mode=headless
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:62 Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:119 Chrome Browser Launched Successfully
INFO     conftest:conftest.py:175 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:184 Driver started → browser=chrome | mode=headless
----------------------------- Captured stderr call -----------------------------
2026-06-14 06:16:38  INFO      actions.ShopbycategoryAction  Launching URL: https://ecommerce-playground.lambdatest.io
2026-06-14 06:16:38  INFO      actions.ShopbycategoryAction  Application launched successfully
2026-06-14 06:16:38  INFO      actions.ShopbycategoryAction  Clicking Shop By Category menu
2026-06-14 06:16:58  ERROR     actions.ShopbycategoryAction  Unable to click Shop By Category menu: Message: 

------------------------------ Captured log call -------------------------------
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:19 Launching URL: https://ecommerce-playground.lambdatest.io
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:23 Application launched successfully
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:32 Clicking Shop By Category menu
ERROR    actions.ShopbycategoryAction:ShopbycategoryAction.py:43 Unable to click Shop By Category menu: Message:
--------------------------- Captured stderr teardown ---------------------------
2026-06-14 06:16:58  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:196 Quitting driver.
_____ TestShopByCategory.test_category_navigation[Web Cameras-Web Cameras] _____

self = <tests.test_shopbycategory.TestShopByCategory object at 0x7f510feeacf0>
driver = (<selenium.webdriver.chrome.webdriver.WebDriver (session="ac36177b63e69679e4da4684f14b2cea")>, <selenium.webdriver.support.wait.WebDriverWait (session="ac36177b63e69679e4da4684f14b2cea")>)
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

self = <selenium.webdriver.support.wait.WebDriverWait (session="ac36177b63e69679e4da4684f14b2cea")>
method = <function element_to_be_clickable.<locals>._predicate at 0x7f510fd2b9c0>
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
2026-06-14 06:16:58  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-14 06:16:59  INFO      conftest  Chrome Browser Launched Successfully
2026-06-14 06:16:59  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-14 06:16:59  INFO      conftest  Driver started → browser=chrome | mode=headless
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:62 Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:119 Chrome Browser Launched Successfully
INFO     conftest:conftest.py:175 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:184 Driver started → browser=chrome | mode=headless
----------------------------- Captured stderr call -----------------------------
2026-06-14 06:16:59  INFO      actions.ShopbycategoryAction  Launching URL: https://ecommerce-playground.lambdatest.io
2026-06-14 06:17:00  INFO      actions.ShopbycategoryAction  Application launched successfully
2026-06-14 06:17:00  INFO      actions.ShopbycategoryAction  Clicking Shop By Category menu
2026-06-14 06:17:20  ERROR     actions.ShopbycategoryAction  Unable to click Shop By Category menu: Message: 

------------------------------ Captured log call -------------------------------
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:19 Launching URL: https://ecommerce-playground.lambdatest.io
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:23 Application launched successfully
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:32 Clicking Shop By Category menu
ERROR    actions.ShopbycategoryAction:ShopbycategoryAction.py:43 Unable to click Shop By Category menu: Message:
--------------------------- Captured stderr teardown ---------------------------
2026-06-14 06:17:20  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:196 Quitting driver.
__ TestShopByCategory.test_category_navigation[Phone, Tablets & Ipod-Tablets] __

self = <tests.test_shopbycategory.TestShopByCategory object at 0x7f510feeaab0>
driver = (<selenium.webdriver.chrome.webdriver.WebDriver (session="f8e379e0a1b0752d2196c866bd849913")>, <selenium.webdriver.support.wait.WebDriverWait (session="f8e379e0a1b0752d2196c866bd849913")>)
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

self = <selenium.webdriver.support.wait.WebDriverWait (session="f8e379e0a1b0752d2196c866bd849913")>
method = <function element_to_be_clickable.<locals>._predicate at 0x7f51152efc40>
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
2026-06-14 06:17:20  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-14 06:17:20  INFO      conftest  Chrome Browser Launched Successfully
2026-06-14 06:17:20  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-14 06:17:21  INFO      conftest  Driver started → browser=chrome | mode=headless
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:62 Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:119 Chrome Browser Launched Successfully
INFO     conftest:conftest.py:175 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:184 Driver started → browser=chrome | mode=headless
----------------------------- Captured stderr call -----------------------------
2026-06-14 06:17:21  INFO      actions.ShopbycategoryAction  Launching URL: https://ecommerce-playground.lambdatest.io
2026-06-14 06:17:22  INFO      actions.ShopbycategoryAction  Application launched successfully
2026-06-14 06:17:22  INFO      actions.ShopbycategoryAction  Clicking Shop By Category menu
2026-06-14 06:17:42  ERROR     actions.ShopbycategoryAction  Unable to click Shop By Category menu: Message: 

------------------------------ Captured log call -------------------------------
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:19 Launching URL: https://ecommerce-playground.lambdatest.io
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:23 Application launched successfully
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:32 Clicking Shop By Category menu
ERROR    actions.ShopbycategoryAction:ShopbycategoryAction.py:43 Unable to click Shop By Category menu: Message:
--------------------------- Captured stderr teardown ---------------------------
2026-06-14 06:17:42  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:196 Quitting driver.
___ TestShopByCategory.test_category_navigation[Laptops & Notebooks-Laptops] ___

self = <tests.test_shopbycategory.TestShopByCategory object at 0x7f510fee9dc0>
driver = (<selenium.webdriver.chrome.webdriver.WebDriver (session="433d5459dbbcb989b13650779c1053da")>, <selenium.webdriver.support.wait.WebDriverWait (session="433d5459dbbcb989b13650779c1053da")>)
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

self = <selenium.webdriver.support.wait.WebDriverWait (session="433d5459dbbcb989b13650779c1053da")>
method = <function element_to_be_clickable.<locals>._predicate at 0x7f510fec5800>
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
2026-06-14 06:17:42  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-14 06:17:42  INFO      conftest  Chrome Browser Launched Successfully
2026-06-14 06:17:42  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-14 06:17:43  INFO      conftest  Driver started → browser=chrome | mode=headless
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:62 Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:119 Chrome Browser Launched Successfully
INFO     conftest:conftest.py:175 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:184 Driver started → browser=chrome | mode=headless
----------------------------- Captured stderr call -----------------------------
2026-06-14 06:17:43  INFO      actions.ShopbycategoryAction  Launching URL: https://ecommerce-playground.lambdatest.io
2026-06-14 06:17:43  INFO      actions.ShopbycategoryAction  Application launched successfully
2026-06-14 06:17:43  INFO      actions.ShopbycategoryAction  Clicking Shop By Category menu
2026-06-14 06:18:04  ERROR     actions.ShopbycategoryAction  Unable to click Shop By Category menu: Message: 

------------------------------ Captured log call -------------------------------
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:19 Launching URL: https://ecommerce-playground.lambdatest.io
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:23 Application launched successfully
INFO     actions.ShopbycategoryAction:ShopbycategoryAction.py:32 Clicking Shop By Category menu
ERROR    actions.ShopbycategoryAction:ShopbycategoryAction.py:43 Unable to click Shop By Category menu: Message:
--------------------------- Captured stderr teardown ---------------------------
2026-06-14 06:18:04  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:196 Quitting driver.
_________________________ test_add_product_via_search __________________________

self = <actions.wishlist_actions.WishListActions object at 0x7f511404d730>

    def get_wishlist_success_message_generic(self):
        """Return the wishlist success notification text, using a fallback locator if needed."""
        try:
>           message = self.get_text(self.wishlist_page.SUCCESS_NOTIFICATION)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

actions/wishlist_actions.py:163: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
actions/BaseAction.py:39: in get_text
    return self.wait.until(ec.visibility_of_element_located(locator)).text
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <selenium.webdriver.support.wait.WebDriverWait (session="0c3db3cf51807c70d8c57b1f8514b914")>
method = <function visibility_of_element_located.<locals>._predicate at 0x7f510fec4d60>
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
E       #0 0x55693447229a <unknown>
E       #1 0x556933e54449 <unknown>
E       #2 0x556933ea8baf <unknown>
E       #3 0x556933ea8e01 <unknown>
E       #4 0x556933ef3ae4 <unknown>
E       #5 0x556933ef0cbf <unknown>
E       #6 0x556933e9c132 <unknown>
E       #7 0x556933e9cf41 <unknown>
E       #8 0x556934438737 <unknown>
E       #9 0x556934436f39 <unknown>
E       #10 0x556934421c26 <unknown>
E       #11 0x556934437ada <unknown>
E       #12 0x556934409bd0 <unknown>
E       #13 0x55693445ec28 <unknown>
E       #14 0x55693445edc5 <unknown>
E       #15 0x556934470e1e <unknown>
E       #16 0x7f7d8909caa4 <unknown>
E       #17 0x7f7d89129c6c <unknown>

../../../.local/lib/python3.12/site-packages/selenium/webdriver/support/wait.py:121: TimeoutException

During handling of the above exception, another exception occurred:

setup = (<selenium.webdriver.chrome.webdriver.WebDriver (session="0c3db3cf51807c70d8c57b1f8514b914")>, <selenium.webdriver.sup...ait (session="0c3db3cf51807c70d8c57b1f8514b914")>, <actions.wishlist_actions.WishListActions object at 0x7f511404d730>)

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
actions/BaseAction.py:39: in get_text
    return self.wait.until(ec.visibility_of_element_located(locator)).text
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <selenium.webdriver.support.wait.WebDriverWait (session="0c3db3cf51807c70d8c57b1f8514b914")>
method = <function visibility_of_element_located.<locals>._predicate at 0x7f510fdd9120>
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
E       #0 0x55693447229a <unknown>
E       #1 0x556933e54449 <unknown>
E       #2 0x556933ea8baf <unknown>
E       #3 0x556933ea8e01 <unknown>
E       #4 0x556933ef3ae4 <unknown>
E       #5 0x556933ef0cbf <unknown>
E       #6 0x556933e9c132 <unknown>
E       #7 0x556933e9cf41 <unknown>
E       #8 0x556934438737 <unknown>
E       #9 0x556934436f39 <unknown>
E       #10 0x556934421c26 <unknown>
E       #11 0x556934437ada <unknown>
E       #12 0x556934409bd0 <unknown>
E       #13 0x55693445ec28 <unknown>
E       #14 0x55693445edc5 <unknown>
E       #15 0x556934470e1e <unknown>
E       #16 0x7f7d8909caa4 <unknown>
E       #17 0x7f7d89129c6c <unknown>

../../../.local/lib/python3.12/site-packages/selenium/webdriver/support/wait.py:121: TimeoutException
---------------------------- Captured stderr setup -----------------------------
2026-06-14 06:18:28  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-14 06:18:28  INFO      conftest  Chrome Browser Launched Successfully
2026-06-14 06:18:28  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-14 06:18:29  INFO      conftest  Driver started → browser=chrome | mode=headless
2026-06-14 06:18:29  INFO      tests.test_wishlist  Landed on home page: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-14 06:18:29  INFO      tests.test_wishlist  Using credentials for user: testlogin@gmail.com
2026-06-14 06:18:29  INFO      tests.test_wishlist  Clicked 'My Account' link
2026-06-14 06:18:29  INFO      tests.test_wishlist  Submitted login credentials
2026-06-14 06:18:30  INFO      tests.test_wishlist  Login successful: True
2026-06-14 06:18:30  INFO      actions.wishlist_actions  Navigating to home page: https://ecommerce-playground.lambdatest.io/
2026-06-14 06:18:30  INFO      actions.wishlist_actions  Home page loaded successfully
2026-06-14 06:18:30  INFO      tests.test_wishlist  Navigated back to home page: https://ecommerce-playground.lambdatest.io/
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
2026-06-14 06:18:30  INFO      tests.test_wishlist  Starting test: add product 'iPod Shuffle' via search
2026-06-14 06:18:30  INFO      actions.wishlist_actions  Searched for product: iPod Shuffle
2026-06-14 06:18:30  INFO      tests.test_wishlist  Searched for product: iPod Shuffle
2026-06-14 06:18:31  INFO      actions.wishlist_actions  Opened product page for: iPod Shuffle
2026-06-14 06:18:31  INFO      tests.test_wishlist  Opened product page for: iPod Shuffle
2026-06-14 06:18:32  INFO      actions.wishlist_actions  Clicked wishlist (heart) button on product page
2026-06-14 06:18:32  INFO      tests.test_wishlist  Clicked wishlist (heart) button on product page
2026-06-14 06:18:47  WARNING   actions.wishlist_actions  Primary success notification not found, using fallback
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
2026-06-14 06:19:02  INFO      conftest  Quitting driver.
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
FAILED tests/test_login.py::TestLogin::test_invalidLogin[camera143@gmail.com-testlogin] - selenium.common.exceptions.TimeoutException: Message: 
Stacktrace:
#0 0x55a72439c29a <unknown>
#1 0x55a723d7e449 <unknown>
#2 0x55a723dd2baf <unknown>
#3 0x55a723dd2e01 <unknown>
#4 0x55a723e1dae4 <unknown>
#5 0x55a723e1acbf <unknown>
#6 0x55a723dc6132 <unknown>
#7 0x55a723dc6f41 <unknown>
#8 0x55a724362737 <unknown>
#9 0x55a724360f39 <unknown>
#10 0x55a72434bc26 <unknown>
#11 0x55a724361ada <unknown>
#12 0x55a724333bd0 <unknown>
#13 0x55a724388c28 <unknown>
#14 0x55a724388dc5 <unknown>
#15 0x55a72439ae1e <unknown>
#16 0x7f9355a9caa4 <unknown>
#17 0x7f9355b29c6c <unknown>
FAILED tests/test_shopbycategory.py::TestShopByCategory::test_category_navigation[Desktops & Monitors-Monitors] - selenium.common.exceptions.TimeoutException: Message:
FAILED tests/test_shopbycategory.py::TestShopByCategory::test_category_navigation[Web Cameras-Web Cameras] - selenium.common.exceptions.TimeoutException: Message:
FAILED tests/test_shopbycategory.py::TestShopByCategory::test_category_navigation[Phone, Tablets & Ipod-Tablets] - selenium.common.exceptions.TimeoutException: Message:
FAILED tests/test_shopbycategory.py::TestShopByCategory::test_category_navigation[Laptops & Notebooks-Laptops] - selenium.common.exceptions.TimeoutException: Message:
FAILED tests/test_wishlist.py::test_add_product_via_search - selenium.common.exceptions.TimeoutException: Message: 
Stacktrace:
#0 0x55693447229a <unknown>
#1 0x556933e54449 <unknown>
#2 0x556933ea8baf <unknown>
#3 0x556933ea8e01 <unknown>
#4 0x556933ef3ae4 <unknown>
#5 0x556933ef0cbf <unknown>
#6 0x556933e9c132 <unknown>
#7 0x556933e9cf41 <unknown>
#8 0x556934438737 <unknown>
#9 0x556934436f39 <unknown>
#10 0x556934421c26 <unknown>
#11 0x556934437ada <unknown>
#12 0x556934409bd0 <unknown>
#13 0x55693445ec28 <unknown>
#14 0x55693445edc5 <unknown>
#15 0x556934470e1e <unknown>
#16 0x7f7d8909caa4 <unknown>
#17 0x7f7d89129c6c <unknown>
============= 8 failed, 20 passed, 1 warning in 294.61s (0:04:54) ==============
```
