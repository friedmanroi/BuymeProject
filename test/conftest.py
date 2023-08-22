import allure
from _pytest.nodes import Item
from _pytest.reports import TestReport
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPage


def pytest_runtest_setup(item: Item) -> None:
    item.cls.driver = webdriver.Chrome()
    item.cls.driver.get("https://buyme.co.il/")
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
