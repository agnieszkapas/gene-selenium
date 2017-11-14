# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.chrome.options import Options

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(executable_path='/usr/lib/selenium/chromedriver', chrome_options=chrome_options)
        #self.driver.implicitly_wait(30)
        self.base_url = "https://gene.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://www.gene.com/medical-professionals/pipeline")
        driver.find_element_by_xpath("//div[3]/ul/li").click()
        driver.find_element_by_xpath("//div[3]/ul/li[4]").click()
        driver.find_element_by_xpath("//div[3]/ul/li[7]").click()
        driver.find_element_by_xpath("//div[3]/ul/li[2]").click()
        driver.find_element_by_xpath("//div[3]/ul/li[5]").click()
        driver.find_element_by_xpath("//div[3]/ul/li[3]").click()
        driver.find_element_by_xpath("//div[3]/ul/li[6]").click()
        driver.find_element_by_xpath("//li[8]").click()
        self.assertEqual("Rigorous and groundbreaking science has always been at the core of what we do at Genentech. Our R&D activities are focused on applying excellent science to discover and develop potential new medicines with the goal of becoming first-in-class or best-in-class therapeutics.", driver.find_element_by_xpath("//div/").text)
    
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
