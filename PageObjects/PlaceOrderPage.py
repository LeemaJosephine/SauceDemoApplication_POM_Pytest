import allure
from selenium.webdriver.common.by import By

from TestLocators.locators import SauceDemoLocators
from conftest import capture_screenshot

class PlaceOrderPage1:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Place_Order")
    def place_order(self, test_type, expected):

        try:

            self.driver.find_element(By.ID, value=SauceDemoLocators.finish_button).click()

            if test_type == "ValidUsernameValidPassword":
                actual_text=self.driver.find_element(By.XPATH,value=SauceDemoLocators.thank_you).text
                capture_screenshot(self.driver, "After successful info")
                assert actual_text==expected, f"Expected: '{expected}', but got: '{actual_text}'"

            self.driver.find_element(By.ID, value=SauceDemoLocators.back).click()

        except Exception as e:
            capture_screenshot(self.driver, f"Exception_Placeorder_Details")
            raise e

        return True

