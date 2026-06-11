import time

import pytest

from actions.FilterPageAction import FilterPageAction
from actions.HomePageAction import HomePageAction
from actions.ProductPageAction import ProductPageAction


class TestFilter_By_Price:

    @pytest.mark.Tamil
    def test_filter_by_price(self, driver):
        drv, wait = driver

        hpa = HomePageAction(drv)
        fpa = FilterPageAction(drv)
        ppa = ProductPageAction(drv)
        hpa.clickShopByCategory()
        hpa.clickMonitor()
        fpa.movePriceSlider()
        assert 2000>int(fpa.getPriceValue())