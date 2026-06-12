from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class Forgetpasswordpage(BasePage):
    def __init__(self, driver):
       super().__init__(driver)
    forgetpassword=(By.XPATH,"//label[@for='input-password']/following-sibling::a")
    login=(By.XPATH,"//a[@class='icon-left both dropdown-item active']/descendant::span")
    email=(By.XPATH,"//div[@class='col-sm-10']/child::input")
    button=(By.XPATH,"//div[@class='float-right']/child::button")
    message=(By.XPATH,"//div[@class='row']/preceding-sibling::div")
    warningmsg=(By.XPATH,"//div[@id='account-forgotten']/child::div[1]")


