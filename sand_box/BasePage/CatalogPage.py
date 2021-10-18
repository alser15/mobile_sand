from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from sand_box.BasePage.BasePage import BasePage
import allure

class CatalogPage(BasePage):
    def __init__(self, init_mobile_device):
        # Доступ к оригиналу driver
        super().__init__(init_mobile_device)
        # Поиск раздела футбол
        self.section_footbal = lambda: self.wait.until(EC.presence_of_element_located(
            (By.XPATH,"//android.widget.TextView[@text='Футбол']")))
        # Поиск раздела Россия
        self.section_footbal_russia = lambda: self.driver.find_element(By.XPATH,
           "//android.widget.TextView[@text='Россия']")
        # Поиск раздела ФНЛ
        self.section_footbal_russia_FNL = lambda: self.driver.find_element(By.XPATH,
            "//android.view.ViewGroup[@index='3']/android.widget.TextView[@index='0']")
        # Поиск коэфицента
        self.koef = lambda: self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//android.widget.FrameLayout[@resource-id='biz.growapp.winline:id/btnKoef3']/android.widget.FrameLayout[@resource-id='biz.growapp.winline:id/vgRoot']/android.widget.LinearLayout/android.widget.TextView[@resource-id='biz.growapp.winline:id/tvKoef']"))) # не тот xpath
        # Поиск названия Секции
        self.text_name_section = lambda : self.driver.find_element(By.XPATH,
            "//android.widget.TextView[@text='ФУТБОЛ']")
        # Поиск названия Категории
        self.text_name_category = lambda : self.driver.find_element(By.XPATH,
            "//android.widget.TextView[@text='ФНЛ-2 | Россия']")
        # Поиск названия Города
        self.text_name_city = lambda : self.driver.find_element(By.XPATH,
            "//android.widget.TextView[@text='Туапсе']")
        # Поиск названия Команды
        self.text_name_team = lambda : self.driver.find_element(By.XPATH,
            "//android.widget.TextView[@text='Биолог Новокубанск']")
        # Поиск даты
        self.text_name_date = lambda : self.driver.find_element(By.XPATH,
            "//android.widget.FrameLayout[@resource-id='biz.growapp.winline:id/vgAdditionalInfo']/android.widget.LinearLayout/android.widget.TextView[@resource-id='biz.growapp.winline:id/tvTime']")
        # Поиск кнопки корзина
        self.button_basket = lambda : self.driver.find_element(By.XPATH,
            "//android.widget.TextView[@text='Корзина']")

    @allure.step("Клик на категорию Футбол")
    def click_selection_footbal(self):
        """ Клик на категорию Футбол """
        self.section_footbal().click()
        self.section_footbal_text = self.section_footbal().text
        return self

    @allure.step("Клик на категорию Россия")
    def click_selection_footbal_russia(self):
        """ Клик на категорию Россия """
        self.section_footbal_russia().click()
        self.section_footbal_russia_text = self.section_footbal_russia().text
        return self

    @allure.step("Клик на категорию ФНЛ")
    def click_selection_footbal_russia_FNL(self):
        """ Клик на категорию ФНЛ """
        self.section_footbal_russia_FNL_text = self.section_footbal_russia_FNL().text
        self.section_footbal_russia_FNL().click()
        return self

    @allure.step("Клик на коэффицент")
    def click_on_koef(self):
        """ Клик на коэффицент """
        self.koef().click()
        return self

    @allure.step("Проверка названия секции")
    def check_text_selection_name(self):
        """ Проверка названия секции """
        assert self.section_footbal_text.upper() in self.text_name_section().text
        return self

    @allure.step("Проверка названия категории")
    def check_text_category_name(self):
        """ Проверка названия категории """
        assert self.section_footbal_russia_FNL_text in self.text_name_category().text
        assert self.section_footbal_russia_FNL_text in self.text_name_category().text
        return self

    @allure.step("Сохраняем название города")
    def find_text_city_name(self):
        """ Сохраняем название города """
        self.name_city = self.text_name_city().text
        return self

    @allure.step("Сохраняем название команд")
    def find_text_team_name(self):
        """ Сохраняем название команд """
        self.name_team = self.text_name_team().text
        return self

    @allure.step("Сохраняем дату")
    def find_text_date_name(self):
        """ Сохраняем дату """
        self.name_date = self.text_name_date().text
        return self

    @allure.step("Сохраняем коэффицент")
    def find_text_koef(self):
        """ Сохраняем коэффицент """
        self.koef = self.koef().text
        return self

    @allure.step("Клик на кнопку Корзина")
    def click_button_basket(self):
        """ Клик на кнопку Корзина """
        self.button_basket().click()
        return self