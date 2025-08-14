"""
Test execution happens here
"""
import allure
import pytest

from PageObjects.HomePage import  HomePage1
from PageObjects.ProductPage import ProductPage1
from TestData.data import SauceDemoData
from Utilities.excel_functions import  ExcelFunction

# Reading data from excel
excel = ExcelFunction(SauceDemoData.file_name, SauceDemoData.sheet_name_cart)
cart_data = excel.get_data_from_excel()

class TestAddToCart :

    @pytest.mark.smoke
    @allure.feature("Add to cart Feature")
    @allure.story("Validate add to cart")
    @pytest.mark.parametrize("username,password,test_type,expected", cart_data)
    def test_add_cart(self,setup_browser,username,password,test_type,expected):
            driver = setup_browser
            assert HomePage1(driver).login(username, password, test_type,expected) == True
            assert ProductPage1(driver).add_item_to_cart() == True
            print("SUCCESS: Item addedd to cart")
