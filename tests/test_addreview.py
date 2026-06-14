import pytest
from utils.configReader import ConfigReader
from actions.HomePageAction import HomePageAction
from actions.AddReviewpageaction import AddReviewpageaction
from utils.excelReader import get_data
from utils.loggerCreator import get_logger

logger = get_logger(__name__)


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
        self.arpa.moveto_review()
        self.arpa.selectrating(rating)
        self.arpa.enterName(name)
        self.arpa.enterfeedback(feedback)
        self.arpa.clicksubmit()

