import allure
from selenium.webdriver.common.by import By

from TestLocators.locators import SauceDemoLocators
from conftest import capture_screenshot

class CartPage1:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Checkout")
    def checkout(self):

        try:
            self.driver.find_element(By.ID,value=SauceDemoLocators.checkout).click()
            # cart_number = self.driver.find_element(By.CLASS_NAME,value=SauceDemoLocators.cart_badge).text
            # assert int(cart_number) == 3
            # self.driver.find_element(By.CLASS_NAME,value=SauceDemoLocators.cart).click()
            capture_screenshot(self.driver, f"Checkout")

        except Exception as e:
            capture_screenshot(self.driver, f"Exception_Checkout")
            raise e

        return True


