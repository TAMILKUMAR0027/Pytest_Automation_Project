import pytest

from actions.blogAction import BlogAction
from utils.configReader import ConfigReader


@pytest.mark.Samiha
class TestBlog:

    def test_blog_menu(self, driver):

        drv, wait = driver
        action = BlogAction(drv)
        drv.get(ConfigReader.get_url())
        action.click_blog_menu()

        assert action.is_latest_article_visible()

    def test_first_article(self, driver):

        drv, wait = driver
        action = BlogAction(drv)
        drv.get(ConfigReader.get_url())
        action.click_blog_menu()
        action.open_first_article()

        assert action.is_article_visible()

    @pytest.mark.parametrize(
        "category",
        [
            "business",
            "electronics",
            "technology",
            "fashion"
        ]
    )
    def test_blog_comment(self, driver, category):

        drv, wait = driver
        action = BlogAction(drv)

        drv.get(ConfigReader.get_url())
        action.click_blog_menu()

        if category == "business":
            action.click_business_category()
        elif category == "electronics":
            action.click_electronics_category()
        elif category == "technology":
            action.click_technology_category()
        else:
            action.click_fashion_category()
        action.open_first_article()

        action.post_comment(
            name="Samiha",
            email="samiha@test.com",
            comment=f"Automation comment for {category}"
        )

        assert action.is_comment_posted()
