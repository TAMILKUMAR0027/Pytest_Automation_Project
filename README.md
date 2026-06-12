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
tests/test_wishlist.py ......                                            [100%]

=================================== FAILURES ===================================
____________ TestCheckout.test_guest_checkout_with_new_address_cod _____________

self = <tests.test_checkout.TestCheckout object at 0x7f81d04d3020>
driver = (<selenium.webdriver.chrome.webdriver.WebDriver (session="055167e48aa94bf2fa4a822f637ccee2")>, <selenium.webdriver.support.wait.WebDriverWait (session="055167e48aa94bf2fa4a822f637ccee2")>)

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
>       action.select_cash_on_delivery()

tests/test_checkout.py:30: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
actions/checkoutAction.py:86: in select_cash_on_delivery
    self.click(self.cp.COD_LABEL)
actions/BaseAction.py:23: in click
    element.click()
../../../.local/lib/python3.12/site-packages/selenium/webdriver/remote/webelement.py:114: in click
    self._execute(Command.CLICK_ELEMENT)
../../../.local/lib/python3.12/site-packages/selenium/webdriver/remote/webelement.py:508: in _execute
    return self._parent.execute(command, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
../../../.local/lib/python3.12/site-packages/selenium/webdriver/remote/webdriver.py:468: in execute
    self.error_handler.check_response(response)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <selenium.webdriver.remote.errorhandler.ErrorHandler object at 0x7f81ca9b4500>
response = {'status': 404, 'value': '{"value":{"error":"stale element reference","message":"stale element reference: stale elemen...\n#19 0x55abb90d6e1e \u003Cunknown>\n#20 0x7f1b0ae9caa4 \u003Cunknown>\n#21 0x7f1b0af29c6c \u003Cunknown>\n"}}'}

    def check_response(self, response: dict[str, Any]) -> None:
        """Check that a JSON response from the WebDriver does not have an error.
    
        Args:
            response: The JSON response from the WebDriver server as a dictionary
                object.
    
        Raises:
            WebDriverException: If the response contains an error message.
        """
        status = response.get("status", None)
        if not status or status == ErrorCode.SUCCESS:
            return
        value = None
        message = response.get("message", "")
        screen: str = response.get("screen", "")
        stacktrace = None
        if isinstance(status, int):
            value_json = response.get("value", None)
            if value_json and isinstance(value_json, str):
                try:
                    value = json.loads(value_json)
                    if isinstance(value, dict):
                        if len(value) == 1:
                            value = value["value"]
                        status = value.get("error", None)
                        if not status:
                            status = value.get("status", ErrorCode.UNKNOWN_ERROR)
                            message = value.get("value") or value.get("message")
                            if not isinstance(message, str):
                                value = message
                                message = message.get("message") if isinstance(message, dict) else None
                        else:
                            message = value.get("message", None)
                except ValueError:
                    pass
    
        exception_class: type[WebDriverException]
        e = ErrorCode()
        error_codes = [item for item in dir(e) if not item.startswith("__")]
        for error_code in error_codes:
            error_info = getattr(ErrorCode, error_code)
            if isinstance(error_info, list) and status in error_info:
                exception_class = getattr(ExceptionMapping, error_code, WebDriverException)
                break
        else:
            exception_class = WebDriverException
    
        if not value:
            value = response["value"]
        if isinstance(value, str):
            raise exception_class(value)
        if message == "" and "message" in value:
            message = value["message"]
    
        screen = None  # type: ignore[assignment]
        if "screen" in value:
            screen = value["screen"]
    
        stacktrace = None
        st_value = value.get("stackTrace") or value.get("stacktrace")
        if st_value:
            if isinstance(st_value, str):
                stacktrace = st_value.split("
")
            else:
                stacktrace = []
                try:
                    for frame in st_value:
                        line = frame.get("lineNumber", "")
                        file = frame.get("fileName", "<anonymous>")
                        if line:
                            file = f"{file}:{line}"
                        meth = frame.get("methodName", "<anonymous>")
                        if "className" in frame:
                            meth = f"{frame['className']}.{meth}"
                        msg = "    at %s (%s)"
                        msg = msg % (meth, file)
                        stacktrace.append(msg)
                except TypeError:
                    pass
        if exception_class == UnexpectedAlertPresentException:
            alert_text = None
            if "data" in value:
                alert_text = value["data"].get("text")
            elif "alert" in value:
                alert_text = value["alert"].get("text")
            raise exception_class(message, screen, stacktrace, alert_text)
>       raise exception_class(message, screen, stacktrace)
E       selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: stale element not found in the current frame
E         (Session info: chrome=149.0.7827.53); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
E       Stacktrace:
E       #0 0x55abb90d829a <unknown>
E       #1 0x55abb8aba449 <unknown>
E       #2 0x55abb8ac162b <unknown>
E       #3 0x55abb8ac3eab <unknown>
E       #4 0x55abb8ac3f53 <unknown>
E       #5 0x55abb8b10d83 <unknown>
E       #6 0x55abb8b0ffea <unknown>
E       #7 0x55abb8b04072 <unknown>
E       #8 0x55abb8b039b7 <unknown>
E       #9 0x55abb8b56cbf <unknown>
E       #10 0x55abb8b02132 <unknown>
E       #11 0x55abb8b02f41 <unknown>
E       #12 0x55abb909e737 <unknown>
E       #13 0x55abb909cf39 <unknown>
E       #14 0x55abb9087c26 <unknown>
E       #15 0x55abb909dada <unknown>
E       #16 0x55abb906fbd0 <unknown>
E       #17 0x55abb90c4c28 <unknown>
E       #18 0x55abb90c4dc5 <unknown>
E       #19 0x55abb90d6e1e <unknown>
E       #20 0x7f1b0ae9caa4 <unknown>
E       #21 0x7f1b0af29c6c <unknown>

../../../.local/lib/python3.12/site-packages/selenium/webdriver/remote/errorhandler.py:232: StaleElementReferenceException
---------------------------- Captured stderr setup -----------------------------
2026-06-12 07:50:05  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-12 07:50:05  INFO      conftest  Chrome Browser Launched Successfully
2026-06-12 07:50:05  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-12 07:50:06  INFO      conftest  Driver started → browser=chrome | mode=headless
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:62 Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:119 Chrome Browser Launched Successfully
INFO     conftest:conftest.py:175 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:184 Driver started → browser=chrome | mode=headless
--------------------------- Captured stderr teardown ---------------------------
2026-06-12 07:50:26  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:196 Quitting driver.
_______________ TestCheckout.test_checkout_with_register_account _______________

self = <tests.test_checkout.TestCheckout object at 0x7f81d04d3590>
driver = (<selenium.webdriver.chrome.webdriver.WebDriver (session="f68d38624aa1e613152eb955c74e3088")>, <selenium.webdriver.support.wait.WebDriverWait (session="f68d38624aa1e613152eb955c74e3088")>)

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
E        +    where is_checkout_or_login_page_displayed = <actions.checkoutAction.CheckoutAction object at 0x7f81d0263860>.is_checkout_or_login_page_displayed

tests/test_checkout.py:62: AssertionError
---------------------------- Captured stderr setup -----------------------------
2026-06-12 07:50:27  INFO      conftest  Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-12 07:50:27  INFO      conftest  Chrome Browser Launched Successfully
2026-06-12 07:50:27  INFO      conftest  Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
2026-06-12 07:50:28  INFO      conftest  Driver started → browser=chrome | mode=headless
------------------------------ Captured log setup ------------------------------
INFO     conftest:conftest.py:62 Config → browser=chrome | mode=headless | url=https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:119 Chrome Browser Launched Successfully
INFO     conftest:conftest.py:175 Launching URL: https://ecommerce-playground.lambdatest.io/index.php?route=common/home
INFO     conftest:conftest.py:184 Driver started → browser=chrome | mode=headless
--------------------------- Captured stderr teardown ---------------------------
2026-06-12 07:50:45  INFO      conftest  Quitting driver.
---------------------------- Captured log teardown -----------------------------
INFO     conftest:conftest.py:196 Quitting driver.
=========================== short test summary info ============================
FAILED tests/test_checkout.py::TestCheckout::test_guest_checkout_with_new_address_cod - selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=149.0.7827.53); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
#0 0x55abb90d829a <unknown>
#1 0x55abb8aba449 <unknown>
#2 0x55abb8ac162b <unknown>
#3 0x55abb8ac3eab <unknown>
#4 0x55abb8ac3f53 <unknown>
#5 0x55abb8b10d83 <unknown>
#6 0x55abb8b0ffea <unknown>
#7 0x55abb8b04072 <unknown>
#8 0x55abb8b039b7 <unknown>
#9 0x55abb8b56cbf <unknown>
#10 0x55abb8b02132 <unknown>
#11 0x55abb8b02f41 <unknown>
#12 0x55abb909e737 <unknown>
#13 0x55abb909cf39 <unknown>
#14 0x55abb9087c26 <unknown>
#15 0x55abb909dada <unknown>
#16 0x55abb906fbd0 <unknown>
#17 0x55abb90c4c28 <unknown>
#18 0x55abb90c4dc5 <unknown>
#19 0x55abb90d6e1e <unknown>
#20 0x7f1b0ae9caa4 <unknown>
#21 0x7f1b0af29c6c <unknown>
FAILED tests/test_checkout.py::TestCheckout::test_checkout_with_register_account - assert False
 +  where False = is_checkout_or_login_page_displayed()
 +    where is_checkout_or_login_page_displayed = <actions.checkoutAction.CheckoutAction object at 0x7f81d0263860>.is_checkout_or_login_page_displayed
=================== 2 failed, 16 passed in 177.57s (0:02:57) ===================
```
