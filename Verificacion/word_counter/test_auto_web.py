from django.test import TestCase
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class selenium_tests(TestCase):
    def set_up(self):
        driver = webdriver.Firefox(executable_path= r'C:\Django projects\Prueba\Verificacion\geckodriver\geckodriver.exe')
        driver.get("http://127.0.0.1:8000/")
        return driver

    def test_execute_button(self):
        box = self.set_up().find_element_by_id("id_name")
        box.clear()
        box.send_keys("testing")
        execute_button = box.find_elements_by_xpath("//input[@class = 'btn btn-primary' and @type = 'submit' and @value = 'Execute']")[0]
        execute_button.click()

    def test_execute_with_enter_key(self):
        box = self.set_up().find_element_by_id("id_name")
        box.clear()
        box.send_keys("testing")
        box.send_keys(Keys.RETURN)

    def test_non_existing_user(self):
        box = self.set_up().find_element_by_id("id_name")
        box.send_keys('asdafadada')
        execute_button = box.find_elements_by_xpath("//input[@class = 'btn btn-primary' and @type = 'submit' and @value = 'Execute']")[0]
        execute_button.click()

    def test_private_existing_user(self):
        box = self.set_up().find_element_by_id("id_name")
        box.send_keys('iloretobr')
        execute_button = box.find_elements_by_xpath("//input[@class = 'btn btn-primary' and @type = 'submit' and @value = 'Execute']")[0]
        execute_button.click()
