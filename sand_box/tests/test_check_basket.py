from sand_box.BasePage.CatalogPage import CatalogPage
from sand_box.BasePage.RegistrationPage import RegistrationPage
from sand_box.BasePage.BasketPage import BasketPage
import allure

def test_check_basket(init_mobile_device):
    catalog_reg = RegistrationPage(init_mobile_device)
    catalog_reg.click_on_banner() \
        .click_catalocg()
    catalog = CatalogPage(init_mobile_device)
    catalog.click_selection_footbal() \
        .click_selection_footbal_russia() \
        .click_selection_footbal_russia_FNL() \
        .click_on_koef() \
        .check_text_selection_name() \
        .check_text_category_name() \
        .find_text_city_name() \
        .find_text_team_name() \
        .find_text_date_name() \
        .find_text_koef() \
        .click_button_basket()
    basket = BasketPage(init_mobile_device)
    basket.find_text_team_name_in_ticket() \
        .find_text_team_and_city_name_in_ticket() \
        .find_text_section_category_name_in_ticket() \
        .find_text_koef_name_in_ticket()
    assert catalog.koef == basket.koef_text, "Коеф не совпадате"
    assert catalog.name_team == basket.team_text, "Названия командр не совпадают"
    assert basket.team_and_city_text == (
                catalog.name_city + " - " + catalog.name_team), "Названия командр и город не совпадают"
    assert basket.section_category_text == f"{catalog.section_footbal_text}, {catalog.section_footbal_russia_text}, {catalog.section_footbal_russia_FNL_text}", "Категория, Страна, еще что-то не совпадают"
