from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class AddOnspage(BasePage):
    def __init__(self, driver):
       super().__init__(driver)

    AddOns=By.XPATH,"//span[normalize-space()='AddOns']"
    designs=By.XPATH,"//span[normalize-space()='Designs']"
    Drawerleft=By.XPATH,"//div[@id='entry_215006']/child::a"
    topcategories=By.XPATH,"//div[@id='mz-component-1626147655']/child::h5"
    Drawerright=By.XPATH,"//div[@id='entry_215007']/child::a"
    rightpanel=By.XPATH,"//div[@id='entry_215089']"




























