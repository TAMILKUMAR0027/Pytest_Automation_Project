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

        logger.info("Brand Found: %s", brand)

        assert brand, "Brand value is empty"

        logger.info("Manufacturer filter validation passed")

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

        logger.info("Availability: %s", availability)

        assert "In Stock" in availability, \
            f"Expected 'In Stock' but got '{availability}'"

        logger.info("In Stock filter validation passed")

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

        logger.info("Filtered Price: %s", price)

        assert price < 2000, \
            f"Price filter failed. Actual Price: {price}"

        logger.info("Price filter validation passed")

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

        logger.info("Availability: %s", availability)

        assert "Out Of Stock" in availability, \
            f"Expected 'Out Of Stock' but got '{availability}'"

        logger.info("Out Of Stock filter validation passed")

    @pytest.mark.Tamil
    def test_list_of_product_By_FilterShow(self, driver):
        drv, wait = driver

        hpa = HomePageAction(drv)
        fpa = FilterPageAction(drv)

        logger.info("Opening Shop By Category")
        hpa.clickShopByCategory()

        logger.info("Opening Monitor Category")
        hpa.clickMonitor()

        logger.info("Selecting dropdown value: 15")
        fpa.selectDropDown()

        logger.info("Fetching displayed products")
        products = fpa.getAllProducts()

        all_products = []

        for product in products:
            product_name = product.text.strip()

            if product_name:
                all_products.append(product_name)
                logger.info("Product Found: %s", product_name)

        product_count = len(all_products)

        logger.info("Total Products Displayed: %s", product_count)

        print("Products:", all_products)

        assert product_count > 0, \
            "No products displayed after applying filter"

        # assert in the codde
        assert product_count == 25, \
            f"Expected maximum 15 products but found {product_count}"

        logger.info("Product list validation passed successfully")