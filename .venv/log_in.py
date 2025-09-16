import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

class Dashboard(unittest.TestCase):
    def setUp(self):
        # Set up the Chrome WebDriver for each test case
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://staging.greenclinic.pk/login")
        #self.login()

    def test_login_WrongCredential(self):
        driver = self.driver
        # Example login steps
        driver.find_element(By.CSS_SELECTOR, "#email").send_keys("staging@gmail.app")
        time.sleep(3)
        driver.find_element(By.NAME, "password").send_keys("testing")
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='login-form']/div[2]/button").click()
        time.sleep(3) 
         # Wait for the toast message to appear
        toast_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Your email/number does not exist')]"))
        )

        toast_text = toast_element.text
        print(f"Toast message: {toast_text}")

        # Assertion
        self.assertEqual(toast_text.strip(), "Your email/number does not exist")

    def test_login_WrongPassword(self):
        driver = self.driver
        # Example login steps
        driver.find_element(By.CSS_SELECTOR, "#email").send_keys("staging@gmail.com")
        time.sleep(3)
        driver.find_element(By.NAME, "password").send_keys("testing")
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='login-form']/div[2]/button").click()
        time.sleep(3) 
         # Wait for the toast message to appear
        toast_elementone = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Invalid Credentials')]"))
        )

        toast_text = toast_elementone.text
        print(f"Toast message: {toast_text}")

        # Assertion
        self.assertEqual(toast_text.strip(), "Invalid Credentials")

    def test_login_Sussessfully(self):
        driver = self.driver
        # Example login steps
        driver.find_element(By.CSS_SELECTOR, "#email").send_keys("staging@gmail.com")
        time.sleep(3)
        driver.find_element(By.NAME, "password").send_keys("Testing@123")
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='login-form']/div[2]/button").click()
        time.sleep(3) 
         # Wait for the toast message to appear
        toast_elementlogin = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Logged In Successfully)]"))
        )

        toast_text = toast_elementlogin.text
        print(f"Toast message: {toast_text}")

        # Assertion
        self.assertEqual(toast_text.strip(), "Logged In Successfully")

    #def test_example(self):
        # Just a sample test to verify title
        #self.assertIn("Dashboard", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
