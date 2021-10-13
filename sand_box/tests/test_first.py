from sand_box.BasePage.RegistrationPage import RegistrationPage


def test_check_input_incorrect_sms_code(init_mobile_device):
    test_one = RegistrationPage(init_mobile_device)
    test_one.click_on_banner()\
        .click_input_phone()\
        .enter_phone('515678809')\
        .click_input_Birthday()\
        .enter_moth('aug')\
        .enter_day('12')\
        .enter_year('1990')\
        .click_button_ok()\
        .enter_password("jhgfs86513")\
        .click_on_promo()\
        .click_promo_input()\
        .enter_promo('qwertyu')\
        .remove_keyboard()\
        .tap_on_switch_button()\
        .click_button_registration()\
        .enter_sms_code('123123')\
        .remove_keyboard()\
        .click_button_next()\
        .check_error_text(test_one.error_sms_text, 'Неправильный код')

