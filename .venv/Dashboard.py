import random
#from tkinter.tix import Select
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service  # Required for the updated Selenium versions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import datetime
import calendar
import time

class Dashboard(unittest.TestCase):

    @classmethod
    def setUp(cls):
        # Set up the Chrome WebDriver
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.get("https://staging.greenclinic.pk/login")
        
    def test_login_valid_credentials(self):
        driver = self.driver
        user_email = driver.find_element(By.CSS_SELECTOR, "#email")
        # Now send the keys to the email input
        user_email.send_keys("staging@gmail.com")
        time.sleep(2)

        user_password = driver.find_element(By.CSS_SELECTOR, "#password-field")
        user_password.send_keys("Testing@123")
        time.sleep(2)

        login_button = driver.find_element(By.CSS_SELECTOR, "#login-form > div.form-button > button")
        login_button.click()
        time.sleep(3)

        continue_button = driver.find_element(By.XPATH, "//a[contains(@class, 'contiiii_mob')]")
        continue_button.click()
        time.sleep(3)
        #self.assertTrue(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "add_appo"))), "Login failed")

       
        # Assert that we're logged in by checking if some element that appears only after login is visible
        logged_in_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "add_appo")))
        self.assertTrue(logged_in_element.is_displayed(), "Log In successfully")
        self.booking_appointment()


    def booking_appointment(self):
        driver = self.driver
        add_new_appointment= driver.find_element(By.CLASS_NAME, "add_appo")
        add_new_appointment.click()
         # Ensure that we're on the dashboard after login
        #add_new_appointment = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "add_appo")))
        #add_new_appointment.click()
        time.sleep(2)
        random_phone_number = "3" + ''.join([str(random.randint(0, 9)) for _ in range(9)])
        phone_number = driver.find_element(By.CSS_SELECTOR, "#mob-num")
        phone_number.send_keys(random_phone_number)
        time.sleep(2)

        random_name = random.choice(["John", "Jane", "Alice", "Bob", "Emily", "Michael", "Sara", "David"])
        name = driver.find_element(By.CSS_SELECTOR, "#fname")
        name.send_keys(random_name)
        time.sleep(2)

        date = driver.find_element(By.CSS_SELECTOR, "#datepickerApps")
        date.click()
        time.sleep(2)

       # Get today's date
        today = datetime.datetime.now().day

        # Use XPath to find today's date dynamically in the datepicker
        today_date_xpath = f"//*[@id='ui-datepicker-div']/table/tbody//a[text()='{today}']"

        # Find and click today's date using the dynamically generated XPath
        today_date = driver.find_element(By.XPATH, today_date_xpath)
        today_date.click()
        time.sleep(2)

        # Locate the dropdown element
        dropdown = driver.find_element(By.XPATH, "//*[@id='time']")
        dropdown.click()
        time.sleep(2)
        dropdown_selection = driver.find_element(By.XPATH, "//*[@id='time']/option[17]")
        dropdown_selection.click()
        time.sleep(2)

        gender = driver.find_element(By.CSS_SELECTOR, "#female")
        gender.click()
        time.sleep(2)

        random_age = random.choice(["20", "18", "25", "35", "40", "48", "54", "63"])
        age = driver.find_element(By.CSS_SELECTOR, "#age")
        age.send_keys(random_age)
        time.sleep(2)

        appointment_save = driver.find_element(By.CSS_SELECTOR, "#app-save")
        appointment_save.click()
        time.sleep(2)

        today_appointment_tile = driver.find_element(By.XPATH,"//*[@id='body-row']/div[3]/div/main/div/div[2]/div[1]/a/div[2]")
        if today_appointment_tile:
            print("update")
        else:
            print("not update")

            time.sleep(2)
            

        self.Add_invoice()

    def Add_invoice(self):
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
        
        self.consult_now()

    def consult_now(self):
        driver = self.driver
        consult_now_button = driver.find_element(By.CSS_SELECTOR,"#body-table > tr.odd > td:nth-child(10) > div > div > a.button.btn-text.blue-btn")
        consult_now_button.click()
        time.sleep(2)

        b_p = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div/main/div/div[2]/div[2]/form/div/div[1]/div/div[1]/div/div/div/ul/li[1]/div/div/div/input")
        b_p.send_keys("120/80")
        time.sleep(2)
        Temp = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div/main/div/div[2]/div[2]/form/div/div[1]/div/div[1]/div/div/div/ul/li[2]/div/div/div/input")
        Temp.send_keys("100")
        height = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/main/div/div[2]/div[2]/form/div/div[1]/div/div[1]/div/div/div/ul/li[3]/div/div/div/input")
        height.send_keys("76")
        weight = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div/main/div/div[2]/div[2]/form/div/div[1]/div/div[1]/div/div/div/ul/li[4]/div/div/div/input")
        weight.send_keys("108")
        present_complains = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div/main/div/div[2]/div[2]/form/div/div[1]/div/div[1]/div/div/div/ul/li[5]/div/textarea")
        present_complains.send_keys("Heart burn, Body pain, High Blood pressure")
        Clinical_Notes = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div/main/div/div[2]/div[2]/form/div/div[1]/div/div[1]/div/div/div/ul/li[6]/div/textarea")
        Clinical_Notes.send_keys("Heart burn, Body pain, High Blood pressure")
        b_p2 = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div/main/div/div[2]/div[2]/form/div/div[1]/div/div[1]/div/div/div/ul/li[7]/div/div/div/input")
        b_p2.send_keys("120/80")
        Temp2 = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div/main/div/div[2]/div[2]/form/div/div[1]/div/div[1]/div/div/div/ul/li[8]/div/div/div/input")
        Temp2.send_keys("100")
        height2 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/main/div/div[2]/div[2]/form/div/div[1]/div/div[1]/div/div/div/ul/li[9]/div/div/div/input")
        height2.send_keys("76")
        weight2 = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div/main/div/div[2]/div[2]/form/div/div[1]/div/div[1]/div/div/div/ul/li[10]/div/div/div/input")
        weight2.send_keys("108")
        time.sleep(2)

        medication_tab = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div/main/div/div[2]/div[2]/div[1]/ul/li[2]/a")
        medication_tab.click()
        time.sleep(3)
        select_medicine = driver.find_element(By.CSS_SELECTOR,"#select2-choose-med1-container > span")
        select_medicine.click()
        time.sleep(3)
        select_medicine_option = driver.find_element(By.XPATH,"/html/body/span[2]/span/span[2]")
        random_option = random.choice(select_medicine_option)
        random_option.click()

    @classmethod
    def tearDown(cls):
    # Close the browser after the test
        cls.driver.quit()   
if __name__ == "__main__":
    unittest.main()   