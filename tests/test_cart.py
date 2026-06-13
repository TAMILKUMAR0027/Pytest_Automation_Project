import pytest
from actions.ProductPageAction import ProductPageAction
from actions.cartpageaction import CartPageAction
from actions.launch_actions import LaunchActions
from utils.configReader import ConfigReader
from utils.loggerCreator import get_logger

logger = get_logger(__name__)


@pytest.mark.Rishwanth
class TestCart:

    def test_single_product_add(self, driver):
        logger.info("Starting test: test_single_product_add")

        drv, wait = driver

        logger.info("Clicking top collection product")
        lp = LaunchActions(drv)
        lp.click_top_collection_product()

        logger.info("Adding product to cart")
        pp = ProductPageAction(drv)
        pp.click_add_to_cart()

        logger.info("Opening cart page")
        pp.click_view_cart()

        logger.info("Verifying single product added in cart")
        cpa = CartPageAction(drv)
        assert cpa.single_product_addCheck() is True

        logger.info("Test passed: Single product added successfully")

    def test_product_quantity_update(self, driver):
        logger.info("Starting test: test_product_quantity_update")

        drv, wait = driver

        q = ConfigReader.get_producct_quantity_update()
        logger.info(f"Quantity value taken from config: {q}")

        logger.info("Clicking top collection product")
        lp = LaunchActions(drv)
        lp.click_top_collection_product()

        logger.info("Adding product to cart")
        pp = ProductPageAction(drv)
        pp.click_add_to_cart()

        logger.info("Opening cart page")
        pp.click_view_cart()

        logger.info("Updating product quantity in cart")
        cpa = CartPageAction(drv)
        assert cpa.quantity_update_check(q) is True

        logger.info("Test passed: Product quantity updated successfully")
