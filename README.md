# SauceDemoApplication_POM_Pytest

A robust **Page Object Model (POM)** + **Selenium WebDriver (Python)** + **PyTest** based automation framework for the SauceDemo web application.  
This project demonstrates end-to-end test automation, modular framework design, configurable test data, and maintainable code, ideal for showcasing Automation skills.

---

##  Tech Stack & Tools

- **Python 3.x**  
- **Selenium WebDriver**  
- **PyTest**  
- **Page Object Model (POM)** design pattern  
- **pytest.ini** – Global PyTest configuration  
- **JSON / Test Data files** – External test data  
- **Utilities / Helpers** – Config reader, driver setup, custom waits, etc.  
- **Reports** – Test report folder (HTML / Allure)  
- **Git & GitHub** – Version control & code hosting  

---

##  Project Structure

```
SauceDemoApplication_POM_Pytest/
│
├── PageObjects/                                          # Page classes → locators + actions
│ ├── LoginPage.py
│ ├── HomePage.py
│ └── CartPage.py
│ └── ProductPage.py
| └── PlaceOrderPage.py
| └── CheckoutPage.py
|
├── TestScripts/                                          # All test cases (PyTest)
│ ├── test_login.py
│ ├── test_add_to_cart.py
│ └── test_checkout.py
| └── test_place_order.py
│
├── TestData/                                            # External test data files
│ └── data.py
| └── TestData.xlsx
│
├── TestLocators
| └── locators.py
|
├── Utilities/                                           # Utility/helper modules
│ └── excel_functions.py
│
├── Reports/                                             # Test execution reports (HTML / Allure)
│
├── conftest.py # PyTest fixtures (setup/teardown)
├── requirements.txt # Python dependencies
├── pytest.ini # Global PyTest configuration
└── README.md # Project documentation

```

##  Features / What this Framework Provides

- **Modular design using POM** — Page classes cleanly separate locators and page methods for maintainability.  
- **PyTest-based test suite** — Easily add, manage, and run test cases with fixtures, parametrization, and configurations.  
- **Externalized test data** — Excel sheet for test data, keeps test logic separate from data.  
- **Configurable driver setup & utilities** — Manage driver initialization, custom waits, config reading centrally via Utilities folder.  
- **Clean reporting support** — Reports folder set up for HTML or other report generation after test execution.  
- **Scalable & extendable** — You can easily add more PageObjects, test scripts, utilities, or integrations (API, CI/CD) without breaking structure. 
---

##  Setup & Execution

### **1. Clone the repository**
```bash
git clone https://github.com/LeemaJosephine/SauceDemoApplication_POM_Pytest.git
cd SauceDemoApplication_POM_Pytest
```
### **2. Install dependencies**
```bash
pip install -r requirements.txt
```
### **3. Run tests**

### Run all tests:
```bash
pytest -v

```
### Run a specific test:
```bash
pytest TestScripts/test_login.py -v

```
### **After execution, check Reports/ folder for HTML or configured report results**

## **Test Cases Covered**
```
1. Login functionality
2. Add product(s) to cart
3. Product details validation
4. Cart operations: add / remove
5. Checkout process
6. Logout 
```
