from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, init_mobile_device):
        # инициализация драйвера
        self.driver = init_mobile_device
        # Ожидание драйвера
        self.wait = WebDriverWait(self.driver, 40)

    def remove_keyboard(self):
        """ Спраятать клавиатуру """
        self.driver.hide_keyboard()
        return self

    def check_error_text(self, element, text_error):
        assert element().text == text_error, "Текст ошибки не совпадает"
        return self

