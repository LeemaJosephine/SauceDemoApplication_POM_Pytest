import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

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

    # Jenkins safe options
    #
    # options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.implicitly_wait(25)
    driver.get(SauceDemoData.url)

    yield driver

    driver.quit()