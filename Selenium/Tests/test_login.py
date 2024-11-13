from Sprint2.Selenium.configuration import get_preconfigured_chrome_driver
from Sprint2.Selenium.page_model import IndexPage
import time


""" USER-STORY: TE24APRI-7 """

TESTUSER = {
    "username": "csogorattila97@gmail.com",
    "password": "Password1!"
}
class TestLogin:
    def setup_method(self):
        self.browser = get_preconfigured_chrome_driver()
        self.page = IndexPage(self.browser)
        self.page.open()
        self.page.maximize_window()



    def teardown_method(self):
           # self.browser.close()
            pass

    def test_login(self):
        self.page.login(TESTUSER["username"], TESTUSER["password"])
        time.sleep(1)
        assert self.page.logout_btn().is_displayed()
        assert self.page.logout_btn().text == "Logout" or self.page.logout_btn().text == "Kijelenetkezés"
