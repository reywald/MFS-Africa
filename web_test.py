from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages import home_page

from pages.home_page import HomePage
from pages.login_page import LoginPage


class AutomationSite():

    """"
    This class encapsulates the site to scrape and operations carried out on it
    """

    def __init__(self, driver):
        self.driver = driver
        self.url = "http://automationpractice.pl/index.php"

    def open_site(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        assert "My Store" in self.driver.title

    def login(self):
        self.home_page = HomePage(driver)
        self.home_page.goto_login()
        self.login_page = LoginPage(driver)
        self.login_page.signin()

    def print_products(self):
        self.home_page.get_bestsellers()


if __name__ == "__main__":
    driver = webdriver.Chrome()
    auto_site = AutomationSite(driver)
    auto_site.open_site()
    auto_site.login()
    auto_site.print_products()

    sleep(5)
