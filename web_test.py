from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.home_page import HomePage
from pages.login_page import LoginPage


class AutomationSite():

    def __init__(self, driver):
        self.driver = driver
        self.url = "http://automationpractice.pl/index.php"

    def open_site(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        assert "My Store" in self.driver.title

    def login(self):
        home_page = HomePage(driver)
        home_page.goto_login()
        login_page = LoginPage(driver)
        login_page.signin()


if __name__ == "__main__":
    driver = webdriver.Chrome()
    auto_site = AutomationSite(driver)
    auto_site.open_site()
    auto_site.login()

    sleep(5)
