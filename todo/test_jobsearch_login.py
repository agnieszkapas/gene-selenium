# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.chrome.options import Options

class PassJobsearchLogin(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(executable_path='/usr/lib/selenium/chromedriver', chrome_options=chrome_options)
        #self.driver.implicitly_wait(30)
        self.base_url = "https://gene.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_pass_jobsearch_login(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Now Hiring").click()
        driver.find_element_by_link_text("Find A Job").click()
        driver.find_element_by_link_text("My Jobs").click()
        driver.find_element_by_id("dialogTemplate-dialogForm-login-name1").clear()
        driver.find_element_by_id("dialogTemplate-dialogForm-login-name1").send_keys("Aga123")
        driver.find_element_by_id("dialogTemplate-dialogForm-login-password").clear()
        driver.find_element_by_id("dialogTemplate-dialogForm-login-password").send_keys("testujemy")
        driver.find_element_by_id("dialogTemplate-dialogForm-login-password").clear()       
	driver.find_element_by_id("dialogTemplate-dialogForm-login-password").send_keys("testujemy2017")
        driver.find_element_by_id("dialogTemplate-dialogForm-login-defaultCmd").click()
        driver.find_element_by_id("editTemplateMultipart-editForm-content-ftf-flowHeader-logoutAction").click()
        driver.find_element_by_css_selector("svg.header__logo").click()
    
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
