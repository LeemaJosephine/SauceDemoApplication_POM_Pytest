import allure
from selenium.webdriver.common.by import By

from TestLocators.locators import SauceDemoLocators
from conftest import capture_screenshot

class ProductPage1:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Adding items to cart")
    def add_item_to_cart(self):

        try:
            self.driver.find_element(By.XPATH,value=SauceDemoLocators.add_item1).click()
            self.driver.find_element(By.XPATH, value=SauceDemoLocators.add_item2).click()
            self.driver.find_element(By.XPATH, value=SauceDemoLocators.add_item3).click()
            cart_number = self.driver.find_element(By.CLASS_NAME,value=SauceDemoLocators.cart_badge).text
            assert int(cart_number) == 3
            self.driver.find_element(By.CLASS_NAME,value=SauceDemoLocators.cart).click()
            capture_screenshot(self.driver, f"AddToCart")

        except Exception as e:
            capture_screenshot(self.driver, f"Exception_AddToCart")
            raise e

        return True


