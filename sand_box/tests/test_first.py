from sand_box.BasePage.RegistrationPage import RegistrationPage


def test_check_input(init_mobile_device):
    test_one = RegistrationPage(init_mobile_device)
    test_one.click_on_banner()
    test_one.input_phone()
    test_one.input_Birthday()
    test_one.input_Password()
    test_one.input_btnGetSmsCode()
