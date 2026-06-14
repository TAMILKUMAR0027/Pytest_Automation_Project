import pytest

from actions.HomePageAction import HomePageAction
from actions.ProductCompareAction import ProductCompareAction


class TestProductCompare:

    @pytest.mark.Tamil
    def test_product_compare(self, driver):
        drv, wait = driver

        hpa = HomePageAction(drv)
        pca = ProductCompareAction(drv)

        hpa.click_CompareLink()

        actual_msg = pca.get_EmptyCompareMessage()
        expected_msg = "You have not chosen any products to compare."

        assert actual_msg == expected_msg, (
            f"Expected: {expected_msg}, but got: {actual_msg}"
        )