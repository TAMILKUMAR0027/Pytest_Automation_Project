import pytest
from actions.ShopbycategoryAction import ShopByCategoryAction
from utils.loggerCreator import get_logger

logger = get_logger(__name__)

@pytest.mark.Samiha
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
        action.launch_url("https://ecommerce-playground.lambdatest.io")
        action.click_shop_by_category()
        action.select_category(category)
        actual_title = action.get_page_title()

        assert expected_title in actual_title
