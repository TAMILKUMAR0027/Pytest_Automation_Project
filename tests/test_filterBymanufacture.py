import pytest

from actions.FilterPageAction import FilterPageAction
from actions.HomePageAction import HomePageAction
from actions.ProductPageAction import ProductPageAction


class TestFilterByManufacture:

    @pytest.mark.Tamil
    def test_filter_by_manufacture(self, driver):
        drv, wait = driver

        hpa = HomePageAction(drv)
        fpa = FilterPageAction(drv)
        ppa = ProductPageAction(drv)

        hpa.clickShopByCategory()
        hpa.clickMonitor()
        fpa.clickManufactureBrand()
        fpa.clickiPodProduct()

        print(ppa.getBrand())