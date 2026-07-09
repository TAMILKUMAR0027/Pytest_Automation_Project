from selenium.webdriver.common.by import By

class ShopByCategoryPage:

    SHOP_BY_CATEGORY_MENU = (By.XPATH, "//button[contains(.,'Shop by Category')] | //a[contains(.,'Shop by Category')]")
    DESKTOPS_CATEGORY = (By.XPATH, "//span[@class='title' and normalize-space()='Desktops and Monitors']")
    CAMERAS = (By.LINK_TEXT, "Web Cameras")
    TABLETS = (By.LINK_TEXT, "Phone, Tablets & Ipod")
    LAPTOPS = (By.LINK_TEXT, "Laptops & Notebooks")