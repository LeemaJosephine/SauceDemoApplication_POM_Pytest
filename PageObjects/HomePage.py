"""
Contains all the methods relevant to home page
https://www.saucedemo.com/
"""

#import all the necessary dependencies
import allure
from selenium.webdriver.common.by import By

# import the data and locators package
from TestLocators.locators import SauceDemoLocators
from conftest import capture_screenshot


class HomePage1:

    def __init__(self,driver):
        self.driver=driver

    # homepage relevant methods
    @allure.step("Login with username: {1} and password: {2}")
    def login(self,username,password,test_type,expected):

        try:
            # enter username
            self.driver.find_element(By.ID,value=SauceDemoLocators.username_locator).send_keys(username)
            #enter password
            self.driver.find_element(By.ID,value=SauceDemoLocators.password_locator).send_keys(password)
            # click submit
            self.driver.find_element(By.ID,value=SauceDemoLocators.submit_locator).click()
            # validate sigin


            if test_type == "ValidUsernameValidPassword":
                actual_text=self.driver.find_element(By.XPATH,value=SauceDemoLocators.product_page).text
                capture_screenshot(self.driver, "After successful login")
                assert actual_text==expected, f"Expected: '{expected}', but got: '{actual_text}'"

            elif test_type == "InvalidUsernameValidPassword":
                actual_text=self.driver.find_element(By.XPATH,value=SauceDemoLocators.login_error).text
                capture_screenshot(self.driver, "InvalidUsernameValidPassword")
                assert actual_text==expected, f"Expected: '{expected}', but got: '{actual_text}'"

            elif test_type == "ValidUsernameInvalidPassword":
                actual_text=self.driver.find_element(By.XPATH,value=SauceDemoLocators.login_error).text
                assert actual_text==expected, f"Expected: '{expected}', but got: '{actual_text}'"

            elif test_type == "InvalidUsernameInvalidPassword":
                actual_text=self.driver.find_element(By.XPATH,value=SauceDemoLocators.login_error).text
                assert actual_text==expected, f"Expected: '{expected}', but got: '{actual_text}'"

            elif test_type == "BlankUsernamPassword":
                actual_text=self.driver.find_element(By.XPATH,value=SauceDemoLocators.login_error).text
                assert actual_text==expected, f"Expected: '{expected}', but got: '{actual_text}'"

            elif test_type == "ValidUsernamBlankPassword":
                actual_text=self.driver.find_element(By.XPATH,value=SauceDemoLocators.login_error).text
                assert actual_text==expected, f"Expected: '{expected}', but got: '{actual_text}'"


        except Exception as e:
            screenshot_path = capture_screenshot(self.driver, f"Exception_{test_type}")
            raise e

        return True
