from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Chrome


class BasePage():

    def __init__(self, driver: Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
