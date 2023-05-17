from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC

from . import BasePage


class HomePage(BasePage):

    """"
    This class encapsulates the site's home page and operations carried out on it
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.sign_in_link = self.driver.find_element(By.CLASS_NAME, "login")

    def goto_login(self):
        self.sign_in_link.click()
        self.wait.until(EC.title_is("Login - My Store"))

    def get_bestsellers(self):
        """
        Get the apparels, sort by their prices and print labels and prices
        """
        self.bestsellers_link = self.driver.find_element(
            By.CSS_SELECTOR, "a.blockbestsellers")
        self.bestsellers_link.click()

        self.product_labels = self.driver.find_elements(
            By.CSS_SELECTOR, ".right-block a.product-name")
        self.product_prices = self.driver.find_elements(
            By.CSS_SELECTOR, ".right-block span.price.product-price")

        price_list = list(zip(self.product_labels, self.product_prices))
        sorted_price_list = sorted(price_list, key=lambda x: x[1].text[1:])

        print("{0:<30}{1:>10}".format("Apparel", "Price"))
        for item in sorted_price_list:
            print(f"{item[0].text:<30} {item[1].text:>10}")

    def navigate_to_category(self, menu_label: str):
        """
        Navigate to the dresses category
        """
        women_menu = self.driver.find_element(
            By.CSS_SELECTOR, "#block_top_menu > ul > li:first-child > a")
        menu_item = self.driver.find_element(
            By.CSS_SELECTOR, f'#block_top_menu > ul > li:first-child a[title^="{menu_label}"]')

        AC(self.driver).move_to_element(
            women_menu).click(menu_item).perform()
        self.wait.until(EC.title_is(f"{menu_label} Dresses - My Store"))
