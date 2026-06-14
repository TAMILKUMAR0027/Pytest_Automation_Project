from actions.AddOnspageaction import AddOnsaction
import pytest
from utils import loggerCreator
from utils.configReader import ConfigReader


logger = loggerCreator.get_logger(__name__)

@pytest.mark.Jothika
class TestAddOns:

    def test_addonsdrawerleft(self,driver):
         drv, wait = driver
         self.adpa=AddOnsaction(drv)

         url=ConfigReader.get_url()
         logger.info("Application launched successfully")
         self.adpa.clickAddOns()
         logger.info("Moved to Addons")
         self.adpa.clickdesigns()
         logger.info("Clicked on designs")
         self.adpa.clickDrawerleft()
         logger.info("Selected drawerleft")
         self.adpa.leftpanel()
         logger.info("left panel is displayed")

    def test_drawerRight(self,driver):  
         drv, wait = driver
         self.adpa=AddOnsaction(drv)

         url=ConfigReader.get_url()
         logger.info("Application launched successfully")
         self.adpa.clickAddOns()
         logger.info("Moved to Addons")
         self.adpa.clickdesigns()
         logger.info("Clicked on designs")
         self.adpa.clickDrawerright()
         logger.info("Clicked on drawer right")
         self.adpa.viewrightpanel()
         logger.info("Right panel appeared")



