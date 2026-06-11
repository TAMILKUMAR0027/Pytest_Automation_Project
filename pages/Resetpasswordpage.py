import logging
from selenium import webdriver
from selenium.webdriver.common.by import By


class ResetPasswordPage:
    def __init__(self, driver):
        self.driver = driver
forgetpassword=(By.XPATH,"//label[@for='input-password']/following-sibling::a")
email=(By.XPATH,"//div[@class='col-sm-10']/child::input")
button=(By.XPATH,"//div[@class='float-right']/child::button")
message=(By.XPATH,"//div[@class='row']/preceding-sibling::div")
warningmsg=(By.XPATH,"//div[@id='account-forgotten']/child::div[1]")


