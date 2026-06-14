import pytest
import logging

from actions.FilterPageAction import FilterPageAction
from actions.HomePageAction import HomePageAction
from actions.ProductPageAction import ProductPageAction
from utils import excelReader
from utils.csvDataProvider import CsvDataProvider


logger = logging.getLogger(__name__)


class TestProductPage:

    @pytest.mark.Tamil
    def test_validate_product_details(self, driver):
        drv, wait = driver
        logger.info("Starting test_validate_product_details")

        hpa = HomePageAction(drv)
        ppa = ProductPageAction(drv)

        csv_path = r"E:\Pytest_Automation\data_provider\ProductDataInformation.csv"
        data_list = CsvDataProvider.get_data(csv_path, None)
        data = data_list[0]

        hpa.click_HpProduct()

        actual_title = ppa.get_ProductTitle()
        actual_price = ppa.get_Product_price()
        actual_stock = ppa.getInstock()

        logger.info(f"Title: {actual_title}")
        logger.info(f"Price: {actual_price}")
        logger.info(f"Stock: {actual_stock}")

        assert actual_title == data["title"]
        assert str(actual_price) == data["price"]
        assert actual_stock == data["availability"]

        logger.info("test_validate_product_details PASSED")

    @pytest.mark.Tamil
    @pytest.mark.parametrize("qty", [1, 2, 3])
    def test_quantity_update_in_ProductPage(self, driver, qty):
        drv, wait = driver
        logger.info(f"Starting quantity test with qty={qty}")

        hpa = HomePageAction(drv)
        ppa = ProductPageAction(drv)

        hpa.click_HpProduct()
        ppa.setQuantity(qty)
        ppa.click_add_to_cart()
        ppa.click_view_cart()

        actual_qty = ppa.get_Product_Quantity()

        logger.info(f"Expected Qty={qty}, Actual Qty={actual_qty}")

        assert str(actual_qty) == str(qty)

    @pytest.mark.Tamil
    def test_Ask_question_ProductPage(self, driver):
        drv, wait = driver
        logger.info("Starting Ask Question test")

        hpa = HomePageAction(drv)
        ppa = ProductPageAction(drv)

        excel_path = r"E:\Pytest_Automation\data_provider\DataProvider.xlsx"
        data_list = excelReader.get_data(excel_path, "EnquiryData")
        data = data_list[0]

        name = data[0]
        email = data[1]
        subject = data[2]
        message = data[3]

        hpa.click_HpProduct()
        ppa.click_ask_question()

        ppa.set_name(name)
        ppa.set_email(email)
        ppa.set_subject(subject)
        ppa.set_message(message)

        ppa.click_send_message()

        actual_msg = ppa.get_submission_message()
        expected_msg = "Your enquiry has been successfully sent to the store owner!"

        logger.info(f"Actual Message: {actual_msg}")

        assert expected_msg in actual_msg

    @pytest.mark.Tamil
    def test_Invalid_Ask_question_ProductPage(self, driver):
        drv, wait = driver
        logger.info("Starting Invalid Ask Question test")

        hpa = HomePageAction(drv)
        ppa = ProductPageAction(drv)

        excel_path = r"E:\Pytest_Automation\data_provider\DataProvider.xlsx"
        data_list = excelReader.get_data(excel_path, "EnquiryData")
        data = data_list[0]

        name = data[0]
        email = data[1]
        hpa.click_HpProduct()
        ppa.click_ask_question()

        ppa.set_name(name)
        ppa.set_email(email)
        ppa.click_send_message()

        actual_error = ppa.get_email_required_message()
        expected_error = "Subject must be between 3 and 78 characters!"

        logger.info(f"Error Message: {actual_error}")

        assert expected_error in actual_error

    @pytest.mark.Tamil
    def test_Multiple_Action(self, driver):
        drv, wait = driver
        logger.info("Starting Multiple Action test")

        hpa = HomePageAction(drv)
        ppa = ProductPageAction(drv)

        hpa.click_HpProduct()

        ppa.click_add_to_cart()
        add_msg = ppa.get_add_to_cart_message()

        ppa.click_To_WishList()
        wishlist_msg = ppa.get_wishlist_added_message()

        logger.info(f"Cart Message: {add_msg}")
        logger.info(f"Wishlist Message: {wishlist_msg}")

        assert "success" in add_msg.lower()
        assert "wish list" in wishlist_msg.lower()

    @pytest.mark.Tamil
    def test_Breadcrumb_action(self, driver):
        drv, wait = driver
        logger.info("Starting Breadcrumb test")

        hpa = HomePageAction(drv)
        ppa = ProductPageAction(drv)
        fpa = FilterPageAction(drv)

        hpa.click_HpProduct()
        ppa.click_SoftwareBreadcrumb()

        actual_title = ppa.get_SoftwareTitle()
        expected_title = "Software"

        logger.info(f"Breadcrumb Title: {actual_title}")

        assert expected_title in actual_title

    @pytest.mark.Tamil
    def test_invalid_quantity(self, driver):
        drv, wait = driver
        logger.info("Starting Invalid Quantity test")

        hpa = HomePageAction(drv)
        ppa = ProductPageAction(drv)

        hpa.click_HpProduct()
        ppa.setQuantity(0)
        ppa.click_add_to_cart()
        ppa.click_view_cart()

        actual_msg = ppa.get_EmptyCartMessage()
        expected_msg = "Your shopping cart is empty!"

        logger.info(f"Empty Cart Message: {actual_msg}")

        assert expected_msg in actual_msg