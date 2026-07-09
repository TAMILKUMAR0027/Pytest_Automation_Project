import pytest

from actions.HomePageAction import HomePageAction
from actions.ProductCompareAction import ProductCompareAction
from actions.ProductPageAction import ProductPageAction

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
    @pytest.mark.Tamil
    def test_compare_product(self, driver):
        drv, wait = driver

        hpa = HomePageAction(drv)
        ppa = ProductPageAction(drv)

        # Select Canon EOS 5D product from home page
        hpa.click_CanonProduct()

        # Click Compare this Product
        ppa.click_CompareButton()

        # Verify success message
        actual_msg = ppa.get_CompareSuccessMessage()

        expected_msg = "Success: You have added Canon EOS 5D to your product comparison!"

        assert expected_msg in actual_msg, (
            f"Expected: {expected_msg}, but got: {actual_msg}"
        )