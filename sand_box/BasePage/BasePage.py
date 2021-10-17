from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure


class BasePage:
    def __init__(self, init_mobile_device):
        # инициализация драйвера
        self.driver = init_mobile_device
        # Ожидание драйвера
        self.wait = WebDriverWait(self.driver, 20)
        self.advertising_banner = lambda: self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "biz.growapp.winline:id/tvAgreement")))

    @allure.step('Клик на банер')
    def click_on_banner(self):
        """ Клик на банер"""
        self.advertising_banner().click()
        return self

    @allure.step('Спраятать клавиатуру')
    def remove_keyboard(self):
        """ Спраятать клавиатуру """
        self.driver.hide_keyboard()
        return self

    @allure.step('Проверка текста ошибки')
    def check_error_text(self, element, text_error):
        """ Проверка текста ошибки """
        assert element().text == text_error, "Текст ошибки не совпадает"
        return self

