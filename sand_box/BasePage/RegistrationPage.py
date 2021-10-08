
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from sand_box.BasePage.BasePage import BasePage


class RegistrationPage(BasePage):
    def __init__(self, init_mobile_device):
        super().__init__(init_mobile_device)
        self.advertising_banner = lambda: self.wait.until(
            EC.element_to_be_clickable((By.ID, "biz.growapp.winline:id/tvAgreement")))
        self.input_phone = lambda: self.driver.find_element_by_id('biz.growapp.winline:id/vgPhone')
        self.input_Birthday = lambda: self.driver.find_element_by_id('biz.growapp.winline:id/vgBirthday')
        self.input_Password = lambda: self.driver.find_element_by_id('biz.growapp.winline:id/vgPassword')
        self.input_btnGetSmsCode = lambda: self.driver.find_element_by_id('biz.growapp.winline:id/btnGetSmsCode')

    def click_on_banner(self):
        self.advertising_banner().click()

    def find_input_phone(self):
        self.input_phone()

    def find_input_Birthday(self):
        self.input_phone()

    def find_input_Password(self):
        self.input_phone()

    def find_input_btnGetSmsCode(self):
        self.input_phone()
