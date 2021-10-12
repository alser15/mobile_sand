import pytest
from appium import webdriver


@pytest.fixture(scope='function')
def init_mobile_device():
    """Инициализация драйвера"""
    desired_caps = {
        "platformName": "Android",
        "deviceName": "Pixel 2 API 28",
        "platformVersion": "9",
        "appPackage": "biz.growapp.winline",
        "appActivity": "biz.growapp.winline.presentation.splash.SplashActivity"
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
    yield driver
    driver.close_app()
    driver.quit()
