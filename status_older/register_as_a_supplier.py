# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class RegisterAsASupplier(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://gene-qa.gene.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_register_as_a_supplier(self):
        driver = self.driver
        driver.get(self.base_url + "/about-us/suppliers/supplier-registration/company-information")
        driver.find_element_by_id("supplier_name").clear()
        driver.find_element_by_id("supplier_name").send_keys("123")
        driver.find_element_by_id("supplier_name").clear()
        driver.find_element_by_id("supplier_name").send_keys("123")
        driver.find_element_by_id("representative_name").clear()
        driver.find_element_by_id("representative_name").send_keys("1")
        driver.find_element_by_id("representative_name").clear()
        driver.find_element_by_id("representative_name").send_keys("1")
        driver.find_element_by_id("supp_address_line_1").clear()
        driver.find_element_by_id("supp_address_line_1").send_keys("742 Evergreen")
        driver.find_element_by_id("supp_address_line_1").clear()
        driver.find_element_by_id("supp_address_line_1").send_keys("742 Evergreen")
        driver.find_element_by_id("supp_city").clear()
        driver.find_element_by_id("supp_city").send_keys("Sunnydale")
        driver.find_element_by_id("supp_city").clear()
        driver.find_element_by_id("supp_city").send_keys("Sunnydale")
        driver.find_element_by_id("supp_state").clear()
        driver.find_element_by_id("supp_state").send_keys("1")
        driver.find_element_by_id("supp_state").clear()
        driver.find_element_by_id("supp_state").send_keys("1")
        driver.find_element_by_id("supp_phone").clear()
        driver.find_element_by_id("supp_phone").send_keys("800000000")
        driver.find_element_by_id("supp_phone").clear()
        driver.find_element_by_id("supp_phone").send_keys("800000000")
        driver.find_element_by_id("supp_zip").clear()
        driver.find_element_by_id("supp_zip").send_keys("123")
        driver.find_element_by_id("supp_zip").clear()
        driver.find_element_by_id("supp_zip").send_keys("123")
        driver.find_element_by_id("supp_email").clear()
        driver.find_element_by_id("supp_email").send_keys("mir-wass-d@gene.com")
        driver.find_element_by_id("supp_email").clear()
        driver.find_element_by_id("supp_email").send_keys("mir-wass-d@gene.com")
        driver.find_element_by_id("tax_id").clear()
        driver.find_element_by_id("tax_id").send_keys("123")
        driver.find_element_by_id("tax_id").clear()
        driver.find_element_by_id("tax_id").send_keys("123")
        driver.find_element_by_id("annual_dollar_volume").clear()
        driver.find_element_by_id("annual_dollar_volume").send_keys("1")
        driver.find_element_by_id("annual_dollar_volume").clear()
        driver.find_element_by_id("annual_dollar_volume").send_keys("1")
        driver.find_element_by_id("year_business_established").clear()
        driver.find_element_by_id("year_business_established").send_keys("1")
        driver.find_element_by_id("year_business_established").clear()
        driver.find_element_by_id("year_business_established").send_keys("1")
        driver.find_element_by_id("total_employees").clear()
        driver.find_element_by_id("total_employees").send_keys("1")
        driver.find_element_by_id("total_employees").clear()
        driver.find_element_by_id("total_employees").send_keys("1")
        driver.find_element_by_id("e_enabled_summary").clear()
        driver.find_element_by_id("e_enabled_summary").send_keys("123")
        driver.find_element_by_id("e_enabled_summary").clear()
        driver.find_element_by_id("e_enabled_summary").send_keys("123")
        driver.find_element_by_name("continue").click()
        driver.find_element_by_name("continue").click()
    
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
