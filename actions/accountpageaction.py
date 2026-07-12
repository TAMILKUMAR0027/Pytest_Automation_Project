from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from pages.accountpage import AccountPage
from actions.BaseAction import BaseAction


class AccountPageAction(BaseAction):
    def __init__(self, driver):
        super().__init__(driver)
        self.apa = AccountPage(driver)

    def success_login(self):
        actual = self.get_text(self.apa.accountLoginSuccess)
        return "My Account" in actual

    def click_subscribe_newsLetter(self):
        self.click(self.apa.subscribe_newsletter)

    def succes_msg_update_newsLetter(self):
        actual = self.get_text(self.apa.subscribeUpdate_Succ_msg)
        return "Your newsletter subscription has been successfully updated!" in actual

    def click_editAccount_info(self, telephone):
        self.click(self.apa.editAccInfo)
        self.clear(self.apa.telephoneEdit)
        self.send_keys(self.apa.telephoneEdit, telephone)
        self.click(self.apa.editContinue)
        actual = self.get_text(self.apa.editSuccessMsg)
        return "Your account has been successfully updated." in actual

    def deleteExistingAddress(self):
        self.click(self.apa.addressBook)
        self.click(self.apa.deleteAddressBookBtn)
        actual = self.get_text(self.apa.deleteAddressSuccessMessage)
        return "Your address has been successfully deleted" in actual

    def rewardPointsLinkClick(self):
        self.click(self.apa.rewardPointLink)

    def assertRewardPoitPageRedirection(self):
        actual = self.get_text(self.apa.assertRewardPoint)
        return "Your Reward Points" in actual
