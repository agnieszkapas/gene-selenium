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
        driver.get("https://www.gene.com/stories/go-biotech-antiquing")
        driver.find_element_by_xpath("//div[@id='game-step-1']/div[2]/div[2]/img").click()
        driver.find_element_by_link_text("Next").click()
        driver.find_element_by_xpath("//div[@id='game-step-2']/div[2]/div[2]/div[2]").click()
        driver.find_element_by_link_text("Next").click()
        #driver.find_element_by_xpath("(//a[contains(text(),'Next')])[2]").click()
        driver.find_element_by_xpath("//div[@id='game-step-3']/div[2]/div[2]/img").click()
        driver.find_element_by_link_text("Next").click()
        #driver.find_element_by_xpath("(//a[contains(text(),'Next')])[3]").click()
        driver.find_element_by_xpath("//div[@id='game-step-4']/div[2]/div[2]/img").click()
        driver.find_element_by_link_text("Next").click()
        #driver.find_element_by_xpath("(//a[contains(text(),'Next')])[4]").click()
        driver.find_element_by_xpath("//div[@id='game-step-5']/div[2]/div[2]/img").click()
        driver.find_element_by_link_text("Next").click()
        #driver.find_element_by_xpath("(//a[contains(text(),'Next')])[5]").click()
        driver.find_element_by_xpath("//div[@id='game-step-6']/div[2]/div[2]/div[2]").click()
        driver.find_element_by_link_text("Next").click()
        #driver.find_element_by_xpath("(//a[contains(text(),'Next')])[6]").click()
        driver.find_element_by_xpath("//div[@id='game-step-7']/div[2]/div[2]/div[2]").click()
        driver.find_element_by_link_text("Next").click()
        #driver.find_element_by_xpath("(//a[contains(text(),'Next')])[7]").click()
        driver.find_element_by_xpath("//div[@id='game-step-8']/div[2]/div[2]/div[2]").click()
        driver.find_element_by_link_text("Next").click()
        #driver.find_element_by_xpath("(//a[contains(text(),'Next')])[8]").click()
        driver.find_element_by_xpath("//div[@id='game-step-9']/div[2]/div[2]/div[2]").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Finish')])[9]").click()
        driver.find_element_by_id("play-again").click()
    
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
