import pytest

from actions.FilterPageAction import FilterPageAction
from actions.HomePageAction import HomePageAction
from actions.ProductPageAction import ProductPageAction
from utils.loggerCreator import get_logger

logger = get_logger(__name__)


class TestFilterByManufacture:

    @pytest.mark.Tamil
    def test_filter_by_manufacture(self, driver):
        drv, wait = driver

        hpa = HomePageAction(drv)
        fpa = FilterPageAction(drv)
        ppa = ProductPageAction(drv)

        logger.info("Opening Shop By Category")
        hpa.clickShopByCategory()

        logger.info("Opening Monitor Category")
        hpa.clickMonitor()

        logger.info("Applying Manufacturer Filter")
        fpa.clickManufactureBrand()

        logger.info("Opening iPod Product")
        fpa.clickiPodProduct()

        brand = ppa.getBrand()

        logger.info(f"Brand Found: {brand}")
        print("Brand:", brand)

        assert brand, "Brand value is empty"

    @pytest.mark.Tamil
    def test_instock_product(self, driver):
        drv, wait = driver

        hpa = HomePageAction(drv)
        fpa = FilterPageAction(drv)
        ppa = ProductPageAction(drv)

        logger.info("Opening Shop By Category")
        hpa.clickShopByCategory()

        logger.info("Opening Monitor Category")
        hpa.clickMonitor()

        logger.info("Applying In Stock Filter")
        fpa.clickInstockOption()

        logger.info("Opening Canon Product")
        fpa.clickCanonProduct()

        availability = ppa.getInstock()

        logger.info(f"Availability: {availability}")
        print("Availability:", availability)

        assert "In Stock" in availability, \
            f"Expected 'In Stock' but got '{availability}'"

    @pytest.mark.Tamil
    def test_filter_by_price(self, driver):
        drv, wait = driver

        hpa = HomePageAction(drv)
        fpa = FilterPageAction(drv)

        logger.info("Opening Shop By Category")
        hpa.clickShopByCategory()

        logger.info("Opening Monitor Category")
        hpa.clickMonitor()

        logger.info("Moving Price Slider")
        fpa.movePriceSlider()

        price = int(fpa.getPriceValue())

        logger.info(f"Filtered Price: {price}")
        print("Price:", price)

        assert price < 2000, \
            f"Price filter failed. Actual Price: {price}"

    @pytest.mark.Tamil
    def test_filter_By_inStock_and_OutStock(self, driver):
        drv, wait = driver

        hpa = HomePageAction(drv)
        fpa = FilterPageAction(drv)
        ppa = ProductPageAction(drv)

        logger.info("Opening Shop By Category")
        hpa.clickShopByCategory()

        logger.info("Opening Monitor Category")
        hpa.clickMonitor()

        logger.info("Applying Out Of Stock Filter")
        fpa.clickOutOfStockOption()

        logger.info("Opening iPod Product")
        fpa.clickiPodProduct()

        availability = ppa.getOutStock()

        logger.info(f"Availability: {availability}")
        print("Availability:", availability)

        assert "Out Of Stock" in availability, \
            f"Expected 'Out Of Stock' but got '{availability}'"