from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from sand_box.BasePage.BasePage import BasePage
import allure


class BasketPage(BasePage):
    def __init__(self, init_mobile_device):
        # Доступ к оригиналу driver
        super().__init__(init_mobile_device)
        # Поиск названия команд в билете
        self.team_name_in_ticket = lambda: self.wait.until(EC.presence_of_element_located(
            (By.XPATH,
             "//android.view.ViewGroup[@resource-id='biz.growapp.winline:id/betContainer']/android.widget.TextView[@resource-id='biz.growapp.winline:id/tvOutcome']")))
        # Поиск названия команд и города в билете
        self.team_and_city_name_in_ticket = lambda: self.driver.find_element(
            By.XPATH,
            "//android.view.ViewGroup[@resource-id='biz.growapp.winline:id/betContainer']/android.widget.TextView[@resource-id='biz.growapp.winline:id/tvTeamTitles']")
        # Поиск категории, страны и  что-то еще
        self.section_category_name = lambda: self.driver.find_element(
            By.XPATH, "//android.widget.TextView[@resource-id='biz.growapp.winline:id/tvChampTitle']")
        # Поиск коэффицента
        self.koef_name = lambda: self.driver.find_element(
            By.XPATH,
            "//android.view.ViewGroup[@resource-id='biz.growapp.winline:id/betContainer']/android.widget.TextView[@resource-id='biz.growapp.winline:id/tvKoef']")

    @allure.step('Сохраняем названия команд в билете')
    def find_text_team_name_in_ticket(self):
        """ Сохраняем названия команд в билете """
        self.team_text = self.team_name_in_ticket().text
        return self

    @allure.step('Сохраняем команд и города в билете')
    def find_text_team_and_city_name_in_ticket(self):
        """ Сохраняем названия команд и города в билете """
        self.team_and_city_text = self.team_and_city_name_in_ticket().text
        return self

    @allure.step('Сохраняем категории, страны и  что-то еще в билете')
    def find_text_section_category_name_in_ticket(self):
        """ Сохраняем названия категории, страны и  что-то еще в билете """
        self.section_category_text = self.section_category_name().text
        return self

    @allure.step('Сохраняем коэффицент в билете')
    def find_text_koef_name_in_ticket(self):
        """ Сохраняем коэффицент в билете """
        self.koef_text = self.koef_name().text
        return self
