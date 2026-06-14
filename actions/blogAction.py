from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from actions.BaseAction import BaseAction
from pages.blogPage import BlogPage


class BlogAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.bp = BlogPage()

    def js_click(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    def click_blog_menu(self): 
        self.driver.get("https://ecommerce-playground.lambdatest.io""/index.php?route=extension/maza/blog/home")

    def is_latest_article_visible(self):
        return self.is_displayed(self.bp.LATEST_ARTICLE_SECTION)

    def click_business_category(self):
        self.js_click(self.bp.BUSINESS_CATEGORY)

    def click_electronics_category(self):
        self.js_click(self.bp.ELECTRONICS_CATEGORY)

    def click_technology_category(self):
        self.js_click(self.bp.TECHNOLOGY_CATEGORY)

    def click_fashion_category(self):
        self.js_click(self.bp.FASHION_CATEGORY)

    def open_first_article(self):
        self.js_click(self.bp.FIRST_ARTICLE)

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.bp.ARTICLE_TITLE))
    def is_article_visible(self):
        return self.is_displayed(self.bp.ARTICLE_TITLE)

    def post_comment(self, name, email, comment):

        self.scroll_into_view(self.bp.COMMENT_NAME)
        self.send_keys(self.bp.COMMENT_NAME, name)
        self.send_keys(self.bp.COMMENT_EMAIL, email)
        self.send_keys(self.bp.COMMENT_TEXT, comment)
        self.js_click(self.bp.POST_COMMENT_BUTTON)

    def is_comment_posted(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.bp.COMMENT_SUCCESS))
            return True
        except Exception:
            return False
