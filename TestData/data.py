"""
Store all the data here
"""
import os


class SauceDemoData:

    url="https://www.saucedemo.com/"
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(BASE_DIR, "..", "TestData", "TestData.xlsx")
    # file_name ="C:\\Users\\leema\\PycharmProjects\\SauceDemoApplication_POM_Pytest\\TestData\\TestData.xlsx"

    # Login
    sheet_name ="LoginTest"
    user_name = "standard_user"
    password =  "secret_sauce"

    # add to cart
    sheet_name_cart = "AddToCart"

    # Checkout
    sheet_name_Checkout = "Checkout"

    #Place order
    sheet_name_place_order="PlaceOrder"