from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.catalog_page import CatalogPage


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
        self.home_page = HomePage(self.driver)
        self.home_page.goto_login()
        self.login_page = LoginPage(self.driver)
        self.login_page.signin()

    def print_products(self):
        self.home_page.get_bestsellers()

    def add_item_to_cart(self):
        self.home_page.navigate_to_category(menu_label="Summer")
        self.catalog_page = CatalogPage(self.driver)
        self.catalog_page.select_size(size="m")
        self.catalog_page.select_color(color="blue")
        # self.catalog_page.set_range("$50.00 - $52.28")
        self.catalog_page.set_range("$16.00 - $30.00")

    def verify_item_details(self):
        pass

    def get_shipping_cost(self):
        pass

    def verify_item_costs(self):
        pass

    def print_product_purchase_details(self):
        pass


if __name__ == "__main__":
    # options = Options()
    # options.add_argument("--headless")
    # driver = webdriver.Chrome(options=options)

    driver = webdriver.Chrome()
    auto_site = AutomationSite(driver)
    auto_site.open_site()
    auto_site.login()
    # auto_site.print_products()
    auto_site.add_item_to_cart()

    sleep(5)
    driver.quit()
