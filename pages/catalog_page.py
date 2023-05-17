from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from . import BasePage


class CatalogPage(BasePage):
    """
    This class encapsulates the Catalog page and its functions
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.filters = (By.ID, "enabled_filters")

    def select_size(self, size: str):
        medium_size_option = self.driver.find_element(
            By.CSS_SELECTOR, f"#layered_form a[href$='size-{size}']")
        medium_size_option.click()
        self.wait.until(EC.presence_of_element_located(self.filters))
        # self.wait.until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, "#enabled_filters li"), " Size: M "))

    def select_color(self, color: str):
        pink_color_option = self.driver.find_element(
            By.CSS_SELECTOR, f"#layered_form a[href*='color-{color}']")
        pink_color_option.click()
        self.wait.until(EC.presence_of_element_located(self.filters))
        # self.wait.until(EC.text_to_be_present_in_element(self.filters, " Color: Pink "))

    def _get_price_range(self, interval: str):
        # Get the new price range
        min_price, max_price = [float(i[1:]) for i in interval.split(" - ")]

        return min_price, max_price

    def set_range(self, interval: str):
        self._get_slide_elements()

        # Calculate the new slider handle position based on min or max values
        min_price, max_price = self._get_price_range(
            self.price_range)
        new_min_price, new_max_price = self._get_price_range(
            interval)

        # print(min_price, max_price)
        # print(new_min_price, new_max_price)

        if max_price > new_max_price:
            offset = -round(self.right_slider_width *
                            (max_price - new_max_price) / (max_price - min_price))
            self._slide(self.right_slider_handle, offset)
            # print(f"Slide to ${offset}")
        # if min_price < new_min_price:
        #     offset = round(self.left_slider_width * (new_min_price -
        #                    min_price) / (max_price - min_price), 0)
        #     self._slide(self.left_slider_handle, offset)
        self.wait.until(EC.presence_of_element_located(self.filters))

    def _get_slide_elements(self):
        # Get the slider elements: range, left and right handles
        self.slider = self.driver.find_element(
            By.CSS_SELECTOR, ".layered_slider .ui-slider-range")
        self.left_slider_handle = self.driver.find_element(
            By.CSS_SELECTOR, "a.ui-slider-handle:nth-of-type(1)")
        self.right_slider_handle = self.driver.find_element(
            By.CSS_SELECTOR, "a.ui-slider-handle:nth-of-type(2)")

        # Fetch the slider dimennsions
        # self.slider_width = int(self.slider.get_attribute("offsetWidth"))
        self.right_slider_width = int(
            self.right_slider_handle.get_attribute("offsetLeft"))

        self.left_slider_width = int(
            self.left_slider_handle.get_attribute("offsetLeft"))

        # Fetch the catalog price range
        self.price_range = self.driver.find_element(
            By.ID, "layered_price_range").text

        # print(self.right_slider_width, self.price_range)

    def _slide(self, handle, offset):
        # Move the slider with the mouse using the calculated offset
        actions = ActionChains(self.driver)
        actions \
            .move_to_element(handle) \
            .click_and_hold(handle) \
            .move_by_offset(offset, 0) \
            .release() \
            .perform()

    def view_catalog_product(self):
        # Hover over a catalog product and click the More button
        self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "ul.product_list > li:first-child > .product-container")))
        dress_product = self.driver.find_element(
            By.CSS_SELECTOR, "ul.product_list > li:first-child > .product-container")
        dress_name = dress_product.find_element(
            By.CSS_SELECTOR, "a.product-name").text
        print(dress_name)

        actions = ActionChains(self.driver)
        actions.move_to_element(dress_product).perform()
        more_button = dress_product.find_element(
            By.CSS_SELECTOR, "a[title='View']")
        actions.click(more_button).perform()

        self.wait.until(EC.title_is(f"{dress_name} - My Store"))
