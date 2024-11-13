from Sprint2.Selenium.configuration import get_preconfigured_chrome_driver
from Sprint2.Selenium.page_model import IndexPage, PropertyCreationPage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CREDENTIALS = {
    "username": "kisel40144@abaot.com",
    "password": "012Test-"
}

class TestPropertyCreate:
    def setup_method(self):
        self.browser = get_preconfigured_chrome_driver()
        self.login_page = IndexPage(self.browser)
        self.creation_page = PropertyCreationPage(self.browser)
        self.login_page.open()
        self.login_page.maximize_window()

    def teardown_method(self):
        self.login_page.close()

    def test_page_loads(self):
        self.login_page.login(CREDENTIALS["username"], CREDENTIALS["password"])

        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/property-form"]'))).click()

        assert self.creation_page.get_url() == "http://localhost:4200/property-form"
        assert self.creation_page.get_title() == "ProHouse"
