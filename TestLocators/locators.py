"""
Contains all the locators
"""

class SauceDemoLocators:
    username_locator ="user-name" #id
    password_locator = "password" #id
    submit_locator = "login-button" #id

    # validate login
    product_page ="//span[text()='Products']" #xpath
    login_error ="//h3[@data-test='error']" #xpath

    # Adding Item to cart
    add_item1 ="(//div[text()='Sauce Labs Backpack']/following::button)[1]" #xpath
    add_item2 ="(//div[text()='Sauce Labs Bike Light']/following::button)[1]" #xpath
    add_item3 ="(//div[text()='Sauce Labs Bolt T-Shirt']/following::button)[1]" #xpath

    cart_badge = "shopping_cart_badge" #classname
    cart ="shopping_cart_link" #classname

    # Cart page
    checkout = "checkout" #id

    # Checkout page
    firstname="first-name" #id
    lastname="last-name" #id
    postal_code="postal-code" #id
    error = "//h3[@data-test='error']" #xpath
    validate = "//span[text()='Checkout: Overview']" #xpath
    continue_button="continue" #id

    #Checkout overview

    finish_button ="finish" #id
    thank_you ="//h2[@class='complete-header']" #xpath
    back ="back-to-products" #id