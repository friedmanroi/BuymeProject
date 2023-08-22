import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.business_page import Business_page
from pages.selection_page import SelectionPage


class constants():
    FIRST_NAME = "roi"
    EMAIL = "ofer123456@gmail.com"
    PASSWORD = "Ofer123456!"


class Test_end_to_end:

    def test_register_existing_client(self):
        self.login.register(constants.FIRST_NAME, constants.EMAIL, constants.PASSWORD)
        error_element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".login-error")))
        error_text = error_element.text
        expected_error_text = "דוא\"ל זה כבר קיים במערכת."
        assert error_text == expected_error_text

    def test_selection_page(self):
        self.login.login(constants.EMAIL, constants.PASSWORD)
        time.sleep(10)
        selection_page = SelectionPage(self.driver, self.wait)
        selection_page.select_sum()
        selection_page.select_category()
        selection_page.select_region()
        selection_page.submit_page()

    def test_3(self):
        pick_it = Business_page(self.driver, self.wait)
        expected_url = "https://buyme.co.il/search?budget=1&category=438&query=%D7%91%D7%92%D7%93%D7%99%D7%9D&region=11"
        current_url = self.driver.current_url
        assert current_url == expected_url, "this is the url"
        pick_it.stage3()
        time.sleep(5)
        result_element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[value='17573218']")))
        result_element.click()
        self.wait.until(EC.element_to_be_clickable((By.ID, "ember1199"))).click()
