"""
Test execution happens here
"""
import allure
import pytest

from PageObjects.HomePage import  HomePage1
from TestData.data import SauceDemoData
from Utilities.excel_functions import  ExcelFunction

# Reading data from excel
excel = ExcelFunction(SauceDemoData.file_name, SauceDemoData.sheet_name)
login_data = excel.get_data_from_excel()

class TestLogin :

    @allure.feature("Login Feature")
    @allure.story("Validate Login with valid and invalid data")
    @pytest.mark.parametrize("username,password,test_type,expected", login_data)
    def test_valid_login(self,setup_browser,username,password,test_type,expected):
            driver = setup_browser
            assert HomePage1(driver).login(username, password, test_type,expected) == True
            print("SUCCESS: Login works fine")
