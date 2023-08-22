from pages.base_page import BasePage
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SelectionPage(BasePage):
    def __init__(self, driver, wait):
        super()._init_(driver, wait)

    def select_sum(self):
        sum_element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[alt='סכום']")))
        sum_element.click()
        time.sleep(1)
        sum_values = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[value='1']")))
        sum_values[1].click()

    def select_region(self):
        region_element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[alt='אזור']")))
        region_element.click()
        time.sleep(5)
        region_values = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[value='11']")))
        region_values[1].click()

    def select_category(self):
        category_element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[alt='קטגוריה']")))
        category_element.click()
        category_values = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[value='358']")))
        category_values[1].click()

    def submit_page(self):
        search_input = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='איזו מתנה תרצו לחפש?']")))
        search_input.send_keys("בגדים")
