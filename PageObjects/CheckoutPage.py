import allure
from selenium.webdriver.common.by import By

from TestLocators.locators import SauceDemoLocators
from conftest import capture_screenshot

class CheckoutPage1:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Checkout_details")
    def checkout_details(self, firstname,lastname,postal_code,test_type, expected):

        try:

            self.driver.find_element(By.ID, value=SauceDemoLocators.firstname).send_keys(firstname)
            self.driver.find_element(By.ID, value=SauceDemoLocators.lastname).send_keys(lastname)
            self.driver.find_element(By.ID, value=SauceDemoLocators.postal_code).send_keys(postal_code)
            self.driver.find_element(By.ID, value=SauceDemoLocators.continue_button).click()

            if test_type == "ValidUsernameValidPassword":
                actual_text=self.driver.find_element(By.XPATH,value=SauceDemoLocators.validate).text
                capture_screenshot(self.driver, "After successful info")
                assert actual_text==expected, f"Expected: '{expected}', but got: '{actual_text}'"

            elif test_type == "BlankFirstName":
                actual_text=self.driver.find_element(By.XPATH,value=SauceDemoLocators.error).text
                capture_screenshot(self.driver, "BlankFirstname")
                assert actual_text==expected, f"Expected: '{expected}', but got: '{actual_text}'"

            elif test_type == "BlankLastName":
                actual_text=self.driver.find_element(By.XPATH,value=SauceDemoLocators.error).text
                capture_screenshot(self.driver, "BlankLastName")
                assert actual_text==expected, f"Expected: '{expected}', but got: '{actual_text}'"

            elif test_type == "BlankPostalCode":
                actual_text=self.driver.find_element(By.XPATH,value=SauceDemoLocators.error).text
                capture_screenshot(self.driver, "BlankPostalCode")
                assert actual_text==expected, f"Expected: '{expected}', but got: '{actual_text}'"

            elif test_type == "BlankPostalCode":
                actual_text=self.driver.find_element(By.XPATH,value=SauceDemoLocators.error).text
                capture_screenshot(self.driver, "BlankPostalCode")
                assert actual_text==expected, f"Expected: '{expected}', but got: '{actual_text}'"

            elif test_type == "AllBlank":
                actual_text=self.driver.find_element(By.XPATH,value=SauceDemoLocators.error).text
                capture_screenshot(self.driver, "AllBlank")
                assert actual_text==expected, f"Expected: '{expected}', but got: '{actual_text}'"

        except Exception as e:
            capture_screenshot(self.driver, f"Exception_Checkout_Details")
            raise e

        return True


