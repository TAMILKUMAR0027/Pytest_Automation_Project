from pages.AddOnspage import AddOnspage
from actions.BaseAction import BaseAction
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddOnsaction(BaseAction):
    def __init__(self,driver):
        super().__init__(driver)
        self.adp=AddOnspage(driver)

    def clickAddOns(self):
      addons = self.wait.until(EC.visibility_of_element_located(self.adp.AddOns))
      ActionChains(self.driver).move_to_element(addons).perform()
    def clickdesigns(self):
       self.click(self.adp.designs)
    def clickDrawerleft(self):
       self.scroll_into_view(self.adp.Drawerleft)
       self.click(self.adp.Drawerleft)
    def leftpanel(self):
        assert self.is_displayed(self.adp.topcategories)
    def clickDrawerright(self):
       self.scroll_into_view(self.adp.Drawerright)
       self.click(self.adp.Drawerright)
    def viewrightpanel(self):
       assert self.is_displayed(self.adp.rightpanel)