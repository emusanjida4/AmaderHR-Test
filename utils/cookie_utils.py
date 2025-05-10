import json
import os


def save_cookies(driver, browser_name):
    path = get_cookie_file(browser_name)
    with open(path, "w") as file:
        json.dump(driver.get_cookies(), file, indent=4)

def load_cookies(driver, browser_name):
    path = get_cookie_file(browser_name)
    if os.path.exists(path):
        with open(path, "r") as file:
            cookies = json.load(file)
            for cookie in cookies:
                # Fix expiry format if needed
                if 'expiry' in cookie and isinstance(cookie['expiry'], float):
                    cookie['expiry'] = int(cookie['expiry'])
                driver.add_cookie(cookie)

def get_cookie_file(browser_name):
    return f"cookies_{browser_name}.json"