from actions.BaseAction import BaseAction
from pages.ProductPage import ProductPage


class ProductPageAction(BaseAction):
    def __init__(self, driver):
        super().__init__(driver)
        self.pp = ProductPage(driver)

    def getBrand(self):
        return self.get_text(self.pp.brand)

    def getInstock(self):
        return self.get_text(self.pp.instock)

    def getOutStock(self):
        return self.get_text(self.pp.outStock)

    def click_add_to_cart(self):
        self.click(self.pp.addToCart)

    def click_view_cart(self):
        self.click(self.pp.viewCartbtn)
    def get_ProductTitle(self):
        return self.get_text(self.pp.productName)
    def get_Product_price(self):
        return self.get_text(self.pp.productPrice)
    def get_Product_Quantity(self):
        return self.get_input_value(self.pp.quantityInput)
    def setQuantity(self, qty):
        self.clear(self.pp.productQuantity)
        self.send_keys(self.pp.productQuantity, str(qty))
    def click_ask_question(self):
        self.click(self.pp.askQuestionLink)
    def set_name(self, name):
        self.send_keys(self.pp.nameInput, name)
    def set_email(self, email): 
        self.send_keys(self.pp.emailInput, email)   
    def set_subject(self, subject):
        self.send_keys(self.pp.subjectInput, subject)
    def set_message(self, message):
        self.send_keys(self.pp.messageInput, message)
    def click_send_message(self):
        self.click(self.pp.sendMessageButton)
    def get_submission_message(self):
        return self.get_text(self.pp.submissionMessage)
    def get_email_required_message(self):
        return self.get_text(self.pp.emailRequiredMessage)
    def get_add_to_cart_message(self):
        return self.get_text(self.pp.addToCartMessage)
    def get_wishlist_added_message(self):
        return self.get_text(self.pp.wishlistAddedMessage)
    def click_To_WishList(self):
        self.click(self.pp.wishListIcon)
    def click_SoftwareBreadcrumb(self):
        self.click(self.pp.softwareBreadcrumb)
    def get_SoftwareTitle(self):
        return self.get_text(self.pp.softwareTitle)
    def get_EmptyCartMessage(self):
        return self.get_text(self.pp.emptyCartMessage)
    def click_CompareButton(self):
        self.click(self.pp.Compare_Button)

    def get_CompareSuccessMessage(self):
        return self.get_text(self.pp.Compare_Success_Message)
