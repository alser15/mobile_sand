from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from sand_box.BasePage.BasePage import BasePage
import allure

class RegistrationPage(BasePage):
    def __init__(self, init_mobile_device):
        # Доступ к оригиналу driver
        super().__init__(init_mobile_device)
        # Поиск поля телефон
        self.input_phone = lambda: self.driver.find_element(By.ID, 'biz.growapp.winline:id/etRegMask')
        # Поиск поля День рождения
        self.input_Birthday = lambda: self.driver.find_element(By.ID, 'biz.growapp.winline:id/vgBirthday')
        # Поиск поля для ввода месяца
        self.input_Birthday_moth = lambda: self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//android.widget.NumberPicker[@index="0"]/android.widget.EditText[@index="1"]')))
        # Поиск поля для ввода дня
        self.input_Birthday_day = lambda: self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//android.widget.NumberPicker[@index="1"]/android.widget.EditText[@index="1"]')))
        # Поиск поля для ввода года
        self.input_Birthday_year = lambda: self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//android.widget.NumberPicker[@index="2"]/android.widget.EditText[@index="1"]')))
        # Поиск кнопки cancel в таблице выбора даты рождения
        self.button_cancel_Birthday = lambda: self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, 'android:id/button2')))
        # Поиск кнопки OK в таблице выбора даты рождения
        self.button_OK_Birthday = lambda: self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, 'android:id/button1')))
        # Поиск поля Пароль
        self.input_Password = lambda: self.wait.until(
            EC.presence_of_element_located(
                (By.ID, 'biz.growapp.winline:id/etReg')))
        # Поиск поля кнопки Регистрации
        self.button_registration = lambda: self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, 'biz.growapp.winline:id/btnGetSmsCode')))
        # Поиск Промокода
        self.promo = lambda: self.driver.find_element(By.ID, "biz.growapp.winline:id/tvHavePromoCode")
        # Поиск поля  промокода
        self.promo_input = lambda: self.wait.until(
            EC.presence_of_element_located(
                (By.ID, "biz.growapp.winline:id/vgPromoCodeField")))
        # Поиск поля ввода промокода
        self.promo_input_enter = lambda: self.driver.find_element(By.XPATH,
                "//android.widget.FrameLayout[@resource-id='biz.growapp.winline:id/vgPromoCodeField']/android.widget.FrameLayout/android.widget.EditText[@resource-id='biz.growapp.winline:id/etReg']")
        # Поиск переключателя с подтверждением правил
        self.switch_button = lambda: self.driver.find_element(By.ID, 'biz.growapp.winline:id/switchAgreement')
        # Поиск поля для ввода смс кода
        self.input_sms_code = lambda: self.wait.until(EC.presence_of_element_located(
            (By.XPATH,
                "//android.widget.FrameLayout[@resource-id='biz.growapp.winline:id/vgSmsCodeField']/android.widget.FrameLayout/android.widget.EditText[@resource-id='biz.growapp.winline:id/etReg']")))
        # Поиск кнопки продолжить
        self.button_next = lambda: self.driver.find_element(By.ID, "biz.growapp.winline:id/btnRegister")
        # Поиск текста ошибки в поле ввода смс кода
        self.error_sms_text = lambda: self.wait.until(EC.presence_of_element_located(
            (By.XPATH,
                "//android.widget.FrameLayout[@resource-id='biz.growapp.winline:id/vgSmsCodeField']/android.widget.FrameLayout/android.widget.TextView[@resource-id='biz.growapp.winline:id/tvReg']")))
        self.button_catalog = lambda: self.driver.find_element(By.XPATH,
                "//android.widget.ImageButton[@content-desc='Open navigation drawer']")


    @allure.step('Клик на поля ввода телефона')
    def click_input_phone(self):
        """ Поиск поля ввода телефона"""
        self.input_phone().click()
        return self

    @allure.step('Ввод номера телефона')
    def enter_phone(self, number_phone):
        """ Ввод номера телефона"""
        self.input_phone().send_keys(number_phone)
        return self

    @allure.step('Клик на форму Дата Рождения')
    def click_input_Birthday(self):
        """ Раскрытие формы дня рождения"""
        self.input_Birthday().click()
        return self

    @allure.step('Ввод месяца в форму Дата Рождения')
    def enter_moth(self, moth):
        """ Ввод месяца в форму дня рождения """
        self.input_Birthday_moth().click()
        self.input_Birthday_moth().clear()
        self.input_Birthday_moth().set_value(moth)
        return self

    @allure.step('Ввод дня в форму Дата Рождения')
    def enter_day(self, day):
        """ Ввод дня в форму дня рождения """
        self.input_Birthday_day().click()
        self.input_Birthday_day().clear()
        self.input_Birthday_day().set_value(day)
        return self

    @allure.step('Ввод года в форму Дата Рождения')
    def enter_year(self, year):
        """ Ввод года в форму дня рождения"""
        self.input_Birthday_year().click()
        self.input_Birthday_year().clear()
        self.input_Birthday_year().set_value(year)
        return self

    @allure.step('Клик на кнопку cancel в форму Дата Рождения')
    def click_button_cancel(self):
        """ Нажать копку cancel в форме выбора даты рождения"""
        self.button_cancel_Birthday().click()
        return self

    @allure.step('Клик на кнопку ОК в форму Дата Рождения')
    def click_button_ok(self):
        """ Нажать копку OK в форме выбора даты рождения"""
        self.button_OK_Birthday().click()
        return self

    @allure.step('Ввод пароля')
    def enter_password(self, password):
        """ Ввод пароля"""
        self.input_Password().send_keys(password)
        return self

    @allure.step('Клик на надпись "У меня есть промокод"')
    def click_on_promo(self):
        """ Клик по надписи У меня есть промокод """
        self.promo().click()
        return self

    @allure.step('Клик на поле с промокодом')
    def click_promo_input(self):
        """ Клик по полю с промокодом """
        self.promo_input().click()
        return self

    @allure.step('Ввод промокода')
    def enter_promo(self, promocode):
        """ Ввод промокода """
        self.promo_input_enter().send_keys(promocode)
        return self

    @allure.step('Клик на кнопку "Соглашение с правилами"')
    def tap_on_switch_button(self):
        """ Клик по соглашению с правилами """
        self.switch_button().click()
        return self

    @allure.step('Клик на кнопку регистрации')
    def click_button_registration(self):
        """ клик на кнопку регистрации"""
        self.button_registration().click()
        return self

    @allure.step('Ввод СМС кода')
    def enter_sms_code(self, sms_code):
        """ Ввод СМС кода """
        self.input_sms_code().send_keys(sms_code)
        return self

    @allure.step('Клик на кнопку продолжить')
    def click_button_next(self):
        """ Клик на кнопку продолжить """
        self.button_next().click()
        return self
    def click_catalocg(self):
        self.button_catalog().click()
        return self