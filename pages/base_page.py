from typing import Tuple, Union

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains, Chrome, Edge, Firefox
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import (
    StaleElementReferenceException,
)
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Wrapper for selenium operations"""

    def _init_(self, driver: Union[Chrome, Firefox, Edge], wait: WebDriverWait):
        self.driver = driver
        self.wait = wait