from unittest import TestCase
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities




class testTestwithnewaccount(TestCase):
  def setUp(self):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  
  
  def test_testwithnewaccount(self):
    self.driver.get("http://127.0.0.1:8000/pongchilling/")
    self.driver.set_window_size(970, 1032)
    self.driver.find_element(By.NAME, "userName").click()
    self.driver.find_element(By.NAME, "userName").send_keys("nicolas12")
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys("nicolas")
    self.driver.find_element(By.CSS_SELECTOR, ".brickValidation").click()
    self.driver.find_element(By.NAME, "oui").click()


  def tearDown(self):
    self.driver.quit()

# a = TestTestwithnewaccount()
# a.setup_method()
# a.test_testwithnewaccount()
# a.teardown_method()