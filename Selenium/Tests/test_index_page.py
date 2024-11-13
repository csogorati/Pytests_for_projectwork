from Sprint2.Selenium.configuration import get_preconfigured_chrome_driver
from Sprint2.Selenium.page_model import IndexPage

class TestIndexPage:
    def setup_method(self):
        self.browser = get_preconfigured_chrome_driver()
        self.page = IndexPage(self.browser)
        self.page.open()
        self.page.maximize_window()

    def teardown_method(self):
        self.page.close()

    def test_page_loads(self):
        assert self.page.get_url() == "http://localhost:4200/"
        assert self.page.get_title() == "ProHouse"
