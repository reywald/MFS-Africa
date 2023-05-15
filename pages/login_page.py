from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from . import BasePage


class LoginPage(BasePage):

    """"
    This class encapsulates the site's Sign in page and operations carried out on it
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.username = "testautomationmfs@gmail.com"
        self.password = "TestAutomation@123"
        self.email_input = self.driver.find_element(By.ID, "email")
        self.password_input = self.driver.find_element(By.ID, "passwd")
        self.submit = self.driver.find_element(By.ID, "SubmitLogin")

    def signin(self):
        """
        Type in the username and password and click the submit button
        """
        self.email_input.clear()
        self.email_input.send_keys(self.username)

        self.password_input.clear()
        self.password_input.send_keys(self.password)

        self.submit.click()

        self.wait.until(EC.title_is("My account - My Store"))
        self.driver.find_element(
            By.CSS_SELECTOR, "div#center_column > ul > li > a").click()
