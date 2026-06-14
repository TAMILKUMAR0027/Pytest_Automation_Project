import pytest
from utils.configReader import ConfigReader
from actions.HomePageAction import HomePageAction
from actions.AddReviewpageaction import AddReviewpageaction
from utils.excelReader import get_data
from utils import loggerCreator

logger = loggerCreator.get_logger(__name__)


@pytest.mark.Jothika
class TestAddreview:

    @pytest.mark.parametrize(
        "rating,name,feedback,expectedMessage",
        get_data(
            "data_provider/DataProvider.xlsx",
            "AddReview-valid",
        ),
    )
    def test_validAddreview(self,driver,rating,name,feedback,expectedMessage):
        drv, wait = driver
        self.arpa=AddReviewpageaction(drv)

        url=ConfigReader.get_url()
        logger.info("Application launch is successful")
        self.arpa.selectproduct()
        logger.info("Selected the product")
        self.arpa.moveto_review()
        logger.info("Found review page")
        self.arpa.selectrating(rating)
        logger.info("Selected Rating")
        self.arpa.enterName(name)
        logger.info("Entered reviewer name")
        self.arpa.enterfeedback(feedback)
        logger.info("Entered feedback")
        self.arpa.clicksubmit()
        logger.info("Submitted review")
        self.arpa.successmsg(expectedMessage)
        logger.info("Review added successfully")

    @pytest.mark.parametrize(
        "rating,expectedMessage",
        get_data(
            "data_provider/DataProvider.xlsx",
            "AddReview-rating",
        ),
    )

    def test_withrating(self,driver,rating,expectedMessage):
          drv, wait = driver
          self.arpa=AddReviewpageaction(drv)
          url=ConfigReader.get_url()
          logger.info("Application launch is successful")
          self.arpa.selectproduct()
          logger.info("Selected the product")
          self.arpa.moveto_review()
          logger.info("Found review page")
          self.arpa.selectrating(rating)
          logger.info("Selected Rating")
          self.arpa.clicksubmit()
          logger.info("Submitted review")
          self.arpa.warningmsg(expectedMessage)
          logger.info("Invalid review submitted successfully")

    @pytest.mark.parametrize(
        "rating,name,feedback,expectedMessage",
        get_data(
            "data_provider/DataProvider.xlsx",
            "AddReview-withoutname",
        ),
    )

    def test_withoutname(self,driver,rating,name,feedback,expectedMessage):
          drv, wait = driver
          self.arpa=AddReviewpageaction(drv)
          url=ConfigReader.get_url()
          logger.info("Application launch is successful")
          self.arpa.selectproduct()
          logger.info("Selected the product")
          self.arpa.moveto_review()
          logger.info("Found review page")
          self.arpa.selectrating(rating)
          logger.info("Selected Rating")
          self.arpa.enterName(name)
          logger.info("Entered empty name")
          self.arpa.enterfeedback(feedback)
          logger.info("Entered feedback")
          self.arpa.clicksubmit()
          logger.info("Submitted review")
          self.arpa.warningmsg(expectedMessage)
          logger.info("Invalid review withoutname submitted successfully")


    @pytest.mark.parametrize(
        "rating,name,expectedMessage",
        get_data(
            "data_provider/DataProvider.xlsx",
            "AddReview-withoutfeedback",
        ),
    )

    def test_addingreviewwithoutfeedback(self,driver,rating,name,expectedMessage):
          drv, wait = driver
          self.arpa=AddReviewpageaction(drv)
          url=ConfigReader.get_url()
          logger.info("Application launch is successful")
          self.arpa.selectproduct()
          logger.info("Selected the product")
          self.arpa.moveto_review()
          logger.info("Found review page")
          self.arpa.selectrating(rating)
          logger.info("Selected Rating")
          self.arpa.enterName(name)
          logger.info("Entered name")
          
          self.arpa.clicksubmit()
          logger.info("Submitted review")
          self.arpa.warningmsg(expectedMessage)
          logger.info("Invalid review withoutfeedback submitted successfully")

          
    @pytest.mark.parametrize(
        "name,feedback,expectedMessage",
        get_data(
            "data_provider/DataProvider.xlsx",
            "AddReview-withoutrating",
        ),
    )

    def test_reviewwithoutrating(self,driver,name,feedback,expectedMessage):
          drv, wait = driver
          self.arpa=AddReviewpageaction(drv)
          url=ConfigReader.get_url()
          logger.info("Application launch is successful")
          self.arpa.selectproduct()
          logger.info("Selected the product")
          self.arpa.moveto_review()
          logger.info("Found review page")
         
          self.arpa.enterName(name)
          logger.info("Entered empty name")
          self.arpa.enterfeedback(feedback)
          logger.info("Entered feedback")
          self.arpa.clicksubmit()
          logger.info("Submitted review")
          self.arpa.warningmsg(expectedMessage)
          logger.info("Invalid review withoutrating submitted successfully")

          






