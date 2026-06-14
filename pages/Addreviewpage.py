from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class Addreviewpage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
    
    product=(By.XPATH , "//a[@id='mz-product-listing-image-39218404-0-1']//div[@class='carousel-item active']//img[@title='HTC Touch HD']")
    reviewtab=(By.XPATH ,"//a[contains(text(),'Reviews')]")
    
    reviewname=	(By.CSS_SELECTOR,"input#input-name")
    reviewtext=	(By.XPATH,"//div[@class='form-group required']/child::textarea")
    writeReview=(By.XPATH , "//button[text()='Write Review']")
    successMessage=(By.XPATH,"//div[contains(@class,'alert-success')]")
    warningMessage =(By.XPATH,"//div[contains(@class,'alert-danger')]")
	

