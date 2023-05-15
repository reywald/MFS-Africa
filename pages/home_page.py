from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from . import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.sign_in_link = self.driver.find_element(By.CLASS_NAME, "login")
        self.bestsellers_link = self.driver.find_element(
            By.LINK_TEXT, "Best Sellers")
        self.product_labels = self.driver.find_elements(
            By.CSS_SELECTOR, ".right-block product-name")
        self.product_prices = self.driver.find_elements(
            By.CSS_SELECTOR, ".right-block .price.product-price")

    def goto_login(self):
        self.sign_in_link.click()
        self.wait.until(EC.title_is("Login - My Store"))

    def get_bestsellers(self):
        self.bestsellers_link.click()

        price_list = list(zip(self.product_labels, self.product_prices))
        sorted_price_list = sorted(price_list, key=lambda x: x[1].text[1:])
        print(price_list)
        print(sorted_price_list)
