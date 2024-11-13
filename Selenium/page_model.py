from Sprint1.Selenium.general_model import GeneralPage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import random


class IndexPage(GeneralPage):
    def __init__(self, browser):
        super().__init__(browser, url="http://localhost:4200")

    def login_form(self):
        return self.browser.find_element(By.TAG_NAME, "form")

    def login(self, username: str, password: str):
        self.browser.find_element(By.XPATH, '//a[contains(., "Sign In") or contains(., "Bejelentkezés")]').click()
        input_fields = self.browser.find_elements(By.TAG_NAME, "input")
        input_fields[0].send_keys(username)
        input_fields[1].send_keys(password)
        self.browser.find_element(By.XPATH, '//button[@type="submit"]').click()

    def logout_btn(self):
        return self.browser.find_element(By.XPATH, '//a[contains(., "Logout") or contains(., "Kijelentkezés")]')

    def search_bar_main(self):
        return self.browser.find_element(By.XPATH, '//input[@type="text"]')

    def search_button(self):
        return self.browser.find_element(By.XPATH, '//button[@class="btn header-search-button"]')

    def searchbar_dropdown(self):
        return self.wait.until(EC.visibility_of_any_elements_located((By.XPATH, '//div[@class="geoapify-autocomplete-item"]')))




class RegistrationPage(GeneralPage):
    def __init__(self, browser):
        super().__init__(browser, url="http://localhost:4200/registration-form")

    # regisztrációs űrlap
    def registration_form(self, last_name: str, first_name: str, phone_number: str, email: str,
                          email_confirmation: str, password: str, password_confirmation: str):
        input_fields = self.browser.find_elements(By.TAG_NAME, "input")[2:]
        input_fields[0].send_keys(last_name)
        input_fields[1].send_keys(first_name)
        input_fields[2].send_keys(phone_number)
        input_fields[3].send_keys(email)
        input_fields[4].send_keys(email_confirmation)
        input_fields[5].send_keys(password)
        input_fields[6].send_keys(password_confirmation)

        self.browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        submit_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(., "Regis")]')))
        submit_btn.click()
    

class Switch(GeneralPage):

    def __init__(self, browser):
        super().__init__(browser, url="http://localhost:4200")

    def switch_window_handle1(self):
        self.browser.switch_to.window(self.browser.window_handles[0])  # Switch to the original window
        return self.browser.window_handles[0]

    def switch_window_handle2(self):
        self.browser.switch_to.window(self.browser.window_handles[1])  # Switch to the temp mail window
        return self.browser.window_handles[1]


class SearchPropertyPage(GeneralPage):
    def __init__(self, browser):
        super().__init__(browser, url="http://localhost:4200/property-list")

    def select_type(self, for_sale=True):
        Select(self.browser.find_element(By.ID, "saleType")).select_by_index(0 if for_sale else 1)

    def select_city(self, city: str):
        self.browser.find_element(By.ID, "city").send_keys(city)

    def search(self):
        self.browser.find_element(locate_with(By.TAG_NAME, "button").to_right_of(self.browser.find_element(By.ID, "city"))).click()

    def property_list_item(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="main-content-list-item"]')))


class PropertyPage(GeneralPage):
    def __init__(self, browser, propertyID):
        super().__init__(browser, url=f"http://localhost:4200/properties/{str(propertyID)}")
