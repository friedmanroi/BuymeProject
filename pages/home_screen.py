import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
class HomeScreen:
    def __init__(self,wait,driver):
        self.driver = driver
        self.wait = wait
        self.press_price = (By.CLASS_NAME,"selected-name")


    def press_price(self):
        self.wait.until(EC.element_to_be_clickable(self.press_price())).click()
        self.dropdown = Select(self.press_price())
        self.dropdown.select_by_index(1)
        time.sleep(5)
