import random
import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from faker import Faker
import string
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class MainPageHelperMethods:
    @staticmethod # véletlenszerű adatok a keresőmező dinamikus kitöltéséhez
    def get_random_city():
        cities = ["Budapest", "Dunaújváros", "Szekszárd"]
        return random.choice(cities)

    # @staticmethod #
    # def get_random_choice():
    #     dropdown_elements = IndexPage.searchbar_dropdown()
    #     random_element = random.choice(dropdown_elements)
    #     return random_element


class RegistrationHelper:

    f = Faker()
    temp_mail_URL = "https://temp-mail.org/en/"
    @staticmethod
    def temp_mail(browser):
        browser.switch_to.new_window('tab')
        browser.get(RegistrationHelper.temp_mail_URL)
        time.sleep(10)
        email_el = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "mail"))
        )

        temp_email_address = email_el.get_attribute("value")
        logging.info(f"Generated temporary email: {temp_email_address}")
        return temp_email_address

    @staticmethod
    def get_email_confirmation(browser):
        return WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='viewLink title-subject']"))).click()
    @staticmethod # ez a függvény generál egy specifikációnak megfelelő, véletlenszerű jelszót a regisztráció ellenőrzéséhez
    def generate_secure_password(length=8):
        digit = random.choice(string.digits)
        lowercase = random.choice(string.ascii_lowercase)
        uppercase = random.choice(string.ascii_uppercase)
        special = random.choice(string.punctuation)

        faker_chars = RegistrationHelper.f.password(length=length - 4)

        password = list(faker_chars) + [digit, lowercase, uppercase, special]
        random.shuffle(password)

        return ''.join(password)

    @staticmethod # ez a függvény véletlenszerű regisztrációs adatokat generál a regisztrációhoz felhasználva az általunk létrehozott jelszót
    def random_user():
        password = RegistrationHelper.generate_secure_password(14)
        test_user = [RegistrationHelper.f.first_name(), RegistrationHelper.f.last_name(), RegistrationHelper.f.phone_number(),
                     RegistrationHelper.f.email(), password]
        return test_user



