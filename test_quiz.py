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
        driver.get("https://www.gene.com/stories/quiz-breast-cancer")
        driver.find_element_by_xpath("//section[3]/div/div/div/div/div[3]/div").click()
        driver.find_element_by_xpath("//section[4]/div/div/div/div/div[2]/div").click()
        driver.find_element_by_xpath("//section[5]/div/div/div/div/div[2]/div").click()
        driver.find_element_by_xpath("//section[6]/div/div/div/div/div[2]/div").click()
        driver.find_element_by_xpath("//section[8]/div/div/div/div/div[2]/div").click()
        driver.find_element_by_xpath("//section[10]/div/div/div/div/div[3]/div").click()
        driver.find_element_by_xpath("//section[12]/div/div/div/div/div[2]/div").click()
        self.assertEqual("Take It Again", driver.find_element_by_xpath("//section[15]/div/div/div/div/a/span").text)
    
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
