# conftest.py
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager

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
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Edge(options=options)
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get(SauceDemoData.url)
    yield driver
    driver.quit()

    #driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    #driver = webdriver.Edge()
    #Chrome(service=Service(ChromeDriverManager().install())))
