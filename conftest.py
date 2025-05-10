import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from utils.cookie_utils import save_cookies, load_cookies, get_cookie_file

def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        help="Run browsers in headless mode"
    )

@pytest.fixture(params=["chrome"])#, "firefox"])
def driver(request):
    browser = request.param
    headless = request.config.getoption("--headless")
    print(f"\n Running tests in {'headless' if headless else 'headed'} mode on {browser}.")

    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)

    # elif browser == "firefox":
    #     options = FirefoxOptions()
    #     if headless:
    #         options.add_argument("--headless")
    #     driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.wait = WebDriverWait(driver, timeout=10)

    # Navigate to base URL and handle cookies
    base_url = "https://amaderit.net/demo/hr/"
    cookie_file = get_cookie_file(browser)
    driver.get(base_url)

    if os.path.exists(cookie_file):
        load_cookies(driver, browser)
        driver.get(base_url)  # Refresh to apply cookies
        if not is_logged_in(driver):
            perform_login_and_save_cookies(driver, browser)
    else:
        perform_login_and_save_cookies(driver, browser)

    yield driver

    # Screenshot on failure
    if request.node.rep_call.failed:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{request.node.name}_{timestamp}.png")
        driver.save_screenshot(screenshot_path)
        print(f"\nScreenshot saved to: {screenshot_path}")

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Attach test result information to the test item."""
    outcome = yield
    result = outcome.get_result()
    setattr(item, f"rep_{result.when}", result)

def login(driver, username: str, password: str):
    driver.get("https://amaderit.net/demo/hr")
    driver.find_element(By.ID, "email").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[normalize-space()='Sign In']").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.XPATH, "//a[@class='aside-logo']//h2[normalize-space()='AmaderHR']"
        ))
    )

def perform_login_and_save_cookies(driver, browser_name):
    login(driver, username="12345678", password="19970204")
    save_cookies(driver, browser_name)

def is_logged_in(driver) -> bool:
    try:
        driver.wait.until(
            EC.presence_of_element_located((
                By.XPATH, "//a[@class='aside-logo']//h2[normalize-space()='AmaderHR']"
            ))
        )
        return True
    except Exception:
        return False
