from datetime import datetime
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait

class GeneralPage:
    def __init__(self, browser: Chrome, url: str):
        self.browser = browser
        self.url = url
        self.wait = WebDriverWait(self.browser, 5)

    def open(self):
        self.browser.get(self.url)
        self.browser.maximize_window()

    def resize_window(self, width: int, height: int):
        self.browser.set_window_size(width, height)

    def maximize_window(self):
        self.browser.maximize_window()

    def get_title(self):
        return self.browser.title

    def get_url(self):
        return self.browser.current_url

    def back(self):
        self.browser.back()

    def refresh(self):
        self.browser.refresh()

    def screenshot(self):
        filename = f"{self.get_title()}-{datetime.now().strftime("%Y%m%d_%H%M%S")}.png"
        print(f"Attempting screenshot: ./screenshots/{filename}")
        if self.browser.save_screenshot(f"./screenshots/{filename}"):
            print("Screenshot saved successfully.")
        else:
            print("Screenshot failed.")

    def close(self):
        self.browser.close()