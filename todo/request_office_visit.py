# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class RequestOfficeVisit(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://gene-qa.gene.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_request_office_visit(self):
        driver = self.driver
        driver.get(self.base_url + "/medical-professionals/medinfo/request-office-visit")
        driver.find_element_by_id("firstName").clear()
        driver.find_element_by_id("firstName").send_keys("John")
        driver.find_element_by_id("firstName").clear()
        driver.find_element_by_id("firstName").send_keys("John")
        driver.find_element_by_id("lastName").clear()
        driver.find_element_by_id("lastName").send_keys("John")
        driver.find_element_by_id("lastName").clear()
        driver.find_element_by_id("lastName").send_keys("John")
        driver.find_element_by_id("streetAddress").clear()
        driver.find_element_by_id("streetAddress").send_keys("742 Evergreen Terrace")
        driver.find_element_by_id("streetAddress").clear()
        driver.find_element_by_id("streetAddress").send_keys("742 Evergreen Terrace")
        driver.find_element_by_id("aptSuite").clear()
        driver.find_element_by_id("aptSuite").send_keys("1")
        driver.find_element_by_id("aptSuite").clear()
        driver.find_element_by_id("aptSuite").send_keys("1")
        driver.find_element_by_id("city").clear()
        driver.find_element_by_id("city").send_keys("Sunnydale")
        driver.find_element_by_id("city").clear()
        driver.find_element_by_id("city").send_keys("Sunnydale")
        driver.find_element_by_id("zip").clear()
        driver.find_element_by_id("zip").send_keys("123")
        driver.find_element_by_id("zip").clear()
        driver.find_element_by_id("zip").send_keys("123")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("mir-wass-d@gene.com")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("mir-wass-d@gene.com")
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("80000000")
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("80000000")
        driver.find_element_by_id("appointmentBy").click()
        driver.find_element_by_link_text("11").click()
        driver.find_element_by_link_text("11").click()
        driver.find_element_by_id("subject").clear()
        driver.find_element_by_id("subject").send_keys("123")
        driver.find_element_by_id("subject").clear()
        driver.find_element_by_id("subject").send_keys("123")
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
