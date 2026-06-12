from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseAction:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, locator, value):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_displayed(self, locator):
        try:
            return self.driver.find_element(*locator).is_displayed()
        except:
            return False

    def js_click(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_into_view(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def move_slider(self, locator, x_offset, y_offset=0):
        element = self.wait.until(EC.visibility_of_element_located(locator))

        ActionChains(self.driver) \
            .click_and_hold(element) \
            .move_by_offset(x_offset, y_offset) \
            .release() \
            .perform()
        
    def wait_for_page_load(self):
        self.long_wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def is_present(self, locator):
        return len(self.driver.find_elements(*locator)) > 0



    def get_input_value(self, locator):
      element = self.wait.until(EC.visibility_of_element_located(locator))
      return element.get_attribute("value")
    

    def get_elements_text(self, locator):
        elements = self.long_wait.until(
            EC.visibility_of_all_elements_located(locator)
        )
        return [el.text.strip() for el in elements if el.text.strip()]

    def dismiss_alert_if_present(self):
        try:
            alert = WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            text = alert.text
            alert.dismiss()
            return text
        except TimeoutException:
            return None