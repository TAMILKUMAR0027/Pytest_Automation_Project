from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class FilterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    Manufacture=By.XPATH,"//label[@for='mz-fm-0-8']"
    iPodProduct=By.XPATH,"//div[@class='carousel-item active']//img[@title='iPod Touch']"
    filterDropDown=By.XPATH,"//select[@id='input-limit-212402']"
    allproducts=By.XPATH,"//div[@class='product-thumb']/descendant::h4"
    inStockOption=By.XPATH,"//label[@for='mz-fss-0--1']"
    canonProduct=By.XPATH,"//a[@id='mz-product-grid-image-30-212408']//div[@class='carousel-item active']//img[@title='Canon EOS 5D']"
    FilterSlider=By.XPATH,"//*[@id='mz-filter-panel-0-0']/div/div[1]/span[2]"
    price=By.XPATH,"//div[@id='mz-filter-panel-0-0']//input[@placeholder='Maximum Price']"
    outStockOption=By.XPATH,"//label[@for='mz-fss-0-5']"
    iPodProduct=By.XPATH,"//div[@class='carousel-item active']//img[@title='iPod Classic']"
    allProducts=By.XPATH,"//div[@class='product-thumb']//h4"