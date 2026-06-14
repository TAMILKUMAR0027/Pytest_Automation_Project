![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Allure](https://img.shields.io/badge/Allure-E6E6E6?style=for-the-badge&logo=allure&logoColor=black)
![Pytest HTML](https://img.shields.io/badge/Pytest_HTML-009688?style=for-the-badge)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)

# Pytest Selenium Automation Framework

A scalable and maintainable UI automation framework built using **Python, Selenium WebDriver, and Pytest** for the **LambdaTest Ecommerce Playground**. This project was developed for learning and implementing modern test automation practices using industry-standard design patterns and tools.

---

## Features

* Cross-browser support (Chrome & Firefox)
* Headless and Normal execution modes
* Page Object Model (POM) design pattern
* Centralized configuration management using `config.ini`
* Automatic driver management with `webdriver-manager`
* Explicit and configurable wait strategies
* Structured logging and debugging support
* Pytest markers for selective test execution
* Allure Reporting integration
* Pytest HTML Reporting
* Parallel execution support using `pytest-xdist`
* CI/CD ready for GitHub Actions and Jenkins

---

## Application Under Test

**LambdaTest Ecommerce Playground**

https://ecommerce-playground.lambdatest.io/

---

## Tech Stack

| Technology         | Purpose              |
| ------------------ | -------------------- |
| Python 3.x         | Programming Language |
| Selenium WebDriver | Browser Automation   |
| Pytest             | Test Framework       |
| WebDriver Manager  | Driver Management    |
| Allure Reports     | Advanced Reporting   |
| Pytest HTML        | HTML Reporting       |
| Logging            | Test Execution Logs  |

---

## Project Structure

```text
Pytest_Automation_Project
│
├── configuration/          # Configuration files
├── pages/                  # Page Object Classes
├── tests/                  # Test Cases
├── utils/                  # Utility Classes
├── actions/                # Reusable Actions
├── data_provider/          # Test Data
├── logs/                   # Log Files
├── reports/                # Generated Reports
├── conftest.py             # Fixtures & Driver Setup
├── pytest.ini              # Pytest Configuration
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd Pytest_Automation_Project
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Update the `configuration/config.ini` file:

```ini
[browser]
browser = firefox
mode = normal

[application]
url = https://ecommerce-playground.lambdatest.io/index.php?route=common/home
title = Your Store

[timeouts]
implicit_wait = 10
explicit_wait = 15
page_load_timeout = 30
```

---

## Running Tests

### Run All Tests

```bash
pytest
```

### Verbose Execution

```bash
pytest -v
```

### Run Specific Test File

```bash
pytest tests/test_launch.py -v
```

### Run Using Markers

```bash
pytest -m smoke
pytest -m regression
pytest -m sanity
pytest -m "sanity and regression"
```

---

## Parallel Execution

Run tests using multiple workers:

```bash
pytest -n 4
```

---

## Generate Reports

### Pytest HTML Report

```bash
pytest --html=reports/report.html --self-contained-html
```

### Allure Report

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

---

## Sample Test Structure

```python
@pytest.mark.smoke
@pytest.mark.regression
def test_homepage_verification(driver):
    drv, wait = driver

    # Test Logic Here
```

---

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Follow the existing POM structure
4. Add proper logging and assertions
5. Test changes in Chrome and Firefox
6. Submit a Pull Request

---

## Future Enhancements

* API Testing Integration
* Docker Execution Support
* Cloud Execution (LambdaTest / BrowserStack)
* Data-Driven Testing with Excel and JSON
* Advanced Reporting Dashboard
* Test Analytics Integration

---

## Contributors

* Tamil Kumar
* Prasanna Venkatesh K
* Rishwanth
* Samiha
* Jothika

---

## License

This project is intended for learning and educational purposes.

---

Built with Python, Selenium, and Pytest for modern UI test automation.

Happy Testing! 🚀
