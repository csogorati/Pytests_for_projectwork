import time

from Sprint2.Selenium.configuration import get_preconfigured_chrome_driver
from Sprint2.Selenium.page_model import RegistrationPage, Switch, IndexPage
from Sprint2.Selenium.Helper_methods import RegistrationHelper

""" USER-STORY: TE24APRI-7 """


class TestRegistration:
    def setup_method(self):
        self.browser = get_preconfigured_chrome_driver()
        self.page = RegistrationPage(self.browser)
        self.page.open()
        self.page.maximize_window()
        self.index_page = IndexPage(self.browser)
        self.switch = Switch(self.browser)
        self.rh = RegistrationHelper()

    def teardown_method(self):
        # self.page.close()
        pass

    def test_page_loads(self):
        assert self.page.get_url() == "http://localhost:4200/registration-form"
        assert self.page.get_title() == "ProHouse"

    """  TC1 VALID DATAS """
    def test_registration_form_valid(self):
        # kitölti a regisztrációs űrlapot generált adatokkal.
        test_user = self.rh.random_user()
        self.page.registration_form(test_user[0], test_user[1], test_user[2], test_user[3],
                                    test_user[3], test_user[4], test_user[4])

        # megvizsgálja, hogy a regisztárció gombra kattintás után megjelenik-e a bejelentkezési felület
        assert self.index_page.login_form().is_displayed()

    """ TC2 INVALID E-MAIL CONFIRMATION"""
    def test_registration_form_inv_e_c(self):
        # kitölti a regisztrációs űrlapot generált adatokkal, de különböző e-mail címmel.
        random_user = self.rh.random_user()
        dif_email = self.rh.f.email()
        self.page.registration_form(random_user[0], random_user[1], random_user[2], random_user[3], dif_email,
                                    random_user[4], random_user[4])

        # megvizsgálja, hogy a regisztárció gombra kattintás után megjelenik-e a bejelentkezési felület
        assert not self.index_page.login_form().is_displayed()

    """ TC3 INVALID INVALID PASSWORD CONFIRMATION"""
    def test_registration_form_inv_p_c(self):
        # kitölti a regisztrációs űrlapot generált adatokkal, de különböző jelszóval.
        test_user = self.rh.random_user()
        diff_password = self.rh.f.password()
        self.page.registration_form(test_user[0], test_user[1], test_user[2], test_user[3], diff_password,
                                    test_user[4], test_user[4])

        # megvizsgálja, hogy a regisztárció gombra kattintás után megjelenik-e a bejelentkezési felület
        assert not self.index_page.login_form().is_displayed()



    def test_registration_form_valid2(self):
        # kitölti a regisztrációs űrlapot generált adatokkal.
        temp_mail = RegistrationHelper.temp_mail(self.browser)
        test_user = self.rh.random_user()
        self.switch.switch_window_handle1()
        self.page.registration_form(test_user[0], test_user[1], test_user[2], temp_mail,
                                    temp_mail, test_user[4], test_user[4])
        time.sleep(1)
        self.switch.switch_window_handle2()
        RegistrationHelper.get_email_confirmation(self.browser)


        # megvizsgálja, hogy a regisztárció gombra kattintás után megjelenik-e a bejelentkezési felület
        assert self.index_page.login_form().is_displayed()



