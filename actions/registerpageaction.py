import time

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from actions.BaseAction import BaseAction
from pages.registerpage import RegisterPage


class RegisterPageAction(BaseAction):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.rp = RegisterPage(driver)

    def enter_register_credentials(self, fname, lname, telephone, password, cpassword):

        self.wait.until(ec.visibility_of_element_located(self.rp.fname)).send_keys(
            fname
        )

        self.email = f"test{int(time.time())}@gmail.com"

        self.driver.find_element(*self.rp.lname).send_keys(lname)
        self.driver.find_element(*self.rp.email).send_keys(self.email)
        self.driver.find_element(*self.rp.telephone).send_keys(telephone)
        self.driver.find_element(*self.rp.password).send_keys(password)
        self.driver.find_element(*self.rp.cpassword).send_keys(cpassword)

        self.click(self.rp.privacyCB)
        self.click(self.rp.regContinue)

        print("Generated Email:", self.email)
