import pytest
from appium import webdriver
import allure
import os


@pytest.fixture(scope='function')
def init_mobile_device():
    """Инициализация драйвера"""
    desired_caps = {
        "platformName": "Android",
        "deviceName": "Pixel XL API 30",
        "platformVersion": "11",
        "appPackage": "biz.growapp.winline",
        "appActivity": "biz.growapp.winline.presentation.splash.SplashActivity"
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
    yield driver
    driver.close_app()
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """ Скрин при падении теста """
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'init_mobile_device' in item.fixturenames:
                    driver = item.funcargs['init_mobile_device']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                driver.get_screenshot_as_png(),
                name='error',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))
