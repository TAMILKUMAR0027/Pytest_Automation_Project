from actions.BaseAction import BaseAction
from pages.ComaprePage import ComparePage


class ProductCompareAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.pc = ComparePage(driver)

    def get_EmptyCompareMessage(self):
        return self.get_text(self.pc.Compare_Message)