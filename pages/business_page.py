import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage

class Business_page(BasePage):
    def __init__(self, driver, wait):
        super()._init_(driver, wait)
        self.press_business = (By.CSS_SELECTOR, 'span.name[andiallelmwithtext="16"]')
        self.pick_price = (By.CSS_SELECTOR, 'input[data-parsley-min="1"][data-parsley-max="1001"]')
        self.press_button = (By.CSS_SELECTOR,'button[id="ember6611"][type="submit"][gtm="בחירה"][uabtn="true"]')
    def stage3(self):
        self.wait.until(EC.element_to_be_clickable(self.press_business)).click()
        time.sleep(5)
        price = self.wait.until(EC.element_to_be_clickable(self.pick_price))
        price.click()
        price.send_keys("95")
        button = self.wait.until(EC.element_to_be_clickable(self.press_button))
        button.click()
        time.sleep(3)



