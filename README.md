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
collected 18 items / 1 error

==================================== ERRORS ====================================
_____________________ ERROR collecting tests/test_login.py _____________________
tests/test_login.py:13: in <module>
    class TestLogin:
tests/test_login.py:17: in TestLogin
    get_data(
utils/excelReader.py:7: in get_data
    Workbook = openpyxl.load_workbook(path)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
../../../.local/lib/python3.12/site-packages/openpyxl/reader/excel.py:346: in load_workbook
    reader = ExcelReader(filename, read_only, keep_vba,
../../../.local/lib/python3.12/site-packages/openpyxl/reader/excel.py:123: in __init__
    self.archive = _validate_archive(fn)
                   ^^^^^^^^^^^^^^^^^^^^^
../../../.local/lib/python3.12/site-packages/openpyxl/reader/excel.py:95: in _validate_archive
    archive = ZipFile(filename, 'r')
              ^^^^^^^^^^^^^^^^^^^^^^
/usr/lib/python3.12/zipfile/__init__.py:1347: in __init__
    self.fp = io.open(file, filemode)
              ^^^^^^^^^^^^^^^^^^^^^^^
E   FileNotFoundError: [Errno 2] No such file or directory: 'data_provider/DataProvider.xlsx'
=========================== short test summary info ============================
ERROR tests/test_login.py - FileNotFoundError: [Errno 2] No such file or directory: 'data_provider/DataProvider.xlsx'
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.26s ===============================
```
