import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class selenium_tests(unittest.TestCase):
    def set_up(self):
        driver = webdriver.Firefox()
        driver.get("http://127.0.0.1:8000/")
        return driver

    def test_execute_button(self):
        box = self.set_up().find_element_by_id("id_name")
        box.clear()
        box.send_keys("testing")
        execute_button = box.find_elements_by_xpath("//input[@class = 'btn btn-primary' and @type = 'submit' and @value = 'Execute']")[0]
        execute_button.click()
        #current_web_url = self.set_up().current_url()
        #assertEqual(current_web_url, "http://127.0.0.1:8000")

    def test_execute_with_enter_key(self):
        box = self.set_up().find_element_by_id("id_name")
        box.clear()
        box.send_keys("testing")
        box.send_keys(Keys.RETURN)
        #current_web_url = self.set_up().current_url()
        #assertEqual(current_web_url, "http://127.0.0.1:8000")

    def test_reset_box(self):
        box = self.set_up().find_element_by_id("id_name")
        box.clear()
        box.send_keys("testing")
        reset_button = box.find_elements_by_xpath("//input[@class = 'btn btn-danger' and @type = 'button' and @value = 'Reset']")[0]
        reset_button.click()
        #current_web_url = self.set_up().current_url()
        #assertEqual(current_web_url, "http://127.0.0.1:8000")

    def test_non_existing_user(self):
        box = self.set_up().find_element_by_id("id_name")
        box.send_keys('asdafadada')
        execute_button = box.find_elements_by_xpath("//input[@class = 'btn btn-primary' and @type = 'submit' and @value = 'Execute']")[0]
        execute_button.click()
        #visible_text = execute_button.findElement(By.tagName("body")).getText();
        #assert visible_text == "USER NOT FOUND. REFRESH TO BACK"

    def test_private_existing_user(self):
        box = self.set_up().find_element_by_id("id_name")
        box.send_keys('iloretobr')
        execute_button = box.find_elements_by_xpath("//input[@class = 'btn btn-primary' and @type = 'submit' and @value = 'Execute']")[0]
        execute_button.click()
        #visible_text = self.home.findElement(By.tagName("body")).getText();
        #assert visible_text == "USER NOT FOUND. REFRESH TO BACK"


if __name__ == '__main__':
    unittest.main()
