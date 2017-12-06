# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.chrome.options import Options

class ContactCorporateGiving(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(executable_path='/usr/lib/selenium/chromedriver', chrome_options=chrome_options)
        #self.driver.implicitly_wait(30)
        self.base_url = "https://gene.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_contact_corporate_giving(self):
        driver = self.driver
        driver.get(self.base_url + "/good/giving/corporate-giving/contact-us")
        driver.find_element_by_id("firstName").clear()
        driver.find_element_by_id("firstName").send_keys("John")
        driver.find_element_by_id("firstName").clear()
        driver.find_element_by_id("firstName").send_keys("John")
        driver.find_element_by_id("lastName").clear()
        driver.find_element_by_id("lastName").send_keys("John")
        driver.find_element_by_id("lastName").clear()
        driver.find_element_by_id("lastName").send_keys("John")
        driver.find_element_by_id("emailAddress").clear()
        driver.find_element_by_id("emailAddress").send_keys("mir-wass-d@gene.com")
        driver.find_element_by_id("emailAddress").clear()
        driver.find_element_by_id("emailAddress").send_keys("mir-wass-d@gene.com")
        driver.find_element_by_id("phoneNumber").clear()
        driver.find_element_by_id("phoneNumber").send_keys("123456788")
        driver.find_element_by_id("phoneNumber").clear()
        driver.find_element_by_id("phoneNumber").send_keys("123456788")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("John")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("John")
        driver.find_element_by_id("grantNumber").clear()
        driver.find_element_by_id("grantNumber").send_keys("1")
        driver.find_element_by_id("grantNumber").clear()
        driver.find_element_by_id("grantNumber").send_keys("1")
        driver.find_element_by_id("description").clear()
        driver.find_element_by_id("description").send_keys("1")
        driver.find_element_by_id("description").clear()
        driver.find_element_by_id("description").send_keys("1")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_id("submit").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
	unittest.main()
