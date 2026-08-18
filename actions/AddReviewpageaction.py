from pages.Addreviewpage import Addreviewpage
from actions.BaseAction import BaseAction
from selenium.webdriver.common.by import By


class AddReviewpageaction(BaseAction):
    def __init__(self,driver):
        super().__init__(driver)
        self.arp=Addreviewpage(driver)

    def selectproduct(self):
         self.click(self.arp.product)
    def moveto_review(self):
        self.scroll_into_view(self.arp.reviewtab)
    def selectrating(self,rating):
         rating_locator = (By.CSS_SELECTOR, f"input[name='rating'][value='{rating}']")
         self.click(rating_locator)
    def enterName(self,name):
        self.send_keys(self.arp.reviewname,name)
    def enterfeedback(self,feedback):
        self.send_keys(self.arp.reviewtext,feedback)
    def clicksubmit(self):
        self.click(self.arp.writeReview)
    def successmsg(self,expectedMessage):
        actualMessage = self.get_text(self.arp.successMessage)
        print(actualMessage)
        assert expectedMessage in actualMessage
    def warningmsg(self,expectedMessage):
        actualMessage = self.get_text(self.arp.warningMessage)
        print(actualMessage)
        assert expectedMessage in actualMessage

