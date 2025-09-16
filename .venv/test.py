import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service  # Required for the updated Selenium versions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import time
class LoginTest(unittest.TestCase):

    def setUp(self):
        # Set up the Chrome WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://staging.greenclinic.pk/login")
        
    def test_login_valid_credentials(self):
        driver = self.driver
        user_email = driver.find_element(By.CSS_SELECTOR, "#email")
        # Now send the keys to the email input
        user_email.send_keys("junaid")
        driver.implicitly_wait(5)

        user_password = driver.find_element(By.CSS_SELECTOR, "#password-field")
        user_password.send_keys("testing123")
        driver.implicitly_wait(7)

        login_button = driver.find_element(By.CSS_SELECTOR, "#login-form > div.form-button > button")
        login_button.click
        driver.implicitly_wait(7)

       
        #expected_url = "https://staging.greenclinic.pk/select-clinic"  # Replace with the actual dashboard URL
        #self.assertEqual(driver.current_url, expected_url)
        #self.assertIn("Green Clinic-EMR Software", driver.title)

    def test_login_invalid_credentials(self):
        driver = self.driver
        user_email = driver.find_element(By.CSS_SELECTOR, "#email")
        # Now send the keys to the email input
        user_email.send_keys("junaid")
        driver.implicitly_wait(5)

        user_password = driver.find_element(By.CSS_SELECTOR, "#password-field")
        user_password.send_keys("testing12")
        driver.implicitly_wait(7)

        login_button = driver.find_element(By.CSS_SELECTOR, "#login-form > div.form-button > button")
        login_button.click
        driver.implicitly_wait(7)

        #error_message = WebDriverWait(driver, 10).until(
        #EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toastify.on.info.toastify-center.toastify-top"))
        #)

        # Print the actual error message text for debugging purposes
        #print("Error Message: ", error_message.text)

        # Assert that the error message contains "Invalid Credentials"
        #self.assertIn("Invalid Credentials", error_message.text)
        
    


    def tearDown(self):
    # Close the browser after the test
        self.driver.quit()

       
       
if __name__ == "__main__":
    unittest.main()   



# Print page title
#   print(driver.title)

# Close the browser

