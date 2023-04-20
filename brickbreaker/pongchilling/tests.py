from unittest import TestCase
from . import DBFunctions as DBF
import time
import json
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities







# class testTestwithnewaccount(TestCase):
#   def setUp(self):
#     self.driver = webdriver.Firefox()
#     self.vars = {}
  
  
  
#   def test_testwithnewaccount(self):
#     a = DBFunctions.searchSave("test_selenium01")
#     if(a!=None):
#         DBFunctions.deleteByUsername("test_selenium01")
#     self.driver.get("http://127.0.0.1:8000/pongchilling/")
#     self.driver.set_window_size(970, 1032)
#     self.driver.find_element(By.NAME, "userName").click()
#     self.driver.find_element(By.NAME, "userName").send_keys("test_selenium01")
#     self.driver.find_element(By.NAME, "password").click()
#     self.driver.find_element(By.NAME, "password").send_keys("test_selenium01")
#     self.driver.find_element(By.CSS_SELECTOR, ".brickValidation").click()
#     self.driver.find_element(By.NAME, "oui").click()


#   def tearDown(self):
#     self.driver.quit()


# class testTestwithotheraccount(TestCase):
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.vars = {}
  
  
#     def test_testwithotheraccount(self):
#         self.driver.get("http://127.0.0.1:8000/pongchilling/")
#         self.driver.set_window_size(970, 1032)
#         self.driver.find_element(By.NAME, "userName").click()
#         self.driver.find_element(By.NAME, "userName").send_keys("test_selenium01")
#         self.driver.find_element(By.NAME, "password").click()
#         self.driver.find_element(By.NAME, "password").send_keys("test_selenium01")
#         self.driver.find_element(By.CSS_SELECTOR, ".brickValidation").click()

#     def tearDown(self):
#         self.driver.quit()    

class Tests_DB(TestCase):

  def setUp(self) -> None:
    DBF.createUser("Test1","Testing")
    idUser = DBF.getNbUser()

  def test_Create_User(self):
    self.idUser = DBF.getNbUser()
    self.assertEquals(DBF.findUserId(self.idUser).username,"Test1")
    

  def test_Check_Password(self):
    self.assertTrue(DBF.checkPass("Test1","Testing"))

class Tests_JS(TestCase):
  pass
