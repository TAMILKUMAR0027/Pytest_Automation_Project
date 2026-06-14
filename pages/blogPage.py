from selenium.webdriver.common.by import By


class BlogPage:

    LATEST_ARTICLE_SECTION = (By.XPATH,"//h3[normalize-space()='Latest Articles']")
    FIRST_ARTICLE = (By.XPATH,"(//a[@class='d-block' and contains(@href,'blog/article')])[1]")
    BUSINESS_CATEGORY = (By.XPATH,"//a[contains(@href,'blog/category') and contains(@href,'path=5')]")
    ELECTRONICS_CATEGORY = ( By.XPATH, "//a[contains(@href,'blog/category') and contains(@href,'path=6')]")
    TECHNOLOGY_CATEGORY = ( By.XPATH,"//a[contains(@href,'blog/category') and contains(@href,'path=7')]")
    FASHION_CATEGORY = (By.XPATH,"//a[contains(@href,'blog/category') and contains(@href,'path=1')]")

    ARTICLE_TITLE = ( By.XPATH,"//h1")
    COMMENT_NAME = ( By.ID,"input-name")
    COMMENT_EMAIL = (By.ID,"input-email")
    COMMENT_TEXT = (By.ID,"input-comment")
    POST_COMMENT_BUTTON = (By.ID,"button-comment")
    COMMENT_SUCCESS = (By.CSS_SELECTOR, ".alert-success")

    BUSINESS_PAGE_HEADER = (By.XPATH,"//h1[contains(text(),'Business')]")
    ELECTRONICS_PAGE_HEADER = (By.XPATH,"//h1[contains(text(),'Electronics')]")
    TECHNOLOGY_PAGE_HEADER = (By.XPATH,"//h1[contains(text(),'Technology')]")
    FASHION_PAGE_HEADER = (By.XPATH,"//h1[contains(text(),'Fashion')]")