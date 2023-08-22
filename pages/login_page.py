import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver, wait):
        super()._init_(driver, wait)
        self.press_registration = (By.XPATH,("//span[@andiallelmwithtext='14' and contains(text(), 'כניסה / הרשמה')]"))
        self.elements_with_placeholder = (By.CSS_SELECTOR, "[placeholder]")
        self.policy_agreement = (By.TAG_NAME, "circle")

    def register(self, FIRST_NAME, EMAIL, PASSWORD):
        self.wait.until(EC.element_to_be_clickable(self.press_registration)).click()
        self.click_on_login_link()

        # Fill in the registration form
        elements_with_placeholder = self.driver.find_elements(*self.elements_with_placeholder)
        elements_with_placeholder[0].send_keys(FIRST_NAME)
        elements_with_placeholder[1].send_keys(EMAIL)
        elements_with_placeholder[2].send_keys(PASSWORD)
        elements_with_placeholder[3].send_keys(PASSWORD)

        # Click the policy agreement checkbox
        PolicyAgreement = self.wait.until(EC.element_to_be_clickable(self.policy_agreement))
        PolicyAgreement.click()

        # Submit the registration form
        Submit1 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "ember1948")))
        Submit1.click()
        time.sleep(5)

    def click_on_login_link(self):
        login_link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".notSigned")))
        login_link.click()

    def login(self,email, password):
        self.click_on_login_link()
        time.sleep(5)
        placeholders = self.driver.find_elements(By.CSS_SELECTOR, "[placeholder]")
        placeholders[0].send_keys(email)
        placeholders[1].send_keys(password)
        submit_buttons = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "[type=submit]")))
        submit_buttons[0].click()
        time.sleep(5)