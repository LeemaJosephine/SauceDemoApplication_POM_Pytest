"""
Test execution happens here
"""
import allure
import pytest

from PageObjects.HomePage import  HomePage1
from PageObjects.ProductPage import ProductPage1
from PageObjects.CartPage import CartPage1
from PageObjects.CheckoutPage import CheckoutPage1
from PageObjects.PlaceOrderPage import PlaceOrderPage1
from TestData.data import SauceDemoData
from Utilities.excel_functions import  ExcelFunction

# Reading data from excel
excel = ExcelFunction(SauceDemoData.file_name, SauceDemoData.sheet_name_place_order)
cart_data = excel.get_data_from_excel()

class TestCheckout :

    @pytest.mark.smoke
    @allure.feature("Place Order Feature")
    @allure.story("Validate Place order")
    @pytest.mark.parametrize("username,password,firstname,lastname,postalcode,test_type,exp,expected,result", cart_data)
    def test_order(self,setup_browser,username,password,firstname,lastname,postalcode,test_type,exp,expected,result):
            driver = setup_browser
            assert HomePage1(driver).login(username, password, test_type,exp) == True
            assert ProductPage1(driver).add_item_to_cart() == True
            assert CartPage1(driver).checkout() == True
            assert CheckoutPage1(driver).checkout_details(firstname,lastname,postalcode,test_type,expected) == True
            assert PlaceOrderPage1(driver).place_order(test_type,result) == True
            print("SUCCESS: Order Placed")