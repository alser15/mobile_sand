
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from sand_box.BasePage.BasePage import BasePage


class RegistrationPage(BasePage):
    def __init__(self, init_mobile_device):
        # Доступ к оригиналу driver
        super().__init__(init_mobile_device)
        # Поиск банера на странице
        self.advertising_banner = lambda: self.wait.until(
            EC.element_to_be_clickable((By.ID, "biz.growapp.winline:id/tvAgreement")))
        # Поиск поля телефон
        self.input_phone = lambda: self.driver.find_element_by_id('biz.growapp.winline:id/vgPhone')
        # Поиск поля День рождения
        self.input_Birthday = lambda: self.driver.find_element_by_id('biz.growapp.winline:id/vgBirthday')
        # Поиск поля Пароль
        self.input_Password = lambda: self.driver.find_element_by_id('biz.growapp.winline:id/vgPassword')
        # Поиск поля кнопки отправки
        self.input_btnGetSmsCode = lambda: self.driver.find_element_by_id('biz.growapp.winline:id/btnGetSmsCode')

    def click_on_banner(self):
        """ Клик на банер"""
        self.advertising_banner().click()

    def find_input_phone(self):
        """ Поиск поля ввода телефона"""
        self.input_phone()

    def find_input_Birthday(self):
        """ Поиск поля ввода дня рождения"""
        self.input_phone()

    def find_input_Password(self):
        """ Поиск поля ввода телефона"""
        self.input_phone()

    def find_input_btnGetSmsCode(self):
        """ Поиск кнопки отправки данных"""
        self.input_phone()
