"""
Search page locators.

No Page Object class — raw (By, value) tuples consumed directly
by BaseAction helper methods.
"""

from selenium.webdriver.common.by import By

# ─── Search Bar ───────────────────────────────────────────────────────────────

SEARCH_BAR = (
    By.XPATH,
    "//div[@id='entry_217822']//input[@placeholder='Search For Products']",
)

# ─── Result Cards ─────────────────────────────────────────────────────────────

RESULT_CARDS = (
    By.XPATH,
    "//div[@id='entry_212469']//div[contains(@class,'product-thumb')]//h4/a",
)

# ─── No-Results Message ───────────────────────────────────────────────────────

NO_RESULT_MSG = (
    By.XPATH,
    "//div[@id='entry_212469']//p",
)

# ─── Manufacturer Label ───────────────────────────────────────────────────────

MANUFACTURER_LABEL = (
    By.XPATH,
    "//div[@class='mz-filter-value both ']//label",
)