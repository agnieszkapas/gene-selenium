# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class SupplierOrderStatus(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://gene-qa.gene.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_supplier_order_status(self):
        driver = self.driver
        driver.get(self.base_url + "/about-us/suppliers/for-current-suppliers/order-status")
        driver.find_element_by_id("entry_1000000").clear()
        driver.find_element_by_id("entry_1000000").send_keys("1234")
        driver.find_element_by_id("entry_1000000").clear()
        driver.find_element_by_id("entry_1000000").send_keys("1234")
        driver.find_element_by_id("entry_1000001").clear()
        driver.find_element_by_id("entry_1000001").send_keys("1")
        driver.find_element_by_id("entry_1000001").clear()
        driver.find_element_by_id("entry_1000001").send_keys("1")
        driver.find_element_by_id("entry_1000002").clear()
        driver.find_element_by_id("entry_1000002").send_keys("1")
        driver.find_element_by_id("entry_1000002").clear()
        driver.find_element_by_id("entry_1000002").send_keys("1")
        driver.find_element_by_id("entry_1000005").clear()
        driver.find_element_by_id("entry_1000005").send_keys("1")
        driver.find_element_by_id("entry_1000005").clear()
        driver.find_element_by_id("entry_1000005").send_keys("1")
        driver.find_element_by_id("entry_1000003").clear()
        driver.find_element_by_id("entry_1000003").send_keys("12345")
        driver.find_element_by_id("entry_1000003").clear()
        driver.find_element_by_id("entry_1000003").send_keys("12345")
        driver.find_element_by_id("ss-submit").click()
        driver.find_element_by_id("ss-submit").click()
    
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
