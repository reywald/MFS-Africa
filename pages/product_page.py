from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from . import BasePage


class ProductPage(BasePage):
    """
    This class encapsulates the Product page and its functions
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.order_box = self.driver.find_element(
            By.CLASS_NAME, "box-info-product")

    def __is_in_stock(self) -> bool:
        # Check if the "In Stock" label is visible and overall quantity is greater than 0
        in_stock = self.driver.find_element(By.ID, "availability_value").text
        self.quantity = self.driver.find_element(
            By.ID, "quantityAvailable").text

        print(in_stock, self.quantity)
        return (in_stock == "In stock" and self.quantity)

    def purchase_product(self, quantity: str, size: str, color: str):
        # Set the quantity, size and color of the product
        self.__set_color(color)
        self.__set_size(size)
        self.__set_quantity(quantity)
        self.__add_to_cart()

        # if self.__is_in_stock():
        #     print("Product in stock")
        # else:
        #     print("Product out of stock")

    def __set_quantity(self, quantity: str):
        # Locate the element displaying the quantity
        qty_input = self.order_box.find_element(By.ID, "quantity_wanted")

        # Next, locate the quantity increment element
        qty_add = self.order_box.find_element(
            By.CLASS_NAME, "product_quantity_up")

        # Get the quantity input's value
        old_quantity = qty_input.get_attribute("value")

        # Click the increment element a number of times
        for i in range(int(quantity) - int(old_quantity)):
            # Use JavaScript to click this element as it is not interactable with selenium
            self.driver.execute_script("arguments[0].click();", qty_add)

        # Confirm that the added quantity equals what is expected
        assert qty_input.get_attribute("value") == quantity

    def __set_size(self, size: str):
        # Locate the element for selecting the size option
        select = Select(self.order_box.find_element(By.ID, "group_1"))
        select.select_by_visible_text(size)

    def __set_color(self, color: str):
        # Locate the color element and click it
        color_choice = self.order_box.find_element(
            By.CSS_SELECTOR, f"#color_to_pick_list li > a[title='{color}' i]")
        color_choice.click()
        self.wait.until(EC.text_to_be_present_in_element_attribute(
            (By.CSS_SELECTOR,
             f"#color_to_pick_list li > a[title='{color}' i]"),
            "class", "selected"))

    def __add_to_cart(self):
        # Locate the Add to cart button element
        add_button = self.order_box.find_element(By.CLASS_NAME, "exclusive")
        add_button.click()

        self.wait.until(EC.presence_of_element_located((By.ID, "layer_cart")))

