from pages.Addreviewpage import Addreviewpage
from actions.BaseAction import BaseAction


class AddReviewpageaction(BaseAction):
    def __init__(self,driver):
        super().__init__(driver)
        self.arp=Addreviewpage(driver)

    def selectproduct(self):
         self.click(self.arp.product)
    def moveto_review(self):
        self.scroll_into_view(self.arp.reviewtab)
    def selectrating(self):
        self.
