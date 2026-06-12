from selenium.webdriver.common.by import By

class CheckoutPage:

    # -------- Product --------
    HP_PRODUCT_IMAGE = (By.XPATH, "//img[@title='HP LP3065']")
    ADD_TO_CART_BTN = (By.XPATH, "//button[contains(@id,'button-cart')]")
    SHOPPING_CART_POPUP_LINK = (By.XPATH, "//a[contains(text(),'shopping cart')]")
    CART_PAGE_CHECKOUT_BTN = (By.XPATH, "//a[text()='Checkout']")

    # -------- Login --------
    LOGIN_RADIO = (By.XPATH, "//label[contains(text(),'Login')]")
    LOGIN_EMAIL = (By.ID, "input-login-email")
    LOGIN_PASSWORD = (By.ID, "input-login-password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Login')]")

    # -------- Register --------
    REGISTER_ACCOUNT_RADIO = (By.XPATH, "//label[@for='input-account-register']")
    PRIVACY_LABEL = (By.XPATH, "//label[@for='input-account-agree']")

    REG_FIRST_NAME_INPUT = (By.ID, "input-payment-firstname")
    REG_LAST_NAME_INPUT = (By.ID, "input-payment-lastname")
    REG_EMAIL_INPUT = (By.ID, "input-payment-email")
    REG_TELEPHONE_INPUT = (By.ID, "input-payment-telephone")
    REG_PASSWORD_INPUT = (By.ID, "input-payment-password")
    REG_CONFIRM_PASSWORD_INPUT = (By.ID, "input-payment-confirm")

    # -------- Billing --------
    FIRST_NAME_INPUT = (By.ID, "input-payment-firstname")
    LAST_NAME_INPUT = (By.ID, "input-payment-lastname")
    COMPANY_INPUT = (By.ID, "input-payment-company")
    ADDRESS1_INPUT = (By.ID, "input-payment-address-1")
    CITY_INPUT = (By.ID, "input-payment-city")
    POSTCODE_INPUT = (By.ID, "input-payment-postcode")

    SAME_BILLING_ADDRESS_LABEL = (By.XPATH, "//label[@for='input-shipping-address-same']")

    # -------- Shipping / Payment --------
    FLAT_RATE_LABEL = (By.XPATH, "//label[@for='input-shipping-method-flat.flat']")
    COD_LABEL = (By.XPATH, "//label[@for='input-payment-method-cod']")
    TERMS_LABEL = (By.XPATH, "//label[@for='input-agree']")
    CONTINUE_CHECKOUT_BTN = (By.ID, "button-save")

    # -------- Assertions --------
    ORDER_CONFIRMATION_MSG = (By.XPATH, "//h1[contains(text(),'Your order has been placed')]")
    EMPTY_CART_MESSAGE = (By.XPATH, "//div[@id='content']//p")