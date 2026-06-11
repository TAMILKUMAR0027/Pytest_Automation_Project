from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from pages.registerpage import RegisterPage


class RegisterPageAction:
    def __int__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.rp = RegisterPage()

    def enter_register_credentials(
        self, fname, lname, email, telephone, password, cpassword
    ):
        self.wait.until(ec.visibility_of_element_located(self.rp.fname)).send_keys(
            fname
        )
        self.driver.find_element(*self.rp.lname).send_keys(lname)
        self.driver.find_element(*self.rp.email).send_keys(email)
        self.driver.find_element(*self.rp.telephone).send_keys(telephone)
        self.driver.find_element(*self.rp.password).send_keys(password)
        self.driver.find_element(*self.rp.cpassword).send_keys(cpassword)
        self.driver.find_element(*self.rp.privacyCB).click()
        self.driver.find_element(*self.rp.regContinue).click()
