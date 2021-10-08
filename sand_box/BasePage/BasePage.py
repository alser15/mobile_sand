from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, init_mobile_device):
        # инициализация драйвера
        self.driver = init_mobile_device
        # Ожидание драйвера
        self.wait = WebDriverWait(self.driver, 30)
