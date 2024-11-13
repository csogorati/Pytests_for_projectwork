from Sprint2.Selenium.configuration import get_preconfigured_chrome_driver
from Sprint2.Selenium.page_model import PropertyPage

class TestIndexPage:
    def setup_method(self):
        self.browser = get_preconfigured_chrome_driver()
        self.page = PropertyPage(self.browser, 2)
        self.page.open()
        self.page.maximize_window()

    def teardown_method(self):
        self.page.close()

    def test_page_loads(self):
        assert "http://localhost:4200/properties" in self.page.get_url()
        assert self.page.get_url().endswith("2")
        assert self.page.get_title() == "ProHouse"


