from actions.FilterPageAction import FilterPageAction
from actions.HomePageAction import HomePageAction
from actions.ProductPageAction import ProductPageAction


class TestInstockProduct:
    def test_instock_product(self,driver):
        drv,wait=driver
        hpa=HomePageAction(drv)
        fpa=FilterPageAction(drv)
        ppa=ProductPageAction(drv)
        hpa.clickShopByCategory()
        hpa.clickMonitor()
        fpa.clickInstockOption()
        fpa.clickCanonProduct()
        print(ppa.getInstock())
        