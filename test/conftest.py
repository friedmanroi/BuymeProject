import json
from pathlib import Path

import allure
from _pytest.nodes import Item
from _pytest.reports import TestReport
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPage


def pytest_runtest_setup(item: Item) -> None:
    json_path = Path(Path(__file__).absolute().parent.parent, "pages", "driver.json")

    with open(json_path) as json_file:
        data = json.load(json_file)

    if 'browser' in data:
        if data['browser'] == 'chrome':
            item.cls.driver = webdriver.Chrome()
        elif data['browser'] == 'firefox':
            item.cls.driver = webdriver.Firefox()
        else:
            raise ValueError("Invalid driver specified in driver.json")
    else:
        raise KeyError("Driver not specified in driver.json")
    item.cls.driver.get(data['url'])
    item.cls.wait = WebDriverWait(item.cls.driver, 20)
    item.cls.login = LoginPage(item.cls.driver, item.cls.wait)

def pytest_exception_interact(node: Item, report: TestReport) -> None:
    if not report.failed:
        return
    allure.attach(
        body=node.cls.driver.get_screenshot_as_png(),
        name="Full Page Screenshot",
        attachment_type=allure.attachment_type.PNG,
    )
