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

    # 🔥 MUST for Jenkins
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--window-size=1920,1080")

    service = Service("C:\\WebDrivers\\msedgedriver.exe")

    driver = webdriver.Edge(service=service, options=options)

    # driver = webdriver.Edge(options=options)
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get(SauceDemoData.url)
    yield driver
    driver.quit()

    #driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    #driver = webdriver.Edge()
    #Chrome(service=Service(ChromeDriverManager().install())))
