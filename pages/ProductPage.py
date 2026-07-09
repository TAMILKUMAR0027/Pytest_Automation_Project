from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    brand = By.XPATH, "//ul[@class='list-unstyled m-0']//a[contains(text(),'Apple')]"
    instock = By.XPATH, "//span[@class='badge badge-success']"
    outStock = By.XPATH, "//span[@class='badge badge-danger']"
    addToCart = (
        By.XPATH,
        "//div[@class='entry-content content-button d-md-none d-lg-block order-1 order-md-0 order-lg-1']/child::button",
    )
    viewCartbtn = (By.XPATH, "//a[contains(text(),'View Cart')]")
    productName = (By.XPATH, "//h1[@class='h3']")
    productPrice = (By.XPATH, "//h3[@class='price-new mb-0']")
    productQuantity = (By.XPATH, "//div[@id='entry_216841']//input[@name='quantity']")
    quantityInput = (By.XPATH, "//input[contains(@name,'quantity')]")
    askQuestionLink = (By.XPATH, "//a[@aria-label='Ask Question']")
    nameInput = (By.XPATH, "//input[@placeholder='Your name']")
    emailInput = (By.XPATH, "//input[@placeholder='Your email']")
    subjectInput = (By.XPATH, "//input[@placeholder='Subject']")
    messageInput = (By.XPATH, "//textarea[@placeholder='Message']")
    sendMessageButton = (By.XPATH, "//button[normalize-space()='Send message']")
    submissionMessage = (By.XPATH, "//div[@class='alert alert-success alert-notification w-50 alert-dismissible']")
    emailRequiredMessage = (By.XPATH, "//div[@class='error text-danger']")
    addToCartMessage = (By.XPATH, "//p[contains(text(),'Success: You have added')]")
    wishlistAddedMessage = (By.XPATH, "//p[contains(text(),'You must')]")
    wishListIcon = (By.XPATH, "//div[@id='image-gallery-216811']//i[@class='far fa-heart']")
    softwareBreadcrumb = (By.XPATH, "//li[@class='breadcrumb-item']//a[contains(text(),'Software')]")
    softwareTitle = (By.XPATH, "//h1[@class='h4']")
    emptyCartMessage = (By.XPATH, "//div[@id='content']//p[contains(text(),'Your shopping cart is empty!')]")
    Compare_Button = (
    By.XPATH,
    "//button[contains(text(),'Compare this Product')]"
)

Compare_Success_Message = (
    By.XPATH,
    "//p[contains(text(),'Success: You have added')]"
)