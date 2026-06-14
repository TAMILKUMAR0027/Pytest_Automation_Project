from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from pages.newsletterpage import NewsLetterPage
from actions.BaseAction import BaseAction


class NewsLetterPageAction(BaseAction):
    def __init__(self, driver):
        super().__init__(driver)
        self.nlp = NewsLetterPage(driver)

    def click_yes_on_subscribe_rb(self):
        try:
            self.click(self.nlp.yesRadioButton)
        except:
            self.click(self.nlp.noRadioButton)
        self.click(self.nlp.continueButton)
