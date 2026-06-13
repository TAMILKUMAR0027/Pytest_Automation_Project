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
collected 21 items

tests/test_Filter.py .....                                               [ 23%]
tests/test_checkout.py FF.                                               [ 38%]
tests/test_forgetpassword.py ..                                          [ 47%]
tests/test_launch.py .                                                   [ 52%]
tests/test_login.py ..                                                   [ 61%]
tests/test_register.py ..                                                [ 71%]
tests/test_wishlist.py ......                                            [100%]

=================================== FAILURES ===================================
_______________________ TestCheckout.test_login_checkout _______________________

self = <tests.test_checkout.TestCheckout object at 0x7fa58d7a1eb0>
driver = (<selenium.webdriver.firefox.webdriver.WebDriver (session="c5442b3c-54ba-46fc-beb7-088b6036d948")>, <selenium.webdriver.support.wait.WebDriverWait (session="c5442b3c-54ba-46fc-beb7-088b6036d948")>)

    def test_login_checkout(self, driver):
    
        drv, wait = driver
        action = CheckoutAction(drv)
    
        drv.get(ConfigReader.get_url())
    
        action.click_hp_product()
>       action.add_product_to_cart()

tests/test_checkout.py:22: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <actions.checkoutAction.CheckoutAction object at 0x7fa58d666cc0>

    def add_product_to_cart(self):
>       self.click(self.cp.PRODUCT_PAGE_CHECKOUT_BTN1)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       AttributeError: 'CheckoutPage' object has no attribute 'PRODUCT_PAGE_CHECKOUT_BTN1'. Did you mean: 'CART_PAGE_CHECKOUT_BTN'?

actions/checkoutAction.py:23: AttributeError
---------------------------- Captured stderr setup -----------------------------
2026-06-12 11:24:26  INFO      conftest  Config → browser=firefox | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-12 11:24:28  INFO      conftest  Firefox Browser Launched Successfully
2026-06-12 11:24:28  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-12 11:24:29  INFO      conftest  Driver started → browser=firefox | mode=headless
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:62 Config → browser=firefox | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:144 Firefox Browser Launched Successfully
INFO     conftest:conftest.py:175 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:184 Driver started → browser=firefox | mode=headless
--------------------------- Captured stderr teardown ---------------------------
2026-06-12 11:24:45  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:196 Quitting driver.
_____________________ TestCheckout.test_register_checkout ______________________

self = <tests.test_checkout.TestCheckout object at 0x7fa58ea39fd0>
driver = (<selenium.webdriver.firefox.webdriver.WebDriver (session="f74f4f79-aa71-41c5-a6c7-21286c4eef17")>, <selenium.webdriver.support.wait.WebDriverWait (session="f74f4f79-aa71-41c5-a6c7-21286c4eef17")>)

    def test_register_checkout(self, driver):
    
        drv, wait = driver
        action = CheckoutAction(drv)
    
>       action.open_home_and_add_product(ConfigReader.get_url())
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       AttributeError: 'CheckoutAction' object has no attribute 'open_home_and_add_product'

tests/test_checkout.py:56: AttributeError
---------------------------- Captured stderr setup -----------------------------
2026-06-12 11:24:45  INFO      conftest  Config → browser=firefox | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-12 11:24:48  INFO      conftest  Firefox Browser Launched Successfully
2026-06-12 11:24:48  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-12 11:24:49  INFO      conftest  Driver started → browser=firefox | mode=headless
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:62 Config → browser=firefox | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:144 Firefox Browser Launched Successfully
INFO     conftest:conftest.py:175 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:184 Driver started → browser=firefox | mode=headless
--------------------------- Captured stderr teardown ---------------------------
2026-06-12 11:24:49  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:196 Quitting driver.
=============================== warnings summary ===============================
tests/test_Filter.py::TestFilterByManufacture::test_filter_by_manufacture
  /usr/lib/python3.12/tarfile.py:2274: DeprecationWarning: Python 3.14 will, by default, filter extracted tar archives and reject files or modify their metadata. Use the filter argument to control this behavior.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ============================
FAILED tests/test_checkout.py::TestCheckout::test_login_checkout - AttributeError: 'CheckoutPage' object has no attribute 'PRODUCT_PAGE_CHECKOUT_BTN1'. Did you mean: 'CART_PAGE_CHECKOUT_BTN'?
FAILED tests/test_checkout.py::TestCheckout::test_register_checkout - AttributeError: 'CheckoutAction' object has no attribute 'open_home_and_add_product'
============= 2 failed, 19 passed, 1 warning in 250.13s (0:04:10) ==============
```
