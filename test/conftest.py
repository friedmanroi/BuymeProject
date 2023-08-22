from _pytest.nodes import Item
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.login_page import LoginPage


def pytest_runtest_setup(item: Item) -> None:
    item.cls.driver = webdriver.Chrome()
    item.cls.driver.get("https://buyme.co.il/")
    item.cls.wait = WebDriverWait(item.cls.driver, 20)
    item.cls.login = LoginPage(item.cls.driver, item.cls.wait)
