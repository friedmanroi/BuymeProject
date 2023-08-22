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

    def test_select_gift(self):
        self.login.login(constants.EMAIL, constants.PASSWORD)
        time.sleep(10)
        selection_page = SelectionPage(self.driver, self.wait)
        selection_page.select_sum()
        selection_page.select_category()
        selection_page.select_region()
        selection_page.submit_page()
        self.wait.until(EC.element_to_be_clickable((By.ID, "ember1199"))).click()
        time.sleep(5)

        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".bm-subtitle-1")))[0].click()

        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[placeholder='הכנס סכום']"))).send_keys("50")

        # Wait for the presence of all elements with type "submit" and click the first one
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[type=submit]")))[0].click()

        time.sleep(5)

        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".bm-subtitle-1")))[0].click()

        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[placeholder='הכנס סכום']"))).send_keys("50")

        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[type=submit]")))[0].click()

        time.sleep(5)
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-parsley-required-message='מי הזוכה המאושר? יש להשלים את שם המקבל/ת']"))).send_keys("zohar")

# Wait for the element with title "לאיזה אירוע?" to be visible and click it
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[title='לאיזה אירוע?']"))).click()

        time.sleep(5)

# Wait for the presence of all elements with value "10" and click the second one (index 1)
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[value='10']")))[1].click()

# Wait for the element with data-parsley-group "voucher-greeting" to be visible and clear it, then send keys "mazal tov"
        greeting_element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-parsley-group='voucher-greeting']")))
        greeting_element.clear()
        greeting_element.send_keys("mazal tov")

        # Upload a file
        self.driver.find_element(By.CSS_SELECTOR, "input[name=logo]").send_keys("test/dog.jpg")

        # Wait for the element with type "submit" to be visible and click it
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[type=submit]"))).click()

        # Wait for the element with gtm "עכשיו" to be visible and click it
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[gtm='עכשיו']"))).click()

        # Wait for the element with gtm "method-sms" to be visible and click it
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[gtm='method-sms']"))).click()

        # Wait for the element with placeholder "נייד מקבל/ת המתנה" to be visible, clear it, and send keys "0542281191"
        mobile_element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[placeholder='נייד מקבל/ת המתנה']")))
        mobile_element.clear()
        mobile_element.send_keys("0542281191")

        # Wait for the element with placeholder "שם שולח המתנה" to be visible, clear it, and send keys "moran"
        sender_element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[placeholder='שם שולח המתנה']")))
        sender_element.clear()
        sender_element.send_keys("roi")

        # Wait for the element with placeholder "מספר נייד" to be visible, clear it, and send keys "0542281191"
        mobile_number_element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[placeholder='מספר נייד']")))
        mobile_number_element.clear()
        mobile_number_element.send_keys("0542281191")
        time.sleep(5)