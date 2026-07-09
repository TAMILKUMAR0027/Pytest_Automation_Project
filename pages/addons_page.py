from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class AddOnsPage:

    ADDONS_LINK = (By.XPATH, "//span[normalize-space()='AddOns']")
    WIDGETS_BUTTON = (By.XPATH, "//span[normalize-space()='Widgets']")

    NAME_FIELD = (By.NAME, "name")
    EMAIL_FIELD = (By.NAME, "email")
    SUBJECT_FIELD = (By.NAME, "subject")
    MESSAGE_FIELD = (By.NAME, "enquiry")

    SUBMIT_BUTTON = (By.XPATH, "//input[@value='Submit']")
    SUCCESS_MESSAGE = (
        By.XPATH,
        "//*[contains(text(),'Your enquiry has been successfully sent to the store owner!')]"
    )
    EMAIL_ERROR_MESSAGE = (
        By.XPATH,
        "//*[contains(text(),'E-Mail Address does not appear to be valid')]"
    )

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def click_addons_link(self):
        self.wait.until(EC.element_to_be_clickable(self.ADDONS_LINK)).click()

    def click_widgets_button(self):
        self.wait.until(EC.element_to_be_clickable(self.WIDGETS_BUTTON)).click()

    def enter_name(self, name):
        element = self.wait.until(EC.visibility_of_element_located(self.NAME_FIELD))
        element.clear()
        element.send_keys(name)

    def enter_email(self, email):
        element = self.wait.until(EC.visibility_of_element_located(self.EMAIL_FIELD))
        element.clear()
        element.send_keys(email)

    def enter_subject(self, subject):
        element = self.wait.until(EC.visibility_of_element_located(self.SUBJECT_FIELD))
        element.clear()
        element.send_keys(subject)

    def enter_message(self, message):
        element = self.wait.until(EC.visibility_of_element_located(self.MESSAGE_FIELD))
        element.clear()
        element.send_keys(message)

    def click_submit(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    def get_success_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        ).text.strip().replace("x", "")

    def get_email_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.EMAIL_ERROR_MESSAGE)
        ).text.strip()