import pytest
from actions.HomePageAction import HomePageAction
from actions.ShopbycategoryAction import ShopByCategoryAction
from utils.loggerCreator import get_logger

logger = get_logger(__name__)

@pytest.mark.ShopByCategory
class TestShopByCategory:
    @pytest.mark.parametrize(
        "category, expected_title",
        [
            ("Desktops & Monitors", "Monitors"),
            ("Web Cameras", "Web Cameras"),
            ("Phone, Tablets & Ipod", "Tablets"),
            ("Laptops & Notebooks", "Laptops"),
        ]
    )
    def test_category_navigation(self, driver, category, expected_title):
        drv, wait = driver
        action = ShopByCategoryAction(drv)
        

        hpa = HomePageAction(drv)
       

        logger.info("Opening Shop By Category")
        hpa.clickShopByCategory()
        action.select_category(category)
        actual_title = action.get_page_title()

        assert expected_title in actual_title