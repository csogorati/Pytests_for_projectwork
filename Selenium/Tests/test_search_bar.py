from Sprint2.Selenium.configuration import get_preconfigured_chrome_driver
from Sprint2.Selenium.page_model import RegistrationPage, Switch, IndexPage, SearchPropertyPage
from Sprint1.Ati.Helper_methods import MainPageHelperMethods
import time





class TestSearchBar:
    def setup_method(self):
        self.browser = get_preconfigured_chrome_driver()
        self.page = IndexPage(self.browser)
        self.page.open()
        self.page.maximize_window()
        self.switch = Switch(self.browser)
        self.search_page = SearchPropertyPage(self.browser)


    def teardown_method(self):
        # self.page.close()
        pass

    def test_page_loads(self):
        assert self.page.get_url() == "http://localhost:4200"
        assert self.page.get_title() == "ProHouse"

    def test_search_bar(self):
        random_city = (MainPageHelperMethods.get_random_city())
        self.page.search_bar_main().send_keys(random_city)

        self.page.searchbar_dropdown()[0].click()
        self.page.search_button().click()

        assert self.search_page.property_list_item().is_displayed()

