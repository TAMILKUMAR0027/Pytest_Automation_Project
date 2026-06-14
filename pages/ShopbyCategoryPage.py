from selenium.webdriver.common.by import By

class ShopByCategoryPage:

    SHOP_BY_CATEGORY_MENU = (By.XPATH, "//a[contains(.,'Shop by Category')]")
    DESKTOPS_CATEGORY = (By.XPATH, "//span[normalize-space()='Desktops and Monitors']")
    CAMERAS = (By.XPATH, "//span[normalize-space()='Web Cameras']")
    TABLETS = (By.XPATH, "//span[normalize-space()='Phone, Tablets & Ipod']")
    LAPTOPS = (By.XPATH, "//span[normalize-space()='Laptops & Notebooks']")