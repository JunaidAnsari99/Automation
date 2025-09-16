import random
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time
from selenium.webdriver.chrome.service import Service

class Dashboard(unittest.TestCase):

    def setUp(self):
        # Set up the Chrome WebDriver for each test case
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://staging.greenclinic.pk/login")
        self.login()

    def login(self):
        """Perform login."""
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, "#email").send_keys("staging@gmail.com")
        driver.find_element(By.CSS_SELECTOR, "#password-field").send_keys("Testing@123")
        driver.find_element(By.CSS_SELECTOR, "#login-form > div.form-button > button").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[contains(@class, 'contiiii_mob')]").click()
        time.sleep(2)

    def test_login_valid_credentials(self):
        driver = self.driver
        # Check if login was successful
        logged_in_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "add_appo"))
        )
        self.assertTrue(logged_in_element.is_displayed(), "Login was not successful")

    def test_booking_appointment(self):
        driver = self.driver
        # Booking an appointment
        driver.find_element(By.CLASS_NAME, "add_appo").click()
        time.sleep(2)

        # Random Phone and Name for Testing
        random_phone_number = "3" + ''.join([str(random.randint(0, 9)) for _ in range(9)])
        driver.find_element(By.CSS_SELECTOR, "#mob-num").send_keys(random_phone_number)
        time.sleep(1)
        random_name = random.choice(["John", "Jane", "Alice", "Bob", "Emily", "Michael", "Sara", "David"])
        driver.find_element(By.CSS_SELECTOR, "#fname").send_keys(random_name)
        time.sleep(1)

        # Selecting today's date
        driver.find_element(By.CSS_SELECTOR, "#datepickerApps").click()
        today_date_xpath = f"//*[@id='ui-datepicker-div']/table/tbody//a[text()='{datetime.datetime.now().day}']"
        driver.find_element(By.XPATH, today_date_xpath).click()
        time.sleep(1)

        # Time slot selection and gender
        driver.find_element(By.XPATH, "//*[@id='time']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='time']/option[17]").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "#female").click()

        # Enter age and save appointment
        driver.find_element(By.CSS_SELECTOR, "#age").send_keys(str(random.randint(18, 65)))
        driver.find_element(By.CSS_SELECTOR, "#app-save").click()
        time.sleep(2)

        # Confirm appointment save
        appointment_tile = driver.find_element(By.XPATH, "//*[@id='body-row']/div[3]/div/main/div/div[2]/div[1]/a/div[2]")
        self.assertTrue(appointment_tile.is_displayed(), "Appointment tile was not updated.")
        self.test_add_invoice()

    def test_add_invoice(self):
        
        driver = self.driver
        add_invoice_button = driver.find_element(By.CSS_SELECTOR,"#body-table > tr > td:nth-child(10) > div > div > a.button.btn-text.green-btn.invoiceModal")
        add_invoice_button.click()
        time.sleep(2)

        add_amount = driver.find_element(By.CSS_SELECTOR, "#amount_recv-invoice")
        add_amount.send_keys("1000")
        time.sleep(1)

        add_invoice_button_save = driver.find_element(By.CSS_SELECTOR, "#invoiceForm > div.modal-footer > button.green-main-btn.InvoiceFormSubmit.save_add_invoice")
        add_invoice_button_save.click()
        time.sleep(2)
        


    def test_consult_now(self):
        driver = self.driver
        # Start Consultation
        driver.find_element(By.CSS_SELECTOR, "#body-table > tr.odd > td:nth-child(10) > div > div > a.button.btn-text.blue-btn").click()
        time.sleep(1)

        # Inputting health stats
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/main/div/div[2]/div[2]/form/div/div[1]/div/div[1]/div/div/div/ul/li[1]/div/div/div/input").send_keys("120/80")
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/main/div/div[2]/div[2]/form/div/div[1]/div/div[1]/div/div/div/ul/li[2]/div/div/div/input").send_keys("100")
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/main/div/div[2]/div[2]/form/div/div[1]/div/div[1]/div/div/div/ul/li[3]/div/div/div/input").send_keys("76")
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/main/div/div[2]/div[2]/form/div/div[1]/div/div[1]/div/div/div/ul/li[4]/div/div/div/input").send_keys("108")
        time.sleep(1)

        # Switch to Medication Tab
        medication_tab = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/main/div/div[2]/div[2]/div[1]/ul/li[2]/a")
        medication_tab.click()
        time.sleep(2)
        choosen_med = driver.find_element(By.CSS_SELECTOR,"#select2-choose-med1-container > span")
        choosen_med.click()
        time.sleep(1)
        serach_bar = driver.find_element(By.CSS_SELECTOR,"body > span.select2-container.select2-container--default.select2-container--open > span > span.select2-search.select2-search--dropdown > input")
        serach_bar.send_keys("capto")
        time.sleep(3)
        med_name = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div/main/div/div[2]/div[2]/form/div/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div/span/span[1]/span/span[1]")
        med_name.click()
        time.sleep(2)


        


    def tearDown(self):
        # Close the browser after each test
        self.driver.quit()

#if __name__ == "__main__":
#    unittest.main()
if __name__ == "__main__":
    # Run a single test case
    suite = unittest.TestSuite()
    suite.addTest(Dashboard("test_consult_now"))
    runner = unittest.TextTestRunner()
    runner.run(suite)