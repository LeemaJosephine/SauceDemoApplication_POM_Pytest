# conftest.py
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.drivers.edge import EdgeChromiumDriver

from TestData.data import SauceDemoData

@allure.step("Take screenshot and attach to Allure report")
def capture_screenshot(driver, step_name):
    allure.attach(
        driver.get_screenshot_as_png(),
        name=step_name,
        attachment_type=allure.attachment_type.PNG
    )

@pytest.fixture
def setup_browser():
    driver = webdriver.Edge()
              #Chrome(service=Service(ChromeDriverManager().install())))
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get(SauceDemoData.url)
    yield driver
    driver.quit()
