from selenium.webdriver.common.by import By


class CheckoutPage:
   
    NEW_ADDRESS_RADIO = (By.XPATH, "//label[@for='input-payment-address-new']")
    REGISTER_ACCOUNT_RADIO = (By.XPATH, "//label[@for='input-account-register']")

    SVG_NAVBAR_CART = (By.XPATH, "//div[@id='entry_217825']//div[@class='icon svg-icon']")
    SIDEBAR_CHECKOUT_BTN = (By.XPATH, "//a[normalize-space()='Checkout']")

    HP_PRODUCT_IMAGE = (By.XPATH,"//a[@id='mz-product-grid-image-47-212469']//div[@class='carousel-item active']//img[@title='HP LP3065']")
    PRODUCT_PAGE_CHECKOUT_BTN1 = (By.XPATH,"//div[@class='entry-content content-button d-md-none d-lg-block order-1 order-md-0 order-lg-1']/child::button")

    SHOPPING_CART_POPUP_LINK = (By.XPATH,"//div[@id='notification-box-top']//a[contains(text(),'shopping cart')]")
    CART_PAGE_CHECKOUT_BTN = (By.XPATH, "//div[@class='buttons d-flex']//a[text()='Checkout']")

    FIRST_NAME_INPUT = (By.XPATH, "//input[@id='input-payment-firstname']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@id='input-payment-lastname']")
    COMPANY_INPUT = (By.XPATH, "//input[@id='input-payment-company']")
    ADDRESS1_INPUT = (By.XPATH, "//input[@id='input-payment-address-1']")
    CITY_INPUT = (By.XPATH, "//input[@id='input-payment-city']")
    POSTCODE_INPUT = (By.XPATH, "//input[@id='input-payment-postcode']")
    COUNTRY_SELECT = (By.XPATH, "//select[@id='input-payment-country']")
    REGION_STATE_SELECT = (By.XPATH, "//select[@id='input-payment-zone']")

    SAME_BILLING_ADDRESS_CHECKBOX = (By.XPATH, "//input[@id='input-shipping-address-same']")
    SAME_BILLING_ADDRESS_LABEL = (By.XPATH, "//label[@for='input-shipping-address-same']")

    CONTINUE_CHECKOUT_BTN = (By.XPATH, "//button[@id='button-save']")
    CONFIRM_BTN = (By.XPATH, "//button[@id='button-confirm']")
    ORDER_CONFIRMATION_MSG = (By.XPATH, "//h1[normalize-space()='Your order has been placed!']")

    COD_LABEL = (By.XPATH, "//label[@for='input-payment-method-cod']")
    FLAT_RATE_LABEL = (By.XPATH, "//label[@for='input-shipping-method-flat.flat']")
    TERMS_LABEL = (By.XPATH, "//label[@for='input-agree']")

    REG_FIRST_NAME_INPUT = (By.XPATH, "//input[@id='input-payment-firstname']")
    REG_LAST_NAME_INPUT = (By.XPATH, "//input[@id='input-payment-lastname']")
    REG_EMAIL_INPUT = (By.XPATH, "//input[@id='input-payment-email']")
    REG_TELEPHONE_INPUT = (By.XPATH, "//input[@id='input-payment-telephone']")
    REG_PASSWORD_INPUT = (By.XPATH, "//input[@id='input-payment-password']")
    REG_CONFIRM_PASSWORD_INPUT = (By.XPATH, "//input[@id='input-payment-confirm']")
    REG_COMPANY_INPUT = (By.XPATH, "//input[@id='input-payment-company']")
    REG_ADDRESS1_INPUT = (By.XPATH, "//input[@id='input-payment-address-1']")
    REG_ADDRESS2_INPUT = (By.XPATH, "//input[@id='input-payment-address-2']")
    REG_CITY_INPUT = (By.XPATH, "//input[@id='input-payment-city']")
    REG_POSTCODE_INPUT = (By.XPATH, "//input[@id='input-payment-postcode']")
    REG_COUNTRY_SELECT = (By.XPATH, "//select[@id='input-payment-country']")
    REG_REGION_STATE_SELECT = (By.XPATH, "//select[@id='input-payment-zone']")
    PRIVACY_LABEL = (By.XPATH, "//label[@for='input-account-agree']")

    CONFIRM_MESSAGE = (By.XPATH, "//h1[@class='page-title mb-3']")
    EMPTY_CART_MESSAGE = (By.XPATH, "//div[@id='content']//p")

